#!/usr/bin/env python3
"""Executa casos de eval em três camadas e grava relatório de execução.

  target_system  roda pytest nos node ids e lê o JUnit XML
  contract       lê OpenAPI servido (--probe) ou o contrato exportado
  static         verifica existência/conteúdo de artefatos

Uso:
  python3 scripts/run_evals.py --project ~/meu-projeto
  python3 scripts/run_evals.py --project ~/meu-projeto --probe lis.api.app:create_app --src src
  python3 scripts/run_evals.py --project ~/meu-projeto --layer static

Exit 1 se qualquer caso falhar. Sem relatório, não existe `passed`.
"""
from __future__ import annotations

import argparse
import importlib
import json
import platform
import subprocess
import sys
import tempfile
import time
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import cases_path, foundation, load_json, reports_dir  # noqa: E402


def run_pytest(project: Path, node_ids: list[str]) -> tuple[dict[str, str], str]:
    if not node_ids:
        return {}, ""
    with tempfile.NamedTemporaryFile(suffix=".xml", delete=False) as handle:
        xml_path = Path(handle.name)
    venv_python = project / ".venv" / "bin" / "python"
    interpreter = str(venv_python) if venv_python.exists() else sys.executable
    cmd = [interpreter, "-m", "pytest", *sorted(set(node_ids)), f"--junitxml={xml_path}", "-q", "--no-header"]
    started = time.perf_counter()
    proc = subprocess.run(cmd, cwd=project, capture_output=True, text=True)
    elapsed = time.perf_counter() - started

    statuses: dict[str, str] = {}
    if xml_path.exists() and xml_path.stat().st_size > 0:
        root = ET.parse(xml_path).getroot()
        for case in root.iter("testcase"):
            classname = (case.get("classname") or "").replace(".", "/")
            file_part = f"{classname}.py" if classname else ""
            node_id = f"{file_part}::{case.get('name')}" if file_part else (case.get("name") or "")
            status = "passed"
            if case.find("failure") is not None:
                status = "failed"
            elif case.find("error") is not None:
                status = "error"
            elif case.find("skipped") is not None:
                status = "skipped"
            statuses[node_id] = status
        xml_path.unlink(missing_ok=True)

    summary = f"pytest exit={proc.returncode} em {elapsed:.2f}s"
    if not statuses and proc.returncode not in (0, 5):
        tail = (proc.stdout or proc.stderr).strip().splitlines()[-1:] or [""]
        summary += f" | sem coleta: {tail[0][:300]}"
    return statuses, summary


def load_openapi(project: Path, probe: str | None, src: str | None) -> tuple[dict, str]:
    if probe:
        module_name, _, attr = probe.partition(":")
        if src:
            sys.path.insert(0, str(project / src))
        module = importlib.import_module(module_name)
        factory = getattr(module, attr or "create_app")
        app = factory()
        return app.openapi(), f"servido via {probe}"
    contract = foundation(project) / "contracts" / "openapi.json"
    return load_json(contract), f"exportado de {contract.name}"


def check_assertion(assertion: dict, spec: dict, project: Path) -> tuple[bool, str]:
    kind = assertion.get("kind")
    if kind == "file_exists":
        path = project / assertion["path"]
        return path.exists(), f"{assertion['path']} {'existe' if path.exists() else 'ausente'}"
    if kind == "file_contains":
        path = project / assertion["path"]
        if not path.exists():
            return False, f"{assertion['path']} ausente"
        text = path.read_text(encoding="utf-8")
        missing = [needle for needle in assertion.get("needles", []) if needle not in text]
        return (not missing), f"faltando {missing}" if missing else "trechos presentes"
    if kind == "openapi_version":
        version = spec.get("info", {}).get("version")
        return version == assertion["value"], f"info.version={version}"
    if kind == "openapi_paths":
        missing = [p for p in assertion.get("paths", []) if p not in spec.get("paths", {})]
        return (not missing), f"rotas ausentes: {missing}" if missing else "rotas presentes"
    if kind == "openapi_unique_operation_ids":
        ids = [
            op.get("operationId")
            for path in spec.get("paths", {}).values()
            for op in path.values()
            if isinstance(op, dict) and op.get("operationId")
        ]
        dupes = sorted({i for i in ids if ids.count(i) > 1})
        return (not dupes), f"duplicados: {dupes}" if dupes else f"{len(ids)} operationIds únicos"
    if kind == "json_has_keys":
        data = load_json(project / assertion["path"])
        missing = [k for k in assertion.get("keys", []) if k not in data]
        return (not missing), f"chaves ausentes: {missing}" if missing else "chaves presentes"
    return False, f"assertion desconhecida: {kind}"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", required=True)
    parser.add_argument("--release", default="r001")
    parser.add_argument("--layer", choices=["target_system", "contract", "static"])
    parser.add_argument("--probe", default=None, help="módulo:função que devolve a app (ex.: lis.api.app:create_app)")
    parser.add_argument("--src", default=None, help="diretório adicionado ao sys.path para o probe")
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()

    project = Path(args.project).expanduser().resolve()
    payload = load_json(cases_path(project, args.release))
    cases = [c for c in payload.get("cases", []) if not args.layer or c.get("layer") == args.layer]

    node_ids = [n for c in cases if c.get("layer") == "target_system" for n in c.get("node_ids", [])]
    pytest_status, pytest_summary = run_pytest(project, node_ids)

    spec: dict = {}
    spec_origin = ""
    results = []
    for case in cases:
        layer = case.get("layer")
        details: list[str] = []
        ok = True
        if layer == "target_system":
            statuses = [pytest_status.get(n, "not_collected") for n in case.get("node_ids", [])]
            ok = bool(statuses) and all(s == "passed" for s in statuses)
            details = [f"{n.split('::')[-1]}={pytest_status.get(n, 'not_collected')}" for n in case.get("node_ids", [])]
        else:
            if layer == "contract" and not spec:
                spec, spec_origin = load_openapi(project, args.probe, args.src)
                details.append(spec_origin)
            for assertion in case.get("assertions", []):
                passed, message = check_assertion(assertion, spec, project)
                ok = ok and passed
                details.append(("ok " if passed else "falhou ") + message)
        results.append({
            "id": case.get("id"),
            "req": case.get("req"),
            "layer": layer,
            "title": case.get("title", ""),
            "status": "passed" if ok else "failed",
            "details": details,
        })

    passed = sum(1 for r in results if r["status"] == "passed")
    run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    report = {
        "run_id": run_id,
        "suite": payload.get("suite", "unnamed"),
        "suite_version": payload.get("version", "0.0.0"),
        "release": args.release,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "environment": {"python": platform.python_version(), "platform": platform.platform()},
        "totals": {"cases": len(results), "passed": passed, "failed": len(results) - passed},
        "pytest": pytest_summary,
        "contract_source": spec_origin,
        "results": results,
    }

    out = reports_dir(project, args.release)
    out.mkdir(parents=True, exist_ok=True)
    body = json.dumps(report, indent=2, ensure_ascii=False) + "\n"
    (out / f"{run_id}.json").write_text(body, encoding="utf-8")
    (out / "latest.json").write_text(body, encoding="utf-8")

    md = [
        f"# Relatório de evals — {run_id}",
        "",
        f"- Suíte: `{report['suite']}` v{report['suite_version']} ({args.release})",
        f"- Casos: **{len(results)}** | passaram: **{passed}** | falharam: **{len(results) - passed}**",
        f"- Ambiente: Python {report['environment']['python']} em {report['environment']['platform']}",
        f"- pytest: {pytest_summary.splitlines()[0] if pytest_summary else 'n/a'}",
        "",
        "| Caso | REQ | Camada | Status |",
        "| --- | --- | --- | --- |",
    ]
    for r in results:
        md.append(f"| {r['id']} | {r['req']} | {r['layer']} | {r['status']} |")
    failed = [r for r in results if r["status"] == "failed"]
    if failed:
        md += ["", "## Falhas", ""] + [f"- **{r['id']}**: " + "; ".join(r["details"]) for r in failed]
    (out / "latest.md").write_text("\n".join(md) + "\n", encoding="utf-8")

    if not args.quiet:
        print(f"evals {run_id}: {passed}/{len(results)} casos passaram")
        for r in results:
            print(f"  {'PASS' if r['status'] == 'passed' else 'FAIL'} {r['id']} [{r['layer']}] {r['title']}")
        print(f"relatório: {out.relative_to(project)}/latest.json")
    return 0 if passed == len(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
