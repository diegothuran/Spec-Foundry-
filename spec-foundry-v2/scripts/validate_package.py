#!/usr/bin/env python3
"""Valida contratos locais do pacote: modelo, specs, evals, manifest.

Uso:
  python3 scripts/validate_package.py --project ~/meu-projeto --report /tmp/validation.json
Exit 1 se houver erro. Avisos não quebram o comando (use --strict para isso).
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import (  # noqa: E402
    PackageError,
    cases_path,
    collect_tests,
    foundation,
    has_placeholder,
    load_json,
    model_path,
)

VALID_LAYERS = {"target_system", "contract", "static", "generator", "package"}


def validate(project: Path, release: str, strict: bool) -> dict:
    errors: list[str] = []
    warnings: list[str] = []
    base = foundation(project, release)

    try:
        model = load_json(model_path(project, release))
    except PackageError as exc:
        return {"status": "failed", "errors": [str(exc)], "warnings": []}

    if model.get("schema_version") != "2.0":
        errors.append("schema_version deve ser '2.0'")
    project_meta = model.get("project", {})
    if not project_meta.get("slug"):
        errors.append("project.slug ausente")
    if project_meta.get("release") != release:
        errors.append(f"project.release ({project_meta.get('release')}) difere de {release}")

    scope = model.get("scope", {})
    if not scope.get("out_of_scope"):
        errors.append("scope.out_of_scope vazio: projeto sem fora de escopo não tem escopo")

    requirements = model.get("requirements", [])
    if not requirements:
        errors.append("nenhum requisito no modelo")
    req_ids: set[str] = set()
    for req in requirements:
        rid = req.get("id", "?")
        if rid in req_ids:
            errors.append(f"{rid} duplicado")
        req_ids.add(rid)
        for field in ("title", "statement", "layer", "priority"):
            if not req.get(field):
                errors.append(f"{rid} sem {field}")
        acceptance = req.get("acceptance") or []
        if len(acceptance) < 2:
            errors.append(f"{rid} precisa de ao menos 2 itens de acceptance (feliz + erro)")
        spec = req.get("spec")
        if spec and not (base / spec).exists():
            errors.append(f"{rid} aponta para spec inexistente: {spec}")

    ids_seen: dict[str, str] = {}
    for collection, prefix in (
        ("decisions", "DEC"), ("assumptions", "ASM"), ("risks", "RSK"), ("open_questions", "Q"),
    ):
        for item in model.get(collection, []):
            item_id = item.get("id", "?")
            if not item_id.startswith(prefix + "-"):
                errors.append(f"{collection}: id {item_id} não usa prefixo {prefix}-")
            if item_id in ids_seen:
                errors.append(f"id repetido entre coleções: {item_id}")
            ids_seen[item_id] = collection
            if collection == "assumptions" and not item.get("impact"):
                errors.append(f"{item_id} sem impact (assunção sem consequência é invisível)")
            if collection == "risks" and not item.get("mitigation"):
                errors.append(f"{item_id} sem mitigation")

    gates = model.get("readiness", {}).get("gates", [])
    if not gates:
        warnings.append("readiness.gates vazio: prontidão não é verificável")
    blocking = [q for q in model.get("open_questions", []) if q.get("blocking") and q.get("status") == "open"]
    if blocking and model.get("readiness", {}).get("status") == "ready_for_review":
        errors.append(f"ready_for_review com pergunta bloqueante aberta: {[q['id'] for q in blocking]}")

    tests = collect_tests(project / "tests")
    try:
        payload = load_json(cases_path(project, release))
    except PackageError as exc:
        errors.append(str(exc))
        payload = {"cases": []}

    cases = payload.get("cases", [])
    case_ids: set[str] = set()
    for case in cases:
        cid = case.get("id", "?")
        if cid in case_ids:
            errors.append(f"caso duplicado: {cid}")
        case_ids.add(cid)
        if case.get("req") not in req_ids:
            errors.append(f"{cid} aponta para requisito inexistente: {case.get('req')}")
        layer = case.get("layer")
        if layer not in VALID_LAYERS:
            errors.append(f"{cid} com layer inválida: {layer}")
        if layer == "target_system":
            nodes = case.get("node_ids") or []
            if not nodes:
                errors.append(f"{cid} target_system sem node_ids")
            for node in nodes:
                if node not in tests:
                    errors.append(f"{cid} cita node id inexistente: {node}")
        elif layer in {"contract", "static"} and not case.get("assertions"):
            errors.append(f"{cid} camada {layer} sem assertions")

    covered = {c.get("req") for c in cases}
    for rid in sorted(req_ids - covered):
        errors.append(f"{rid} sem caso de eval")

    docs = base / "docs"
    if not (docs / "specs" / "00-index.md").exists():
        errors.append("docs/specs/00-index.md ausente")
    for path in list(docs.rglob("*.md")) + [base / "manifest.json", base / "evals" / "cases.json"]:
        if path.exists() and has_placeholder(path):
            errors.append(f"marcador de rascunho em {path.relative_to(project)}")

    manifest_file = base / "manifest.json"
    if not manifest_file.exists():
        errors.append("manifest.json ausente")
    else:
        manifest = load_json(manifest_file)
        if manifest.get("release") != release:
            errors.append("manifest.release difere da release do projeto")
        if manifest.get("requirements") not in (None, len(requirements)):
            errors.append(f"manifest.requirements ({manifest.get('requirements')}) difere do modelo ({len(requirements)})")
        if manifest.get("cases") not in (None, len(cases)):
            errors.append(f"manifest.cases ({manifest.get('cases')}) difere de cases.json ({len(cases)})")
        if not manifest.get("artifacts"):
            errors.append("manifest.artifacts vazio")

    if strict and warnings:
        errors.extend(warnings)

    return {
        "status": "passed" if not errors else "failed",
        "project": str(project),
        "release": release,
        "checked_at": datetime.now(timezone.utc).isoformat(),
        "counts": {"requirements": len(requirements), "cases": len(cases), "tests": len(tests)},
        "errors": errors,
        "warnings": warnings,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", required=True)
    parser.add_argument("--release", default="r001")
    parser.add_argument("--report", default=None)
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()

    project = Path(args.project).expanduser().resolve()
    report = validate(project, args.release, args.strict)

    if args.report:
        target = Path(args.report)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    counts = report.get("counts", {})
    print(f"validação {report['status']}: {counts.get('requirements', 0)} requisitos, "
          f"{counts.get('cases', 0)} casos, {counts.get('tests', 0)} testes")
    for warning in report.get("warnings", []):
        print(f"  AVISO {warning}")
    for error in report.get("errors", []):
        print(f"  ERRO  {error}")
    return 0 if report["status"] == "passed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
