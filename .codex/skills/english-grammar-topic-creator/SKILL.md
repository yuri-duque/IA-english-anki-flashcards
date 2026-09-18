---
name: english-grammar-topic-creator
description: "Creates didactic English grammar-topic notes from a topic name or excerpt. Use for lesson-style grammar modules; not for vocabulary or standalone flashcards."
---

# English Grammar Topic Creator

Create a coherent set of English-language Markdown notes for studying an English grammar topic. The input may be a topic name, one or more forms, a short excerpt, or a broad label such as `quantifiers`.

Use this skill for lesson-style notes in `flashcards/Grammar Patterns/`. Do not use it for vocabulary, phrasal verbs, or an Anki-only request. If the user asks specifically for flashcards, use `english-grammar-flashcard-creator` instead.

## Required reference

Before proposing or creating notes, read [templates/didactic-note-template.md](../../../templates/didactic-note-template.md). It defines the required note shape and the quality rules for examples, Mermaid diagrams, and exercises.

## Phase 1 — resolve, analyse, and propose

Do not create or modify notes in this phase.

1. Classify the input:
   - A named grammatical area, such as `quantifiers`.
   - Specific forms, such as `a, an, some, and any`.
   - A grammar excerpt that may contain several concepts.
2. Normalize it into a conceptual topic name and a lowercase hyphenated folder slug. Do not merely turn a list of words into a folder name if a clearer grammatical concept exists.
3. Resolve the intended scope. Search `flashcards/Grammar Patterns/` and related English notes for equivalent or overlapping topics. State the interpretation, existing notes, and any ambiguity that would materially change the module. For example, `a, an, some, and any` may require a combined articles-and-quantifiers module or two separate modules depending on the learner's intended scope.
4. Build a teaching map before choosing files:
   - essential concepts and forms;
   - meaningful contrasts and common confusions;
   - affirmative, negative, question, past, future, or perfect forms when those forms are natural for the target structure;
   - register, frequency, regional variation, and prerequisites when they affect use;
   - adjacent concepts that should be deferred because they express a different meaning.
5. Divide the module by learning decisions, not by arbitrary word lists. A different function, register, or example is not by itself a reason for a new file: keep closely related variations (affirmative, negative, questions, permission, requests, and common contexts) with the form or contrast they explain. Create separate files only when the parts have substantially different core behaviour—such as a different time reference, syntax, meaning contrast, prerequisite, or error pattern—and would become confusing or unwieldy in one lesson. Never make a file for every individual word or function.
6. When several related forms are provided, one file per form can be appropriate only if each form has a distinct central behaviour; otherwise use one comparative file. For example, `can` and `could` may be organized as two files for present versus past/conditional behaviour, while permission and request variants stay inside the relevant form's file. State why the split improves study rather than assuming that each form needs its own file.
7. Propose the folder and the numbered files. For each file, give its main contrast, the learner's decision it teaches, and the expected difficulty. Keep the first module focused; put advanced or semantically different extensions in a future module.
7. Ask for explicit approval before creating or altering files. The user may approve all files or selected numbers.

## Phase 2 — create approved notes

1. Recheck the proposed folder and duplicates. Never overwrite an existing note without specific authorization.
2. Create only approved files directly inside `flashcards/Grammar Patterns/<topic-slug>/` and preserve numeric prefixes for study order.
3. Write the note content in English unless the user explicitly requests another language.
4. Follow the required template. Keep every section that is applicable; `Examples in context`, `Decision guide`, `Common pitfalls`, and `Mini practice` are mandatory for every note.
5. Use complete form patterns, such as `subject + will have to + base verb + rest of the sentence`, rather than abbreviated labels such as only `will have to`.
6. Use a Mermaid `flowchart` in each `Decision guide` when there is a real usage choice. It must help the learner choose by meaning or context, not repeat the form table.
7. Make the mini practice short and retrieval-focused. Include an answer key in a Markdown `<details>` block. When more than one answer is natural, state the accepted alternatives or rewrite the exercise.
8. Keep examples natural, varied, and contextual. Do not use translations as a substitute for explanation when the module is English-only.

## Teaching and scope rules

- Explain a useful generalization without presenting it as an absolute rule when English usage is more nuanced. For example, `must` and `have to` can both describe external rules; the distinction is not simply internal versus external obligation.
- Teach contrasts explicitly when confusing one form changes the meaning, such as `mustn't` versus `don't have to`.
- Mark less common, formal, British, or American forms when that changes a learner's best default choice.
- Do not force nonexistent forms. Explain a replacement when a structure does not normally take a past, future, or question form.
- Keep the module compact and progressive. There is no target number of notes: start with one note when the topic is coherent, and expand only when each additional file teaches a substantially different behaviour or decision that would impair clarity if combined. A typical topic may therefore have one to several notes, but convenience, word lists, or isolated functions are insufficient justification for a split.
- Do not add flashcard fields or `Study cards` sections by default. Flashcards are a separate workflow.

## Completion

After creation, report the folder, files created, existing duplicates skipped, and any concepts intentionally deferred. Briefly state how the chosen organization supports study order.
