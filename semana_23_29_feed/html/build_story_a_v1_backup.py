import subprocess, json, re
from PIL import Image
F='/home/rodrigo/.openclaw/workspace/arara_social/semana1/_fontes/'
G='/home/rodrigo/.openclaw/workspace/arara_social/semana_23_29_feed/gen/'
R='/home/rodrigo/.openclaw/workspace/arara_social/semana1/recortes/'
H='/home/rodrigo/.openclaw/workspace/arara_social/semana_23_29_feed/html/'
O='/home/rodrigo/.openclaw/workspace/arara_social/semana_23_29_feed/final/'
CSS=f"""
@font-face{{font-family:'Nunito';src:url('file://{F}Nunito.ttf');font-weight:200 1000}}
@font-face{{font-family:'Mochiy';src:url('file://{F}MochiyPopOne-Regular.ttf')}}
*{{box-sizing:border-box;margin:0;padding:0}} body{{background:#000}}
#post{{position:relative;width:1080px;height:1920px;overflow:hidden;font-family:'Nunito'}}
.bg{{position:absolute;inset:0;width:1080px;height:1920px}}
.lbl{{position:absolute;left:64px;top:232px;display:flex;align-items:center;gap:16px;font-weight:900;font-size:40px;letter-spacing:.18em;text-transform:uppercase;z-index:6}}
.lbl::after{{content:'';width:60px;height:6px;border-radius:3px;background:#FFC83D}}
h1{{position:absolute;left:64px;width:950px;font-weight:900;line-height:1.04;letter-spacing:-.01em;z-index:6}}
.hl{{background:linear-gradient(transparent 55%,#FFC83D 55%,#FFC83D 92%,transparent 92%);padding:0 6px}}
.sub{{position:absolute;left:64px;width:950px;font-weight:800;line-height:1.2;z-index:6}}
.bal{{position:absolute;left:64px;width:700px;z-index:6;background:#fff;border-radius:48px;border-bottom:16px solid #CFE0FF;padding:20px 44px 22px;box-shadow:0 16px 34px rgba(30,40,90,.22)}}
.tag{{font-weight:900;font-size:40px;letter-spacing:.16em;text-transform:uppercase;color:#FF6B57;line-height:1.1}}
.big{{font-weight:900;font-size:104px;line-height:1.05;letter-spacing:-.01em;color:#081226}}
.tr{{font-weight:800;font-size:50px;line-height:1.15;color:#2b3a5c}}
.floor{{position:absolute;left:0;top:1500px;width:1080px;height:420px;background:linear-gradient(180deg,#1B43B8,#17399B);border-top:6px solid rgba(255,255,255,.22)}}
.card{{position:absolute;left:64px;width:952px;z-index:6;background:#FFF5E1;border-radius:40px;border-bottom:14px solid #E6D3AA;padding:24px 34px;box-shadow:0 14px 30px rgba(5,20,80,.28)}}
.row{{display:flex;align-items:center;gap:22px}}
.ib{{width:76px;height:76px;border-radius:50%;background:#2457E6;display:flex;align-items:center;justify-content:center;flex:none}}
.num{{width:50px;height:50px;border-radius:50%;background:#FFC83D;font-weight:900;font-size:30px;display:flex;align-items:center;justify-content:center;flex:none}}
"""
TAIL='<svg style="position:absolute;left:0;top:0;z-index:7" width="1080" height="1920"><polygon id="pg" fill="#fff" stroke="#CFE0FF" stroke-width="5" stroke-linejoin="round" style="filter:drop-shadow(0 5px 6px rgba(30,40,90,.25))"/></svg><script>addEventListener("load",()=>document.fonts.ready.then(()=>{{const r=document.querySelector(".bal").getBoundingClientRect();const [tx,ty]=[%d,%d];const y=r.bottom-8;document.getElementById("pg").setAttribute("points",(tx-50)+","+y+" "+(tx+50)+","+y+" "+tx+","+ty)}}))</script>'
def doc(inner,bg): return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body><div id="post">{bg}{inner}</div></body></html>'
P=[]
# 216
P.append(('story-216',doc('<div class="lbl" style="color:#081226">Bom dia da Rara</div><h1 data-box="h1" style="top:292px;font-size:86px;color:#081226">Bom dia, <span class="hl">presidente</span></h1><div class="sub" data-box="sub" style="top:392px;font-size:44px;color:#081226">minha frase favorita pra quando alguém erra</div>'
 '<div class="bal" data-box="bal" style="top:470px;left:150px"><div class="tag">em sueco</div><div class="big">Ingen fara!</div><div class="tr">sem problema, relaxa</div></div>'+TAIL%(531,770),f'<img class="bg" src="file://{G}st216_base.jpg">')))
# 218
P.append(('story-218',doc('<div class="lbl" style="color:#fff">Modo carente</div><h1 data-box="h1" style="top:292px;font-size:84px;color:#fff;text-shadow:0 4px 18px rgba(60,20,80,.45)">Presidente, <span style="color:#FFC83D;white-space:nowrap">3 minutinhos</span></h1><div class="sub" data-box="sub" style="top:466px;font-size:54px;color:#fff;text-shadow:0 3px 14px rgba(60,20,80,.5)">eu conto como abdominal</div>',f'<img class="bg" src="file://{G}st218_base.jpg">')))
# 217
SC=0.8
im=Image.open(R+'G07_cx.png'); bb=im.getbbox(); w,h=im.size
x=int(540-(bb[0]*SC+(bb[2]-bb[0])*SC/2)); y=int(1700-bb[3]*SC)
ic_t='<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/>'
card=('<div class="card" data-box="card" style="top:586px"><div class="row" style="margin-bottom:14px"><div class="ib"><svg width="44" height="44" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round">'+ic_t+'</svg></div><div><div style="font-weight:900;font-size:46px;line-height:1">Sua missão</div><div style="font-weight:800;font-size:40px;color:#46557a">3 expressões para tentar usar</div></div></div>'
 '<div class="row" style="margin-top:6px;gap:22px">'+''.join(f'<div class="row" style="gap:12px"><div class="num">{i}</div><div style="font-weight:800;font-size:40px;color:#46557a">expressão</div></div>' for i in (1,2,3))+'</div></div>')
bg217='<div style="position:absolute;inset:0;background:linear-gradient(180deg,#3F73F2 0%,#2457E6 55%,#1F4FD6 100%)"></div><div style="position:absolute;left:-200px;top:900px;width:700px;height:700px;border-radius:50%;background:radial-gradient(circle,rgba(255,255,255,.2),rgba(255,255,255,0) 70%)"></div><div class="floor"></div>'
P.append(('story-217',doc('<div class="lbl" style="color:#fff">Bastidores</div><h1 data-box="h1" style="top:300px;font-size:70px;color:#fff">já tá no feed como funciona a <span style="color:#FFC83D">missão</span> de cada conversa</h1>'+card+
 '<div class="sub" data-box="sub" style="top:910px;font-size:46px;color:#EAF1FF">vai lá no post e me conta se ficou claro</div>'
 f'<img src="file://{R}G07_cx.png" style="position:absolute;z-index:3;left:{x}px;top:{y}px;width:{int(w*SC)}px;height:{int(h*SC)}px">',bg217)))
for k,html,*bgx in [(p[0],p[1]) for p in P]:
    open(H+k+'.html','w').write(html)
    r=subprocess.run(['node',H+'render_a.mjs',H+k+'.html',O+k+'.jpg','1080','1920'],capture_output=True,text=True)
    print(k,r.stdout.strip()[-200:],r.stderr[:200])
