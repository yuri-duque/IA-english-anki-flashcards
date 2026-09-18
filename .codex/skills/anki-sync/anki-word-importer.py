#!/usr/bin/env python3
"""Sincroniza notas Markdown dos decks de flashcards com o AnkiConnect."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Any

import frontmatter
import requests

ANKI_CONNECT_URL = "http://localhost:8765"
DECKS = {
    "Vocabulary": ("Vocabulary", "English Vocabulary", [
        "Word", "Meaning", "PartOfSpeech", "Example", "ExampleTranslation", "Definition",
        "Audio", "AudioSource", "AudioLicense", "HowToUse", "WordFamily", "RelatedWords", "CommonExpressions",
        "Etymology", "Image", "Source",
    ]),
    "Sentences": ("Sentences", "English Sentence", [
        "Sentence", "Translation", "Audio", "AudioSource", "AudioLicense", "Focus",
        "FocusTranslations", "HowToUse", "KeyVocabulary", "GrammarNote", "AlternativeTranslation", "Source",
    ]),
    "Expressions": ("Expressions", "English Expression", [
        "Expression", "Translation", "Audio", "AudioSource", "AudioLicense", "HowToUse",
        "Example", "ExampleTranslation", "Register", "LiteralMeaning", "Variations", "CommonExpressions", "Source",
    ]),
    "Phrasal Verbs": ("Phrasal Verbs", "English Phrasal Verb", [
        "PhrasalVerb", "Translation", "Audio", "AudioSource", "AudioLicense", "Verb", "Particle",
        "HowToUse", "Pattern", "Separable", "Example", "ExampleTranslation", "AlternativeExamples",
        "Synonyms", "CommonExpressions", "Source",
    ]),
    "Production": ("Production", "English Production", [
        "Prompt", "Context", "Answer", "PossibleAnswers", "Focus", "HowToUse", "Example",
        "ExampleTranslation", "CommonMistakes", "Source",
    ]),
}


def find_project_root() -> Path:
    for candidate in (Path(__file__).resolve(), *Path(__file__).resolve().parents):
        if (candidate / "flashcards").is_dir():
            return candidate
    raise RuntimeError("Não encontrei a raiz do vault (flashcards/).")


PROJECT_ROOT = find_project_root()


def invoke(action: str, params: dict[str, Any] | None = None) -> Any:
    try:
        response = requests.post(ANKI_CONNECT_URL, json={"action": action, "version": 6, "params": params or {}}, timeout=10)
        response.raise_for_status()
        body = response.json()
        if body.get("error"):
            raise RuntimeError(body["error"])
        return body.get("result")
    except requests.exceptions.ConnectionError as exc:
        raise RuntimeError(
            "Não foi possível acessar o AnkiConnect em http://localhost:8765. "
            "Confirme que o Anki Desktop e o complemento AnkiConnect estão ativos; "
            "em um ambiente isolado, execute o sincronizador com acesso ao host."
        ) from exc


def markdown_to_html(value: str) -> str:
    value = value.strip()
    value = re.sub(r"\[([^]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', value)
    value = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", value)
    value = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<i>\1</i>", value)
    value = re.sub(r"^\s*-\s+", "• ", value, flags=re.MULTILINE)
    return value.replace("\n", "<br>")


def section(content: str, title: str) -> str:
    match = re.search(rf"^##\s+{re.escape(title)}\s*$([\s\S]*?)(?=^##\s+|\Z)", content, re.MULTILINE)
    return match.group(1).strip() if match else ""


def note_data(path: Path) -> tuple[frontmatter.Post, dict[str, str]]:
    post = frontmatter.load(path)
    data: dict[str, str] = {}
    for match in re.finditer(r"^-\s+\*\*([^*]+):\*\*[ \t]*([^\r\n]*)$", section(post.content, "Dados da nota"), re.MULTILINE):
        value = match.group(2).strip()
        if value and value.lower() not in {"pendente", "a preencher"}:
            data[match.group(1)] = value.strip("`")
    if "Word" not in data:
        title = re.search(r"^#\s+(.+?)\s*$", post.content, re.MULTILINE)
        if title:
            data["Word"] = title.group(1).strip()
    verse = section(post.content, "Verso")
    headings = list(re.finditer(r"^###\s+(.+?)\s*$", verse, re.MULTILINE))
    for index, heading in enumerate(headings):
        name = heading.group(1).strip().lower()
        value = verse[heading.end(): headings[index + 1].start() if index + 1 < len(headings) else len(verse)].strip()
        key = {
            "how to use": "HowToUse", "example": "Example", "common expressions": "CommonExpressions",
            "word family": "WordFamily", "related words and differences": "RelatedWords",
            "etymology": "Etymology", "source": "Source",
        }.get(name)
        if key and key not in data:
            lines = [line.strip() for line in value.splitlines() if line.strip()]
            if key == "Example" and lines:
                data[key] = lines[0]
                if len(lines) > 1 and lines[1].startswith("_") and lines[1].endswith("_"):
                    data.setdefault("ExampleTranslation", lines[1].strip("_"))
            elif lines:
                data[key] = "\n".join(lines)
    return post, data


def model_layout(model_name: str, fields: list[str]) -> tuple[dict[str, str], str]:
    if model_name == "English Vocabulary":
        return {
            "Name": "Recognition",
            "Front": """<div class=\"card vocabulary-card\">
  <div class=\"deck-label\">VOCABULARY</div>
  <div class=\"word\">{{Word}}</div>
  {{#Audio}}<div class=\"audio\">{{Audio}}</div>{{/Audio}}
  <div class=\"instruction\">What does this word mean and how is it used?</div>
</div>""",
            "Back": """{{FrontSide}}
<hr id=\"answer\">
<div class=\"answer\">
  <div class=\"meaning\">{{Meaning}}</div>
  {{#PartOfSpeech}}<div class=\"part-of-speech\">{{PartOfSpeech}}</div>{{/PartOfSpeech}}
  {{#Definition}}<div class=\"definition\">{{Definition}}</div>{{/Definition}}
  {{#HowToUse}}<div class=\"section-title\">How to use</div><div class=\"details\">{{HowToUse}}</div>{{/HowToUse}}
  {{#Example}}<div class=\"section-title\">Example</div><div class=\"example\">{{Example}}</div>{{/Example}}
  {{#ExampleTranslation}}<div class=\"example-translation\">{{ExampleTranslation}}</div>{{/ExampleTranslation}}
  {{#CommonExpressions}}<div class=\"section-title\">Common expressions</div><div class=\"details\">{{CommonExpressions}}</div>{{/CommonExpressions}}
  {{#WordFamily}}<div class=\"section-title\">Word family</div><div class=\"details\">{{WordFamily}}</div>{{/WordFamily}}
  {{#RelatedWords}}<div class=\"section-title\">Related words</div><div class=\"details\">{{RelatedWords}}</div>{{/RelatedWords}}
  {{#Etymology}}<div class=\"section-title\">Etymology</div><div class=\"details\">{{Etymology}}</div>{{/Etymology}}
  {{#Image}}<div class=\"section-title\">Image</div><div class=\"details\">{{Image}}</div>{{/Image}}
  {{#Source}}<div class=\"source\">Source: {{Source}}</div>{{/Source}}
</div>""",
        }, """.card { background: #f7f8fa; color: #20242a; font-family: -apple-system, BlinkMacSystemFont, \"Segoe UI\", sans-serif; font-size: 20px; line-height: 1.45; padding: 28px 20px; text-align: center; }
.vocabulary-card { min-height: 260px; }
.deck-label, .section-title { color: #64748b; font-size: 11px; font-weight: 700; letter-spacing: .1em; text-transform: uppercase; }
.deck-label { margin-bottom: 28px; }
.word { color: #1d4ed8; font-size: clamp(34px, 8vw, 56px); font-weight: 700; margin: 20px 0 8px; }
.instruction { color: #64748b; font-size: 15px; margin-top: 34px; }
hr#answer { border: 0; border-top: 1px solid #d8dee8; margin: 28px 0; }
.answer { text-align: left; }
.meaning { color: #15803d; font-size: 29px; font-weight: 700; text-align: center; }
.part-of-speech { color: #64748b; font-size: 14px; font-style: italic; margin: 5px 0 24px; text-align: center; }
.section-title { margin: 24px 0 7px; }
.details, .example-translation, .definition { color: #475569; font-size: 17px; }
.details, .definition { background: #fff; border-radius: 6px; padding: 10px 12px; }
.example { background: #eaf2ff; border-radius: 8px; color: #1e3a8a; font-size: 21px; padding: 14px 16px; }
.example b, .details b { color: #1d4ed8; font-weight: 800; }
.example-translation { margin-top: 8px; }
.source { color: #94a3b8; font-size: 12px; margin-top: 28px; }
@media (prefers-color-scheme: dark) { .card { background: #171a21; color: #e5e7eb; } .example { background: #172554; color: #dbeafe; } .details, .definition { background: #222631; } }"""
    if model_name == "English Sentence":
        return {
            "Name": "Recognition",
            "Front": """<div class="card sentence-card"><div class="deck-label">SENTENCES</div><div class="sentence">{{Sentence}}</div>{{#Audio}}<div class="audio">{{Audio}}</div>{{/Audio}}<div class="instruction">What does this sentence mean?</div></div>""",
            "Back": """{{FrontSide}}<hr id="answer"><div class="answer"><div class="translation">{{Translation}}</div>{{#AlternativeTranslation}}<div class="alternative">{{AlternativeTranslation}}</div>{{/AlternativeTranslation}}{{#Focus}}<div class="section-title">Focus</div><div class="focus">{{Focus}}</div>{{/Focus}}{{#FocusTranslations}}<div class="section-title">Possible translations</div><div class="focus-translations">{{FocusTranslations}}</div>{{/FocusTranslations}}{{#HowToUse}}<div class="section-title">How to use</div><div class="details">{{HowToUse}}</div>{{/HowToUse}}{{#KeyVocabulary}}<div class="section-title">Key vocabulary</div><div class="details">{{KeyVocabulary}}</div>{{/KeyVocabulary}}{{#GrammarNote}}<div class="section-title">Grammar</div><div class="details">{{GrammarNote}}</div>{{/GrammarNote}}{{#Source}}<div class="source">Source: {{Source}}</div>{{/Source}}</div>""",
        }, """.card{background:#f7f8fa;color:#20242a;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;font-size:20px;line-height:1.45;padding:28px 20px;text-align:center}.sentence-card{min-height:260px}.deck-label,.section-title{color:#64748b;font-size:11px;font-weight:700;letter-spacing:.1em;text-transform:uppercase}.deck-label{margin-bottom:30px}.sentence{color:#1d4ed8;font-size:clamp(25px,5vw,38px);font-weight:600;margin:28px auto;max-width:720px}.sentence b{color:#b45309}.instruction{color:#64748b;font-size:15px;margin-top:34px}hr#answer{border:0;border-top:1px solid #d8dee8;margin:28px 0}.answer{text-align:left}.translation{color:#15803d;font-size:26px;font-weight:700;text-align:center}.alternative{color:#475569;font-size:17px;font-style:italic;margin-top:8px;text-align:center}.section-title{margin:24px 0 7px}.focus{background:#fff7ed;border-left:3px solid #f59e0b;color:#9a3412;font-size:21px;font-weight:700;padding:10px 12px}.focus-translations{color:#15803d;font-size:20px;font-weight:700}.details{background:#fff;border-radius:6px;color:#475569;font-size:17px;padding:10px 12px}.source{color:#94a3b8;font-size:12px;margin-top:28px}@media (prefers-color-scheme:dark){.card{background:#171a21;color:#e5e7eb}.focus{background:#431407;color:#fed7aa}.details{background:#222631}}"""
    if model_name == "English Expression":
        return {
            "Name": "Recognition",
            "Front": """<div class="card expression-card"><div class="deck-label">EXPRESSIONS</div><div class="expression">{{Expression}}</div>{{#Audio}}<div class="audio">{{Audio}}</div>{{/Audio}}<div class="instruction">What does this expression mean?</div></div>""",
            "Back": """{{FrontSide}}<hr id="answer"><div class="answer"><div class="translation">{{Translation}}</div>{{#Register}}<div class="register">{{Register}}</div>{{/Register}}{{#HowToUse}}<div class="section-title">How to use</div><div class="details">{{HowToUse}}</div>{{/HowToUse}}{{#Example}}<div class="section-title">Example</div><div class="example">{{Example}}</div>{{/Example}}{{#ExampleTranslation}}<div class="example-translation">{{ExampleTranslation}}</div>{{/ExampleTranslation}}{{#LiteralMeaning}}<div class="section-title">Literal meaning</div><div class="details">{{LiteralMeaning}}</div>{{/LiteralMeaning}}{{#Variations}}<div class="section-title">Variations</div><div class="details">{{Variations}}</div>{{/Variations}}{{#CommonExpressions}}<div class="section-title">Related expressions</div><div class="details">{{CommonExpressions}}</div>{{/CommonExpressions}}{{#Source}}<div class="source">Source: {{Source}}</div>{{/Source}}</div>""",
        }, """.card{background:#f7f8fa;color:#20242a;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;font-size:20px;line-height:1.45;padding:28px 20px;text-align:center}.expression-card{min-height:260px}.deck-label,.section-title{color:#718096;font-size:11px;font-weight:700;letter-spacing:.1em;text-transform:uppercase}.deck-label{margin-bottom:30px}.expression{color:#7c3aed;font-size:clamp(27px,6vw,44px);font-weight:700;margin:28px auto;max-width:720px}.instruction{color:#64748b;font-size:15px;margin-top:34px}hr#answer{border:0;border-top:1px solid #d8dee8;margin:28px 0}.answer{text-align:left}.translation{color:#15803d;font-size:26px;font-weight:700;text-align:center}.register{color:#64748b;font-size:14px;font-style:italic;margin:7px 0 24px;text-align:center}.section-title{margin:24px 0 7px}.details{background:#fff;border-radius:6px;color:#475569;font-size:17px;padding:10px 12px}.example{background:#f3e8ff;border-radius:8px;color:#581c87;font-size:21px;padding:14px 16px}.example b,.details b{color:#7c3aed;font-weight:800}.example-translation{color:#475569;font-size:17px;margin-top:8px}.source{color:#94a3b8;font-size:12px;margin-top:28px}@media (prefers-color-scheme:dark){.card{background:#171a21;color:#e5e7eb}.example{background:#3b0764;color:#f3e8ff}.details{background:#222631}}"""
    if model_name == "English Phrasal Verb":
        return {
            "Name": "Recognition",
            "Front": """<div class="card phrasal-card"><div class="deck-label">PHRASAL VERBS</div><div class="phrasal-verb">{{PhrasalVerb}}</div>{{#Audio}}<div class="audio">{{Audio}}</div>{{/Audio}}<div class="instruction">What does this phrasal verb mean?</div></div>""",
            "Back": """{{FrontSide}}<hr id="answer"><div class="answer"><div class="translation">{{Translation}}</div>{{#Verb}}<div class="section-title">Structure</div><div class="structure"><b>{{Verb}}</b> + <b>{{Particle}}</b></div>{{/Verb}}{{#HowToUse}}<div class="section-title">How to use</div><div class="details">{{HowToUse}}</div>{{/HowToUse}}{{#Pattern}}<div class="section-title">Pattern</div><div class="structure">{{Pattern}}</div>{{/Pattern}}{{#Separable}}<div class="section-title">Separable?</div><div class="details">{{Separable}}</div>{{/Separable}}{{#Example}}<div class="section-title">Example</div><div class="example">{{Example}}</div>{{/Example}}{{#ExampleTranslation}}<div class="example-translation">{{ExampleTranslation}}</div>{{/ExampleTranslation}}{{#AlternativeExamples}}<div class="section-title">More examples</div><div class="details">{{AlternativeExamples}}</div>{{/AlternativeExamples}}{{#Synonyms}}<div class="section-title">Alternatives</div><div class="details">{{Synonyms}}</div>{{/Synonyms}}{{#CommonExpressions}}<div class="section-title">Common combinations</div><div class="details">{{CommonExpressions}}</div>{{/CommonExpressions}}{{#Source}}<div class="source">Source: {{Source}}</div>{{/Source}}</div>""",
        }, """.card{background:#f7f8fa;color:#20242a;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;font-size:20px;line-height:1.45;padding:28px 20px;text-align:center}.phrasal-card{min-height:260px}.deck-label,.section-title{color:#718096;font-size:11px;font-weight:700;letter-spacing:.1em;text-transform:uppercase}.deck-label{margin-bottom:30px}.phrasal-verb{color:#db2777;font-size:clamp(30px,7vw,50px);font-weight:700;margin:28px auto}.instruction{color:#64748b;font-size:15px;margin-top:34px}hr#answer{border:0;border-top:1px solid #d8dee8;margin:28px 0}.answer{text-align:left}.translation{color:#15803d;font-size:26px;font-weight:700;text-align:center}.section-title{margin:24px 0 7px}.structure{background:#fce7f3;border-radius:6px;color:#9d174d;font-size:20px;padding:10px 12px}.details{background:#fff;border-radius:6px;color:#475569;font-size:17px;padding:10px 12px}.example{background:#fdf2f8;border-radius:8px;color:#831843;font-size:21px;padding:14px 16px}.example b,.details b{color:#db2777;font-weight:800}.example-translation{color:#475569;font-size:17px;margin-top:8px}.source{color:#94a3b8;font-size:12px;margin-top:28px}@media (prefers-color-scheme:dark){.card{background:#171a21;color:#e5e7eb}.structure,.example{background:#500724;color:#fbcfe8}.details{background:#222631}}"""
    if model_name == "English Production":
        return {
            "Name": "Recognition",
            "Front": """<div class="card production-card"><div class="deck-label">PRODUCTION</div><div class="prompt">{{Prompt}}</div>{{#Context}}<div class="context">{{Context}}</div>{{/Context}}<div class="instruction">How would you say this in English?</div></div>""",
            "Back": """{{FrontSide}}<hr id="answer"><div class="answer"><div class="answer-label">Answer</div><div class="answer-text">{{Answer}}</div>{{#PossibleAnswers}}<div class="section-title">Other natural answers</div><div class="details">{{PossibleAnswers}}</div>{{/PossibleAnswers}}{{#Focus}}<div class="section-title">Focus</div><div class="focus">{{Focus}}</div>{{/Focus}}{{#HowToUse}}<div class="section-title">How to use</div><div class="details">{{HowToUse}}</div>{{/HowToUse}}{{#Example}}<div class="section-title">Example</div><div class="example">{{Example}}</div>{{/Example}}{{#ExampleTranslation}}<div class="example-translation">{{ExampleTranslation}}</div>{{/ExampleTranslation}}{{#CommonMistakes}}<div class="section-title">Common mistakes</div><div class="details">{{CommonMistakes}}</div>{{/CommonMistakes}}{{#Source}}<div class="source">Source: {{Source}}</div>{{/Source}}</div>""",
        }, """.card{background:#f7f8fa;color:#20242a;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;font-size:20px;line-height:1.45;padding:28px 20px;text-align:center}.production-card{min-height:260px}.deck-label,.section-title,.answer-label{color:#64748b;font-size:11px;font-weight:700;letter-spacing:.1em;text-transform:uppercase}.deck-label{margin-bottom:30px}.prompt{color:#0f766e;font-size:clamp(25px,5vw,38px);font-weight:600;margin:28px auto;max-width:720px}.context{background:#ccfbf1;border-radius:8px;color:#115e59;font-size:17px;margin:18px auto;max-width:650px;padding:12px 16px}.instruction{color:#64748b;font-size:15px;margin-top:34px}hr#answer{border:0;border-top:1px solid #d8dee8;margin:28px 0}.answer{text-align:left}.answer-label{text-align:center}.answer-text{color:#15803d;font-size:28px;margin:10px 0 24px;text-align:center}.section-title{margin:24px 0 7px}.details,.focus{background:#fff;border-radius:6px;color:#475569;font-size:17px;padding:10px 12px}.focus{color:#0f766e;font-size:20px;font-weight:700}.example{background:#ecfdf5;border-radius:8px;color:#065f46;padding:14px 16px}.answer-text b,.focus b,.details b,.example b{color:#047857;font-weight:800}.example-translation{color:#475569;font-size:17px;margin-top:8px}.source{color:#94a3b8;font-size:12px;margin-top:28px}@media (prefers-color-scheme:dark){.card{background:#171a21;color:#e5e7eb}.context,.example{background:#042f2e;color:#ccfbf1}.details,.focus{background:#222631}}"""
    return {
        "Name": "Recognition",
        "Front": "<div>{{" + fields[0] + "}}</div>",
        "Back": "<div>{{" + fields[1] + "}}</div><hr>{{FrontSide}}",
    }, ".card { font-family: sans-serif; font-size: 20px; text-align: left; }"


def ensure_model(model_name: str, fields: list[str]) -> None:
    template, css = model_layout(model_name, fields)
    if model_name in (invoke("modelNames") or []):
        existing_fields = invoke("modelFieldNames", {"modelName": model_name}) or []
        for field in fields:
            if field not in existing_fields:
                invoke("modelFieldAdd", {
                    "modelName": model_name,
                    "fieldName": field,
                    "index": len(existing_fields),
                })
                existing_fields.append(field)
        invoke("updateModelTemplates", {"model": {"name": model_name, "templates": {template["Name"]: {
            "Front": template["Front"], "Back": template["Back"],
        }}}})
        invoke("updateModelStyling", {"model": {"name": model_name, "css": css}})
        return
    invoke("createModel", {
        "modelName": model_name,
        "inOrderFields": fields,
        "css": css,
        "isCloze": False,
        "cardTemplates": [template],
    })


def update_sync_metadata(path: Path, note_id: int) -> None:
    """Registra a identidade da nota do Anki e confirma a sincronização."""
    post = frontmatter.load(path)
    post["anki_note_id"] = str(note_id)
    post["anki"] = True
    path.write_text(frontmatter.dumps(post), encoding="utf-8")


def frontmatter_note_id(post: frontmatter.Post) -> int | None:
    value = post.metadata.get("anki_note_id")
    if value in (None, ""):
        return None
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def update_index(index_path: Path, stem: str) -> None:
    content = index_path.read_text(encoding="utf-8")
    pattern = re.compile(rf"^(\|.*\[[^]]+\]\([^)]*{re.escape(stem)}\.md\)[^\n]*\|\s*)[❌✅](\s*\|?\s*)$", re.MULTILINE | re.IGNORECASE)
    updated, count = pattern.subn(r"\1✅\2", content)
    if count:
        index_path.write_text(updated, encoding="utf-8")
    else:
        print(f"⚠️  {index_path.relative_to(PROJECT_ROOT)} não tem linha para {stem}.md")


def existing_notes(deck: str, model: str, primary_field: str) -> tuple[dict[int, dict[str, Any]], dict[str, list[dict[str, Any]]]]:
    note_ids = invoke("findNotes", {"query": f'deck:"{deck}" note:"{model}"'}) or []
    if not note_ids:
        return {}, {}
    notes = invoke("notesInfo", {"notes": note_ids}) or []
    by_id: dict[int, dict[str, Any]] = {}
    by_primary: dict[str, list[dict[str, Any]]] = {}
    for note in notes:
        note_id = int(note["noteId"])
        by_id[note_id] = note
        primary_value = note["fields"].get(primary_field, {}).get("value", "").strip()
        if primary_value:
            by_primary.setdefault(primary_value, []).append(note)
    return by_id, by_primary


def note_fields(values: dict[str, str], fields: list[str]) -> dict[str, str]:
    return {field: markdown_to_html(values.get(field, "")) for field in fields}


def note_needs_update(note: dict[str, Any], desired_fields: dict[str, str]) -> bool:
    current_fields = note.get("fields", {})
    return any(
        current_fields.get(field, {}).get("value", "") != value
        for field, value in desired_fields.items()
    )


def update_existing_note(note: dict[str, Any], desired_fields: dict[str, str]) -> bool:
    """Atualiza os campos gerenciados e informa se houve alteração."""
    if not note_needs_update(note, desired_fields):
        return False
    invoke("updateNoteFields", {"note": {
        "id": int(note["noteId"]),
        "fields": desired_fields,
    }})
    return True


def sync_folder(folder_name: str, config: tuple[str, str, list[str]]) -> tuple[int, int, int]:
    folder = PROJECT_ROOT / "flashcards" / folder_name
    if not folder.is_dir():
        return 0, 0, 0
    index = folder / "index.md"
    if not index.is_file():
        print(f"❌ {folder.relative_to(PROJECT_ROOT)} ignorada: index.md não encontrado.")
        return 0, 0, 1
    deck, model, fields = config
    ensure_model(model, fields)
    invoke("createDeck", {"deck": deck})

    # Fase 1: traz todas as notas do deck e reconcilia suas identidades com o
    # vault. O ID é mais confiável que o campo principal quando este foi editado.
    notes_by_id, notes_by_primary = existing_notes(deck, model, fields[0])
    parsed: list[tuple[Path, frontmatter.Post, dict[str, str]]] = []
    primary_counts: dict[str, int] = {}
    for path in sorted(folder.glob("*.md")):
        if path.name == "index.md":
            continue
        try:
            post, values = note_data(path)
            parsed.append((path, post, values))
            primary_value = values.get(fields[0], "").strip()
            if primary_value:
                primary_counts[primary_value] = primary_counts.get(primary_value, 0) + 1
        except Exception as exc:
            print(f"⚠️ Erro ao ler {path.name}: {exc}")

    pending: list[tuple[Path, frontmatter.Post, dict[str, str], dict[str, Any] | None]] = []
    for path, post, values in parsed:
        note: dict[str, Any] | None = None
        stored_id = frontmatter_note_id(post)
        if stored_id is not None:
            note = notes_by_id.get(stored_id)

        # Compatibilidade com notas já criadas antes da introdução de
        # anki_note_id. O campo principal só é seguro quando é único no
        # Markdown e no Anki; duplicidade deve resultar em uma nota nova.
        if note is None:
            primary_value = values.get(fields[0], "").strip()
            candidates = (
                notes_by_primary.get(primary_value, [])
                if primary_value and primary_counts.get(primary_value) == 1
                else []
            )
            if len(candidates) == 1:
                note = candidates[0]
            elif len(candidates) > 1:
                print(f"  ⚠️ {folder_name}/{path.stem}: múltiplas notas no Anki para {fields[0]}={primary_value!r}; será criada uma nota nova")

        pending.append((path, post, values, note))

    # Fase 2: Markdown é a fonte dos campos gerenciados. updateNoteFields
    # preserva a nota e o histórico; addNote só é usado para notas novas.
    created = updated = failed = 0
    for path, post, values, note in pending:
        try:
            desired_fields = note_fields(values, fields)
            if note is not None:
                changed = update_existing_note(note, desired_fields)
                update_sync_metadata(path, int(note["noteId"]))
                update_index(index, path.stem)
                if changed:
                    updated += 1
                    print(f"  🔄 {folder_name}/{path.stem}: nota atualizada ({note['noteId']})")
                else:
                    print(f"  ↪ {folder_name}/{path.stem}: já sincronizada ({note['noteId']})")
                continue

            note_id = invoke("addNote", {"note": {
                "deckName": deck, "modelName": model, "fields": desired_fields,
                "options": {
                    "allowDuplicate": folder_name == "Production",
                    "duplicateScope": "deck",
                },
                "tags": ["english", folder_name.lower().replace(" ", "-")],
            }})
            if note_id is None:
                raise RuntimeError("AnkiConnect não retornou o ID da nota")
            update_sync_metadata(path, int(note_id))
            update_index(index, path.stem)
            print(f"  ✅ {folder_name}/{path.stem}: nota criada ({note_id})")
            created += 1
        except Exception as exc:
            print(f"  ❌ {folder_name}/{path.stem}: {exc}")
            failed += 1
    orphaned = len(notes_by_id) - sum(1 for _, _, _, note in pending if note is not None)
    if orphaned:
        print(f"  ℹ️ {folder_name}: {orphaned} nota(s) do Anki não encontradas no Markdown; preservadas")
    return created, updated, failed


def main() -> int:
    invoke("version")
    created = updated = failed = 0
    for folder_name, config in DECKS.items():
        current_created, current_updated, current_failed = sync_folder(folder_name, config)
        created += current_created
        updated += current_updated
        failed += current_failed
    if created == 0 and updated == 0 and failed == 0:
        print("✅ Nenhum flashcard pendente para sincronizar.")
    else:
        print(f"\n📊 Criadas: {created} | Atualizadas: {updated} | Falharam: {failed}")
    return 1 if failed else 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\n⚠️ Operação cancelada.")
        sys.exit(130)
    except Exception as exc:
        print(f"❌ Erro fatal: {exc}")
        sys.exit(1)
