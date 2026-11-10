import io, contextlib, pathlib
with contextlib.redirect_stdout(io.StringIO()):
    import build_proto2 as b
R = b.R; (R / "exemplos").mkdir(exist_ok=True)
css = '''
.micro{position:absolute;left:70px;right:70px;display:flex;justify-content:space-between;font-weight:800;font-size:22px;letter-spacing:.14em;text-transform:uppercase;color:rgba(255,255,255,.8)}
.lead{position:absolute;left:70px;right:70px;top:120px;margin:0;font-family:"Nunito",sans-serif;font-weight:800;font-size:50px;line-height:1.16;color:#fff;text-shadow:0 4px 18px rgba(0,0,0,.25)}
.badge{position:absolute;left:150px;top:340px;width:560px;background:#fff;color:#0f1e36;border-radius:34px;padding:26px 28px 30px;transform:rotate(-3deg);box-shadow:0 36px 60px rgba(0,0,0,.4)}
.badge .top{font-weight:900;font-size:19px;letter-spacing:.16em;color:#7a869d;margin-bottom:16px;display:flex;justify-content:space-between}
.photo{height:250px;border-radius:22px;background:linear-gradient(160deg,#FFD23F,#FF8A4D);position:relative;overflow:hidden}
.photo img{position:absolute;left:50%;top:10px;height:290px;transform:translateX(-50%);filter:drop-shadow(0 10px 14px rgba(0,0,0,.25))}
.fields{margin-top:20px;display:grid;grid-template-columns:120px 1fr;row-gap:8px;font-weight:800;font-size:23px;letter-spacing:.06em;text-transform:uppercase}
.fields span:nth-child(odd){color:#7a869d}.fields span:nth-child(even){color:#0f1e36}
.bars{margin-top:18px;height:46px;background:repeating-linear-gradient(90deg,#0f1e36 0 3px,transparent 3px 7px,#0f1e36 7px 8px,transparent 8px 14px)}
.stamp{position:absolute;left:400px;top:284px;transform:rotate(4deg);background:#FFC928;color:#10224a;font-weight:900;font-size:25px;letter-spacing:.06em;padding:10px 18px;border-radius:8px;box-shadow:0 10px 20px rgba(0,0,0,.3);text-transform:uppercase}
.gag{position:absolute;left:70px;right:70px;top:985px;font-family:"Baloo 2",sans-serif;font-weight:800;line-height:.95;text-transform:uppercase}
.gag .l1{font-size:120px;color:#fff}
.gag s{text-decoration:none;position:relative;color:rgba(255,255,255,.75)}
.gag s::after{content:"";position:absolute;left:-8px;right:-8px;top:52%;height:10px;border-radius:6px;background:#FF4F6D;transform:rotate(-2deg)}
.gag .l2{font-size:132px;color:#FFD43B;transform:rotate(-3deg);transform-origin:0 50%;margin-top:6px;text-shadow:0 8px 0 rgba(0,0,0,.18)}
'''
body = ('<div class="light"></div><div class="micro" style="top:46px"><span>03 / 06</span><span>Arara</span></div>'
        '<p class="lead">A Arara entrou na reunião em inglês e esqueceu de ligar o microfone.</p>'
        '<div class="badge"><div class="top"><span>CRACHÁ DA ARARA</span><span>N° 0001</span></div>'
        '<div class="photo"><img src="../cutouts/story_26.png"></div>'
        '<div class="fields"><span>Nome</span><span>Arara</span><span>Cargo</span><span>Mascote em treinamento</span><span>Humor</span><span>Nervosa, mas tentando</span><span>Desde</span><span>2026</span></div>'
        '<div class="bars"></div></div><div class="stamp">Modo reunião ligado</div>'
        '<div class="gag"><div class="l1">Ficou <s>fluente</s></div><div class="l2">no mudo.</div></div>'
        '<div class="micro" style="bottom:50px"><span>Arara</span><span>Arrasta →</span></div>')
html = f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>{b.FONTS}{b.CSS}{css}</style></head><body>
<div id="post" style="--c1:#8A5CF0;--c2:#2B1273;--hl:#FFD43B;--acc:#4B2FC0">{body}</div>
<script>document.fonts.ready.then(()=>{{window.__ready=true}});</script></body></html>'''
(R / "exemplos" / "cracha.html").write_text(html); print("ok")
