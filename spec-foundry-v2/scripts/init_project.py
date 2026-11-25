#!/usr/bin/env python3
"""Cria a árvore de um projeto Spec Foundry v2 a partir dos templates.

Uso:
  python3 scripts/init_project.py --project ~/meu-projeto --slug meu-projeto --release r001
"""
from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SKILL = HERE.parent
TEMPLATES = SKILL / "templates" / "foundation"


def build_model(slug: str, release: str) -> dict:
    return {
        "schema_version": "2.0",
        "project": {
            "name": slug,
            "slug": slug,
            "release": release,
            "status": "discovery",
            "purpose": "Descrever em uma frase o que esta fundação prova.",
        },
        "scope": {
            "in_scope": ["Substituir pelos itens que a release entrega"],
            "out_of_scope": ["Substituir pelo que explicitamente NÃO será feito nesta release"],
        },
        "entities": [],
        "invariants": [],
        "requirements": [],
        "decisions": [],
        "assumptions": [],
        "risks": [],
        "open_questions": [],
        "readiness": {"status": "discovery", "gates": []},
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", required=True, help="raiz do projeto")
    parser.add_argument("--slug", default=None)
    parser.add_argument("--release", default="r001")
    parser.add_argument("--force", action="store_true", help="escreve sobre projeto existente")
    args = parser.parse_args()

    project = Path(args.project).expanduser().resolve()
    slug = args.slug or project.name
    base = project / "foundation" / args.release

    if base.exists() and not args.force:
        print(f"ERRO   {base} já existe; use --force para completar arquivos ausentes", file=sys.stderr)
        return 1

    for folder in ("model", "docs/specs", "docs/adr", "evals/reports", "contracts"):
        (base / folder).mkdir(parents=True, exist_ok=True)

    created: list[str] = []
    model_file = base / "model" / "project-model.json"
    if not model_file.exists() or args.force:
        model_file.write_text(json.dumps(build_model(slug, args.release), indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        created.append(str(model_file.relative_to(project)))

    mapping = {
        "spec.md": base / "docs" / "specs" / "01-primeira-spec.md",
        "eval-cases.json": base / "evals" / "cases.json",
        "adr.md": base / "docs" / "adr" / "0001-primeira-decisao.md",
        "manifest.json": base / "manifest.json",
        "AGENTS.md": project / "AGENTS.md",
    }
    for template_name, target in mapping.items():
        source = TEMPLATES / template_name
        if not source.exists():
            continue
        if target.exists() and not args.force:
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        text = source.read_text(encoding="utf-8")
        text = text.replace("{{slug}}", slug).replace("{{release}}", args.release)
        target.write_text(text, encoding="utf-8")
        created.append(str(target.relative_to(project)))

    print(f"projeto {slug} ({args.release}) em {project}")
    for item in created:
        print(f"  criado {item}")
    print("próximo passo: preencher model/project-model.json antes de escrever prosa")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
