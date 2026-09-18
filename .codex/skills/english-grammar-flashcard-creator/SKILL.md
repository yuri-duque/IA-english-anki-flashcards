---
name: english-grammar-flashcard-creator
description: "Analisa tópicos ou textos de gramática inglesa, propõe cards de Grammar Patterns para aprovação e cria notas Markdown organizadas em subpastas por conteúdo."
---

# English Grammar Flashcard Creator

Use esta skill quando o usuário fornecer um tópico, explicação, anotação ou texto sobre gramática inglesa e quiser transformá-lo em flashcards. O conteúdo pode ser impreciso ou ter um nome informal; propor um nome conceitual melhor quando necessário.

## Fonte de verdade

Antes de gerar qualquer nota, ler [templates/grammar-patterns-template.md](../../../templates/grammar-patterns-template.md). Seguir seus campos, o card de completar lacuna e a visualização em Markdown. O deck corresponde a `English::Grammar Patterns`.

Não criar cards de vocabulário, expressões ou phrasal verbs. Se o material misturar gramática com esses conteúdos, separar os conceitos e informar quais partes pertencem a outra skill.

## Organização dos arquivos

O destino padrão é:

```text
flashcards/Grammar Patterns/<topic-slug>/
```

Usar um `topic-slug` em minúsculas, sem acentos, com hífens e baseado no nome conceitual aprovado. Cada arquivo deve manter o prefixo do conteúdo:

```text
flashcards/Grammar Patterns/quantifiers/
├── 01-quantifiers-overview.md
├── 02-some-any.md
└── 03-much-many.md
```

Os cards ficam diretamente na subpasta do conteúdo; não criar subpastas por subtema. Se a pasta já existir, examinar seus arquivos e propor complementação, sem sobrescrever. O nome original do usuário pode ser registrado em `Source` ou em uma seção de metadados.

## Fluxo obrigatório

### Fase 1 — análise e proposta

Não criar ou alterar arquivos nesta fase.

1. Identificar se a entrada é um tópico curto ou um material explicativo.
2. Extrair os padrões gramaticais realmente ensinados e descartar repetições.
3. Normalizar o conceito e propor um nome melhor quando o nome recebido for amplo, informal ou incorreto.
4. Dividir assuntos amplos em subtemas úteis. Por exemplo, `would` pode envolver hipóteses, pedidos educados, hábitos passados e `would rather`.
5. Pesquisar a pasta `flashcards/Grammar Patterns/` e o conteúdo relacionado para detectar notas equivalentes, mesmo com nomes diferentes.
6. Ler o template e preparar uma proposta numerada. Para cada card, informar brevemente:
   - subtema;
   - tipo de exercício;
   - estrutura testada;
   - frase ou situação resumida;
   - eventual contraste ou erro comum.
7. Preferir poucos cards não redundantes. Como referência, sugerir 3–5 cards para um tópico simples e 5–10 para um tópico amplo.
8. Apontar ambiguidades, respostas alternativas, nível estimado e partes que foram descartadas.
9. Pedir aprovação explícita, permitindo aprovação total ou parcial por número. Perguntas, comentários vagos ou silêncio não autorizam a criação.

Tipos possíveis: completar lacuna, cloze, corrigir erro, tradução para produção, escolha contextual entre formas e contraste entre estruturas. Usar apenas os tipos que testem uma habilidade clara.

Exemplo de proposta:

```text
Nome sugerido: quantifiers
Pasta: flashcards/Grammar Patterns/quantifiers/

1. some × any — escolha contextual em frases afirmativas, negativas e perguntas.
2. much × many — completar lacuna distinguindo incontáveis e contáveis.
3. few × a few — contraste de sentido positivo e negativo.

Já existem: nenhum.
Posso criar os cards 1–3? Você também pode aprovar apenas números específicos.
```

### Fase 2 — criação após aprovação

1. Revalidar o nome, a pasta, as duplicatas e os cards aprovados.
2. Criar somente os cards autorizados e a pasta do conteúdo, se necessário.
3. Usar o template `grammar-patterns-template.md`, preenchendo `SentenceWithBlank`, `Answer`, `CompletedSentence`, `Translation`, `Pattern`, `HowToUse`, `Focus` e os campos opcionais relevantes.
4. Criar uma única habilidade principal por card. A frente deve exigir recuperação ativa e não revelar a resposta por tradução ou explicação.
5. Garantir contexto suficiente para existir uma resposta preferencialmente única. Se houver mais de uma resposta natural, reescrever a frase ou transformar o card em contraste explícito.
6. Usar exemplos naturais em inglês e explicações em português. Destacar somente o foco e as formas diretamente relacionadas.
7. Incluir `CommonMistakes` quando o contraste for uma fonte provável de erro, sem transformar o verso em uma aula longa.
8. Adicionar tags úteis, como `grammar`, subtema e nível estimado (`A1`–`C1`), quando puderem ser inferidos com segurança.
9. Nunca sobrescrever nota existente. Se houver uma nota equivalente, informar o caminho e pular por padrão; só atualizar ou complementar mediante autorização específica.

## Critérios de qualidade

- Um card deve testar uma decisão gramatical, não apenas pedir a definição de uma regra.
- Cards contrastivos devem fornecer contexto suficiente para distinguir as alternativas.
- Não transformar cada frase do texto original em um card.
- Não criar automaticamente versões de reconhecimento e produção para tudo; propor produção quando ela acrescentar valor.
- Separar usos diferentes da mesma forma quando o contexto e o significado mudarem.
- Registrar a fonte do texto ou do tópico quando disponível.
- Áudio é opcional nesta skill e só deve ser incluído se houver uma necessidade clara de prática oral e uma fonte real; nunca inventar arquivos, URLs ou licenças.

## Confirmação final

Depois de criar, informar os arquivos criados, a subpasta usada, os cards aprovados que foram descartados ou já existiam, eventuais duplicatas puladas e qualquer pendência de conteúdo.
