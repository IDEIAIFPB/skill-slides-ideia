# IDE.IA — Fundamentos da marca

Fonte de verdade para cor, tipo, forma, ícone, logo e voz. Vale para todo slide.
As regras duras que você precisa saber antes de qualquer coisa estão no
SKILL.md; este arquivo é a referência completa, para consultar quando a decisão
não estiver óbvia.

## Paleta

Dois verdes mais preto/branco/navy. **Nenhuma outra matiz, nenhum gradiente.**

| Token | Valor | Papel |
|---|---|---|
| `--green-600` | `#3FA14C` | Verde folha — marca, sobrelinhas, ícones e destaques no claro |
| `--green-400` | `#80E978` | Menta — grandes preenchimentos, divisórias, badges, destaque no escuro |
| `--green-200` / `--green-100` | `#B7EFB2` / `#E7F9E5` | Tintas derivadas, preenchimentos sutis |
| `--black` / `--white` | `#000` / `#FFF` | Base |
| `--gray-900` / `--gray-600` / `--gray-200` | `#1A1A1A` / `#5C5C5C` / `#E3E3E3` | Corpo / legenda / fio |
| `--navy-900` | `#111A24` | Fundo do modo escuro |
| `--navy-800` | `#182430` | Painel de cartão sobre navy |
| `--green-legend-dark` | `#1B4220` | Célula destacada em tabela escura |

Prefira sempre os apelidos semânticos (`--surface-page`, `--text-brand`,
`--text-body-inverse`, …) em vez do hex ou do token de paleta cru.

**Contraste:** a menta reprova como texto sobre branco. Ela é preenchimento —
ou texto sobre navy. Corpo de texto é `--text-body` no claro e
`--text-body-inverse` no escuro.

## Tipografia

**Urbanist, e só ela.** Não existe segunda família, nem fonte substituta. O
contraste entre níveis vem de três coisas:

- **Peso** — rótulo de seção e display em 800, subtítulo em 600, corpo em 400,
  kicker da capa em 700. O subtítulo é mais leve de propósito: ele já vem logo
  abaixo de um rótulo em 800, e dois pesos pesados empilhados brigam.
- **Tamanho** — os saltos da escala são largos de propósito. Níveis próximos
  demais leem como um borrão.
- **Caixa** — tudo em caixa de frase ("Exemplo de título"), inclusive o rótulo
  de seção que faz o papel de título. A caixa alta sobrou num lugar só: o kicker
  pequeno da capa e do encerramento, onde é rótulo e não título — e lá o CSS
  aplica sozinho, então escreva em caixa de frase no HTML. Nunca Title Case.

Tracking negativo em display e título (`--tr-display`, `--tr-title`) não é
detalhe: a Urbanist é geométrica e de x-height alto, e sem isso um título de 81px
parece frouxo. As classes `.display` e `.titulo` já aplicam.

**O rótulo de seção é o título.** Num slide de conteúdo a hierarquia é rótulo
(92px, caixa de frase, verde) → subtítulo (58px) → corpo (48px) → legenda (26px). O
rótulo diz do que o slide trata; a frase abaixo desenvolve o rótulo. Não inverta:
um rótulo menor que a frase que ele encabeça deixa de rotular qualquer coisa.

Todo texto do slide é **justificado**, herdado da `.area`, com hifenização
automática. Quanto mais estreita a coluna, mais visíveis ficam os vãos entre as
palavras — em coluna estreita, como a dos cartões, prefira frases mais curtas.

Na capa e no encerramento a lógica muda, porque ali o `display` (134px) é o
título e o rótulo volta a ser um kicker discreto de 34px.

Piso absoluto: **26px no canvas de referência** (`--t-caption`). Nada menor
existe num slide, seja legenda, fonte de dado ou rodapé.

## Forma

- **Claro: quina viva em tudo.** Sem cartão arredondado, sem imagem
  arredondada, sem botão pílula. As únicas curvas são os pontos do logo e o
  badge circular de ícone (`--radius-icon-badge`).
- **Escuro:** painéis de cartão arredondados, `--radius-card-dark`. É o único
  lugar onde raio é permitido num container.
- **Sem sombra** como recurso de separação no claro. Separe com espaço em branco
  e contraste. Um fio (`--border-hairline`) serve para tabela e divisor quando o
  branco não basta.

Não misture os dois regimes num mesmo slide.

## Ícones

**Atenção: os dois conjuntos não são o mesmo ícone em dois estilos.** São
coleções diferentes, com nomes diferentes e sem correspondência entre si.
Consulte o inventário abaixo antes de escolher — pedir `icon-analytics` no
conjunto escuro devolve imagem quebrada, porque ele não existe lá.

**Claro** — `assets/icons/`, 21 ícones. Duas cores chapadas: preto (`#000000`) e
verde folha (`#3fa14c`).

```
ai-chip · ai-circuit · analytics · bug-scan · check-circle · check-clock
checklist · dashboard · data-pipeline · direction · gis-badge · laptop-check
leadership · misc-a · people-pair · rocket-growth · rocket-launch
search · search-settings · team · trophy
```

**Escuro** — `assets/icons-dark/`, 9 ícones. Uma cor só, menta (`#80e978`).

```
ai-brain · customization · dev-console · globe · id-card
infinity · person · risk-cost · support
```

Todos existem em `.svg` e `.png`. Prefira o SVG: escala limpo na projeção.

**Nunca misture os dois conjuntos no mesmo slide** — os pesos de traço e o número
de cores são diferentes e a mistura fica evidente.

Como os ícones claros têm preto chapado, eles **somem sobre o navy**. Se o
conjunto escuro não tiver o conceito que você precisa, há duas saídas honestas:
escolher outro conceito que exista no conjunto escuro, ou embutir o SVG claro
inline no HTML (não via `<img>`, que não recolore) e trocar `#000000` por
`#FFFFFF` e `#3fa14c` por `#80e978`.

Ícones soltos junto ao texto, ou dentro de um badge circular preenchido quando
precisam ser lidos de relance numa grade. Emoji e glifo unicode como ícone estão
fora.

## Logo e padrão

- **No HTML use sempre `assets/logo/ideia-logo-full.png`**, inclusive nos slides
  escuros. A troca para `ideia-logo-full-white.png` é automática via CSS
  (`.dark .marca`), para não depender de alguém lembrar de trocar o `src`.
- **O logo aparece em três lugares e só neles:** primeiro slide, divisórias que
  abrem um bloco, e último slide. Nos slides de miolo não há logo — a marca já
  está na cor, na tipografia e no padrão, e repetir o lockup em todo slide só
  rouba espaço do conteúdo.
- Tamanho único: 4.6cqw (~88px @1920), canto inferior direito.
- A regra é por layout no CSS, não por disciplina: um `<img class="marca">` posto
  num slide de miolo simplesmente não renderiza.
- Só os layouts com logo reservam a faixa dele no padding de baixo. Os de miolo
  usam a altura inteira do slide.
- A marca isolada (`ideia-logo-mark.png`) é quadrada e some quando reduzida ao
  tamanho do logo corrente. Use o lockup completo. Os SVGs em
  `assets/logo/svg/01–10.svg` cobrem variações de badge e uma marca mono em
  `currentColor` (`09.svg`) para recolorir exato — índice em
  `assets/logo/README.md`.
- **Assinatura da marca:** o line-art de rede
  (`assets/patterns/network-outline-*.png`) ampliado e sangrando por um canto,
  em opacidade baixa. Nunca centralizado, nunca disputando com o texto. Funciona
  em capa, divisória e encerramento.

## Voz (PT-BR)

- Português do Brasil por padrão. Tom institucional, instrutivo, terceira
  pessoa. Sem hype, sem adjetivo de venda.
- Títulos em caixa de frase. Sobrelinhas em caixa alta, 1–2 palavras:
  "LABORATÓRIO", "MÉTODO", "RESULTADO".
- Escreva do lado de quem lê. Específico sempre ganha de esperto.
- Um slide afirma uma coisa. Se o título tem "e" no meio, provavelmente são dois
  slides.
- Sem emoji.
- Fechamento caloroso: "Obrigada!" no deck claro, "Obrigado!" no escuro — nunca
  "obrigado pela atenção".
- Lorem Ipsum é aceitável como preenchimento, desde que sinalizado como
  provisório.
