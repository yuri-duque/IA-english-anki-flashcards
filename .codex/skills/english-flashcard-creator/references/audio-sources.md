# Catálogo de fontes de áudio

Este arquivo registra fontes de áudio já pesquisadas pela skill `english-flashcard-creator`. Consultá-lo antes de pesquisar uma palavra nova e atualizá-lo sempre que uma fonte nova for encontrada.

## Critérios de registro

Para cada site novo, registrar:

- nome e URL;
- tipo de material: palavra isolada, frase, expressão ou gravação de falante;
- variantes e idiomas disponíveis;
- formato ou forma de download;
- licença e condições de reutilização;
- observações sobre qualidade, cobertura e necessidade de conversão;
- data da verificação, quando relevante.

Não assumir que um áudio pode ser baixado ou redistribuído apenas porque pode ser reproduzido no navegador. Se a licença não estiver clara, registrar a fonte, mas deixar a licença como não verificada e não anexar o arquivo ao Anki para redistribuição sem confirmação.

## Fontes conhecidas

### 1000EnglishWords

- **URL:** [1000 English Words — Audio](https://www.1000englishwords.com/audio/#top)
- **Tipo:** pronúncia de palavras isoladas da lista de 1.000 palavras; não é uma fonte geral para frases ou expressões.
- **Variantes:** a página apresenta pronúncia em inglês; a variante regional deve ser tratada como não especificada, salvo indicação explícita no próprio player.
- **Formato:** player HTML/JavaScript acionado ao clicar na palavra; identificar o `src` real do elemento de áudio antes de baixar. Não gravar o URL remoto diretamente no campo `Audio`.
- **Licença:** não presumir licença de redistribuição apenas porque o áudio pode ser reproduzido. Registrar como não verificada até existir uma indicação explícita da fonte.
- **Procedimento:** procurar a palavra na lista; inspecionar o elemento/player correspondente; obter o arquivo somente se o `src` estiver acessível e a reutilização for aceitável; anexar o arquivo à mídia do Anki e então usar `[sound:arquivo.mp3]`. Se não houver correspondência ou arquivo utilizável, deixar os campos de áudio vazios.
- **Otimização:** reutilizar um cache local por palavra e URL normalizada, evitar baixar duas vezes o mesmo áudio e validar o conteúdo retornado antes de salvar. Não fazer varredura dos 1.000 arquivos antecipadamente.
- **Observação:** a página é dinâmica; o HTML indexado pode mostrar apenas placeholders. A extração deve preferir o DOM/estado do player e ter fallback silencioso para ausência de áudio.
- **Verificação:** 2026-09-17.

### Wiktionary / Wikimedia Commons

- **URL:** [Wiktionary](https://en.wiktionary.org/) / [Wikimedia Commons](https://commons.wikimedia.org/)
- **Tipo:** pronúncia de palavras e algumas expressões; normalmente gravações curtas de uma palavra.
- **Variantes:** depende do verbete; procurar principalmente US e UK.
- **Formato:** frequentemente `.ogg`; converter para `.mp3` para maior compatibilidade com Anki e aplicativos móveis.
- **Licença:** conferir a página individual do arquivo no Wikimedia Commons. A licença pode variar entre arquivos.
- **Procedimento:** abrir o verbete em inglês, localizar `Pronunciation`, abrir o arquivo e conferir a licença antes de baixar.
- **Exemplos verificados:** [en-us-huge.ogg](https://en.wiktionary.org/wiki/File:en-us-huge.ogg) e [en-us-usually.ogg](https://en.wiktionary.org/wiki/File:en-us-usually.ogg).
- **Observação:** é a fonte padrão inicial por combinar boa cobertura com informações de origem e licença, mas a existência do arquivo não significa que ele já esteja na coleção de mídia do Anki.

## Histórico de novas fontes

Quando uma pesquisa futura encontrar um site que não esteja acima, adicionar uma nova subseção antes de concluir a execução. Não remover fontes antigas; atualizar apenas informações verificadas.
