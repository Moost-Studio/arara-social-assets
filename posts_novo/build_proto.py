#!/usr/bin/env python3
"""Protótipos do post da conta (16/11) no visual novo: conceito 4 (Arara em cenário 3D) e conceito 3 (correção como protagonista).
Gera proto/c4_s1.html, c4_s2.html, c3_s1.html, c3_s2.html (1080x1350)."""
import pathlib, re
R = pathlib.Path(__file__).resolve().parent; RT = R.parent / "reel_teste"
v9 = (RT / "index_v9_aprovado.html").read_text()
css9 = v9[v9.index("<style>") + 7:v9.index("</style>")].replace("url(assets/", "url(../../reel_teste/assets/")
sym = v9[v9.index('<svg width="0" height="0"'):]; sym = sym[:sym.index("</svg>") + 6]
sbline = re.search(r"  const SB = .*", v9).group(0)
FL = re.search(r"  const FL = \{.*?\n  \};\n", v9, re.S).group(0)
helpers = re.search(r"  const star = .*?\n  const sv = .*?\n  const tri3 = .*?\n  const hor3 = .*?\n", v9, re.S).group(0)
MIC = '<svg viewBox="0 0 24 24" class="ic"><path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3Z"/><path d="M19 10v2a7 7 0 0 1-14 0v-2"/><path d="M12 19v3"/></svg>'
ARROW = '<svg viewBox="0 0 24 24" class="ic"><path d="M5 12h14M12 5l7 7-7 7"/></svg>'
SPK = '<svg viewBox="0 0 24 24" class="ic"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.5 8.5a5 5 0 0 1 0 7"/><path d="M19 5a10 10 0 0 1 0 14"/></svg>'

base_css = """
html, body { margin: 0; background: #07152F !important; }
* { box-sizing: border-box; }
#post { position: relative; width: 1080px; height: 1350px; overflow: hidden; font-family: "Nunito", sans-serif; background: radial-gradient(ellipse 90% 60% at 30% 8%, #17387a 0%, rgba(23,56,122,0) 70%), radial-gradient(ellipse 80% 50% at 85% 100%, rgba(54,201,245,.16) 0%, rgba(54,201,245,0) 70%), linear-gradient(180deg, #0b1d44 0%, #07152F 55%, #050f24 100%); }
.tag { position: absolute; left: 70px; top: 76px; display: inline-flex; align-items: center; gap: 12px; padding: 12px 24px 12px 18px; border-radius: 40px; background: rgba(255,255,255,.1); border: 2px solid rgba(255,255,255,.18); color: #cfe0ff; font-weight: 800; font-size: 28px; letter-spacing: .02em; }
.tag .ic { width: 30px; height: 30px; color: #FFC928; stroke-width: 2.4; }
h1 { position: absolute; left: 70px; right: 70px; margin: 0; font-family: "Baloo 2", sans-serif; font-weight: 800; color: #fff; letter-spacing: -.01em; line-height: 1.02; text-shadow: 0 6px 30px rgba(0,0,0,.35); }
h1 b { color: #FFC928; font-weight: 800; }
.hint { position: absolute; left: 70px; right: 70px; bottom: 56px; display: flex; align-items: center; justify-content: space-between; color: #cfe0ff; font-weight: 700; font-size: 30px; }
.hint .go { display: inline-flex; align-items: center; justify-content: center; width: 78px; height: 78px; border-radius: 50%; background: #FFC928; color: #07152F; }
.hint .go .ic { width: 38px; height: 38px; stroke-width: 3; }
.masc { position: absolute; filter: drop-shadow(-5px -4px 0 rgba(54,201,245,.55)) drop-shadow(0 14px 26px rgba(0,0,0,.45)); }
.shadow { position: absolute; border-radius: 50%; background: radial-gradient(closest-side, rgba(0,0,0,.55), rgba(0,0,0,0)); }
"""

def page(name, body, extra_css="", js=""):
    html = f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>{css9}{base_css}{extra_css}</style></head><body>{sym}
<div id="post">{body}</div>
<script>
(function(){{
{sbline}
{helpers}{FL}
document.querySelectorAll(".win").forEach(w => w.insertAdjacentHTML("afterbegin", SB));
document.querySelectorAll("[data-flag]").forEach(e => e.innerHTML = FL[e.dataset.flag]);
{js}
document.fonts.ready.then(() => {{ window.__ready = true; }});
}})();
</script></body></html>'''
    (R / "proto" / f"{name}.html").write_text(html)

# ---------- conceito 4: Arara em cenário 3D (restaurante) ----------
scene_css = """
.bokeh { position: absolute; border-radius: 50%; filter: blur(8px); }
.stage3d { position: absolute; left: 0; right: 0; bottom: 0; height: 760px; perspective: 1300px; overflow: hidden; }
.floor { position: absolute; left: -500px; right: -500px; bottom: -380px; height: 1100px; transform-origin: 50% 100%; transform: rotateX(66deg);
  background: repeating-linear-gradient(90deg, rgba(120,170,255,.24) 0 2px, transparent 2px 140px), repeating-linear-gradient(0deg, rgba(120,170,255,.24) 0 2px, transparent 2px 140px), linear-gradient(0deg, #0f2a5e, #07152F);
  -webkit-mask-image: linear-gradient(0deg, #000 35%, transparent 100%); mask-image: linear-gradient(0deg, #000 35%, transparent 100%); }
.tside { position: absolute; left: 150px; width: 780px; top: 980px; height: 130px; border-radius: 0 0 390px 390px / 0 0 110px 110px; background: linear-gradient(180deg, #0c214c, #07152F); box-shadow: 0 40px 60px rgba(0,0,0,.5); }
.ttop { position: absolute; left: 150px; width: 780px; top: 880px; height: 210px; border-radius: 50%; background: radial-gradient(ellipse at 50% 35%, #29529f 0%, #163670 60%, #10285a 100%); border: 3px solid rgba(160,205,255,.35); box-shadow: inset 0 -14px 30px rgba(0,0,0,.25), 0 0 80px rgba(54,201,245,.12); }
.plate { position: absolute; border-radius: 50%; background: radial-gradient(ellipse at 50% 40%, #fff 0%, #dce8ff 70%, #b6c9ec 100%); box-shadow: 0 10px 14px rgba(0,0,0,.35); }
.plate::after { content: ""; position: absolute; inset: 14% 16%; border-radius: 50%; border: 3px solid rgba(37,99,235,.18); }
.bill { position: absolute; width: 150px; height: 190px; border-radius: 12px; background: #fff; box-shadow: 0 12px 20px rgba(0,0,0,.4); transform: rotate(8deg); padding: 18px 16px; }
.bill i { display: block; height: 9px; border-radius: 5px; background: #cfdaf0; margin-bottom: 12px; }
.bill i.k { width: 55%; background: #245BFA; }
.bill i.t { margin-top: 18px; height: 16px; width: 70%; background: #FFC928; }
.card { position: absolute; left: 70px; right: 70px; background: #fff; border-radius: 44px; padding: 38px 44px 40px; box-shadow: 0 30px 60px rgba(0,0,0,.45), 0 0 0 2px rgba(255,255,255,.4); }
.card .row { display: flex; align-items: center; gap: 22px; margin-bottom: 20px; }
.card .fl { width: 118px; height: 79px; border-radius: 14px; overflow: hidden; box-shadow: 0 0 0 4px rgba(15,30,54,.1); flex: none; }
.card .fl svg { display: block; width: 100%; height: 100%; }
.card .lang { font-weight: 900; font-size: 30px; letter-spacing: .04em; text-transform: uppercase; color: #1E4FB8; }
.card .sp { margin-left: auto; width: 70px; height: 70px; border-radius: 50%; background: #1E4FB8; color: #fff; display: grid; place-items: center; }
.card .sp .ic { width: 34px; height: 34px; }
.card .ph { font-family: "Baloo 2", sans-serif; font-weight: 800; font-size: 74px; line-height: 1.03; color: #0f1e36; letter-spacing: -.01em; }
.card .tr { margin-top: 16px; font-weight: 700; font-size: 38px; color: #55657d; }
.card::after { content: ""; position: absolute; left: 190px; bottom: -34px; width: 64px; height: 64px; background: #fff; transform: rotate(45deg); border-radius: 0 0 16px 0; }
"""
def scene(body_top, masc_html):
    return f"""
<div class="bokeh" style="left:80px;top:430px;width:150px;height:150px;background:rgba(255,201,40,.22)"></div>
<div class="bokeh" style="left:880px;top:560px;width:130px;height:130px;background:rgba(255,201,40,.14)"></div>
<div class="bokeh" style="left:620px;top:520px;width:110px;height:110px;background:rgba(54,201,245,.20)"></div>
<div class="stage3d"><div class="floor"></div></div>
<div class="tside"></div><div class="ttop"></div>
<div class="plate" style="left:200px;top:955px;width:190px;height:60px"></div>
<div class="plate" style="left:730px;top:945px;width:150px;height:48px"></div>
<div class="bill" style="left:760px;top:830px"><i class="k"></i><i></i><i></i><i></i><i class="t"></i></div>
<div class="shadow" style="left:300px;top:955px;width:420px;height:70px"></div>
{masc_html}{body_top}"""
c4s1 = scene(f'<div class="tag">{MIC}O PIO DA SEMANA</div><h1 style="top:150px;font-size:98px">A <b>conta</b>, por favor,<br>em 4 idiomas</h1><div class="hint"><span>Arrasta para o lado e salva<br>para o próximo restaurante.</span><span class="go">{ARROW}</span></div>',
             '<img class="masc" src="m2_limpo.png" style="left:290px;top:480px;height:520px">')
c4s2 = scene(f'<div class="tag">{MIC}FRASE ÚTIL · INGLÊS</div><h1 style="top:150px;font-size:98px">Pedir a <b>conta</b></h1>'
             f'<div class="card" style="top:350px"><div class="row"><div class="fl" data-flag="en"></div><span class="lang">Inglês</span><span class="sp">{SPK}</span></div><div class="ph">Can I have the check, please?</div><div class="tr">Posso pedir a conta, por favor?</div></div>'
             f'<div class="hint"><span>Arrasta para o espanhol</span><span class="go">{ARROW}</span></div>',
             '<img class="masc" src="m2_limpo.png" style="left:330px;top:728px;height:290px">')
page("c4_s1", c4s1, scene_css); page("c4_s2", c4s2, scene_css)

# ---------- conceito 3: a correção como protagonista (tela do app) ----------
c3_css = """
.phone { position: absolute; left: 400px; top: 420px; transform: perspective(1800px) rotateY(-9deg) rotateX(3deg) scale(.92); transform-origin: 50% 0; box-shadow: none; }
.dev { top: 54px; }
.bub, .fbchip, .why { opacity: 1 !important; }
.fbcard { height: auto !important; }
.fbcard .fbin { padding: 14px 0; }
.glow { position: absolute; left: 220px; top: 520px; width: 840px; height: 840px; border-radius: 50%; background: radial-gradient(closest-side, rgba(54,201,245,.28), rgba(54,201,245,0)); }
"""
def phone(inner):
    return f'<div class="glow"></div><div class="phone"><div class="win"><div class="dev"><div class="scr" style="transform:none">{inner}</div></div></div></div>'
hdr = '<div class="hdr2"><span class="back"><svg class="ic"><use href="#i-cl"/></svg>Voltar</span><span class="hdr-t" style="margin-left:6px">Conversa e correções</span></div>'
conv = '<div class="bub t">Good evening! Are you ready to pay?</div><div class="bub u">Yes. Give me the account, please.</div>'
chip = '<span class="fbchip"><svg class="ic"><use href="#i-spark"/></svg>1 correção<svg class="ic"><use href="#i-cd"/></svg></span>'
card = ('<div class="fbcard"><div class="fbin">'
        '<div class="line bad"><svg class="ic"><use href="#i-xc"/></svg><div><small>Você disse</small><p>Give me the account</p></div></div>'
        '<div class="line good"><svg class="ic"><use href="#i-cc"/></svg><div><small>Melhor assim</small><p>Can I have the check, please?</p></div></div>'
        '<p class="why">Em inglês, account é conta de banco. Para a conta do restaurante, use check nos EUA ou bill no Reino Unido.</p></div></div>')
s1 = phone(hdr + '<div class="msgs" style="margin-top:18px">' + conv + chip + '</div>')
s2 = phone(hdr + '<div class="msgs" style="margin-top:18px">' + conv + chip + card + '</div>')
c3s1 = (f'<div class="tag">{MIC}O PIO DA SEMANA</div><h1 style="top:150px;font-size:94px">Pedir a <b>conta</b><br>sem errar</h1>' + s1 +
        '<img class="masc" src="m2_limpo.png" style="left:20px;top:900px;height:400px">')
c3s2 = (f'<div class="tag">{MIC}A CORREÇÃO, EM PORTUGUÊS</div><h1 style="top:150px;font-size:94px">Errou? O app <b>explica</b></h1>' + s2 +
        '<img class="masc" src="m6_limpo.png" style="left:20px;top:900px;height:400px">')
page("c3_s1", c3s1, c3_css); page("c3_s2", c3s2, c3_css)
print("ok")
