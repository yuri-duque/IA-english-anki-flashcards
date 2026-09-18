# Template — Production

## Objetivo do deck

O deck `English::Production` serve para praticar a produção ativa de palavras, expressões e frases em inglês.

Enquanto `Vocabulary` testa “eu reconheço este termo?”, este deck testa:

> “Consigo recuperar e usar este termo em inglês quando preciso dele?”

## Decisão sobre a frente

A frente fica em **português**, em uma situação ou em uma intenção comunicativa. Ela não deve mostrar a palavra, a frase em inglês nem o áudio.

Neste deck não haverá áudio. O objetivo é exigir a recuperação da forma em inglês sem pistas fonéticas. O áudio pode ser estudado nos próprios cards de `English::Vocabulary`, `English::Sentences`, `English::Expressions` e `English::Phrasal Verbs`.

## Campos da nota

Criar um tipo de nota chamado `English Production` com estes campos:

| Campo | Obrigatório | Conteúdo |
|---|---:|---|
| `Prompt` | sim | Pergunta, tradução ou situação em português |
| `Context` | recomendado | Contexto adicional que torna a resposta específica |
| `Answer` | sim | Palavra, expressão ou frase correta em inglês |
| `PossibleAnswers` | recomendado | Outras respostas naturais aceitáveis |
| `Focus` | recomendado | Termo ou estrutura que está sendo praticado |
| `HowToUse` | recomendado | Como e quando usar a resposta |
| `Example` | opcional | Outro exemplo natural em inglês |
| `ExampleTranslation` | opcional | Tradução do exemplo |
| `CommonMistakes` | opcional | Erros comuns a evitar |
| `Source` | recomendado | Origem ou motivo para estudar o card |

A frente deve fornecer contexto suficiente para evitar várias respostas igualmente corretas. Quando houver mais de uma resposta natural, preencher `PossibleAnswers`.

Na resposta, colocar em negrito somente o termo em foco e suas formas diretamente relacionadas usando `<b>...</b>`. O restante da resposta deve permanecer com formatação normal.

## Card principal — produção inglês

### Front Template

```html
<div class="card production-card">
  <div class="deck-label">ENGLISH · PRODUCTION</div>

  <div class="prompt">{{Prompt}}</div>

  {{#Context}}
  <div class="context">{{Context}}</div>
  {{/Context}}

  <div class="instruction">How would you say this in English?</div>
</div>
```

### Back Template

```html
<hr id="answer" />

<div class="answer">
  <div class="answer-label">Answer</div>
  <div class="answer-text">{{Answer}}</div>

  {{#PossibleAnswers}}
  <div class="section-title">Other natural answers</div>
  <div class="possible-answers">{{PossibleAnswers}}</div>
  {{/PossibleAnswers}}

  {{#Focus}}
  <div class="section-title">Focus</div>
  <div class="focus"><b>{{Focus}}</b></div>
  {{/Focus}}

  {{#HowToUse}}
  <div class="section-title">How to use</div>
  <div class="how-to-use">{{HowToUse}}</div>
  {{/HowToUse}}

  {{#Example}}
  <div class="section-title">Example</div>
  <div class="example">{{Example}}</div>
  {{/Example}}

  {{#ExampleTranslation}}
  <div class="example-translation">{{ExampleTranslation}}</div>
  {{/ExampleTranslation}}

  {{#CommonMistakes}}
  <div class="section-title">Common mistakes</div>
  <div class="common-mistakes">{{CommonMistakes}}</div>
  {{/CommonMistakes}}

  {{#Source}}
  <div class="source">Source: {{Source}}</div>
  {{/Source}}
</div>
```

## CSS

```css
.card {
  background: #f7f8fa;
  color: #20242a;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  font-size: 20px;
  line-height: 1.45;
  padding: 28px 20px;
  text-align: center;
}

.production-card {
  min-height: 260px;
}

.deck-label {
  color: #718096;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.12em;
  margin-bottom: 30px;
}

.prompt {
  color: #0f766e;
  font-size: clamp(25px, 5vw, 38px);
  font-weight: 600;
  margin: 28px auto;
  max-width: 720px;
}

.context {
  background: #ccfbf1;
  border-radius: 8px;
  color: #115e59;
  font-size: 17px;
  margin: 18px auto;
  max-width: 650px;
  padding: 12px 16px;
}

.instruction {
  color: #64748b;
  font-size: 15px;
  margin-top: 34px;
}

hr#answer {
  border: 0;
  border-top: 1px solid #d8dee8;
  margin: 28px 0;
}

.answer {
  text-align: left;
}

.answer-label {
  color: #64748b;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-align: center;
  text-transform: uppercase;
}

.answer-text {
  color: #15803d;
  font-size: 28px;
  font-weight: 500;
  margin: 10px 0 24px;
  text-align: center;
}

.section-title {
  color: #64748b;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.1em;
  margin: 24px 0 7px;
  text-transform: uppercase;
}

.possible-answers,
.focus,
.how-to-use,
.example,
.common-mistakes,
.example-translation {
  color: #475569;
  font-size: 17px;
}

.possible-answers,
.focus,
.how-to-use,
.common-mistakes {
  background: #ffffff;
  border-radius: 6px;
  padding: 10px 12px;
}

.focus {
  color: #0f766e;
  font-size: 20px;
  font-weight: 700;
}

.example {
  background: #ecfdf5;
  border-radius: 8px;
  color: #065f46;
  padding: 14px 16px;
}

.answer-text b,
.focus b,
.how-to-use b,
.example b,
.possible-answers b {
  color: #047857;
  font-weight: 800;
}

.example-translation {
  margin-top: 8px;
}

.source {
  color: #94a3b8;
  font-size: 12px;
  margin-top: 28px;
}

@media (prefers-color-scheme: dark) {
  .card {
    background: #171a21;
    color: #e5e7eb;
  }

  .context,
  .example {
    background: #042f2e;
    color: #ccfbf1;
  }

  .possible-answers,
  .focus,
  .how-to-use,
  .common-mistakes {
    background: #222631;
  }
}
```

## Exemplo preenchido

```text
Prompt: Eu preciso buscar meu irmão depois do trabalho.
Context: Estou falando sobre ir até algum lugar para buscar uma pessoa.
Answer: I need to <b>pick up</b> my brother after work.
PossibleAnswers: I have to <b>pick up</b> my brother after work.
Focus: pick up
HowToUse: <b>Pick up</b> significa buscar alguém em algum lugar neste contexto. Também pode significar pegar um objeto.
Example: Can you <b>pick me up</b> at eight?
ExampleTranslation: Você pode me buscar às oito?
CommonMistakes: Não dizer “pick my brother up” quando o objeto for um pronome. Com pronome, use <b>pick him up</b>.
Source: flashcards/words/pick.md
```

## Visualização em Markdown

### Frente

```markdown
### ENGLISH · PRODUCTION

Eu preciso buscar meu irmão depois do trabalho.

_Estou falando sobre ir até algum lugar para buscar uma pessoa._

_How would you say this in English?_
```

### Verso

```markdown
**Answer**

I need to **pick up** my brother after work.

#### Other natural answers

I have to **pick up** my brother after work.

#### Focus

**pick up**

#### How to use

**Pick up** significa buscar alguém em algum lugar neste contexto. Também pode significar pegar um objeto.

#### Example

Can you **pick me up** at eight?

_Você pode me buscar às oito?_

#### Common mistakes

Não dizer “pick my brother up” quando o objeto for um pronome. Com pronome, use **pick him up**.

_Source: flashcards/words/pick.md_
```

## Regras de qualidade

- A frente deve conter uma intenção ou situação específica, não apenas uma tradução solta.
- Não mostrar o inglês, o áudio ou a pronúncia antes da tentativa.
- Criar uma resposta principal natural e registrar alternativas em `PossibleAnswers`.
- Não exigir uma única formulação quando várias respostas forem corretas.
- Colocar em negrito somente o termo em foco e suas formas relacionadas na resposta; não colocar a resposta inteira em negrito.
- Mostrar padrões, preposições e posição de pronomes quando forem importantes.
- Usar `HowToUse` para explicar a escolha da resposta, sem transformar o card em uma aula longa.
- Se o card tiver muitas respostas possíveis, adicionar mais contexto ou movê-lo para `English::Sentences`.
- Usar `Again` quando não conseguir produzir a resposta, mesmo que tenha reconhecido a palavra em outro deck.
- Não adicionar áudio a este deck.
