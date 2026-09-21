# IA English Anki Flashcards

Repository dedicated to studying English with Markdown flashcards and optional synchronization with Anki Desktop through AnkiConnect, that we can create flashcards to **Vocabulary**, **Expressions**, **Phrasal Verbs** and **Production**.

<img width="1672" height="941" alt="post-flashcards" src="https://github.com/user-attachments/assets/361fe7be-d2b6-4ac9-a3bc-67dc49a0a8b3" />

#### Exemples of flashcards on anki:

Vocabulary

<img width="773" height="1600" alt="vocabulary-frente" src="https://github.com/user-attachments/assets/5e7de0ef-be9b-4ea1-97bc-4a8261cf8a1c" />
<img width="771" height="1600" alt="vocabulary-verso" src="https://github.com/user-attachments/assets/1e8c53f9-2bc8-4e95-9d13-ded8506e404c" />


Production

<img width="775" height="1600" alt="production-frente" src="https://github.com/user-attachments/assets/e4be8fba-029b-45c7-b3d2-c7629cde0c96" />
<img width="769" height="1600" alt="production-verso" src="https://github.com/user-attachments/assets/f0aa90c6-7827-42d1-91d0-cdf8980142d1" />



## Structure

```text
flashcards/
├── Vocabulary/
├── Expressions/
├── Phrasal Verbs/
├── Production/
└── Grammar Patterns/
templates/
.codex/skills/
```

Cards are stored in `flashcards/`. The templates used to create them are centralized in `templates/`. `Grammar Patterns` notes are instructional material and are not synchronized by the current importer.

## Creating flashcards

Use the skills in `.codex/skills/`:

- `english-flashcard-creator`: Vocabulary, Expressions, Phrasal Verbs, Sentences, and Production;
- `english-grammar-flashcard-creator`: grammar-pattern cards;
- `english-grammar-topic-creator`: instructional grammar notes;
- `anki-sync`: synchronization with Anki Desktop.

The creation workflow has two phases: first, the skill analyzes the item, checks for duplicates, selects the template, and requests approval; the files are created only after approval.

For each new `Vocabulary` card, also create at least three distinct `Production` cards with different prompts or situations.

Every card must:

1. follow the deck template;
2. begin with YAML front matter containing `anki: false`;
3. contain the `Dados da nota`, `Frente`, and `Verso` sections;
4. be included in the `index.md` file for its respective deck.

After Anki accepts the note, the synchronizer adds `anki_note_id` and changes `anki` to `true`. Do not edit these fields manually.

## Templates

| Template | Uso |
|---|---|
| `templates/vocabulary-template.md` | Words and lexical terms |
| `templates/sentences-template.md` | Complete sentences |
| `templates/expressions-template.md` | Fixed and idiomatic expressions |
| `templates/phrasal-verbs-template.md` | Phrasal verbs |
| `templates/production-template.md` | Active production from Portuguese, context, or intent |
| `templates/grammar-patterns-template.md` | Grammar patterns for filling in the blanks |
| `templates/didactic-note-template.md` | Instructional grammar notes |

Read the corresponding template before creating or updating a note. Anki's HTML/CSS belongs to the Anki model; Markdown files should remain easy to review.

## AnkiConnect setup

1. Install Anki Desktop.
2. In Anki, open `Tools > Add-ons > Get Add-ons...`.
3. Install AnkiConnect using the code published by the project.
4. Restart Anki Desktop.
5. Keep Anki open during synchronization.

The synchronizer expects AnkiConnect at:

```text
http://localhost:8765
```

Back up your collection before the first run.

## Synchronizing cards

From the root of this repository, run:

```bash
./.codex/skills/anki-sync/run.sh
```

The script processes the following directories and Anki root decks:

| Directory | Deck |
|---|---|
| `flashcards/Vocabulary/` | `Vocabulary` |
| `flashcards/Sentences/` | `Sentences` |
| `flashcards/Expressions/` | `Expressions` |
| `flashcards/Phrasal Verbs/` | `Phrasal Verbs` |
| `flashcards/Production/` | `Production` |

Deck names are kept as they are to avoid creating duplicates. After the script finishes, use Anki's `Sync` button to send the changes to AnkiWeb.

The synchronizer updates existing notes when it finds `anki_note_id` or a single match by the primary field. Orphaned notes in Anki are reported and preserved; they are not deleted automatically.

Grammar Patterns is not part of this workflow because its notes are stored in subfolders and use a different instructional format. A dedicated synchronizer may be defined in the future.

## Audio

The `Audio` field should contain a local media reference, such as `[sound:word-en-us.mp3]`, only when the file already exists in Anki's media collection. The importer does not download remote audio automatically.

## Troubleshooting

If the connection fails, make sure Anki is open and check the port:

```bash
lsof -nP -iTCP:8765 -sTCP:LISTEN
```

If the port is open but the script cannot access it, run the synchronizer in an environment with access to the host where Anki is running.

## Dependencies

The script uses Python 3, `requests`, and `python-frontmatter`. `run.sh` creates `.venv/` when necessary and installs these dependencies. They are also listed in `requirements.txt`.

## Legacy content

Some migrated notes still point to `flashcards/words/`, but this folder does not exist in the current source state. The recovery of these historical files should be decided before relying on the `english-word` skill.
