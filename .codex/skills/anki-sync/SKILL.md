---
name: anki-sync
description: Sincroniza os flashcards Markdown das subpastas de flashcards com o Anki Desktop via AnkiConnect e atualiza o progresso nos index.md.
---

# Anki Word Sync

Use quando o usuário pedir para sincronizar os flashcards de `flashcards/` com o Anki Desktop.

## Estrutura suportada

O importador procura notas diretamente nestas subpastas, usando o nome da pasta como parte do deck:

```text
flashcards/Vocabulary/       → Vocabulary
flashcards/Sentences/        → Sentences
flashcards/Expressions/      → Expressions
flashcards/Phrasal Verbs/    → Phrasal Verbs
flashcards/Production/       → Production
```

Grammar Patterns fica fora do escopo desta skill por enquanto.

Cada subpasta que será sincronizada precisa conter um `index.md`. O importador ignora a subpasta e informa o problema quando o índice não existir; ele não cria um índice silenciosamente.

As notas são lidas no formato documentado pelos templates em `templates/`: frontmatter no início do arquivo, campos na seção `Dados da nota`, seguidos das seções `Frente` e `Verso`. Cada campo deve usar uma única linha no formato `- **NomeDoCampo:** valor`. Campos sem valor, como `Audio` quando nenhum arquivo foi anexado, devem ser omitidos — não deixados vazios. Para notas legadas de `Vocabulary`, o importador usa o título `# palavra` como `Word` quando esse campo estiver ausente.

`anki: true` registra que a nota foi aceita anteriormente. O campo `anki_note_id` guarda o ID da nota no perfil do Anki e é a forma preferencial de reconciliação. Para notas legadas sem esse campo, o importador usa o primeiro campo do modelo (`Word`, `Sentence`, etc.) quando existe uma única correspondência no deck. O ID não é o ID do card de revisão: é o ID da nota, que pode gerar um ou mais cards.

## Fluxo

1. Verifique se o Anki Desktop está aberto e se o AnkiConnect está instalado.
   - Se `localhost:8765` recusar a conexão, verifique a porta com `lsof -nP -iTCP:8765 -sTCP:LISTEN`.
   - Se houver um processo escutando, mas o script não conseguir acessá-lo, a execução está isolada do host: execute o script com acesso ao host, mediante aprovação, em vez de concluir que o Anki está fechado.
2. Execute `./.codex/skills/anki-sync/run.sh` na raiz do vault.
3. Para cada deck, o script cria ou usa o deck raiz, garante o modelo de nota e faz um `findNotes` seguido de `notesInfo` para trazer todas as notas daquele deck e modelo.
4. O script reconcilia cada Markdown com uma nota existente, preferindo `anki_note_id` e usando o campo principal apenas para notas legadas. Após a reconciliação, registra o ID no frontmatter.
5. Na segunda fase, compara os campos gerenciados do Markdown com os campos da nota. Notas existentes diferentes são atualizadas com `updateNoteFields`, preservando o histórico de revisão; notas novas são criadas com `addNote`.
6. Só depois de a operação no Anki ser aceita, grava `anki: true` e `anki_note_id` no arquivo e atualiza a coluna `Anki` do `index.md`.
7. Notas que existem no Anki, mas não têm Markdown correspondente, são apenas informadas e preservadas; a skill não apaga notas automaticamente.

O script não envia `templates/*-template.md`, `README.md` nem `index.md`. A atualização é feita nos campos da nota; a frente e o verso renderizados continuam sendo produzidos pelos templates do modelo.

Pré-requisitos: Anki Desktop aberto e AnkiConnect disponível em `http://localhost:8765`. O botão `Sync` do Anki ainda precisa ser acionado para enviar as alterações ao AnkiWeb.

## Áudio na frente do card

O campo `Audio` é enviado como HTML pelo `addNote`. Quando contém uma referência de mídia local, por exemplo `[sound:huge-en-us.mp3]`, o Anki associa o arquivo à nota e o template frontal renderiza o player dentro do bloco condicional `{{#Audio}}...{{/Audio}}`. O arquivo precisa existir na coleção de mídia do Anki; uma URL HTTP no campo não é um anexo de mídia confiável.

O sincronizador não baixa nem anexa automaticamente arquivos remotos: ele transmite o valor textual dos campos Markdown. Portanto, antes de marcar a nota como sincronizada, o áudio deve ter sido anexado à coleção de mídia por um fluxo que conheça o arquivo local. Se não houver arquivo real, omitir `Audio` e deixar o bloco de áudio ausente na frente.
