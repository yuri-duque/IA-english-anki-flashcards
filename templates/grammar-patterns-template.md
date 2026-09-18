# Template — Grammar Patterns

## Objetivo do deck

O deck `English::Grammar Patterns` serve para estudar estruturas recorrentes da língua, e não regras abstratas isoladas.

Exemplos:

- `be interested in doing something`;
- `avoid doing something`;
- `want to do something`;
- `used to do something`;
- `depend on something`.

O foco é lembrar qual forma vem depois de uma palavra ou expressão e conseguir usar o padrão em uma frase natural.

## Decisão sobre a frente

A frente mostra uma frase com uma lacuna e contexto suficiente para que a resposta seja recuperada. O verso mostra a resposta, o padrão completo e uma explicação curta.

Não colocar a resposta, a tradução completa ou uma dica gramatical explícita na frente.

## Campos da nota

Criar um tipo de nota chamado `English Grammar Pattern` com estes campos:

| Campo | Obrigatório | Conteúdo |
|---|---:|---|
| `SentenceWithBlank` | sim | Frase em inglês com a lacuna |
| `Answer` | sim | Palavra ou trecho que completa a lacuna |
| `CompletedSentence` | recomendado | Frase completa em inglês |
| `Translation` | sim | Tradução natural da frase |
| `Pattern` | sim | Estrutura abstrata do padrão |
| `PatternTranslations` | recomendado | Possíveis traduções ou funções |
| `HowToUse` | recomendado | Quando e como usar o padrão |
| `Focus` | recomendado | Palavra, preposição ou forma gramatical principal |
| `Examples` | opcional | Outros exemplos do mesmo padrão |
| `CommonMistakes` | opcional | Erros frequentes |
| `Source` | recomendado | Origem ou motivo para estudar o padrão |

Na resposta, colocar em negrito somente o foco do card e as formas diretamente relacionadas:

```html
I'm interested <b>in learning</b> English.
```

## Card principal — completar o padrão

### Front Template

```html
<div class="card grammar-card">
  <div class="deck-label">ENGLISH · GRAMMAR PATTERNS</div>

  <div class="prompt">Complete the sentence</div>
  <div class="sentence-with-blank">{{SentenceWithBlank}}</div>

  <div class="instruction">Which word or form completes the sentence?</div>
</div>
```

### Back Template

```html
<hr id="answer" />

<div class="answer">
  <div class="answer-label">Answer</div>
  <div class="answer-text"><b>{{Answer}}</b></div>

  {{#CompletedSentence}}
  <div class="section-title">Complete sentence</div>
  <div class="completed-sentence">{{CompletedSentence}}</div>
  {{/CompletedSentence}}

  <div class="section-title">Translation</div>
  <div class="translation">{{Translation}}</div>

  <div class="section-title">Pattern</div>
  <div class="pattern">{{Pattern}}</div>

  {{#PatternTranslations}}
  <div class="section-title">Possible meanings</div>
  <div class="pattern-translations">{{PatternTranslations}}</div>
  {{/PatternTranslations}}

  {{#HowToUse}}
  <div class="section-title">How to use</div>
  <div class="how-to-use">{{HowToUse}}</div>
  {{/HowToUse}}

  {{#Focus}}
  <div class="section-title">Focus</div>
  <div class="focus"><b>{{Focus}}</b></div>
  {{/Focus}}

  {{#Examples}}
  <div class="section-title">More examples</div>
  <div class="examples">{{Examples}}</div>
  {{/Examples}}

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

.grammar-card {
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
  color: #9333ea;
  font-size: 17px;
  font-weight: 700;
  margin: 24px 0 16px;
  text-transform: uppercase;
}

.sentence-with-blank,
.completed-sentence {
  border-radius: 8px;
  font-size: 25px;
  margin: 22px auto;
  max-width: 720px;
  padding: 16px;
}

.sentence-with-blank {
  background: #f3e8ff;
  color: #581c87;
  font-weight: 600;
}

.completed-sentence {
  background: #faf5ff;
  color: #6b21a8;
}

.completed-sentence b,
.how-to-use b,
.examples b,
.common-mistakes b {
  color: #9333ea;
  font-weight: 800;
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

.answer-label,
.section-title {
  color: #64748b;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
}

.answer-label {
  text-align: center;
}

.answer-text {
  color: #15803d;
  font-size: 28px;
  font-weight: 500;
  margin: 10px 0 24px;
  text-align: center;
}

.answer-text b,
.focus b {
  color: #047857;
  font-weight: 800;
}

.section-title {
  margin: 24px 0 7px;
}

.translation,
.pattern-translations,
.how-to-use,
.focus,
.examples,
.common-mistakes {
  color: #475569;
  font-size: 17px;
}

.translation {
  color: #15803d;
  font-size: 22px;
  font-weight: 700;
}

.pattern,
.focus {
  background: #ede9fe;
  border-radius: 6px;
  color: #6d28d9;
  font-size: 20px;
  font-weight: 700;
  padding: 10px 12px;
}

.pattern-translations,
.how-to-use,
.focus,
.examples,
.common-mistakes {
  background: #ffffff;
  border-radius: 6px;
  padding: 10px 12px;
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

  .sentence-with-blank,
  .completed-sentence,
  .pattern,
  .focus,
  .pattern-translations,
  .how-to-use,
  .examples,
  .common-mistakes {
    background: #2e1065;
    color: #ede9fe;
  }
}
```

## Exemplo preenchido

```text
SentenceWithBlank: I'm interested ___ learning English.
Answer: in
CompletedSentence: I'm interested <b>in learning</b> English.
Translation: Tenho interesse em aprender inglês.
Pattern: be interested in + noun / gerund (-ing)
PatternTranslations: ter interesse em; estar interessado em
HowToUse: Depois de <b>interested in</b>, use um substantivo ou um verbo terminado em <b>-ing</b>. Não use “interested to learning”.
Focus: interested in
Examples: She's <b>interested in working</b> abroad. — Ela tem interesse em trabalhar no exterior.
CommonMistakes: Usar “interested on” ou “interested to doing”. A preposição correta é <b>in</b>.
Source: exemplo de padrão gramatical comum
```

## Visualização em Markdown

### Frente

```markdown
### ENGLISH · GRAMMAR PATTERNS

## Complete the sentence

I'm interested ___ learning English.

_Which word or form completes the sentence?_
```

### Verso

```markdown
**Answer**

**in**

#### Complete sentence

I'm interested **in learning** English.

#### Translation

**Tenho interesse em aprender inglês.**

#### Pattern

**be interested in** + noun / gerund (-ing)

#### Possible meanings

ter interesse em; estar interessado em

#### How to use

Depois de **interested in**, use um substantivo ou um verbo terminado em **-ing**. Não use “interested to learning”.

#### Focus

**interested in**

#### More examples

She's **interested in working** abroad. — Ela tem interesse em trabalhar no exterior.

#### Common mistakes

Usar “interested on” ou “interested to doing”. A preposição correta é **in**.

_Source: exemplo de padrão gramatical comum_
```

## Regras de qualidade

- Uma nota deve ensinar um padrão específico, não uma regra gramatical inteira.
- A lacuna deve ter uma resposta clara pelo contexto.
- Se várias respostas forem possíveis, adicionar contexto ou registrar as alternativas.
- Colocar em negrito somente o foco do card e suas formas diretamente relacionadas.
- Mostrar o padrão abstrato, como `interested in + -ing`, além do exemplo concreto.
- Incluir uma tradução natural da frase.
- Explicar preposições, infinitivo, gerúndio ou ordem das palavras quando forem o ponto principal.
- Usar exemplos naturais e curtos.
- Não transformar o verso em uma explicação longa de gramática.
- Para treinar a produção livre, criar um card em `English::Production`.
