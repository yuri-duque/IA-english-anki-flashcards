# Template — Expressions

## Objetivo do deck

O deck `English::Expressions` serve para aprender expressões fixas, idiomáticas e fórmulas comuns como unidades de significado.

Exemplos:

- `by the way`;
- `once in a while`;
- `that makes sense`;
- `I'm looking forward to it`;
- `It's raining cats and dogs`.

O foco é reconhecer a expressão inteira, entender quando ela é usada e conseguir identificá-la em situações reais. Não estudar cada palavra da expressão como se ela tivesse necessariamente o sentido literal.

## Decisão sobre a frente

A frente fica em **inglês**, com o áudio. O verso não repete a expressão em inglês: mostra as traduções possíveis, o uso e um exemplo adicional.

Para aprender a produzir a expressão, criar um card separado no deck `English::Production`.

## Campos da nota

Criar um tipo de nota chamado `English Expression` com estes campos:

| Campo | Obrigatório | Conteúdo |
|---|---:|---|
| `Expression` | sim | Expressão completa em inglês |
| `Translation` | sim | Tradução principal e possíveis traduções |
| `Audio` | recomendado | Áudio da expressão no formato `[sound:arquivo.mp3]` |
| `AudioSource` | recomendado | Página de onde o áudio foi obtido |
| `AudioLicense` | recomendado | Licença e atribuição informadas pela fonte |
| `HowToUse` | recomendado | Como, quando e com quem usar a expressão |
| `Example` | sim | Frase natural usando a expressão |
| `ExampleTranslation` | sim | Tradução natural da frase |
| `Register` | recomendado | Informal, neutra, formal, literária etc. |
| `LiteralMeaning` | opcional | Sentido literal, quando ajudar a memorizar |
| `Variations` | opcional | Variações ou estruturas relacionadas |
| `CommonExpressions` | opcional | Outras expressões relacionadas |
| `Source` | recomendado | Livro, série, vídeo, conversa etc. |

Destacar todas as ocorrências da expressão em foco com `<b>...</b>`:

```html
I was tired, but <b>that makes sense</b>.
```

No verso, manter em negrito o termo em foco sempre que ele aparecer em `HowToUse`, `Example`, `Variations` ou em qualquer observação.

## Card principal — reconhecimento da expressão

### Front Template

```html
<div class="card expression-card">
  <div class="deck-label">ENGLISH · EXPRESSIONS</div>

  <div class="expression">{{Expression}}</div>

  {{#Audio}}
  <div class="audio">{{Audio}}</div>
  {{/Audio}}

  <div class="instruction">What does this expression mean?</div>
</div>
```

### Back Template

```html
<hr id="answer" />

<div class="answer">
  <div class="translation">{{Translation}}</div>

  {{#Register}}
  <div class="register">{{Register}}</div>
  {{/Register}}

  {{#HowToUse}}
  <div class="section-title">How to use</div>
  <div class="how-to-use">{{HowToUse}}</div>
  {{/HowToUse}}

  <div class="section-title">Example</div>
  <div class="example">{{Example}}</div>

  {{#ExampleTranslation}}
  <div class="example-translation">{{ExampleTranslation}}</div>
  {{/ExampleTranslation}}

  {{#LiteralMeaning}}
  <div class="section-title">Literal meaning</div>
  <div class="literal-meaning">{{LiteralMeaning}}</div>
  {{/LiteralMeaning}}

  {{#Variations}}
  <div class="section-title">Variations</div>
  <div class="variations">{{Variations}}</div>
  {{/Variations}}

  {{#CommonExpressions}}
  <div class="section-title">Related expressions</div>
  <div class="common-expressions">{{CommonExpressions}}</div>
  {{/CommonExpressions}}

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

.expression-card {
  min-height: 260px;
}

.deck-label {
  color: #718096;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.12em;
  margin-bottom: 30px;
}

.expression {
  color: #7c3aed;
  font-size: clamp(27px, 6vw, 44px);
  font-weight: 700;
  margin: 28px auto;
  max-width: 720px;
}

.audio {
  margin: 22px 0;
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

.translation {
  color: #15803d;
  font-size: 26px;
  font-weight: 700;
  text-align: center;
}

.register {
  color: #64748b;
  font-size: 14px;
  font-style: italic;
  margin: 7px 0 24px;
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

.how-to-use,
.literal-meaning,
.variations,
.common-expressions,
.example-translation {
  color: #475569;
  font-size: 17px;
}

.how-to-use,
.literal-meaning,
.variations,
.common-expressions {
  background: #ffffff;
  border-radius: 6px;
  padding: 10px 12px;
}

.example {
  background: #f3e8ff;
  border-radius: 8px;
  color: #581c87;
  font-size: 21px;
  padding: 14px 16px;
}

.example b,
.how-to-use b,
.variations b,
.common-expressions b {
  color: #7c3aed;
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

  .example {
    background: #3b0764;
    color: #f3e8ff;
  }

  .how-to-use,
  .literal-meaning,
  .variations,
  .common-expressions {
    background: #222631;
  }
}
```

## Exemplo preenchido

```text
Expression: It's raining cats and dogs.
Translation: Está chovendo muito; está caindo uma chuva forte.
Audio: [sound:raining-cats-and-dogs.mp3]
AudioSource: fonte do áudio
AudioLicense: licença da fonte
HowToUse: Expressão informal e exagerada usada para dizer que está chovendo muito. Não precisa ser interpretada literalmente.
Example: We stayed home because <b>it's raining cats and dogs</b>.
ExampleTranslation: Ficamos em casa porque está chovendo muito.
Register: informal
LiteralMeaning: Está chovendo gatos e cachorros.
Variations: It's raining heavily — está chovendo muito; It's pouring — está caindo um temporal.
CommonExpressions: rain or shine — faça chuva ou faça sol
Source: flashcards/words/expressions.md
```

## Visualização em Markdown

### Frente

```markdown
### ENGLISH · EXPRESSIONS

# It's raining cats and dogs.

🔊 `[sound:raining-cats-and-dogs.mp3]`

_What does this expression mean?_
```

### Verso

```markdown
**Resposta**

**Está chovendo muito; está caindo uma chuva forte.**

_informal_

#### How to use

Expressão informal e exagerada usada para dizer que está chovendo muito. Não precisa ser interpretada literalmente.

#### Example

We stayed home because **it's raining cats and dogs**.

_Ficamos em casa porque está chovendo muito._

#### Literal meaning

Está chovendo gatos e cachorros.

#### Variations

**It's raining heavily** — está chovendo muito  
**It's pouring** — está caindo um temporal

#### Related expressions

**rain or shine** — faça chuva ou faça sol

_Source: flashcards/words/expressions.md_
```

## Regras de qualidade

- Registrar a expressão completa, não apenas uma palavra curiosa dentro dela.
- Usar traduções naturais e listar mais de uma quando houver sentidos equivalentes.
- Colocar em negrito todas as ocorrências da expressão em foco na resposta, usando `<b>...</b>`.
- Explicar se a expressão é informal, formal, regional, antiga ou rara.
- Informar o sentido literal somente quando ele ajudar a entender ou memorizar.
- Não forçar uma explicação literal para expressões cujo sentido não depende dela.
- Usar uma frase natural e compreensível.
- Não repetir a expressão em inglês no verso, exceto dentro da frase de exemplo ou de uma explicação necessária.
- Colocar o áudio na frente e garantir que ele corresponda à expressão exibida.
- Para praticar a produção, criar um card correspondente em `English::Production`.

## Áudio

Usar o mesmo procedimento documentado em [vocabulary-template.md](vocabulary-template.md): baixar um áudio confiável, preferir `.mp3`, anexá-lo ao campo `Audio` e registrar a origem e a licença.
