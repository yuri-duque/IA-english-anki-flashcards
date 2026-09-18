# IA English Anki Flashcards

Repositório dedicado ao estudo de inglês com flashcards em Markdown e sincronização opcional com o Anki Desktop por meio do AnkiConnect.

## Estrutura

```text
flashcards/
├── Vocabulary/
├── Expressions/
├── Phrasal Verbs/
├── Production/
└── Grammar Patterns/
templates/
.codex/skills/
```

Os cards ficam em `flashcards/`. Os modelos usados para criá-los ficam centralizados em `templates/`. As notas de `Grammar Patterns` são material didático e não são sincronizadas pelo importador atual.

## Como criar flashcards

Use as skills em `.codex/skills/`:

- `english-flashcard-creator`: Vocabulary, Expressions, Phrasal Verbs, Sentences e Production;
- `english-grammar-flashcard-creator`: cards de padrões gramaticais;
- `english-grammar-topic-creator`: notas didáticas de gramática;
- `anki-sync`: sincronização com o Anki Desktop.

O fluxo de criação é feito em duas fases: primeiro a skill analisa o item, verifica duplicatas, escolhe o template e pede aprovação; somente depois da aprovação os arquivos são criados.

Para cada novo card de `Vocabulary`, crie também pelo menos três cards distintos em `Production`, com prompts ou situações diferentes.

Todo card deve:

1. seguir o template do deck;
2. começar com frontmatter YAML contendo `anki: false`;
3. conter as seções `Dados da nota`, `Frente` e `Verso`;
4. ser incluído no `index.md` do respectivo deck.

Depois que o Anki aceitar a nota, o sincronizador adiciona `anki_note_id` e muda `anki` para `true`. Não altere esses campos manualmente.

## Templates

| Template | Uso |
|---|---|
| `templates/vocabulary-template.md` | Palavras e termos lexicais |
| `templates/sentences-template.md` | Frases completas |
| `templates/expressions-template.md` | Expressões fixas e idiomáticas |
| `templates/phrasal-verbs-template.md` | Verbos frasais |
| `templates/production-template.md` | Produção ativa a partir de português, contexto ou intenção |
| `templates/grammar-patterns-template.md` | Padrões gramaticais para completar lacunas |
| `templates/didactic-note-template.md` | Notas didáticas de gramática |

Leia o template correspondente antes de criar ou atualizar uma nota. O HTML/CSS do Anki pertence ao modelo do Anki; os arquivos Markdown devem permanecer fáceis de revisar.

## Configuração do AnkiConnect

1. Instale o Anki Desktop.
2. No Anki, abra `Tools > Add-ons > Get Add-ons...`.
3. Instale o AnkiConnect usando o código publicado pelo projeto.
4. Reinicie o Anki Desktop.
5. Mantenha o Anki aberto durante a sincronização.

O sincronizador espera o AnkiConnect em:

```text
http://localhost:8765
```

Faça backup da coleção antes da primeira execução.

## Sincronizar os cards

Na raiz deste repositório, execute:

```bash
./.codex/skills/anki-sync/run.sh
```

O script processa estes diretórios e decks raiz do Anki:

| Diretório | Deck |
|---|---|
| `flashcards/Vocabulary/` | `Vocabulary` |
| `flashcards/Sentences/` | `Sentences` |
| `flashcards/Expressions/` | `Expressions` |
| `flashcards/Phrasal Verbs/` | `Phrasal Verbs` |
| `flashcards/Production/` | `Production` |

Os nomes dos decks são mantidos como estão para evitar a criação de duplicatas. Após o script concluir, use o botão `Sync` do próprio Anki para enviar as alterações ao AnkiWeb.

O sincronizador atualiza notas existentes quando encontra `anki_note_id` ou uma única correspondência pelo campo principal. Notas órfãs no Anki são informadas e preservadas; elas não são apagadas automaticamente.

Grammar Patterns não participa desse fluxo porque suas notas ficam em subpastas e usam um formato didático diferente. Um sincronizador específico poderá ser definido futuramente.

## Áudio

O campo `Audio` deve conter uma referência de mídia local, por exemplo `[sound:word-en-us.mp3]`, somente quando o arquivo já existir na coleção de mídia do Anki. O importador não baixa áudio remoto automaticamente.

## Troubleshooting

Se a conexão falhar, confirme que o Anki está aberto e verifique a porta:

```bash
lsof -nP -iTCP:8765 -sTCP:LISTEN
```

Se a porta estiver aberta, mas o script não conseguir acessá-la, execute o sincronizador em um ambiente com acesso ao host onde o Anki está rodando.

## Dependências

O script usa Python 3, `requests` e `python-frontmatter`. O `run.sh` cria `.venv/` quando necessário e instala essas dependências. Elas também estão listadas em `requirements.txt`.

## Conteúdo legado

Algumas notas migradas ainda apontam para `flashcards/words/`, mas essa pasta não existe no estado atual da origem. A recuperação desses arquivos históricos deve ser decidida antes de depender da skill `english-word`.
