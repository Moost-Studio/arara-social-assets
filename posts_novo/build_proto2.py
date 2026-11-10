#!/usr/bin/env python3
"""Protótipo v2 do post da conta (16/11): cores por tema/idioma e mais expressões da mascote. Gera proto2/*.html e .png (1080x1350)."""
import pathlib, re, subprocess, json
R = pathlib.Path(__file__).resolve().parent; RT = R.parent / "reel_teste"
(R / "proto2").mkdir(exist_ok=True)
v9 = (RT / "index_v9_aprovado.html").read_text()
FL = re.search(r"  const FL = \{.*?\n  \};\n", v9, re.S).group(0)
helpers = re.search(r"  const star = .*?\n  const sv = .*?\n  const tri3 = .*?\n  const hor3 = .*?\n", v9, re.S).group(0)
FONTS = """@font-face { font-family: "Baloo 2"; src: url(../../reel_teste/assets/fonts/Baloo2.ttf); font-weight: 400 800; }
@font-face { font-family: "Nunito"; src: url(../../reel_teste/assets/fonts/Nunito.ttf); font-weight: 200 1000; }"""
MIC = '<svg viewBox="0 0 24 24"><path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3Z"/><path d="M19 10v2a7 7 0 0 1-14 0v-2"/><path d="M12 19v3"/></svg>'
ARROW = '<svg viewBox="0 0 24 24"><path d="M5 12h14M12 5l7 7-7 7"/></svg>'
SPK = '<svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.5 8.5a5 5 0 0 1 0 7"/><path d="M19 5a10 10 0 0 1 0 14"/></svg>'
CSS = """
html,body{margin:0;background:#111}*{box-sizing:border-box}
svg{fill:none;stroke:currentColor;stroke-width:2.4;stroke-linecap:round;stroke-linejoin:round}
#post{position:relative;width:1080px;height:1350px;overflow:hidden;font-family:"Nunito",sans-serif;color:#fff;background:linear-gradient(160deg,var(--c1) 0%,var(--c2) 100%)}
.light{position:absolute;inset:0;background:radial-gradient(ellipse 80% 55% at 25% 6%,rgba(255,255,255,.28) 0%,rgba(255,255,255,0) 65%),radial-gradient(ellipse 70% 40% at 90% 100%,rgba(0,0,0,.30) 0%,rgba(0,0,0,0) 70%)}
.orb{position:absolute;border-radius:50%;background:rgba(255,255,255,.07)}
.tag{position:absolute;left:70px;top:76px;display:inline-flex;align-items:center;gap:12px;padding:12px 26px 12px 18px;border-radius:40px;background:rgba(0,0,0,.22);border:2px solid rgba(255,255,255,.28);font-weight:800;font-size:28px;letter-spacing:.03em;text-transform:uppercase}
.tag svg{width:30px;height:30px;color:var(--hl)}
h1{position:absolute;left:70px;right:70px;margin:0;font-family:"Baloo 2",sans-serif;font-weight:800;letter-spacing:-.01em;line-height:1.02;text-shadow:0 6px 24px rgba(0,0,0,.28)}
h1 b{color:var(--hl);font-weight:800}
.hint{position:absolute;left:70px;right:70px;bottom:56px;display:flex;align-items:center;justify-content:space-between;font-weight:800;font-size:30px;line-height:1.25}
.hint .go{display:inline-flex;align-items:center;justify-content:center;width:80px;height:80px;border-radius:50%;background:var(--hl);color:#10224a;flex:none}
.hint .go svg{width:38px;height:38px;stroke-width:3}
.stage{position:absolute;border-radius:50%;background:radial-gradient(closest-side,rgba(0,0,0,.42),rgba(0,0,0,0))}
.masc{position:absolute;filter:drop-shadow(0 0 3px rgba(255,255,255,.55)) drop-shadow(0 18px 24px rgba(0,0,0,.35))}
.card{position:absolute;left:70px;right:70px;background:#fff;color:#0f1e36;border-radius:44px;padding:36px 44px 40px;box-shadow:0 34px 60px rgba(0,0,0,.35),0 0 0 6px var(--acc)}
.card::after{content:"";position:absolute;left:210px;bottom:-30px;width:60px;height:60px;background:#fff;transform:rotate(45deg);border-radius:0 0 14px 0}
.row{display:flex;align-items:center;gap:22px;margin-bottom:18px}
.fl{width:118px;height:79px;border-radius:14px;overflow:hidden;box-shadow:0 0 0 4px rgba(15,30,54,.1);flex:none}
.fl svg{display:block;width:100%;height:100%;stroke:none}
.lang{font-weight:900;font-size:30px;letter-spacing:.05em;text-transform:uppercase;color:var(--acc)}
.sp{margin-left:auto;width:70px;height:70px;border-radius:50%;background:var(--acc);color:#fff;display:grid;place-items:center}
.sp svg{width:34px;height:34px}
.ph{font-family:"Baloo 2",sans-serif;font-weight:800;font-size:74px;line-height:1.03;letter-spacing:-.01em}
.tr{margin-top:14px;font-weight:700;font-size:38px;color:#55657d}
"""
SLIDES = [
 dict(n="s1", c1="#FF8A4D", c2="#B9301F", hl="#FFE08A", acc="#D6452A", tag="O PIO DA SEMANA", flag=None,
      title='A <b>conta</b>, por favor,<br>em 4 idiomas', hint="Arrasta para o lado e salva<br>para o próximo restaurante.", mascot="story_08", mh=720, mx=230, my=470),
 dict(n="s2", c1="#2F63EA", c2="#102A72", hl="#FFC928", acc="#1E4FB8", tag="FRASE ÚTIL · INGLÊS", flag="en", lang="Inglês",
      title='Pedir a <b>conta</b>', ph="Can I have the check, please?", tr="Posso pedir a conta, por favor?", hint="Arrasta para o espanhol", mascot="perfil_ouvido", mh=430, mx=300, my=800),
 dict(n="s3", c1="#E8384F", c2="#8A0B22", hl="#FFD43B", acc="#C8102E", tag="FRASE ÚTIL · ESPANHOL", flag="es", lang="Espanhol",
      title='Pedir a <b>conta</b>', ph="La cuenta, por favor.", tr="A conta, por favor.", hint="Arrasta para o francês", mascot="v2_reel_acolhe", mh=430, mx=300, my=800),
 dict(n="s4", c1="#8A5CF0", c2="#38198F", hl="#FFD43B", acc="#4B2FC0", tag="FRASE ÚTIL · FRANCÊS", flag="fr", lang="Francês",
      title='Pedir a <b>conta</b>', ph="L'addition, s'il vous plaît.", tr="A conta, por favor.", hint="Arrasta para o italiano", mascot="story_27_clean", mh=430, mx=300, my=800),
 dict(n="s5", c1="#17C08E", c2="#08674A", hl="#FFE066", acc="#0A8F4B", tag="FRASE ÚTIL · ITALIANO", flag="it", lang="Italiano",
      title='Pedir a <b>conta</b>', ph="Il conto, per favore.", tr="A conta, por favor.", hint="Salva para a próxima viagem", mascot="v2_reel_festa", mh=430, mx=300, my=800),
]
def html(s):
    cover = s["flag"] is None
    body = '<div class="light"></div><div class="orb" style="left:-160px;top:620px;width:520px;height:520px"></div><div class="orb" style="left:700px;top:240px;width:420px;height:420px"></div>'
    body += f'<div class="tag">{MIC}{s["tag"]}</div>'
    body += f'<h1 style="top:150px;font-size:{98 if cover else 100}px">{s["title"]}</h1>'
    if not cover:
        body += (f'<div class="card" style="top:350px"><div class="row"><div class="fl" data-flag="{s["flag"]}"></div><span class="lang">{s["lang"]}</span><span class="sp">{SPK}</span></div>'
                 f'<div class="ph">{s["ph"]}</div><div class="tr">{s["tr"]}</div></div>')
    mw = s["mh"]
    body += f'<div class="stage" style="left:{s["mx"]-60}px;top:{s["my"]+s["mh"]-60}px;width:560px;height:110px"></div>'
    body += f'<img class="masc" src="../cutouts/{s["mascot"]}.png" style="left:{s["mx"]}px;top:{s["my"]}px;height:{s["mh"]}px">'
    body += f'<div class="hint"><span>{s["hint"]}</span><span class="go">{ARROW}</span></div>'
    return f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>{FONTS}{CSS}</style></head><body>
<div id="post" style="--c1:{s["c1"]};--c2:{s["c2"]};--hl:{s["hl"]};--acc:{s["acc"]}">{body}</div>
<script>(function(){{{helpers}{FL}
document.querySelectorAll("[data-flag]").forEach(e=>e.innerHTML=FL[e.dataset.flag]);
document.fonts.ready.then(()=>{{window.__ready=true}});}})();</script></body></html>'''
for s in SLIDES: (R / "proto2" / f'{s["n"]}.html').write_text(html(s))
print("ok", len(SLIDES))
