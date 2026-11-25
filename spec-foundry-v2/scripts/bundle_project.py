#!/usr/bin/env python3
"""Empacota o projeto em ZIP, com manifest de artefatos e hashes.

Uso:
  python3 scripts/bundle_project.py --project ~/meu-projeto --output ~/meu-projeto-r001.zip

Exclui .venv, caches, banco local, sources/ e relatórios antigos (mantém latest.*).
Recusa sobrescrever ZIP existente.
"""
from __future__ import annotations

import argparse
import json
import sys
import zipfile
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import foundation, load_json, sha256_file  # noqa: E402

EXCLUDE_DIRS = {".venv", "__pycache__", ".pytest_cache", ".git", ".mypy_cache", ".ruff_cache", "node_modules", "sources", ".idea"}
EXCLUDE_SUFFIXES = {".pyc", ".pyo", ".db", ".sqlite", ".sqlite3", ".zip"}
EXCLUDE_NAMES = {".DS_Store", "Thumbs.db"}


def included(path: Path, project: Path) -> bool:
    rel = path.relative_to(project)
    if any(part in EXCLUDE_DIRS for part in rel.parts):
        return False
    if path.name in EXCLUDE_NAMES or path.suffix in EXCLUDE_SUFFIXES:
        return False
    if "evals/reports" in rel.as_posix() and path.name != "latest.json" and path.name != "latest.md":
        return False
    return path.is_file()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--release", default="r001")
    args = parser.parse_args()

    project = Path(args.project).expanduser().resolve()
    output = Path(args.output).expanduser().resolve()
    if output.exists():
        print(f"ERRO   {output} já existe; escolha outro nome", file=sys.stderr)
        return 1

    files = sorted(p for p in project.rglob("*") if included(p, project))
    if not files:
        print("ERRO   nenhum arquivo para empacotar", file=sys.stderr)
        return 1

    manifest_file = foundation(project, args.release) / "manifest.json"
    manifest = load_json(manifest_file) if manifest_file.exists() else {}
    manifest["bundled_at"] = datetime.now(timezone.utc).isoformat()
    manifest["files"] = [
        {"path": p.relative_to(project).as_posix(), "bytes": p.stat().st_size, "sha256": sha256_file(p)}
        for p in files
    ]
    manifest["file_count"] = len(files)

    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED) as archive:
        for path in files:
            archive.write(path, path.relative_to(project).as_posix())
        archive.writestr("BUNDLE-MANIFEST.json", json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")

    print(f"pacote {output.name}: {len(files)} arquivos, {output.stat().st_size / 1024:.0f} KB")
    print(f"sha256 {sha256_file(output)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
