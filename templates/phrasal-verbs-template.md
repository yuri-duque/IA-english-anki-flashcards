# Template — Phrasal Verbs

## Objetivo do deck

O deck `English::Phrasal Verbs` serve para estudar combinações de verbo + partícula, como `pick up`, `give up`, `look after` e `run out of`.

O foco não é decorar o verbo e a partícula separadamente. É aprender o significado da combinação, os complementos que ela aceita e a posição correta dos pronomes e objetos.

## Decisão sobre a frente

A frente fica em **inglês**, com o áudio do phrasal verb. O verso não repete o termo em inglês: apresenta as traduções, os padrões de uso e os exemplos.

Para treinar a produção, criar um card no deck `English::Production`.

## Campos da nota

Criar um tipo de nota chamado `English Phrasal Verb` com estes campos:

| Campo | Obrigatório | Conteúdo |
|---|---:|---|
| `PhrasalVerb` | sim | Phrasal verb completo |
| `Translation` | sim | Tradução principal e possíveis traduções |
| `Audio` | recomendado | Áudio no formato `[sound:arquivo.mp3]` |
| `AudioSource` | recomendado | Página de onde o áudio foi obtido |
| `AudioLicense` | recomendado | Licença e atribuição da fonte |
| `Verb` | recomendado | Verbo principal, como `pick` |
| `Particle` | recomendado | Partícula ou preposição, como `up` |
| `HowToUse` | recomendado | Como e quando usar a combinação |
| `Pattern` | recomendado | Estrutura do complemento |
| `Separable` | recomendado | Se o objeto pode ficar entre verbo e partícula |
| `Example` | sim | Frase natural em inglês |
| `ExampleTranslation` | sim | Tradução natural da frase |
| `AlternativeExamples` | opcional | Exemplos com outras estruturas |
| `Synonyms` | opcional | Sinônimos ou alternativas naturais |
| `CommonExpressions` | opcional | Combinações frequentes relacionadas |
| `Source` | recomendado | Origem da frase ou do phrasal verb |

Destacar o phrasal verb em foco com HTML:

```html
I need to <b>pick up</b> my brother after work.
```

Na resposta, colocar em negrito todas as ocorrências do phrasal verb e dos padrões diretamente relacionados a ele.

## Card principal — reconhecimento

### Front Template

```html
<div class="card phrasal-card">
  <div class="deck-label">ENGLISH · PHRASAL VERBS</div>

  <div class="phrasal-verb">{{PhrasalVerb}}</div>

  {{#Audio}}
  <div class="audio">{{Audio}}</div>
  {{/Audio}}

  <div class="instruction">What does this phrasal verb mean?</div>
</div>
```

### Back Template

```html
<hr id="answer" />

<div class="answer">
  <div class="translation">{{Translation}}</div>

  <div class="section-title">Structure</div>
  <div class="structure">
    <b>{{Verb}}</b> + <b>{{Particle}}</b>
  </div>

  {{#HowToUse}}
  <div class="section-title">How to use</div>
  <div class="how-to-use">{{HowToUse}}</div>
  {{/HowToUse}}

  {{#Pattern}}
  <div class="section-title">Pattern</div>
  <div class="pattern">{{Pattern}}</div>
  {{/Pattern}}

  {{#Separable}}
  <div class="section-title">Separable?</div>
  <div class="separable">{{Separable}}</div>
  {{/Separable}}

  <div class="section-title">Example</div>
  <div class="example">{{Example}}</div>

  {{#ExampleTranslation}}
  <div class="example-translation">{{ExampleTranslation}}</div>
  {{/ExampleTranslation}}

  {{#AlternativeExamples}}
  <div class="section-title">More examples</div>
  <div class="alternative-examples">{{AlternativeExamples}}</div>
  {{/AlternativeExamples}}

  {{#Synonyms}}
  <div class="section-title">Alternatives</div>
  <div class="synonyms">{{Synonyms}}</div>
  {{/Synonyms}}

  {{#CommonExpressions}}
  <div class="section-title">Common combinations</div>
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

.phrasal-card {
  min-height: 260px;
}

.deck-label {
  color: #718096;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.12em;
  margin-bottom: 30px;
}

.phrasal-verb {
  color: #db2777;
  font-size: clamp(30px, 7vw, 50px);
  font-weight: 700;
  margin: 28px auto;
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

.section-title {
  color: #64748b;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.1em;
  margin: 24px 0 7px;
  text-transform: uppercase;
}

.structure,
.pattern {
  background: #fce7f3;
  border-radius: 6px;
  color: #9d174d;
  font-size: 20px;
  padding: 10px 12px;
}

.separable,
.how-to-use,
.alternative-examples,
.synonyms,
.common-expressions,
.example-translation {
  color: #475569;
  font-size: 17px;
}

.separable,
.how-to-use,
.alternative-examples,
.synonyms,
.common-expressions {
  background: #ffffff;
  border-radius: 6px;
  padding: 10px 12px;
}

.example {
  background: #fdf2f8;
  border-radius: 8px;
  color: #831843;
  font-size: 21px;
  padding: 14px 16px;
}

.example b,
.how-to-use b,
.alternative-examples b,
.common-expressions b {
  color: #db2777;
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

  .structure,
  .pattern,
  .example {
    background: #500724;
    color: #fbcfe8;
  }

  .separable,
  .how-to-use,
  .alternative-examples,
  .synonyms,
  .common-expressions {
    background: #222631;
  }
}
```

## Exemplo preenchido

```text
PhrasalVerb: pick up
Translation: buscar; pegar; apanhar
Audio: [sound:pick-up.mp3]
AudioSource: fonte do áudio
AudioLicense: licença da fonte
Verb: pick
Particle: up
HowToUse: Neste contexto, <b>pick up</b> significa buscar alguém em algum lugar. Também pode significar pegar um objeto ou aprender algo informalmente.
Pattern: <b>pick up someone</b> / <b>pick someone up</b>
Separable: Sim. Com pronomes, o pronome fica entre o verbo e a partícula: <b>pick him up</b>.
Example: I need to <b>pick up</b> my brother after work.
ExampleTranslation: Eu preciso buscar meu irmão depois do trabalho.
AlternativeExamples: Can you <b>pick me up</b> at eight? — Você pode me buscar às oito?; She <b>picked up</b> the keys. — Ela pegou as chaves.
Synonyms: collect someone; fetch someone
CommonExpressions: <b>pick up the phone</b> — atender o telefone; <b>pick up a skill</b> — aprender uma habilidade
Source: flashcards/words/pick.md
```

## Visualização em Markdown

### Frente

```markdown
### ENGLISH · PHRASAL VERBS

# pick up

🔊 `[sound:pick-up.mp3]`

_What does this phrasal verb mean?_
```

### Verso

```markdown
**Resposta**

**buscar; pegar; apanhar**

#### Structure

**pick** + **up**

#### How to use

Neste contexto, **pick up** significa buscar alguém em algum lugar. Também pode significar pegar um objeto ou aprender algo informalmente.

#### Pattern

**pick up someone** / **pick someone up**

#### Separable?

Sim. Com pronomes, o pronome fica entre o verbo e a partícula: **pick him up**.

#### Example

I need to **pick up** my brother after work.

_Eu preciso buscar meu irmão depois do trabalho._

#### More examples

Can you **pick me up** at eight? — Você pode me buscar às oito?  
She **picked up** the keys. — Ela pegou as chaves.

#### Alternatives

`collect someone` — buscar alguém  
`fetch someone` — buscar alguém

#### Common combinations

**pick up the phone** — atender o telefone  
**pick up a skill** — aprender uma habilidade

_Source: flashcards/words/pick.md_
```

## Regras de qualidade

- Registrar o phrasal verb completo, incluindo preposições como `out of`, `up to` e `on`.
- Listar as possíveis traduções do sentido estudado.
- Colocar em negrito todas as ocorrências do phrasal verb e dos padrões relacionados na resposta, usando `<b>...</b>`.
- Informar se o phrasal verb é separável ou inseparável.
- Mostrar a posição correta de objetos e pronomes.
- Usar frases naturais e indicar sentidos diferentes em notas separadas quando necessário.
- Não misturar vários sentidos sem contexto claro.
- Colocar o áudio na frente e garantir que ele corresponda ao phrasal verb.
- Para praticar a produção, criar um card correspondente em `English::Production`.

## Áudio

Usar o mesmo procedimento documentado em [vocabulary-template.md](vocabulary-template.md): baixar um áudio confiável, preferir `.mp3`, anexá-lo ao campo `Audio` e registrar a origem e a licença.
