---
name: english-flashcard-creator
description: "Analisa palavras, expressões e phrasal verbs, pede aprovação e cria arquivos Markdown de flashcards nos decks de inglês do vault. Não cria cards de gramática."
---

# English Flashcard Creator

Use esta skill quando o usuário fornecer uma palavra, expressão, phrasal verb ou frase em inglês e quiser transformá-la em um ou mais arquivos Markdown de flashcards.

## Escopo

Esta skill cria cards para estes diretórios, usando os templates correspondentes como fonte de verdade:

```text
flashcards/Vocabulary/
flashcards/Sentences/
flashcards/Expressions/
flashcards/Phrasal Verbs/
flashcards/Production/
```

Não criar cards de `Grammar Patterns`. Quando o conteúdo for principalmente um padrão gramatical, informar que ele pertence a uma skill separada e não criar o arquivo nesta skill.

Os templates ficam em `templates/`:

- `vocabulary-template.md`
- `sentences-template.md`
- `expressions-template.md`
- `phrasal-verbs-template.md`
- `production-template.md`

Áudio é opcional, mas deve ser procurado automaticamente para palavras e expressões elegíveis durante a análise do card. Consultar [references/audio-sources.md](references/audio-sources.md) e tentar primeiro o 1000EnglishWords quando o item for uma palavra isolada. Se não houver correspondência, o arquivo não puder ser obtido com segurança ou a licença não estiver clara, deixar `Audio`, `AudioSource` e `AudioLicense` vazios e continuar sem bloquear a criação do card.

Ler o template correspondente antes de gerar o arquivo. Não copiar o CSS ou o HTML do Anki para os arquivos de conteúdo; os arquivos Markdown devem registrar os campos preenchidos e uma visualização legível do card, seguindo rigorosamente o modelo do template.

Para `flashcards/Vocabulary`, o template oficial é o único formato válido. Não usar cards existentes como fonte de estrutura quando eles divergirem de `templates/vocabulary-template.md`.

## Fluxo obrigatório em duas fases

### Fase 1 — analisar e pedir aprovação

Quando receber o conteúdo, não criar nem alterar arquivos ainda.

1. Interpretar o que o usuário forneceu: palavra, frase, expressão fixa, phrasal verb ou padrão gramatical.
2. Normalizar o texto para comparação, preservando a forma original para o conteúdo do card.
3. Validar a grafia. Para palavras comuns, usar o conhecimento linguístico; para termos raros, gírias, nomes próprios ou casos duvidosos, consultar uma fonte confiável. Se houver provável erro, apresentar a correção e pedir confirmação antes de continuar.
4. Identificar todos os templates aplicáveis. Um item pode pertencer a mais de um deck, mas não deve ser colocado em um deck apenas porque uma palavra aparece incidentalmente em uma frase.
5. Verificar se já existe um arquivo equivalente em cada diretório candidato, considerando caixa, hífens, espaços e acentos na normalização do nome.
6. Ler o template de cada candidato e preparar uma proposta curta de conteúdo.
7. Responder com uma análise para aprovação contendo:
   - item reconhecido e grafia normalizada;
   - templates candidatos e motivo de cada um;
   - três propostas distintas de `flashcards/Production` para cada novo card de `flashcards/Vocabulary`;
   - templates descartados e motivo, quando houver ambiguidade;
   - arquivos que já existem;
   - arquivos novos que seriam criados;
   - resultado da busca de áudio: arquivo obtido, fonte encontrada sem arquivo local ou ausência de correspondência;
   - eventual correção de grafia ou informação que precise de confirmação.
8. Pedir aprovação explícita. Exemplo:

```text
Encontrei "pick up".

Proposta:
- Expressions — não aplicável: não é uma expressão idiomática fixa neste uso.
- Phrasal Verbs — aplicável: verbo + partícula, com mais de um sentido.
- Production — obrigatório: cada novo Vocabulary gera pelo menos três cards de produção distintos.

Já existe: nenhum arquivo.
Criaria:
- flashcards/Phrasal Verbs/pick-up.md
- flashcards/Production/pick-up-01.md
- flashcards/Production/pick-up-02.md
- flashcards/Production/pick-up-03.md

A grafia está correta. Posso criar os dois arquivos?
```

Antes de pedir aprovação, aplicar o checklist de conteúdo abaixo. Se algum item obrigatório estiver incompleto, não apresentar o card como pronto para criação.

A aprovação deve ser específica o bastante para saber quais diretórios estão autorizados. Não interpretar silêncio, “parece bom” ou uma nova pergunta como autorização para criar.

### Fase 2 — após aprovação

Somente depois de uma aprovação clara:

1. Revalidar a grafia e a existência dos arquivos, pois o estado do vault pode ter mudado entre as mensagens.
2. Não sobrescrever um arquivo existente. Para cada duplicata, mostrar o caminho e perguntar se o usuário quer complementar, atualizar ou pular. A opção padrão é pular.
3. Criar os diretórios aprovados se ainda não existirem.
4. Gerar o conteúdo em português, mantendo os termos e exemplos em inglês.
5. Aplicar o template do deck escolhido, incluindo campos úteis, visualização em Markdown e as regras de formatação daquele template.
6. Destacar em negrito somente o termo ou trecho em foco. Não colocar a resposta inteira em negrito.
7. Para campos que contenham múltiplas traduções, listar primeiro a tradução mais provável no contexto e depois as alternativas relevantes.
8. Tentar obter áudio de palavra isolada em `https://www.1000englishwords.com/audio/#top`. Se a palavra não estiver na lista, o player não expuser um arquivo utilizável ou a licença/condição de reutilização não puder ser verificada, deixar os campos de áudio vazios.
9. Só registrar `[sound:arquivo.mp3]` em `Audio` quando o arquivo real tiver sido anexado à coleção de mídia do Anki. O sincronizador atual não baixa arquivos remotos automaticamente. Registrar `AudioSource` com a página de origem e `AudioLicense` somente com informação verificada; se houver apenas uma página ou um arquivo remoto, não preencher `Audio`.
10. Nunca inventar nomes de arquivos, URLs, fontes ou licenças. A existência de um áudio na internet não significa que ele já esteja anexado à coleção de mídia do Anki.
11. Confirmar os caminhos criados e resumir quais decks foram preenchidos.

Para cada novo arquivo de `flashcards/Vocabulary/`, criar obrigatoriamente pelo menos três arquivos distintos em `flashcards/Production/`. Os três cards devem usar prompts ou situações diferentes e exercitar usos relevantes do vocabulário; não criar três cópias do mesmo card.

### Checklist obrigatório — Vocabulary

Todo arquivo de `flashcards/Vocabulary/` deve conter os itens abaixo, tanto nos dados da nota quanto na visualização do verso:

- [ ] `Meaning`: significado principal em português, seguido das alternativas relevantes;
- [ ] `PartOfSpeech`: classe gramatical;
- [ ] `Definition`: definição curta em inglês — obrigatória, nunca deixar vazia;
- [ ] `HowToUse`: explicação em português sobre quando e como usar o termo;
- [ ] `Example`: pelo menos uma frase natural em inglês, com o termo em foco destacado;
- [ ] `ExampleTranslation`: tradução de cada exemplo, apresentada logo abaixo dele;
- [ ] `CommonExpressions`: expressões frequentes e úteis, quando existirem;
- [ ] `WordFamily`: derivados relevantes, quando existirem;
- [ ] `RelatedWords`: avaliar palavras semanticamente relacionadas ou facilmente confundidas e, quando houver, registrar diferenças de uso de forma simples;
- [ ] `Etymology`, `Image` e `Source`: preencher somente quando houver informação relevante e verificável;
- [ ] `Audio`, `AudioSource` e `AudioLicense`: preencher somente conforme as regras de áudio, sem inventar dados;
- [ ] a frente contém apenas o termo em inglês, áudio quando disponível e a instrução em inglês;
- [ ] o verso segue a ordem: significado, classe gramatical, definição, uso, exemplo, tradução, expressões, família de palavras, etimologia, imagem e fonte;
- [ ] quando `RelatedWords` for preenchido, ele aparece junto de `WordFamily`, depois das expressões, com diferenças de uso curtas e claras;
- [ ] campos adicionais, como `NounType` ou `QuantityOrder`, podem ser incluídos, mas não substituem nenhum item obrigatório nem alteram essa ordem;
- [ ] o termo em foco está destacado nos campos e exemplos relevantes;
- [ ] `anki: false` está presente na criação e o índice foi atualizado.
- [ ] pelo menos três cards distintos de `flashcards/Production/` foram criados para este Vocabulary, cada um com `Prompt`, `Answer` e contexto suficiente;

Um card só pode ser criado depois que todos os itens obrigatórios estiverem concluídos. Se não houver uma definição curta confiável em inglês, pesquisar uma fonte adequada ou pedir esclarecimento; não criar o card com `Definition` vazio.

## Como identificar os templates

### Vocabulary

Aplicar quando o item principal for uma palavra individual ou um termo lexical estudado por seus significados, classe gramatical e uso.

O formato do vocabulário é rígido. Os campos `Meaning`, `PartOfSpeech`, `Definition`, `HowToUse`, `Example` e `ExampleTranslation` são obrigatórios. `CommonExpressions`, `WordFamily`, `RelatedWords`, `Etymology`, `Image` e `Source` são incluídos quando aplicáveis, mas não devem ser inventados nem usados para substituir os campos obrigatórios.

Exemplos: `huge`, `ground`, `turn`, `pretty`.

### Sentences

Aplicar quando o item principal for uma frase completa encontrada ou criada para mostrar uso em contexto.

Exemplos: `She stood up when the teacher entered.` ou `I need to pick up my brother after work.`

Uma frase pode gerar também um card de `Production` se o usuário aprovar essa segunda habilidade.

### Expressions

Aplicar quando o item for uma expressão fixa, idiomática ou fórmula comunicativa aprendida como uma unidade.

Exemplos: `by the way`, `once in a while`, `that makes sense`, `It's raining cats and dogs`.

Não classificar toda combinação de palavras como expressão idiomática. Se o sentido for principalmente verbo + partícula, preferir `Phrasal Verbs`.

### Phrasal Verbs

Aplicar quando houver verbo combinado com partícula ou preposição e a combinação funcionar como uma unidade lexical.

Exemplos: `pick up`, `give up`, `look after`, `run out of`.

Registrar traduções, padrão de complemento, separabilidade e posição de pronomes quando relevante.

### Production

Aplicar obrigatoriamente junto com `Vocabulary`: cada novo vocabulário deve gerar pelo menos três cards distintos em `flashcards/Production`, praticando a recuperação ativa a partir de português, situação ou intenção comunicativa.

Na Fase 1, apresentar as três propostas de produção e seus arquivos como parte obrigatória da criação. A aprovação do Vocabulary inclui esses três cards; não tratá-los como candidatos opcionais.

### Grammar Patterns

Não criar nesta skill. Exemplos: `be interested in + -ing`, `avoid doing` e `want to do`. Informar que o item será encaminhado para a skill específica de gramática quando ela existir.

## Validação e duplicatas

Normalizar nomes de arquivo assim:

- minúsculas;
- espaços e pontuação separando palavras convertidos em hífens;
- acentos removidos somente no nome do arquivo;
- extensão `.md`;
- manter a expressão completa, por exemplo `run-out-of.md`.

Antes de criar, pesquisar tanto pelo nome normalizado quanto pelo termo dentro dos arquivos do diretório. Considerar duplicata uma nota que documente o mesmo item, mesmo que o nome do arquivo use outra separação.

Se o usuário fornecer uma palavra com erro provável:

```text
Você escreveu "huje". A forma mais provável é "huge".
Deseja que eu analise "huge"?
```

Não criar o arquivo corrigido sem confirmação.

Se a entrada puder ser uma palavra ou expressão dependendo do contexto, pedir uma frase ou oferecer as classificações possíveis para aprovação.

## Regras de conteúdo

- Responder em português; exemplos e termos estudados permanecem em inglês.
- Usar frases naturais e compreensíveis.
- Não criar definições longas quando uma explicação curta resolve.
- Toda nota de vocabulário deve ter uma `Definition` curta em inglês. Esse campo é obrigatório, mesmo quando a palavra parecer simples.
- Separar sentidos diferentes em cards ou arquivos distintos quando o contexto exigir.
- Colocar possíveis traduções do foco em campo próprio quando o template possuir esse campo.
- Usar `HowToUse` para explicar quando e como usar o termo.
- Incluir expressões comuns somente quando forem realmente úteis e frequentes.
- Avaliar palavras semanticamente relacionadas ou facilmente confundidas. Quando houver alternativas úteis, preencher `RelatedWords` com diferenças de uso simples; não confundir esse campo com `WordFamily`.
- Usar etimologia como informação complementar, nunca como núcleo do card.
- Para palavras isoladas, tentar o 1000EnglishWords antes das demais fontes registradas em [references/audio-sources.md](references/audio-sources.md). Para frases, expressões e phrasal verbs, só buscar áudio quando houver fonte compatível ou quando o usuário solicitar. Se a busca falhar, manter os campos de áudio vazios sem inventar fallback.
- Não inventar fonte, áudio, licença, pronúncia ou exemplo atribuído a uma fonte.
- Preservar alterações existentes e nunca substituir arquivos sem autorização específica.

## Formatação dos arquivos

Cada arquivo criado deve seguir rigorosamente o template do seu deck e conter:

1. título do item;
2. campos da nota preenchidos;
3. seção `Frente` em Markdown;
4. seção `Verso` em Markdown;
5. termo em foco destacado com `<b>...</b>` nos campos HTML e com `**...**` na visualização Markdown;
6. origem do conteúdo e, quando houver, do áudio.

## Controle de sincronização

Todo arquivo de flashcard deve começar com frontmatter YAML contendo:

```yaml
---
anki: false
---
```

O atributo `anki` é obrigatório e representa o estado da nota no Anki. Ao criar um arquivo, use `anki: false`. Nunca marque esse atributo como `true` durante a criação: somente a skill `anki-sync` pode fazer isso depois que o Anki aceitar a nota.

Depois de criar ou atualizar um card, atualizar também o `index.md` da subpasta correspondente (`Vocabulary`, `Sentences`, `Expressions`, `Phrasal Verbs` ou `Production`). Se o índice ainda não existir, criar `index.md` antes de concluir, mantendo uma tabela com o link para cada card e uma coluna `Anki` iniciada com `❌`. Ao complementar um card existente, preservar o valor atual de `anki` e o estado da coluna `Anki`.

Os campos técnicos do Anki ficam documentados nos templates em `templates/`; os arquivos de conteúdo devem ser fáceis de revisar no Obsidian.

## Confirmação final

Depois de criar, informar:

- quais arquivos foram criados;
- quais diretórios/decks foram usados;
- quais candidatos foram descartados;
- se algum arquivo existente foi pulado;
- se a entrada foi corrigida ou se alguma informação ficou pendente.
- se o `index.md` foi criado ou atualizado e qual estado de sincronização foi registrado.
