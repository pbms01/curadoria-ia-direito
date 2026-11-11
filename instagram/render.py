#!/usr/bin/env python3
"""Renderiza o carrossel do dia a partir de posts/AAAA-MM-DD/post.json.

Uso (na raiz do repositorio): python3 instagram/render.py instagram/posts/2026-11-11

Decisao de arquitetura: o agente so escreve o JSON (texto); todo o design mora
aqui, em HTML/CSS fixo. Isso garante identidade visual identica todo dia e
impede que o modelo "redesenhe" o post a cada execucao.

Saida: slide-01.jpg ... slide-NN.jpg (1080x1350, JPEG, exigencia da API do
Instagram) e legenda.txt, na mesma pasta do post.json.
Codigo de saida 2 = algum slide estourou a area util; o agente deve encurtar
o texto do slide indicado e renderizar de novo.
"""
import html
import json
import re
import shutil
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

RAIZ = Path(__file__).resolve().parent
LARGURA, ALTURA = 1080, 1350
HANDLE = "@pedroborgesmourao"
MARCA = "IA Jurídica por Dentro"
LIMITE_LEGENDA = 2200  # limite da API do Instagram


def fmt(texto: str) -> str:
    """Escapa HTML e converte *trecho* em destaque laranja.

    O texto vem de conteudo coletado na web e resumido por LLM: e dado, nunca
    marcacao. Escapar antes de qualquer coisa impede injecao de HTML no slide.
    """
    seguro = html.escape(str(texto), quote=False)
    return re.sub(r"\*(.+?)\*", r'<span class="hl">\1</span>', seguro)


CSS = """
@font-face{font-family:"Inter Tight";font-weight:600;src:url("../../fonts/inter-tight-latin-600-normal.woff2")}
@font-face{font-family:"Inter Tight";font-weight:700;src:url("../../fonts/inter-tight-latin-700-normal.woff2")}
@font-face{font-family:"Inter Tight";font-weight:800;src:url("../../fonts/inter-tight-latin-800-normal.woff2")}
@font-face{font-family:"Inter";font-weight:400;src:url("../../fonts/inter-latin-400-normal.woff2")}
@font-face{font-family:"Inter";font-weight:500;src:url("../../fonts/inter-latin-500-normal.woff2")}
@font-face{font-family:"Inter";font-weight:600;src:url("../../fonts/inter-latin-600-normal.woff2")}
@font-face{font-family:"JetBrains Mono";font-weight:500;src:url("../../fonts/jetbrains-mono-latin-500-normal.woff2")}
:root{--bg:#0A0A0B;--card:#131315;--linha:#26262A;--txt:#F4F4F2;--txt2:#B9B9B4;--txt3:#7C7C78;--lar:#FF6A1A}
*{box-sizing:border-box;margin:0;padding:0}
body{background:#000;font-family:"Inter",sans-serif;-webkit-font-smoothing:antialiased}
.slide{position:relative;width:1080px;height:1350px;background:var(--bg);color:var(--txt);
  padding:84px 88px 76px;display:flex;flex-direction:column;overflow:hidden}
/* textura de riscos diagonais no canto superior direito, herdada da identidade do perfil */
.slide::before{content:"";position:absolute;top:0;right:0;width:560px;height:560px;
  background:repeating-linear-gradient(135deg,transparent 0 26px,rgba(255,255,255,.055) 26px 28px);
  -webkit-mask-image:radial-gradient(circle at 100% 0,#000 0,transparent 72%);pointer-events:none}
.topo,.base{display:flex;justify-content:space-between;align-items:center;
  font-family:"JetBrains Mono",monospace;font-weight:500;font-size:22px;letter-spacing:.08em;text-transform:uppercase;position:relative}
.topo .marca{color:var(--lar)} .topo .num{color:var(--txt3)}
.base{color:var(--txt3);border-top:1px solid var(--linha);padding-top:28px;text-transform:none;letter-spacing:.02em}
.base .seta{color:var(--txt)}
.corpo{flex:1;min-height:0;display:flex;flex-direction:column;justify-content:center;padding:48px 0;position:relative}
.hl{color:var(--lar)}
.rotulo{font-family:"JetBrains Mono",monospace;font-weight:500;font-size:24px;letter-spacing:.1em;
  text-transform:uppercase;color:var(--lar);margin-bottom:28px;display:flex;align-items:center;gap:18px}
.rotulo::before{content:"";width:44px;height:3px;background:var(--lar)}
h1{font-family:"Inter Tight",sans-serif;font-weight:800;font-size:98px;line-height:1.0;letter-spacing:-.035em}
h2{font-family:"Inter Tight",sans-serif;font-weight:700;font-size:66px;line-height:1.06;letter-spacing:-.028em;margin-bottom:44px}
p{font-size:37px;line-height:1.42;color:var(--txt2)}
p+p{margin-top:30px}
/* capa */
.capa .corpo{justify-content:flex-end;padding-bottom:36px}
.selo{align-self:flex-start;font-family:"JetBrains Mono",monospace;font-weight:500;font-size:23px;letter-spacing:.08em;
  text-transform:uppercase;color:var(--txt);border:1.5px solid var(--linha);border-radius:999px;padding:14px 26px;margin-bottom:44px}
.capa h1 .hl{display:block}
.capa .sub{font-size:38px;line-height:1.36;color:var(--txt2);margin-top:40px;max-width:820px}
.capa .caso{font-family:"JetBrains Mono",monospace;font-size:23px;color:var(--txt3);margin-top:44px;letter-spacing:.02em}
/* cartoes */
.cartao{background:var(--card);border:1.5px solid var(--linha);border-radius:26px;padding:30px 36px}
.cartao+.cartao{margin-top:22px}
.cartao .t{font-family:"Inter Tight",sans-serif;font-weight:700;font-size:38px;letter-spacing:-.015em;color:var(--txt);margin-bottom:10px}
.cartao .d{font-size:31px;line-height:1.4;color:var(--txt2)}
.cartao.destaque{border-color:var(--lar)} .cartao.destaque .t{color:var(--lar)}
.pontos .cartao{display:flex;gap:28px;align-items:flex-start}
.pontos .n{font-family:"JetBrains Mono",monospace;font-size:26px;color:var(--lar);padding-top:8px}
.ressalva{margin-top:30px;display:flex;gap:22px;align-items:flex-start}
.ressalva .tag{flex:none;font-family:"JetBrains Mono",monospace;font-size:20px;letter-spacing:.1em;text-transform:uppercase;
  color:var(--bg);background:var(--lar);border-radius:8px;padding:8px 14px;margin-top:4px}
.ressalva .d{font-size:29px;line-height:1.4;color:var(--txt)}
.fonte{margin-top:26px;font-family:"JetBrains Mono",monospace;font-size:22px;line-height:1.5;color:var(--txt3)}
/* cta */
.cta h2{font-size:76px;margin-bottom:28px}
.cta .txt{font-size:38px;color:var(--txt2);margin-bottom:44px}
.passos{display:flex;flex-direction:column;gap:18px}
.passo{display:flex;align-items:center;gap:26px;background:var(--card);border:1.5px solid var(--linha);border-radius:22px;
  padding:24px 32px;font-family:"Inter Tight",sans-serif;font-weight:600;font-size:38px}
.passo .n{font-family:"JetBrains Mono",monospace;font-size:24px;color:var(--lar)}
.passo:first-child{border-color:var(--lar)}
.autor{display:flex;align-items:center;gap:28px;margin-top:48px}
.autor img{width:124px;height:124px;border-radius:50%;object-fit:cover;border:4px solid var(--txt)}
.autor .h{font-family:"Inter Tight",sans-serif;font-weight:700;font-size:36px;color:var(--lar)}
.autor .r{font-size:26px;color:var(--txt3);margin-top:6px}
"""


def corpo_slide(s: dict) -> str:
    tipo = s["tipo"]
    rot = f'<div class="rotulo">{fmt(s["rotulo"])}</div>' if s.get("rotulo") else ""
    if tipo == "capa":
        return (f'<div class="selo">{fmt(s["selo"])}</div><h1>{fmt(s["titulo"])}</h1>'
                f'<div class="sub">{fmt(s["subtitulo"])}</div><div class="caso">{fmt(s["rodape"])}</div>')
    if tipo == "texto":
        return rot + f'<h2>{fmt(s["titulo"])}</h2>' + "".join(f"<p>{fmt(b)}</p>" for b in s["blocos"])
    if tipo == "decisao":
        cartoes = "".join(
            f'<div class="cartao{" destaque" if c.get("destaque") else ""}">'
            f'<div class="t">{fmt(c["t"])}</div><div class="d">{fmt(c["d"])}</div></div>'
            for c in s["cartoes"])
        # a ressalva fica no mesmo slide da afirmacao que ela qualifica: quem
        # faz captura de tela do slide da decisao leva a ressalva junto
        return (rot + f'<h2>{fmt(s["titulo"])}</h2>' + cartoes +
                f'<div class="ressalva"><span class="tag">Ressalva</span><div class="d">{fmt(s["ressalva"])}</div></div>'
                f'<div class="fonte">Fonte: {fmt(s["fonte"])}</div>')
    if tipo == "pontos":
        itens = "".join(
            f'<div class="cartao"><div class="n">{i:02d}</div><div>'
            f'<div class="t">{fmt(p["t"])}</div><div class="d">{fmt(p["d"])}</div></div></div>'
            for i, p in enumerate(s["pontos"], 1))
        return rot + f'<h2>{fmt(s["titulo"])}</h2><div class="pontos">{itens}</div>'
    if tipo == "cta":
        passos = "".join(f'<div class="passo"><span class="n">{i:02d}</span><span>{fmt(p)}</span></div>'
                         for i, p in enumerate(s["passos"], 1))
        return (f'<h2>{fmt(s["titulo"])}</h2><div class="txt">{fmt(s["texto"])}</div>'
                f'<div class="passos">{passos}</div>'
                f'<div class="autor"><img src="../../assets/perfil.jpg"><div>'
                f'<div class="h">{HANDLE}</div><div class="r">{fmt(s["rodape"])}</div></div></div>')
    raise ValueError(f"tipo de slide desconhecido: {tipo}")


def montar_html(post: dict) -> str:
    slides = post["slides"]
    total = len(slides)
    partes = []
    for i, s in enumerate(slides, 1):
        ultimo = i == total
        base_dir = "" if ultimo else '<span class="seta">arraste →</span>'
        partes.append(
            f'<section class="slide {s["tipo"]}" id="s{i}">'
            f'<div class="topo"><span class="marca">{MARCA}</span><span class="num">{i:02d}/{total:02d}</span></div>'
            f'<div class="corpo">{corpo_slide(s)}</div>'
            f'<div class="base"><span>{HANDLE}</span>{base_dir}</div></section>')
    return f'<!doctype html><html lang="pt-BR"><meta charset="utf-8"><style>{CSS}</style><body>{"".join(partes)}</body></html>'


def main() -> int:
    pasta = Path(sys.argv[1]).resolve()
    post = json.loads((pasta / "post.json").read_text(encoding="utf-8"))
    total = len(post["slides"])
    if not 2 <= total <= 10:  # limites do carrossel na API do Instagram
        print(f"ERRO: carrossel precisa de 2 a 10 slides, veio {total}")
        return 2
    if len(post["legenda"]) > LIMITE_LEGENDA:
        print(f"ERRO: legenda com {len(post['legenda'])} caracteres, limite {LIMITE_LEGENDA}")
        return 2

    arq_html = pasta / "_carrossel.html"
    arq_html.write_text(montar_html(post), encoding="utf-8")

    # usa o Chrome do sistema quando existe, para nao depender do download de
    # navegador do Playwright (a rede da nuvem nem sempre libera esse host)
    chrome = shutil.which("google-chrome") or shutil.which("chromium")
    estouros = []
    with sync_playwright() as p:
        nav = p.chromium.launch(executable_path=chrome) if chrome else p.chromium.launch()
        pag = nav.new_page(viewport={"width": LARGURA, "height": ALTURA}, device_scale_factor=1)
        pag.goto(arq_html.as_uri())
        pag.evaluate("document.fonts.ready")
        for i in range(1, total + 1):
            # estouro = conteudo do corpo maior que a area util do slide
            sobra = pag.evaluate(
                "(id)=>{const c=document.querySelector('#'+id+' .corpo');return c.scrollHeight-c.clientHeight}", f"s{i}")
            if sobra > 0:
                estouros.append((i, sobra))
            pag.locator(f"#s{i}").screenshot(path=str(pasta / f"slide-{i:02d}.jpg"), type="jpeg", quality=92)
        nav.close()
    arq_html.unlink(missing_ok=True)

    (pasta / "legenda.txt").write_text(post["legenda"], encoding="utf-8")
    if estouros:
        for i, sobra in estouros:
            print(f"ERRO: slide {i} estourou a area util em {sobra}px; encurte o texto")
        return 2
    print(f"OK: {total} slides em {pasta}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
