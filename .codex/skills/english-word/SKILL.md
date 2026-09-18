---
name: english-word
description: Estudo e documentação de palavras em inglês em flashcards/words, mantendo o índice e o progresso de estudo/Anki.
---

# English Word

Use esta skill quando o usuário quiser estudar, adicionar, documentar ou atualizar o progresso de uma palavra em inglês.

Esta skill mantém a documentação detalhada das palavras em `flashcards/words/`. A pasta histórica `flashcards/words/` ainda precisa ser recuperada ou criada antes de usar este fluxo.

Regras essenciais:

- Salve a palavra em `flashcards/words/<palavra-normalizada>.md`.
- Atualize `flashcards/words/index.md`, mantendo a tabela em ordem alfabética.
- Preserve `estudado` e `anki` ao complementar ou regenerar um documento existente.
- Não marque `estudado` ou `anki` como `true` por inferência; só faça isso quando o usuário pedir.
- Responda no idioma do usuário e mantenha o documento em português, com exemplos em inglês e tradução.
