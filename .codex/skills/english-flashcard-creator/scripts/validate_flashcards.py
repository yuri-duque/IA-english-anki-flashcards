#!/usr/bin/env python3
"""Valida a estrutura de flashcards Markdown criados no vault.

O script interpreta o formato de campos que o sincronizador aceita: uma linha
``- **Campo:** valor`` dentro de ``## Dados da nota``. Os campos obrigatórios
são lidos dos templates do próprio vault para evitar uma segunda fonte manual
de verdade.
"""

from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from dataclasses import dataclass
from pathlib import Path


DECKS = {
    "Vocabulary": "vocabulary-template.md",
    "Sentences": "sentences-template.md",
    "Expressions": "expressions-template.md",
    "Phrasal Verbs": "phrasal-verbs-template.md",
    "Production": "production-template.md",
}
EMPTY_VALUES = {"", "pendente", "a preencher", "n/a", "na"}


@dataclass
class Note:
    path: Path
    deck: str
    fields: dict[str, str]
    errors: list[str]


def project_root() -> Path:
    for candidate in Path(__file__).resolve().parents:
        if (candidate / "flashcards").is_dir() and (candidate / "templates").is_dir():
            return candidate
    raise RuntimeError("Não encontrei a raiz do vault.")


def required_fields(root: Path, template_name: str) -> set[str]:
    template = (root / "templates" / template_name).read_text(encoding="utf-8")
    section = re.search(r"^## Campos da nota\s*$([\s\S]*?)(?=^##\s+|\Z)", template, re.MULTILINE)
    if not section:
        raise RuntimeError(f"Não encontrei 'Campos da nota' em {template_name}.")
    fields: set[str] = set()
    for line in section.group(1).splitlines():
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) >= 2 and cells[1].casefold() == "sim":
            fields.add(cells[0].strip("`"))
    if not fields:
        raise RuntimeError(f"Não encontrei campos obrigatórios em {template_name}.")
    return fields


def normalize(value: str) -> str:
    value = re.sub(r"<[^>]+>|\*+|`", "", value).casefold()
    value = "".join(char for char in unicodedata.normalize("NFD", value) if not unicodedata.combining(char))
    return re.sub(r"[^a-z0-9]+", "-", value).strip("-")


def empty_value(value: str) -> bool:
    compact = re.sub(r"\s+", " ", value).strip().casefold()
    return compact in EMPTY_VALUES or compact.startswith("pendente") or compact.startswith("a preencher")


def deck_for(path: Path, root: Path) -> str | None:
    try:
        relative = path.resolve().relative_to(root / "flashcards")
    except ValueError:
        return None
    return relative.parts[0] if relative.parts and relative.parts[0] in DECKS else None


def parse_note(path: Path, root: Path) -> Note | None:
    deck = deck_for(path, root)
    if deck is None or path.name == "index.md":
        return None
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []
    frontmatter = re.match(r"\A---\s*\n([\s\S]*?)\n---\s*\n", text)
    if not frontmatter:
        errors.append("frontmatter YAML ausente ou inválido")
    else:
        anki = re.search(r"^anki:\s*(.*?)\s*$", frontmatter.group(1), re.MULTILINE)
        if not anki or anki.group(1) not in {"true", "false"}:
            errors.append("frontmatter deve conter 'anki: true' ou 'anki: false'")
    data = re.search(r"^## Dados da nota\s*$([\s\S]*?)(?=^##\s+|\Z)", text, re.MULTILINE)
    fields: dict[str, str] = {}
    if not data:
        errors.append("seção '## Dados da nota' ausente")
    else:
        for match in re.finditer(r"^-\s+\*\*([^*]+):\*\*[ \t]*(.*?)\s*$", data.group(1), re.MULTILINE):
            name, value = match.group(1).strip(), match.group(2).strip()
            if name in fields:
                errors.append(f"campo duplicado: {name}")
            fields[name] = value
            if empty_value(value):
                errors.append(f"campo sem valor utilizável: {name}")
    for field in required_fields(root, DECKS[deck]):
        if field not in fields:
            errors.append(f"campo obrigatório ausente: {field}")
        elif empty_value(fields[field]):
            errors.append(f"campo obrigatório sem valor: {field}")
    return Note(path=path, deck=deck, fields=fields, errors=errors)


def collect_paths(values: list[str]) -> list[Path]:
    paths: list[Path] = []
    for raw in values:
        path = Path(raw)
        if not path.exists():
            raise RuntimeError(f"Caminho não encontrado: {path}")
        if path.is_dir():
            paths.extend(sorted(candidate for candidate in path.rglob("*.md") if candidate.name != "index.md"))
        elif path.suffix == ".md":
            paths.append(path)
        else:
            raise RuntimeError(f"Esperava um arquivo .md ou diretório: {path}")
    return list(dict.fromkeys(paths))


def production_errors(notes: list[Note], root: Path) -> list[str]:
    productions = [note for note in (parse_note(path, root) for path in (root / "flashcards" / "Production").glob("*.md")) if note]
    errors: list[str] = []
    for note in notes:
        if note.deck != "Vocabulary" or "Word" not in note.fields or empty_value(note.fields["Word"]):
            continue
        word = normalize(note.fields["Word"])
        matches = [
            production
            for production in productions
            if not production.errors and normalize(production.fields.get("Focus", "")) == word
        ]
        if len(matches) < 3:
            errors.append(f"{note.path}: Vocabulary '{note.fields['Word']}' exige 3 Production com Focus correspondente; encontrei {len(matches)}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Valida a estrutura de arquivos Markdown de flashcards.")
    parser.add_argument("paths", nargs="+", help="Arquivos .md ou diretórios a validar")
    args = parser.parse_args()
    try:
        root = project_root()
        notes = [note for note in (parse_note(path, root) for path in collect_paths(args.paths)) if note]
    except (OSError, RuntimeError) as exc:
        print(f"Erro: {exc}", file=sys.stderr)
        return 2
    if not notes:
        print("Nenhum flashcard suportado foi encontrado nos caminhos informados.", file=sys.stderr)
        return 2
    errors = [f"{note.path}: {error}" for note in notes for error in note.errors]
    errors.extend(production_errors(notes, root))
    if errors:
        print("Flashcards inválidos:", file=sys.stderr)
        print("\n".join(f"- {error}" for error in errors), file=sys.stderr)
        return 1
    print(f"OK: {len(notes)} flashcard(s) válido(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
