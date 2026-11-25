#!/usr/bin/env python3
"""Verifica REQ -> caso de eval -> teste e gera docs/traceability.md.

Uso:
  python3 scripts/check_traceability.py --project ~/meu-projeto
  python3 scripts/check_traceability.py --project ~/meu-projeto --check   # não escreve o .md

Exit 1 em qualquer violação R1–R5 (ver references/traceability.md).
"""
from __future__ import annotations

import argparse
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import cases_path, collect_tests, foundation, load_json, model_path  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", required=True)
    parser.add_argument("--release", default="r001")
    parser.add_argument("--tests", default="tests")
    parser.add_argument("--marker", default="req")
    parser.add_argument("--check", action="store_true", help="só verifica, não gera docs/traceability.md")
    args = parser.parse_args()

    project = Path(args.project).expanduser().resolve()
    base = foundation(project, args.release)
    model = load_json(model_path(project, args.release))
    cases = load_json(cases_path(project, args.release)).get("cases", [])
    tests = collect_tests(project / args.tests, marker=args.marker)

    requirements = {r["id"]: r for r in model.get("requirements", [])}
    failures: list[str] = []

    cases_by_req: dict[str, list[str]] = defaultdict(list)
    for case in cases:
        cid, req = case.get("id", "?"), case.get("req")
        cases_by_req[req].append(cid)
        if req not in requirements:
            failures.append(f"R5 caso {cid} aponta para {req} inexistente")
        for node in case.get("node_ids", []):
            if node not in tests:
                failures.append(f"R3 caso {cid} cita node id inexistente: {node}")

    tests_by_req: dict[str, list[str]] = defaultdict(list)
    for ref in tests.values():
        for req in ref.ids:
            tests_by_req[req].append(ref.node_id)
            if req not in requirements:
                failures.append(f"R4 teste {ref.node_id} marca {req} inexistente")

    for rid in requirements:
        if not cases_by_req.get(rid):
            failures.append(f"R1 {rid} sem caso de eval")
        if not tests_by_req.get(rid):
            failures.append(f"R2 {rid} sem teste marcado")

    covered = {node for case in cases for node in case.get("node_ids", [])}
    orphans = [node for node in tests if node not in covered]

    lines = [
        f"# Matriz de rastreabilidade — {args.release}",
        "",
        "Gerado por `scripts/check_traceability.py`. Não editar à mão.",
        "",
        f"- Requisitos: **{len(requirements)}**",
        f"- Casos de eval: **{len(cases)}**",
        f"- Testes: **{len(tests)}**",
        f"- Testes sem caso vinculado: **{len(orphans)}**",
        f"- Violações: **{len(failures)}**",
        "",
        "| REQ | Título | Camada | Casos | Testes |",
        "| --- | --- | --- | --- | --- |",
    ]
    for rid, req in requirements.items():
        case_cell = ", ".join(sorted(cases_by_req.get(rid, []))) or "—"
        test_cell = ", ".join(f"`{n.split('::')[-1]}`" for n in tests_by_req.get(rid, [])) or "—"
        lines.append(f"| {rid} | {req.get('title', '')} | {req.get('layer', '—')} | {case_cell} | {test_cell} |")

    if orphans:
        lines += ["", "## Testes sem caso de eval", ""] + [f"- `{node}`" for node in orphans]
    if failures:
        lines += ["", "## Violações", ""] + [f"- {item}" for item in failures]

    if not args.check:
        target = base / "docs" / "traceability.md"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"REQ: {len(requirements)} | casos: {len(cases)} | testes: {len(tests)} | órfãos: {len(orphans)}")
    for failure in failures:
        print(f"  FALHA {failure}")
    if failures:
        return 1
    print("OK rastreabilidade íntegra" + ("" if args.check else " -> docs/traceability.md"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
