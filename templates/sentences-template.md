# Template — Sentences

## Objetivo do deck

O deck `English::Sentences` serve para aprender inglês dentro de frases completas. O foco não é decorar uma palavra isolada, mas reconhecer o sentido da frase e perceber como as palavras se combinam naturalmente.

Este deck é especialmente útil para:

- frases encontradas em livros, séries, vídeos ou conversas;
- estruturas que aparecem repetidamente;
- combinações naturais de palavras;
- frases que você entende com dificuldade;
- exemplos que ajudam a fixar uma palavra do deck `Vocabulary`.

## Decisão sobre a frente

A frente fica em **inglês**, com o áudio visível ou reproduzível. Isso treina compreensão de uma frase real e associa a forma escrita à pronúncia.

O verso não repete a frase em inglês. Ele apresenta apenas a tradução, a explicação e observações úteis. Para treinar a produção da frase, criar um card separado no deck `English::Production`.

## Campos da nota

Criar um tipo de nota chamado `English Sentence` com estes campos:

| Campo                    | Obrigatório | Conteúdo                                        |
| ------------------------ | ----------: | ----------------------------------------------- |
| `Sentence`               |         sim | Frase natural em inglês                         |
| `Translation`            |         sim | Tradução natural em português                   |
| `Audio`                  | recomendado | Áudio da frase no formato `[sound:arquivo.mp3]` |
| `AudioSource`            | recomendado | Página de onde o áudio foi obtido               |
| `AudioLicense`           | recomendado | Licença e atribuição informadas pela fonte      |
| `Focus`                  | recomendado | Palavra, expressão ou estrutura principal       |
| `FocusTranslations`      | recomendado | Possíveis traduções do termo em foco            |
| `HowToUse`               | recomendado | Como e quando usar o elemento principal         |
| `KeyVocabulary`          |    opcional | Vocabulário relevante da frase                  |
| `GrammarNote`            |    opcional | Observação gramatical curta                     |
| `AlternativeTranslation` |    opcional | Outra tradução possível                         |
| `Source`                 | recomendado | Livro, série, vídeo, conversa etc.              |

No campo `Sentence`, destacar o elemento principal com HTML:

```html
I need to <b>pick up</b> my brother after work.
```

Destacar somente a palavra, expressão ou estrutura que merece atenção. Não destacar a frase inteira.

Na resposta, manter em negrito todas as ocorrências do termo em foco que aparecerem nos campos `Focus`, `HowToUse`, `KeyVocabulary`, `GrammarNote` ou em qualquer observação adicional. Isso mantém a atenção visual no elemento que o card pretende ensinar.

## Card principal — compreensão em contexto

### Front Template

```html
<div class="card sentence-card">
  <div class="deck-label">ENGLISH · SENTENCES</div>

  <div class="sentence">{{Sentence}}</div>

  {{#Audio}}
  <div class="audio">{{Audio}}</div>
  {{/Audio}}

  <div class="instruction">What does this sentence mean?</div>
</div>
```

### Back Template

```html
<hr id="answer" />

<div class="answer">
  <div class="translation">{{Translation}}</div>

  {{#AlternativeTranslation}}
  <div class="alternative-translation">{{AlternativeTranslation}}</div>
  {{/AlternativeTranslation}} {{#Focus}}
  <div class="section-title">Focus</div>
  <div class="focus"><b>{{Focus}}</b></div>

  {{/Focus}} {{#FocusTranslations}}
  <div class="section-title">Possible translations</div>
  <div class="focus-translations">{{FocusTranslations}}</div>
  {{/FocusTranslations}} {{#HowToUse}}
  <div class="section-title">How to use</div>
  <div class="how-to-use">{{HowToUse}}</div>
  {{/HowToUse}} {{#KeyVocabulary}}
  <div class="section-title">Key vocabulary</div>
  <div class="key-vocabulary">{{KeyVocabulary}}</div>
  {{/KeyVocabulary}} {{#GrammarNote}}
  <div class="section-title">Grammar</div>
  <div class="grammar-note">{{GrammarNote}}</div>
  {{/GrammarNote}} {{#Source}}
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

.sentence-card {
  min-height: 260px;
}

.deck-label {
  color: #718096;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.12em;
  margin-bottom: 30px;
}

.sentence {
  color: #1d4ed8;
  font-size: clamp(25px, 5vw, 38px);
  font-weight: 600;
  margin: 28px auto;
  max-width: 720px;
}

.sentence b {
  color: #b45309;
  font-weight: 800;
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

.alternative-translation,
.focus-translations,
.how-to-use,
.key-vocabulary,
.grammar-note {
  color: #475569;
  font-size: 17px;
}

.alternative-translation {
  font-style: italic;
  margin-top: 8px;
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

.focus {
  background: #fff7ed;
  border-left: 3px solid #f59e0b;
  color: #9a3412;
  font-size: 21px;
  font-weight: 700;
  padding: 10px 12px;
}

.focus-translations {
  color: #15803d;
  font-size: 20px;
  font-weight: 700;
}

.how-to-use,
.key-vocabulary,
.grammar-note {
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

  .focus {
    background: #431407;
    color: #fed7aa;
  }

  .how-to-use,
  .key-vocabulary,
  .grammar-note {
    background: #222631;
  }
}
```

## Exemplo preenchido

```text
Sentence: I need to <b>pick up</b> my brother after work.
Translation: Eu preciso buscar meu irmão depois do trabalho.
Audio: [sound:pick-up-brother.mp3]
AudioSource: fonte do áudio
AudioLicense: licença da fonte
Focus: pick up
FocusTranslations: buscar; pegar; buscar alguém
HowToUse: Neste contexto, <b>pick up</b> significa buscar alguém em algum lugar. A estrutura é <b>pick up someone</b> ou <b>pick someone up</b>.
KeyVocabulary: <b>after work</b> — depois do trabalho; <b>brother</b> — irmão
GrammarNote: O pronome pode vir entre o verbo e a partícula: <b>pick him up</b>.
Source: frase criada a partir de uma situação cotidiana
```

## Visualização em Markdown

### Frente

```markdown
### ENGLISH · SENTENCES

I need to **pick up** my brother after work.

🔊 `[sound:pick-up-brother.mp3]`

_What does this sentence mean?_
```

### Verso

```markdown
**Resposta**

Eu preciso **buscar** meu irmão depois do trabalho.

#### Focus

**pick up**

#### Possible translations

**buscar; pegar; buscar alguém**

#### How to use

Neste contexto, **pick up** significa buscar alguém em algum lugar. A estrutura é **pick up someone** ou **pick someone up**.

#### Key vocabulary

`after work` — depois do trabalho  
`brother` — irmão

#### Grammar

O pronome pode vir entre o verbo e a partícula: **pick him up**.

_Source: frase criada a partir de uma situação cotidiana_
```

## Regras de qualidade

- Uma nota deve conter uma frase completa e natural.
- Usar uma frase que você entende parcialmente, não uma frase completamente incompreensível.
- Destacar somente um foco principal por card.
- Colocar em negrito todas as ocorrências do termo em foco na resposta, usando `<b>...</b>`.
- Manter a tradução natural, sem traduzir palavra por palavra.
- Registrar as possíveis traduções do termo em foco separadamente da tradução completa da frase.
- O áudio deve corresponder exatamente à frase exibida.
- Colocar o áudio na frente; ele ajuda a associar escrita e pronúncia sem revelar a tradução.
- Não repetir a frase em inglês no verso.
- Usar `HowToUse` para explicar o foco, não para criar uma aula gramatical extensa.
- Se a frase contiver muitas palavras desconhecidas, dividi-la ou estudar o vocabulário antes.
- Para praticar a produção da frase, criar outro card em `English::Production`.

## Áudio

Usar o mesmo procedimento documentado em [vocabulary-template.md](vocabulary-template.md): baixar um áudio confiável, preferir `.mp3`, anexá-lo ao campo `Audio` e registrar a origem e a licença.
