# skill-slides-ideia

Sistema de criação de apresentações desenvolvido pela **Squad SDD** para o **Laboratório IDE.IA**.

A `skill-slides-ideia` foi criado para **padronizar a produção de apresentações do laboratório**, tornando mais simples criar slides que sigam a identidade visual do IDE.IA sem que cada pessoa precise reconstruir manualmente cores, tipografia, espaçamentos e layouts.

A solução reúne:

- identidade visual do IDE.IA;
- sistema de cores e tipografia;
- layouts pré-definidos;
- elementos e ativos da marca;
- regras de composição e hierarquia;
- limites de conteúdo por layout;
- geração de apresentações em HTML 16:9.

O resultado é um **arquivo HTML autocontido**, que pode ser aberto diretamente no navegador, apresentado em tela cheia ou convertido para PDF.

---

## Por que o skill-slides-ideia existe?

Antes de um sistema padronizado, cada apresentação pode acabar seguindo uma lógica visual diferente: fontes, tamanhos, cores, espaçamentos e formas de organizar o conteúdo.

A `skill-slides-ideia` busca resolver isso criando uma **base visual única para as apresentações do IDE.IA**.

A proposta é simples:

> **Quem cria a apresentação deve se preocupar com a mensagem. O sistema cuida da consistência visual.**

Isso permite que diferentes pessoas e equipes produzam materiais que mantenham uma identidade comum, mesmo sem conhecimento aprofundado de design ou CSS.

---

# Como usar

Você não precisa conhecer HTML ou CSS para utilizar o sistema.

A forma mais simples é utilizar a skill em uma ferramenta compatível, como o Claude, e descrever o que precisa apresentar.

### Exemplo

> Crie uma apresentação de 8 slides sobre o nosso projeto de inteligência artificial. O público é institucional e o objetivo é apresentar o problema, a solução, os resultados e os próximos passos. Use modo claro.

A partir dessas informações, a skill organiza o conteúdo utilizando os padrões visuais definidos pela `skill-slides-ideia`.

Você pode informar:

- **Tema**
- **Objetivo**
- **Público**
- **Quantidade de slides**
- **Tom da apresentação**
- **Modo claro ou escuro**
- **Informações obrigatórias**
- **Dados ou conteúdos que precisam ser destacados**

### Outro exemplo

> Preciso apresentar o processo de SDD para novos integrantes do laboratório. Faça uma apresentação didática de 7 slides, começando pelo problema, passando pelo processo e terminando com os benefícios.

Não é necessário dizer qual layout deve ser utilizado em cada slide.

**O sistema escolhe a estrutura mais adequada para cada conteúdo.**

---

# Estrutura dos slides

O sistema possui nove layouts principais:

| Layout | Utilização |
|---|---|
| `l-abertura` | Abertura visual da apresentação |
| `l-capa` | Apresentação do tema |
| `l-divisoria` | Separação entre grandes blocos |
| `l-titulo-texto` | Uma afirmação acompanhada de texto ou bullets |
| `l-cartoes` | Apresentação de até três itens paralelos |
| `l-dado` | Destaque para um número ou métrica |
| `l-comparacao` | Tabelas e comparações |
| `l-imagem` | Conteúdo visual com imagem em destaque |
| `l-encerramento` | Encerramento da apresentação |

Cada layout possui uma estrutura própria e um limite de conteúdo.

### O conteúdo não deve ser comprimido para caber.

Se uma informação ultrapassa o limite adequado de um layout, o correto é **dividir o conteúdo em outro slide**, mantendo a legibilidade.

---

# Identidade visual

A `skill-slides-ideia` aplica os fundamentos visuais definidos pelo IDE.IA.

### Cores

A paleta trabalha principalmente com:

- Verde principal
- Verde secundário
- Preto
- Branco
- Navy

O sistema evita a utilização de cores adicionais ou gradientes que descaracterizem a identidade visual.

### Tipografia

A fonte principal é **Urbanist**.

A hierarquia tipográfica diferencia:

- títulos;
- subtítulos;
- corpo de texto;
- legendas.

A diferenciação acontece principalmente por **tamanho e peso**, mantendo uma hierarquia consistente entre os slides.

### Composição

As apresentações seguem princípios como:

- uma ideia principal por slide;
- hierarquia visual clara;
- espaçamento adequado;
- conteúdo objetivo;
- boa leitura em projeção;
- consistência entre slides;
- ausência de elementos desnecessários.

Também existe um **piso tipográfico**, evitando que textos sejam reduzidos excessivamente apenas para acomodar mais conteúdo.

---

# Como criar uma boa apresentação

O sistema cuida da parte visual, mas o conteúdo continua sendo fundamental.

Ao solicitar uma apresentação, procure informar principalmente **o que precisa ser comunicado**.

### 1. Explique o objetivo

Em vez de:

> Faça slides sobre inteligência artificial.

Prefira:

> Explique para gestores como a inteligência artificial pode reduzir o tempo gasto em tarefas operacionais.

---

### 2. Informe quem vai assistir

Por exemplo:

> O público não possui conhecimento técnico.

ou:

> A apresentação será para desenvolvedores que já conhecem SDD.

Isso ajuda a definir o nível de profundidade da apresentação.

---

### 3. Informe a narrativa

Se já souber como quer conduzir a apresentação, informe a sequência:

> Quero apresentar:
>
> 1. O problema
> 2. A solução
> 3. Como funciona
> 4. Resultados
> 5. Próximos passos

A estrutura visual será organizada a partir dessa narrativa.

---

# Apresentação

Abra o arquivo gerado em qualquer navegador compatível.

A apresentação utiliza proporção **16:9**, podendo ser exibida em:

- computador;
- notebook;
- televisão;
- projetor;
- tela cheia do navegador.

O sistema foi desenvolvido para preservar a composição visual em diferentes tamanhos de exibição.

---

# Uso como sistema CSS

Além da geração automatizada, a `skill-slides-ideia` também pode ser utilizado diretamente como sistema de CSS.

A estrutura principal do projeto é:

```text
skill-slides-ideia/
├── tokens/
│   ├── colors.css
│   ├── typography.css
│   └── canvas.css
│
├── layouts.css
├── styles.css
│
├── build/
│   ├── deck-fonte.html
│   └── build-template.py
│
├── references/
├── assets/
├── fonts/
└── examples/
```

Os tokens definem os fundamentos visuais, enquanto `layouts.css` contém os layouts disponíveis.

---

# Escala e responsividade

O sistema utiliza `cqw` para dimensionar os elementos em relação ao próprio slide.

No canvas de referência:

```text
1920 × 1080
```

`1cqw` corresponde a aproximadamente `19,2px`.

Isso permite que a apresentação mantenha proporções consistentes em diferentes tamanhos.

### Importante

Não utilize `vw` para dimensionar elementos internos dos slides.

`vw` considera a largura da janela do navegador.

`cqw` considera a largura do próprio slide.

---

# Compatibilidade

O sistema utiliza recursos modernos de CSS.

| Recurso | Suporte |
|---|---|
| Container Queries | Chrome 105+, Safari 16+, Firefox 110+ |
| Subgrid | Chrome 117+, Safari 16+, Firefox 71+ |

Existem valores de fallback para navegadores sem suporte a `cqw`.

O documento deve utilizar:

```html
<html lang="pt-BR">
```

para que o navegador reconheça corretamente o idioma da apresentação e aplique os recursos de hifenização disponíveis.

---

# Organização

### `tokens/`

Fundamentos visuais:

- cores;
- tipografia;
- escala;
- espaçamento;
- canvas.

### `layouts.css`

Os nove layouts disponíveis.

### `assets/`

Elementos da identidade do IDE.IA:

- logos;
- ícones;
- padrões;
- ilustrações.

### `fonts/`

Arquivos da fonte Urbanist para utilização offline.

### `references/`

Documentação dos fundamentos visuais e regras do sistema.

### `examples/`

Arquivos HTML de exemplo e saída do sistema.

---

# Licenças

## Urbanist

A Urbanist é distribuída sob a **SIL Open Font License 1.1**.

A licença correspondente está disponível em:

```text
fonts/OFL-Urbanist.txt
```

Esse arquivo deve acompanhar a fonte em qualquer redistribuição.

## Identidade visual do IDE.IA

Logos, ícones, padrões, ilustrações e demais ativos visuais pertencem à identidade visual do **IDE.IA**.

Os materiais são disponibilizados para utilização relacionada ao laboratório e não representam uma licença de uso da identidade visual por terceiros.

---