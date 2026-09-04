#!/usr/bin/env python3
"""
Gera examples/deck-exemplo.html como um arquivo HTML AUTOCONTIDO.

Por que isso existe
-------------------
Um deck que aponta para `styles.css` e `assets/` só funciona se estiver dentro
da pasta da skill. Como artifact, como anexo, ou como arquivo solto na máquina
de outra pessoa, nada disso resolve — e o HTML abre completamente sem estilo.

Este script embute tudo num arquivo só: o CSS inteiro num `<style>` e todo asset
referenciado como data URI. O resultado abre em qualquer lugar.

Como usar
---------
    python3 build/build-template.py

Rode sempre que mexer em tokens/, layouts.css, nos assets, ou no HTML fonte
(build/deck-fonte.html). O arquivo em examples/ é derivado — não edite ele à
mão, edite o fonte e rebuilde.

Requer Pillow: pip install Pillow --break-system-packages
"""

import base64
import io
import pathlib
import re
import sys

RAIZ = pathlib.Path(__file__).resolve().parent.parent
FONTE = RAIZ / "build" / "deck-fonte.html"
SAIDA = RAIZ / "examples" / "deck-exemplo.html"

# Ordem de import declarada em styles.css. Mantenha em sincronia com ele.
CSS_NA_ORDEM = [
    "tokens/colors.css",
    "tokens/typography.css",
    "tokens/canvas.css",
    "layouts.css",
]

LARGURA_MAX = 1200  # padrões de rede grandes não precisam de mais que isso


def embute(caminho: pathlib.Path) -> tuple[str, int]:
    """Devolve (data URI, bytes). SVG vai como texto; bitmap vai otimizado.

    Os assets da marca são line art e chapados, de pouquíssimas cores. Uma
    paleta indexada corta cerca de 85% do peso sem diferença visível, e é isso
    que torna a incorporação viável — sem ela o padrão de rede sozinho passaria
    de 400KB em base64.
    """
    ext = caminho.suffix.lower()

    if ext == ".svg":
        bruto = caminho.read_bytes()
        b64 = base64.b64encode(bruto).decode()
        return f"data:image/svg+xml;base64,{b64}", len(bruto)

    from PIL import Image

    im = Image.open(caminho)
    if im.width > LARGURA_MAX:
        im = im.resize(
            (LARGURA_MAX, round(im.height * LARGURA_MAX / im.width)),
            Image.LANCZOS,
        )
    buf = io.BytesIO()
    if ext in (".jpg", ".jpeg"):
        im.convert("RGB").save(buf, "JPEG", quality=82, optimize=True)
        mime = "image/jpeg"
    else:
        im.convert("RGBA").quantize(colors=64, method=Image.FASTOCTREE).save(
            buf, "PNG", optimize=True
        )
        mime = "image/png"
    dados = buf.getvalue()
    return f"data:{mime};base64," + base64.b64encode(dados).decode(), len(dados)


def main() -> None:
    if not FONTE.exists():
        sys.exit(f"fonte não encontrada: {FONTE}")

    # 1. CSS empacotado na ordem correta
    partes = []
    for rel in CSS_NA_ORDEM:
        arq = RAIZ / rel
        if not arq.exists():
            sys.exit(f"CSS ausente: {rel}")
        partes.append(f"/* ===== {rel} ===== */\n{arq.read_text()}")
    css = "\n\n".join(partes)

    html = FONTE.read_text()
    if "<!--CSS-->" not in html:
        sys.exit("o fonte precisa do marcador <!--CSS-->")

    # 2. Todo asset referenciado no HTML, embutido
    total = 0
    refs = sorted(set(re.findall(r'src="(\.\./assets/[^"]+)"', html)))
    for ref in refs:
        arq = (RAIZ / "examples" / ref).resolve()
        if not arq.exists():
            sys.exit(f"asset ausente: {ref}")
        uri, tam = embute(arq)
        total += tam
        html = html.replace(f'src="{ref}"', f'src="{uri}"')
        print(f"  {ref[3:]:48s} {tam/1024:6.1f}KB")

    # 3. O logo branco do modo escuro entra pelo CSS (content: url), não pelo
    #    HTML. Sem embutir esse também, o modo escuro quebra fora da pasta.
    alvo = "assets/logo/ideia-logo-full-white.png"
    if alvo in css:
        uri, tam = embute(RAIZ / alvo)
        total += tam
        css = css.replace(f'url("{alvo}")', f'url("{uri}")')
        print(f"  {alvo:48s} {tam/1024:6.1f}KB  (via CSS)")

    html = html.replace("<!--CSS-->", f"<style>\n{css}\n</style>")

    # 4. Verificação: nada pode ter sobrado apontando para fora
    sobras = re.findall(r'(?:src|href)="(?!data:)([^"]*(?:\.\./|\.css)[^"]*)"', html)
    if sobras:
        sys.exit(f"referências externas remanescentes: {sorted(set(sobras))}")

    SAIDA.write_text(html)
    print(f"\n  CSS embutido      {len(css)/1024:6.1f}KB")
    print(f"  assets embutidos  {total/1024:6.1f}KB  ({len(refs)+1} arquivos)")
    print(f"\n{SAIDA.relative_to(RAIZ)} — {len(html)/1024:.0f}KB, autocontido")


if __name__ == "__main__":
    main()
