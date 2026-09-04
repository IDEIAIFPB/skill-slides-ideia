# IDE.IA — Layouts e orçamento de conteúdo

Oito layouts. Cada um tem um número fixo de espaços e um limite de palavras por
espaço. Escolha o layout pelo formato da ideia, preencha os espaços, e pare.

O limite existe porque a saída errada é sempre a mesma: espremer mais um item no
slide que já está cheio. **Quando o conteúdo não cabe nos espaços, ele vira outro
slide.** Diminuir o corpo de texto para caber está proibido — o piso da escala
(24px no canvas de referência) não é negociável.

Os limites são de conteúdo, não de caracteres: estourar uma palavra não invalida
o slide, mas estourar em 50% significa que a ideia não é uma só e precisa ser
dividida.

## Estrutura de todo slide

Dois níveis, sempre. A classe do layout vai na `.area`; o modo vai na `.slide`.
Elementos sangrados (logo corrente, padrão de rede) ficam fora da `.area`, como
filhos diretos da `.slide`.

```html
<section class="slide">              <!-- + .dark ou .accent quando for o caso -->
  <div class="area l-titulo-texto">
    …conteúdo…
  </div>
  <img class="marca" src="assets/logo/ideia-logo-full.png" alt="IDE.IA">
</section>
```

Nunca coloque padding na `.slide`: ela é o container de consulta, e padding em
`cqw` nela mesma é circular — o navegador devolve um valor diferente do escrito e
a escala de texto passa a variar de layout para layout. A margem vive na `.area`.

---

## Tabela de decisão

| A ideia é… | Layout | Classe da `.area` | Modo |
|---|---|---|---|
| o primeiro slide, antes de tudo | Abertura | `l-abertura` | `.dark` |
| a capa da apresentação | Capa | `l-capa` | — |
| a virada para uma nova seção | Divisória | `l-divisoria` | `.accent` |
| uma afirmação com apoio | Título + texto | `l-titulo-texto` | — |
| três coisas paralelas | Três cartões | `l-cartoes` | — |
| um número que carrega o argumento | Dado | `l-dado` | — |
| opções avaliadas nos mesmos critérios | Comparação | `l-comparacao` | `.dark` |
| algo que precisa ser visto | Imagem + texto | `l-imagem` | — |
| o fim | Encerramento | `l-encerramento` | `.dark` |

Se nenhum serve, o problema quase sempre é a ideia estar grande demais para um
slide. Divida antes de inventar um nono layout.

---

## 0. Abertura — `l-abertura`

O primeiro slide do deck: **só o logo, centrado, em fundo escuro.** Nenhum texto,
nem título, nem data. É a marca sozinha antes de a apresentação começar.

Use a versão branca do logo, já que o fundo é escuro. Este é o único lugar em que
o logo vai no meio do slide, com a classe `logo-central` em vez de `marca`.

```html
<section class="slide dark">
  <div class="area l-abertura">
    <img class="logo-central" src="assets/logo/ideia-logo-full-white.png" alt="IDE.IA">
  </div>
</section>
```

## 1. Capa — `l-capa`

Espaços: sobrelinha · título display · régua · legenda opcional.

- Título: **máximo 8 palavras**, caixa de frase.
- Kicker: 1–2 palavras. Escreva em caixa de frase — na capa o CSS aplica a
  caixa alta sozinho.
- Legenda: uma linha (autor, data, contexto). Opcional.
- Sem bullets, sem subtítulo longo.
- A sobrelinha e o `bloco-titulo` são dois grupos: o layout empurra um para o
  topo e o outro para a base. Sem esse agrupamento os quatro elementos se
  espalham soltos pela altura toda.

```html
<section class="slide">
  <div class="area l-capa">
    <p class="eyebrow">Laboratório</p>
    <div class="bloco-titulo">
      <h1 class="display">Título da apresentação em caixa de frase</h1>
      <hr class="regua">
      <p class="legenda">Nome do time · Março de 2026</p>
    </div>
  </div>
  <img class="padrao" src="assets/patterns/network-outline-large.png" alt="">
  <img class="marca" src="assets/logo/ideia-logo-full.png" alt="IDE.IA">
</section>
```

## 2. Divisória — `l-divisoria`

A divisória é um dos três slides com logo — junto da capa e do encerramento.

Banda menta cheia. Espaços: número da seção · título.

- Título: **máximo 6 palavras**, em tamanho display.
- **Centralizado.** Junto com o encerramento, é o único layout centrado — o
  contraste com os slides alinhados à esquerda é o que dá ritmo ao deck.
- Nada mais entra. Sem descrição, sem prévia do que vem a seguir.

```html
<section class="slide accent">
  <div class="area l-divisoria">
    <p class="num">02</p>
    <h2 class="titulo">Método</h2>
  </div>
</section>
```

## 3. Título + texto — `l-titulo-texto`

**Coluna única de largura cheia**, empilhada: sobrelinha, título, régua e o
bloco de conteúdo, cada um ocupando a largura inteira da área. O parágrafo sai
em `--t-prosa` e justificado; os bullets, em `--t-prosa` e distribuídos na
altura que sobra.

Espaços: rótulo de seção (o título, 92px) · subtítulo (60px) · régua · **um** bloco de conteúdo.

- Título: máximo 8 palavras.
- O bloco é **ou** um parágrafo de até 40 palavras **ou** até 3 bullets de até
  12 palavras cada. Nunca os dois.
- Quatro bullets significam dois slides.
- Os bullets saem em `--t-lead` (49px @1920), não em corpo, e o bloco cresce para
  ocupar o que sobra da área. Isso é automático — não sobrescreva.

```html
<section class="slide">
  <div class="area l-titulo-texto">
    <div>
      <p class="eyebrow">Contexto</p>
      <h2 class="titulo">Uma afirmação por slide</h2>
      <hr class="regua">
    </div>
    <ul class="bullets">
      <li>Primeiro ponto, curto e verificável</li>
      <li>Segundo ponto, no mesmo nível de abstração</li>
      <li>Terceiro ponto, e nada além disso</li>
    </ul>
  </div>
  <img class="marca" src="assets/logo/ideia-logo-full.png" alt="IDE.IA">
</section>
```

Para a versão em parágrafo, troque a `<ul class="bullets">` por
`<p class="corpo">…</p>`.

## 4. Três cartões — `l-cartoes`

Espaços: título · **exatamente três** cartões.

- Cada cartão: ícone · título de até 4 palavras · texto de até 18 palavras.
- Os três saem **sempre do mesmo tamanho**, e as faixas internas (ícone, título,
  texto) se alinham entre eles via `subgrid` — um título de duas linhas não
  desloca o texto dos vizinhos. Não sobrescreva a altura do cartão.
- O texto do cartão sai em `--t-lead` e o título em 3.2cqw. Em tamanho de corpo
  o cartão não preenche a altura e abre um vão morto entre título e texto.
- **Não use `class="corpo"` no texto do cartão** — use `<p>` puro. A `.corpo`
  justifica, e numa coluna de 528px a justificação sobra 4 ou 5 palavras por
  linha, estoura os vãos e hifeniza palavra no meio. O CSS do cartão já força o
  alinhamento à esquerda, mas escreva certo mesmo assim.
- Dois itens não são este layout (use título + texto). Quatro não são este
  layout (corte para três ou vire dois slides).
- O `numero-fantasma` só entra se os três cartões forem uma **sequência real** —
  etapa 01, 02, 03. Em itens paralelos, numerar é mentira.

```html
<section class="slide">
  <div class="area l-cartoes">
    <h2 class="titulo">Título da seção</h2>
    <div class="grade-cartoes">
      <article class="cartao">
        <span class="numero-fantasma">01</span>
        <img class="icone" src="assets/icons/icon-data-pipeline.svg" alt="">
        <h3>Coletar</h3>
        <p>Frase curta que explica a etapa sem repetir o título.</p>
      </article>
      <!-- mais dois, mesma estrutura -->
    </div>
  </div>
  <img class="marca" src="assets/logo/ideia-logo-full.png" alt="IDE.IA">
</section>
```

## 5. Dado — `l-dado`

Espaços: rótulo de seção (92px) · um número · o que ele mede · uma frase de contexto · fonte.

- Empilhado: número, rótulo em tamanho de título e contexto justificado de
  largura cheia. O rótulo grande é o que segura a composição embaixo do número.
- O rótulo de seção fica **colado no número**, como rótulo dele — os dois centram
  juntos. A fonte ancora sozinha no rodapé. Escala do slide: 34 · 346 · 100 ·
  59 · 26.
- **Um** número por slide. Dois números competem e nenhum é lido.
- Rótulo: até 5 palavras. Contexto: até 20 palavras.
- Sempre cite a fonte na legenda — é um laboratório de pesquisa.
- Três grupos: sobrelinha, `bloco-metrica` e legenda. O número é a estrela do
  slide e ocupa 346px no canvas 1920 — não o encolha para abrir espaço.

```html
<section class="slide">
  <div class="area l-dado">
    <p class="eyebrow">Resultado</p>
    <div class="bloco-metrica">
      <p class="metrica">87%</p>
      <p class="rotulo">de precisão na validação</p>
      <p class="contexto">Medido em 1.200 casos anotados por três revisores independentes.</p>
    </div>
    <p class="legenda">Fonte: relatório interno, fev/2026</p>
  </div>
  <img class="marca" src="assets/logo/ideia-logo-full.png" alt="IDE.IA">
</section>
```

## 6. Comparação — `l-comparacao`

Modo escuro. Espaços: título · tabela.

- **Máximo 4 colunas × 6 linhas**, contando o cabeçalho.
- Cada célula: até 4 palavras. Célula é rótulo, não frase.
- Marque as vencedoras com `class="destaque"` — e marque poucas, senão o
  destaque deixa de destacar.
- Tabela maior que isso não é slide, é anexo.

```html
<section class="slide dark">
  <div class="area l-comparacao">
    <h2 class="titulo">Comparação de abordagens</h2>
    <table class="tabela">
      <tr><th>Critério</th><th>Opção A</th><th>Opção B</th></tr>
      <tr><td>Custo</td><td class="destaque">Baixo</td><td>Alto</td></tr>
    </table>
  </div>
  <img class="marca" src="assets/logo/ideia-logo-full.png" alt="IDE.IA">
</section>
```

## 7. Imagem + texto — `l-imagem`

Espaços: uma imagem sangrando na metade · sobrelinha · título · um parágrafo.

- Título até 8 palavras, parágrafo até 30 palavras.
- A imagem ocupa metade inteira e sangra até a borda. Imagem pequena e centrada
  com legenda embaixo não é este layout — e não é a marca.

```html
<section class="slide">
  <div class="area l-imagem">
    <img class="figura" src="assets/illustrations/landscape-placeholder.jpeg" alt="Descrição">
    <div class="texto">
      <p class="eyebrow">Campo</p>
      <h2 class="titulo">O que a imagem sustenta</h2>
      <p class="corpo">Parágrafo curto que diz o que ver, não o que já está visível.</p>
    </div>
  </div>
</section>
```

## 8. Encerramento — `l-encerramento`

**Sempre em modo escuro**, espelhando a abertura: o deck abre e fecha na marca.

Espaços: agradecimento · até três linhas de contato.

- Alinhado à esquerda, ancorado embaixo. O logo sobe para o **alto à esquerda**
  (o CSS reposiciona sozinho) e o padrão de rede toma a metade direita.
- "Obrigada!" — informal, nunca "obrigado pela atenção".
- Sem resumo, sem próximos passos, sem QR code decorativo.

```html
<section class="slide dark">
  <div class="area l-encerramento">
    <h2 class="display">Obrigada!</h2>
    <div class="contatos">
      <span>@ide.ia_</span>
      <span>IDE.IA</span>
    </div>
  </div>
  <img class="padrao" src="assets/patterns/network-outline-large.png" alt="">
  <img class="marca" src="assets/logo/ideia-logo-full.png" alt="IDE.IA">
</section>
```

O pacote não traz ícones de Instagram ou LinkedIn — os conjuntos em `assets/`
são temáticos, não de redes sociais, e logos de terceiros não entram aqui. Se
quiser os ícones ao lado dos contatos, coloque os oficiais em `assets/icons/` e
referencie por nome.

---

## Ocupação

O teto de conteúdo desta skill é rígido, e por isso ela tende ao erro oposto:
slide com pouca coisa boiando no branco. Por isso existe também um piso.

O conteúdo tem que ocupar **pelo menos 75% da altura e 80% da largura** da área.
Se não ocupar, na ordem:

1. Título com 5 palavras ou menos? Troque `.titulo` por `.display`.
2. Ainda sobra metade do slide? Falta conteúdo — junte com o slide vizinho em vez
   de esticar o que existe.
3. Nunca resolva aumentando margem ou entrelinha até o texto "preencher". Isso
   dilui, não preenche.

Um alerta sobre `space-between`: ele distribui os **filhos diretos** da `.area`.
Se você deixar cinco elementos soltos, eles se espalham e abrem um buraco no
meio. Agrupe em dois ou três blocos, como fazem a capa e o slide de dado.

## Ritmo do deck

Um deck que só usa `l-titulo-texto` cansa mesmo respeitando todos os limites.
Alterne: uma divisória a cada 4–6 slides, e pelo menos um slide de dado ou imagem
entre blocos de texto. A divisória menta é o respiro visual do deck — ela existe
para quebrar sequências brancas.

Uma assinatura por slide, não três. O padrão de rede, a régua menta e o algarismo
fantasma são fortes; usar os três no mesmo slide anula todos.
