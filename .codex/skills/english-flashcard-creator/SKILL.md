---
name: english-flashcard-creator
description: "Analisa itens lexicais em inglês, propõe decks e cria, após aprovação explícita, flashcards Markdown de Vocabulary, Sentences, Expressions, Phrasal Verbs e Production. Não cria cards de gramática."
---

# English Flashcard Creator

Use esta skill quando o usuário quiser transformar uma palavra, expressão, phrasal verb ou frase em inglês em flashcards Markdown. Use `english-grammar-flashcard-creator` para padrões gramaticais.

## Contratos do vault

Os templates em `templates/` são a fonte de verdade para formato, campos, direção do card e critérios de qualidade. Antes de propor ou criar uma nota, leia o template de cada deck candidato:

- `vocabulary-template.md`
- `sentences-template.md`
- `expressions-template.md`
- `phrasal-verbs-template.md`
- `production-template.md`

Os destinos suportados são `flashcards/Vocabulary/`, `Sentences/`, `Expressions/`, `Phrasal Verbs/` e `Production/`. Não crie `Grammar Patterns` nesta skill.

Crie conteúdo explicativo em português; mantenha termos, exemplos e instruções do card em inglês conforme o template. Os arquivos Markdown registram os campos, a frente e o verso legíveis; não copie HTML/CSS dos templates para a nota.

## Fase 1 — análise e aprovação

Não crie nem altere arquivos nesta fase.

1. Identifique o item e valide sua grafia. Para termos raros, gíria, nomes próprios ou dúvidas reais, consulte uma fonte confiável. Se houver provável erro, mostre a correção e peça confirmação antes de seguir.
2. Classifique o item: palavra/termo lexical, frase completa, expressão fixa ou phrasal verb. Não classifique uma combinação incidental de palavras como expressão. Quando for principalmente um padrão gramatical, encaminhe para a skill de gramática.
3. Determine os decks candidatos pelo objetivo de estudo, não apenas pelas palavras que aparecem na entrada. Um item pode pertencer a mais de um deck quando cada card treinar uma habilidade distinta.
4. Procure duplicatas nos diretórios candidatos pelo nome normalizado e pelo conteúdo. Normalize para minúsculas, hífens entre palavras e sem acentos no nome do arquivo.
5. Leia os templates aplicáveis e prepare uma proposta curta: classificação, decks e motivo, arquivos já existentes, arquivos novos e candidatos descartados quando houver ambiguidade.
6. Para cada novo card de `Vocabulary`, proponha obrigatoriamente três cards distintos de `Production`. Eles devem exigir recuperação ativa em contextos diferentes e ter respostas naturais, não três variações superficiais do mesmo prompt.
7. Peça aprovação explícita dos diretórios e cards que serão criados. Silêncio, comentários vagos ou uma nova pergunta não autorizam escrita. A aprovação de um Vocabulary inclui as três propostas de Production correspondentes.

## Fase 2 — criação aprovada

Somente depois de uma aprovação clara:

1. Revalide grafia, duplicatas e os caminhos autorizados. Nunca sobrescreva uma nota: informe a duplicata e peça autorização específica para complementar ou atualizar; pular é o padrão.
2. Leia novamente o template de cada deck aprovado e gere apenas os arquivos autorizados. Separe sentidos que demandem contexto ou cards distintos.
3. Comece toda nota com frontmatter YAML contendo `anki: false`. Preservar `anki` e `anki_note_id` existentes é obrigatório ao complementar uma nota.
4. Preencha todos os campos obrigatórios do template e mantenha os opcionais apenas quando forem úteis e verificáveis. Destaque somente o termo ou a forma diretamente relacionada; a resposta inteira não deve ficar em negrito.
5. Atualize ou crie o `index.md` do deck com o link da nota e estado `❌`. Não marque `anki: true`: isso cabe exclusivamente à skill `anki-sync` após a aceitação pelo Anki.
6. Execute `python3 .codex/skills/english-flashcard-creator/scripts/validate_flashcards.py <caminhos-criados>` antes de concluir. Corrija qualquer falha estrutural reportada.
7. Confirme caminhos criados, decks usados, duplicatas puladas, candidatos descartados, atualização dos índices e eventuais pendências.

## Áudio

Áudio é opcional e nunca bloqueia a criação de um card. Só pesquise ou obtenha áudio quando o usuário solicitar ou quando houver um fluxo de mídia realmente disponível.

Para `Vocabulary`, siga a prioridade e o procedimento de `templates/vocabulary-template.md`: Wiktionary/Wikimedia Commons, com licença verificada na página do arquivo. Consulte [references/audio-sources.md](references/audio-sources.md) somente quando estiver pesquisando áudio.

Preencha `Audio`, `AudioSource` e `AudioLicense` somente quando houver um arquivo de mídia local verificável, já anexado à coleção do Anki, uma fonte real e licença confirmada. Caso contrário, omita os três campos; não use valores vazios, "pendente", nomes inventados ou URL remota em `Audio`.

O sincronizador não baixa nem anexa áudio remoto. Não altere o catálogo de fontes automaticamente durante a criação de cards; registre uma nova fonte somente quando o usuário aprovar essa manutenção.

## Limites de responsabilidade

- Esta skill decide conteúdo, classificação e a proposta pedagógica.
- O script de validação verifica apenas a estrutura; ele não prova que uma tradução, exemplo ou classificação é boa. Revise esses aspectos antes de criar.
- `anki-sync` é responsável pela integração com Anki Desktop e por marcar notas aceitas como sincronizadas.
