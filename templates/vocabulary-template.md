# Template — Vocabulary

## Decisão sobre o idioma da frente

Para o deck `English::Vocabulary`, a frente deve ficar em **inglês**.

O motivo é que este deck treina principalmente reconhecimento: ao encontrar uma palavra em um texto ou conversa, você precisa entender o que ela significa. Colocar a tradução portuguesa na frente transformaria o card em um exercício de produção, que deve ficar no deck `English::Production` e ter seu próprio agendamento.

Portanto:

- `Vocabulary`: inglês → significado e uso;
- `Production`: português ou situação → palavra/frase em inglês;
- O áudio fica na própria nota quando disponível; um deck específico de escuta pode ser criado no futuro.

Não é necessário escolher um único idioma para todos os cards de inglês. A direção deve corresponder à habilidade que o deck pretende treinar.

## Objetivo do card

O card deve responder a uma pergunta simples:

> “Quando encontro esta palavra em inglês, consigo reconhecer seu significado e entender como ela é usada?”

O card não deve exigir que você memorize uma definição de dicionário inteira. A frase e o contexto são mais importantes que uma lista extensa de traduções.

## Campos da nota

Criar um tipo de nota chamado `English Vocabulary` com estes campos:

| Campo | Obrigatório | Conteúdo |
|---|---:|---|
| `Word` | sim | Palavra ou expressão curta em inglês |
| `Meaning` | sim | Tradução principal e possíveis traduções em português |
| `PartOfSpeech` | sim | Classe gramatical: noun, verb, adjective etc. |
| `Example` | sim | Frase natural em inglês |
| `ExampleTranslation` | sim | Tradução da frase |
| `Definition` | sim | Definição curta em inglês |
| `Audio` | recomendado | Áudio da palavra ou da frase no formato `[sound:arquivo.mp3]` |
| `AudioSource` | recomendado | Página de onde o áudio foi obtido |
| `AudioLicense` | recomendado | Licença e atribuição informadas pela fonte |
| `HowToUse` | sim | Explicação em português de como e quando usar a palavra |
| `WordFamily` | opcional | Derivados relevantes |
| `CommonExpressions` | opcional | Expressões comuns com a palavra |
| `RelatedWords` | recomendado | Palavras semanticamente relacionadas e diferenças de uso |
| `Etymology` | opcional | Origem histórica resumida |
| `Image` | opcional | Imagem, apenas quando representar bem o conceito |
| `Source` | opcional | Origem: série, livro, conversa etc. |

No campo `Example`, destacar manualmente a palavra estudada com HTML:

```html
She <b>stood up</b> when the teacher entered.
```

### Checklist obrigatório

Todo card de vocabulário deve conter:

- `Meaning`, com o significado principal em português e alternativas relevantes;
- `PartOfSpeech`, com a classe gramatical;
- `Definition`, com uma definição curta em inglês;
- `HowToUse`, com a explicação em português;
- `Example`, com pelo menos uma frase natural em inglês e o termo destacado;
- `ExampleTranslation`, com a tradução do exemplo;
- `CommonExpressions` e `WordFamily`, quando houver conteúdo útil;
- `RelatedWords`, quando houver palavras semanticamente relacionadas ou facilmente confundidas, com uma explicação curta da diferença;
- `Etymology`, `Image` e `Source`, somente quando aplicáveis e verificáveis.

`RelatedWords` não é sinônimo de `WordFamily`: o primeiro reúne palavras de sentido próximo ou facilmente confundidas; o segundo reúne derivados da mesma família morfológica. As diferenças devem ser explicadas de forma simples, com exemplos curtos quando ajudarem. Campos adicionais, como `NounType` e `QuantityOrder`, são complementares. Eles não substituem `Definition`, `Example` ou `ExampleTranslation`, nem mudam a ordem do verso.

Não colocar a tradução, o significado ou a definição na frente. O áudio fica na frente para associar a forma escrita à pronúncia sem revelar a resposta.

Na resposta, colocar em negrito todas as ocorrências da palavra ou expressão estudada que aparecerem em `HowToUse`, `CommonExpressions`, `WordFamily`, `RelatedWords` ou em observações adicionais, usando `<b>...</b>`. Em `RelatedWords`, destacar também as palavras relacionadas que estiverem sendo comparadas.

No campo `Meaning`, listar as traduções relevantes separadas por ponto e vírgula. Colocar em negrito o significado principal no card; as demais traduções podem aparecer como alternativas.

## Card principal — reconhecimento

### Front Template

```html
<div class="card vocabulary-card">
  <div class="deck-label">ENGLISH · VOCABULARY</div>

  <div class="word">{{Word}}</div>

  {{#Audio}}
  <div class="audio">{{Audio}}</div>
  {{/Audio}}

  <div class="instruction">What does this word mean and how is it used?</div>
</div>
```

### Back Template

```html
<hr id="answer">

<div class="answer">
  <div class="meaning">{{Meaning}}</div>

  {{#PartOfSpeech}}
  <div class="part-of-speech">{{PartOfSpeech}}</div>
  {{/PartOfSpeech}}

  {{#Definition}}
  <div class="definition">{{Definition}}</div>
  {{/Definition}}

  {{#HowToUse}}
  <div class="section-title">How to use</div>
  <div class="how-to-use">{{HowToUse}}</div>
  {{/HowToUse}}

  <div class="section-title">Example</div>
  <div class="example">{{Example}}</div>

  {{#ExampleTranslation}}
  <div class="example-translation">{{ExampleTranslation}}</div>
  {{/ExampleTranslation}}

  {{#CommonExpressions}}
  <div class="section-title">Common expressions</div>
  <div class="common-expressions">{{CommonExpressions}}</div>
  {{/CommonExpressions}}

  {{#WordFamily}}
  <div class="section-title">Word family</div>
  <div class="word-family">{{WordFamily}}</div>
  {{/WordFamily}}

  {{#RelatedWords}}
  <div class="section-title">Related words and differences</div>
  <div class="related-words">{{RelatedWords}}</div>
  {{/RelatedWords}}

  {{#Etymology}}
  <div class="section-title">Etymology</div>
  <div class="etymology">{{Etymology}}</div>
  {{/Etymology}}

  {{#Image}}
  <div class="image">{{Image}}</div>
  {{/Image}}

  {{#Source}}
  <div class="source">Source: {{Source}}</div>
  {{/Source}}
</div>
```

## Como obter os áudios

### Fonte recomendada: Wiktionary/Wikimedia Commons

Usar primeiro o áudio de pronúncia disponível no Wiktionary. Os arquivos de pronúncia do Wiktionary são armazenados no Wikimedia Commons, que mantém a informação de licença na página de cada arquivo ([Wiktionary — Pronunciations](https://meta.wikimedia.org/wiki/Wiktionary/Pronunciations/en)).

Para cada palavra:

1. Acessar `https://en.wiktionary.org/wiki/PALAVRA`.
2. Localizar a seção `English` e a área `Pronunciation`.
3. Escolher `US` ou `UK`, conforme a variante desejada.
4. Abrir o link do arquivo de áudio.
5. Na página do arquivo, conferir a licença e baixar o áudio.
6. Converter para `.mp3` se o arquivo estiver em `.ogg`, pois MP3 é o formato mais compatível com Anki, AnkiWeb e aplicativos móveis ([Anki Manual — Media](https://docs.ankiweb.net/media.html)).
7. Usar um nome simples e único, por exemplo `huge-en-us.mp3`.
8. Adicionar o arquivo ao campo `Audio` pelo botão de anexo do Anki. O Anki copiará o arquivo para a coleção de mídia.
9. Preencher `AudioSource` e `AudioLicense` para manter a origem e a atribuição.

Exemplo encontrado para esta documentação:

- Palavra: `huge`
- Variante: inglês americano
- Arquivo original: `en-us-huge.ogg`
- Página do arquivo: [en-us-huge.ogg](https://en.wiktionary.org/wiki/File:en-us-huge.ogg)
- Download direto: [Special:FilePath/en-us-huge.ogg](https://commons.wikimedia.org/wiki/Special:FilePath/en-us-huge.ogg?download=1)
- Nome local recomendado: `huge-en-us.mp3`

Se for necessário converter `.ogg` para `.mp3` localmente e o `ffmpeg` estiver instalado:

```bash
ffmpeg -i en-us-huge.ogg -codec:a libmp3lame -q:a 4 huge-en-us.mp3
```

Não usar o endereço da internet diretamente no card. O arquivo deve ser anexado ou copiado para a coleção de mídia do Anki e referenciado pelo campo:

```text
[sound:huge-en-us.mp3]
```

Manter o arquivo diretamente na coleção de mídia, sem subpastas. Se arquivos forem copiados manualmente, executar `Tools > Check Media` no Anki depois.

## CSS

```css
.card {
  background: #f7f8fa;
  color: #20242a;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  font-size: 20px;
  line-height: 1.45;
  text-align: center;
  padding: 28px 20px;
}

.vocabulary-card {
  min-height: 260px;
}

.deck-label {
  color: #718096;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.12em;
  margin-bottom: 28px;
}

.word {
  color: #1d4ed8;
  font-size: clamp(34px, 8vw, 56px);
  font-weight: 700;
  margin: 20px 0 8px;
}

.audio {
  margin: 18px 0;
  text-align: center;
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

.meaning {
  color: #15803d;
  font-size: 29px;
  font-weight: 700;
  text-align: center;
}

.part-of-speech {
  color: #64748b;
  font-size: 14px;
  font-style: italic;
  margin: 5px 0 24px;
  text-align: center;
}

.definition,
.how-to-use,
.common-expressions,
.word-family,
.etymology,
.example-translation {
  color: #475569;
  font-size: 17px;
}

.definition {
  border-left: 3px solid #93c5fd;
  margin: 18px 0;
  padding-left: 12px;
}

.section-title {
  color: #64748b;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.1em;
  margin: 24px 0 7px;
  text-transform: uppercase;
}

.example {
  background: #eaf2ff;
  border-radius: 8px;
  color: #1e3a8a;
  font-size: 21px;
  padding: 14px 16px;
}

.example b {
  color: #1d4ed8;
  font-weight: 800;
}

.example-translation {
  margin-top: 8px;
}

.how-to-use,
.common-expressions,
.word-family,
.etymology {
  background: #ffffff;
  border-radius: 6px;
  padding: 10px 12px;
}

.image img {
  border-radius: 8px;
  margin-top: 18px;
  max-height: 220px;
  max-width: 100%;
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
    background: #172554;
    color: #dbeafe;
  }

  .how-to-use,
  .common-expressions,
  .etymology,
  .word-family {
    background: #222631;
  }
}
```

## Exemplo preenchido

```text
Word: huge
Meaning: enorme; muito grande
PartOfSpeech: adjective
Example: They live in a <b>huge</b> house near the beach.
ExampleTranslation: Eles moram em uma casa enorme perto da praia.
Definition: Very large in size or amount.
Audio: [sound:huge-en-us.mp3]
AudioSource: https://en.wiktionary.org/wiki/File:en-us-huge.ogg
AudioLicense: conferir na página do arquivo antes de redistribuir
HowToUse: Usada para descrever algo muito grande em tamanho, quantidade, importância ou intensidade. É comum em conversas e geralmente vem antes de um substantivo, como em <b>huge house</b> ou <b>huge problem</b>.
WordFamily: hugely (adv.) — enormemente
CommonExpressions: <b>a huge hit</b> — um grande sucesso; <b>a huge difference</b> — uma diferença enorme; <b>huge fan</b> — grande fã
Etymology: Do francês antigo huge, provavelmente relacionado a uma palavra nórdica antiga com o sentido de “enorme” ou “muito grande”.
Source: flashcards/words/huge.md
```

## Visualização em Markdown

O exemplo abaixo representa como o card apareceria durante o estudo. A frente não revela o significado nem a tradução.

### Frente

```markdown
### ENGLISH · VOCABULARY

# huge

🔊 `[sound:huge-en-us.mp3]`

*What does this word mean?*
```

### Verso

```markdown
### ENGLISH · VOCABULARY

**Resposta**

**enorme; muito grande**

_adjective_

> Very large in size or amount.

#### How to use

Usada para descrever algo muito grande em tamanho, quantidade, importância ou intensidade. É comum em conversas e geralmente vem antes de um substantivo.

#### Example

They live in a **huge** house near the beach.

_Eles moram em uma casa enorme perto da praia._

#### Common expressions

**a huge hit** — um grande sucesso  
**a huge difference** — uma diferença enorme  
**huge fan** — grande fã

#### Word family

`hugely` (adverb) — enormemente

#### Etymology

Do francês antigo *huge*, provavelmente relacionado a uma palavra nórdica antiga com o sentido de “enorme” ou “muito grande”.

_Source: flashcards/words/huge.md_
```

## Critério para decidir a direção

Use inglês na frente quando a pergunta for:

> “Consigo reconhecer e compreender esta palavra?”

Use português, uma situação ou uma imagem na frente quando a pergunta for:

> “Consigo produzir esta palavra em inglês?”

Nesse segundo caso, o card deve ir para `English::Production`, e não ser misturado automaticamente ao card de `Vocabulary`. Cards de reconhecimento e produção são habilidades diferentes e podem exigir intervalos de revisão diferentes. O Anki também recomenda separar esses cards quando o desempenho em cada direção precisa ser acompanhado independentemente ([Anki Manual](https://docs.ankiweb.net/getting-started.html#notes-fields)).

## Regras de qualidade

- Uma palavra por nota, exceto expressões que funcionam como uma unidade.
- Usar um significado principal por card quando a palavra tiver muitos sentidos.
- Escolher frases naturais e compreensíveis.
- Manter a tradução curta; detalhes de uso ficam em `HowToUse` ou no documento de `flashcards/words`.
- Adicionar `CommonExpressions` somente quando houver combinações realmente comuns e úteis.
- Adicionar `Etymology` como contexto complementar, nunca como informação principal do card.
- Colocar em negrito todas as ocorrências do termo estudado na resposta, usando `<b>...</b>`.
- Usar áudio no campo `Audio` com o formato nativo do Anki, por exemplo `[sound:huge-en-us.mp3]`.
- Colocar o arquivo de áudio na coleção de mídia do Anki; o nome usado no campo deve corresponder exatamente ao nome do arquivo.
- Preferir arquivos `.mp3`, que são mais compatíveis entre Anki Desktop, AnkiWeb e aplicativos móveis.
- Registrar a página de origem e a licença nos campos `AudioSource` e `AudioLicense`.
- Manter o áudio na frente neste deck para associar a palavra escrita à pronúncia sem revelar a tradução.
- Usar imagem quando ela realmente facilitar a associação, não como decoração.
- Se o card ficar ambíguo, adicionar contexto ou reformulá-lo.
- Para cada novo card de vocabulário, criar pelo menos três cards distintos no deck `English::Production`, com prompts ou situações variadas. Esses cards são obrigatórios, não opcionais.
