"""Utilidades compartilhadas pelos scripts da Spec Foundry v2 (somente stdlib)."""
from __future__ import annotations

import ast
import hashlib
import json
import re
import secrets
import string
import sys
from dataclasses import dataclass
from pathlib import Path

PLACEHOLDER = re.compile(r"\b(TBD|TODO|FIXME)\b")
REQ_MARK = re.compile(r'pytest\.mark\.(?P<marker>[a-z_]+)\(\s*["\'](?P<id>REQ-\d{3})["\']')
ALPHABET = string.ascii_lowercase + string.digits


class PackageError(Exception):
    """Falha de contrato do pacote (erro de uso, não de domínio)."""


def new_id(prefix: str, size: int = 12) -> str:
    return f"{prefix}_{''.join(secrets.choice(ALPHABET) for _ in range(size))}"


def canonical_json(value: object) -> str:
    return json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":"))


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_json(path: Path) -> dict:
    if not path.exists():
        raise PackageError(f"arquivo obrigatório ausente: {path}")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise PackageError(f"JSON inválido em {path}: {exc}") from exc


def foundation(project: Path, release: str = "r001") -> Path:
    return project / "foundation" / release


def model_path(project: Path, release: str = "r001") -> Path:
    return foundation(project, release) / "model" / "project-model.json"


def cases_path(project: Path, release: str = "r001") -> Path:
    return foundation(project, release) / "evals" / "cases.json"


def reports_dir(project: Path, release: str = "r001") -> Path:
    return foundation(project, release) / "evals" / "reports"


@dataclass(frozen=True)
class TestRef:
    node_id: str
    file: str
    name: str
    ids: tuple[str, ...]


def collect_tests(tests_dir: Path, marker: str = "req") -> dict[str, TestRef]:
    """Mapeia node id -> requisitos marcados, lendo decoradores por AST."""
    found: dict[str, TestRef] = {}
    if not tests_dir.exists():
        return found
    for path in sorted(tests_dir.glob("test_*.py")):
        source = path.read_text(encoding="utf-8")
        tree = ast.parse(source)
        for node in ast.walk(tree):
            if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                continue
            if not node.name.startswith("test_"):
                continue
            ids: list[str] = []
            for deco in node.decorator_list:
                segment = ast.get_source_segment(source, deco) or ""
                for match in REQ_MARK.finditer(segment):
                    if match.group("marker") == marker:
                        ids.append(match.group("id"))
            rel = path.relative_to(tests_dir.parent).as_posix()
            node_id = f"{rel}::{node.name}"
            found[node_id] = TestRef(node_id=node_id, file=rel, name=node.name, ids=tuple(ids))
    return found


def has_placeholder(path: Path) -> bool:
    if path.suffix not in {".md", ".json", ".yml", ".yaml", ".txt"}:
        return False
    try:
        return bool(PLACEHOLDER.search(path.read_text(encoding="utf-8")))
    except (UnicodeDecodeError, OSError):
        return False


def warn(message: str) -> None:
    print(f"AVISO  {message}", file=sys.stderr)


def fail(message: str) -> None:
    print(f"ERRO   {message}", file=sys.stderr)
