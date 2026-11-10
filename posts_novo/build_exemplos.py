import pathlib, sys, io, contextlib
with contextlib.redirect_stdout(io.StringIO()):
    import build_proto2 as b
R = b.R; (R / "exemplos").mkdir(exist_ok=True)
covers = [
 dict(n="e1", c1="#FF8A4D", c2="#B9301F", hl="#FFE08A", ink="#fff", acc="#D6452A", tag="PIO DA SEMANA", title='A <b>conta</b>, por favor,<br>em 4 idiomas', mascot="story_08"),
 dict(n="e2", c1="#FFD23F", c2="#F2A100", hl="#C2185B", ink="#10224a", acc="#C98700", tag="HUMOR", title='Rindo da piada<br><b>3 segundos</b> atrasado', mascot="v2_enem_torcida"),
 dict(n="e3", c1="#2F63EA", c2="#102A72", hl="#FFC928", ink="#fff", acc="#1E4FB8", tag="NO APP", title='Receba <b>correções</b><br>em português', mascot="s3_tutor"),
 dict(n="e4", c1="#8A5CF0", c2="#38198F", hl="#FFD43B", ink="#fff", acc="#4B2FC0", tag="FALSO AMIGO", title='<b>Exquisita</b> não é o<br>que você pensa', mascot="v2_falsos_pretend"),
 dict(n="e5", c1="#17C08E", c2="#08674A", hl="#FFE066", ink="#fff", acc="#0A8F4B", tag="VIAGEM", title='Onde fica<br>o <b>banheiro</b>?', mascot="story_17"),
 dict(n="e6", c1="#FF4F8B", c2="#A3124B", hl="#FFE08A", ink="#fff", acc="#D6286B", tag="DATA", title='Dia da <b>Saudação</b><br>Oi, e agora?', mascot="perfil_aventureira"),
]
css_extra = '#post{color:var(--ink)}h1{color:var(--ink)}.tag{background:rgba(0,0,0,.18);color:var(--ink);border-color:rgba(255,255,255,.3)}.hint .go{color:#10224a}'
for s in covers:
    body = '<div class="light"></div><div class="orb" style="left:-160px;top:620px;width:520px;height:520px"></div><div class="orb" style="left:700px;top:240px;width:420px;height:420px"></div>'
    body += f'<div class="tag">{b.MIC}{s["tag"]}</div><h1 style="top:150px;font-size:100px">{s["title"]}</h1>'
    body += '<div class="stage" style="left:170px;top:1190px;width:560px;height:110px"></div>'
    body += f'<img class="masc" src="../cutouts/{s["mascot"]}.png" style="left:230px;top:470px;height:720px">'
    body += f'<div class="hint"><span>Arrasta para o lado</span><span class="go">{b.ARROW}</span></div>'
    html = f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>{b.FONTS}{b.CSS}{css_extra}</style></head><body>
<div id="post" style="--c1:{s["c1"]};--c2:{s["c2"]};--hl:{s["hl"]};--acc:{s["acc"]};--ink:{s["ink"]}">{body}</div>
<script>document.fonts.ready.then(()=>{{window.__ready=true}});</script></body></html>'''
    (R / "exemplos" / f'{s["n"]}.html').write_text(html)
# panorâmico: cena larga de 2160x1350, cortada em dois slides
pano = f'''<!doctype html><html><head><meta charset="utf-8"><style>{b.FONTS}{b.CSS}
#post{{width:2160px}}h1{{left:70px}}.card{{left:1430px;right:auto;width:640px}}.card::after{{left:-26px;top:120px;bottom:auto;transform:rotate(45deg)}}
.table{{position:absolute;left:380px;width:1400px;top:1080px;height:300px;border-radius:50%;background:radial-gradient(ellipse at 50% 30%,rgba(255,255,255,.28),rgba(255,255,255,.06));}}
</style></head><body>
<div id="post" style="--c1:#FF8A4D;--c2:#B9301F;--hl:#FFE08A;--acc:#D6452A">
<div class="light"></div><div class="orb" style="left:300px;top:500px;width:700px;height:700px"></div><div class="orb" style="left:1500px;top:200px;width:560px;height:560px"></div>
<div class="table"></div>
<div class="tag">{b.MIC}O PIO DA SEMANA</div>
<h1 style="top:150px;font-size:100px">A <b>conta</b>, por favor,<br>em 4 idiomas</h1>
<div class="stage" style="left:610px;top:1170px;width:560px;height:110px"></div>
<img class="masc" src="../cutouts/story_08.png" style="left:640px;top:470px;height:720px">
<div class="card" style="top:300px"><div class="row"><div class="fl" data-flag="en"></div><span class="lang">Inglês</span><span class="sp">{b.SPK}</span></div><div class="ph">Can I have the check, please?</div><div class="tr">Posso pedir a conta, por favor?</div></div>
<div class="hint"><span>Arrasta para o lado e salva<br>para o próximo restaurante.</span><span class="go">{b.ARROW}</span></div>
</div>
<script>(function(){{{b.helpers}{b.FL}document.querySelectorAll("[data-flag]").forEach(e=>e.innerHTML=FL[e.dataset.flag]);document.fonts.ready.then(()=>{{window.__ready=true}});}})();</script></body></html>'''
(R / "exemplos" / "pano.html").write_text(pano)
print("ok")
