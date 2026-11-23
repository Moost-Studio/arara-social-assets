import subprocess, json
F='/home/rodrigo/.openclaw/workspace/arara_social/semana1/_fontes/'
G='/home/rodrigo/.openclaw/workspace/arara_social/semana_23_29_feed/gen/'
H='/home/rodrigo/.openclaw/workspace/arara_social/semana_23_29_feed/html/'
O='/home/rodrigo/.openclaw/workspace/arara_social/semana_23_29_feed/final/'
CSS=f"""
@font-face{{font-family:'Nunito';src:url('file://{F}Nunito.ttf');font-weight:200 1000}}
@font-face{{font-family:'Mochiy';src:url('file://{F}MochiyPopOne-Regular.ttf')}}
@font-face{{font-family:'JP';src:url('file://{F}NotoSansJP.ttf');font-weight:100 900}}
*{{box-sizing:border-box;margin:0;padding:0}} body{{background:#000}}
#post{{position:relative;width:1080px;height:1350px;overflow:hidden;font-family:'Nunito';color:#3A1620}}
.bg{{position:absolute;inset:0;width:1080px;height:1350px}}
.wash{{position:absolute;left:0;top:0;width:1080px;height:640px;background:linear-gradient(180deg,rgba(242,201,210,.78),rgba(242,201,210,.35) 62%,rgba(242,201,210,0))}}
.lbl{{position:absolute;left:64px;top:58px;display:flex;align-items:center;gap:16px;font-weight:900;font-size:34px;letter-spacing:.22em;text-transform:uppercase;color:#9C1630;z-index:5}}
.lbl::after{{content:'';width:56px;height:5px;border-radius:3px;background:#D6203F}}
h1{{position:absolute;left:64px;top:118px;width:940px;font-weight:900;font-size:72px;line-height:1.04;letter-spacing:-.01em;z-index:5}}
.hl{{color:#D6203F}}
.sub{{position:absolute;left:64px;font-weight:800;font-size:42px;line-height:1.22;z-index:5;color:#3A1620}}
.pill{{position:absolute;left:44px;bottom:36px;z-index:6;display:flex;gap:22px;align-items:center;font-weight:800;font-size:36px;background:rgba(255,255,255,.92);padding:10px 14px 10px 30px;border-radius:999px;color:#3A1620}}
.btn{{width:76px;height:76px;border-radius:50%;background:#D6203F;display:flex;align-items:center;justify-content:center;box-shadow:0 6px 0 #9C1630}}
.btn svg{{width:42px;height:42px;stroke:#fff;fill:none;stroke-width:2.8;stroke-linecap:round;stroke-linejoin:round}}
.bal{{position:absolute;left:64px;top:108px;width:900px;z-index:6;background:#fff;border-radius:44px;border-bottom:14px solid #F2C9D2;padding:18px 40px 20px;box-shadow:0 14px 30px rgba(120,40,60,.18)}}
.row{{display:block}}
.jp{{font-family:'JP','Nunito';font-weight:900;font-size:70px;line-height:1.12;white-space:nowrap}}
.ro{{font-weight:900;font-size:40px;line-height:1.1;color:#D6203F;white-space:nowrap}}
.tr{{font-weight:900;font-size:44px;line-height:1.15;margin-top:2px}}
.ap{{font-weight:700;font-size:40px;line-height:1.2;margin-top:6px;color:#6B3A48}}
.punch{{position:absolute;left:64px;top:122px;width:940px;font-family:'Mochiy';font-size:64px;line-height:1.16;color:#9C1630;z-index:5;text-transform:uppercase}}
"""
ARR='<svg viewBox="0 0 24 24"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg>'
def page(body, bg, tail=None):
    t=''
    if tail: t='<svg id="tl" style="position:absolute;left:0;top:0;z-index:7" width="1080" height="1350"><polygon id="pg" fill="#fff"/></svg><script>addEventListener("load",()=>document.fonts.ready.then(()=>{const b=document.querySelector(".bal");const r=b.getBoundingClientRect();const [tx,ty]=%s;const y=r.bottom-6;document.getElementById("pg").setAttribute("points",(tx-48)+","+y+" "+(tx+48)+","+y+" "+tx+","+ty)}))</script>' % tail
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body><div id="post"><img class="bg" src="file://{G}{bg}"><div class="wash"></div>{t}{body}</div></body></html>'
slides=[]
slides.append(('pio-japones-1','seg_s1_base.jpg',None,
 '<div class="lbl">Pio da Semana</div><h1>Hoje o Japão agradece quem <span class="hl">trabalha</span></h1><div class="sub" data-box="sub" style="top:318px;width:900px">e eu trouxe 3 frases pra você<br>usar com os colegas</div><div class="pill">Arrasta para o lado<div class="btn">'+ARR+'</div></div>'))
def phrase(n,bg,jp,ro,tr,ap,tipx):
    bal=f'<div class="lbl">Pio da Semana</div><div class="bal" data-box="bal" style="top:100px"><div class="row"><div class="jp">{jp}</div><div class="ro">{ro}</div></div><div class="tr">{tr}</div><div class="ap">{ap}</div></div>'
    return (f'pio-japones-{n}',bg,tipx,bal)
slides.append(phrase(2,'seg_s2_base.jpg','お疲れ様です','otsukaresama desu','obrigado pelo seu esforço','serve pra cumprimentar colega e pra fechar o dia',None))
slides.append(phrase(3,'seg_s3_base.jpg','よろしくお願いします','yoroshiku onegaishimasu','conto com você','a gente diz no começo de um projeto ou numa apresentação',None))
slides.append(phrase(4,'seg_s4_base.jpg','お先に失礼します','osaki ni shitsurei shimasu','com licença, vou sair antes','pra sair do escritório sem parecer que fugiu hahaha',None))
slides.append(('pio-japones-5','seg_s5_base.jpg',None,
 '<div class="lbl">Pio da Semana</div><div class="punch" data-box="punch">Salva pra usar no <span style="color:#D6203F">primeiro dia</span> de trabalho</div><div class="sub" data-box="sub" style="top:360px;width:900px">e manda pro colega que sonha com o Japão</div>'))
import sys
import numpy as np
from PIL import Image
def crest(bg):
    a=np.array(Image.open(G+bg).convert('RGB')).astype(int)
    m=(a[...,2]>170)&(a[...,0]<70)&(a[...,1]<140)
    ys,xs=np.where(m[:700])
    y=ys.min(); x=int(np.median(xs[ys<y+6]))
    return x,y
tips={}
for n in (2,3,4):
    x,y=crest(f'seg_s{n}_base.jpg'); tips[n]=(x,y-10); print('crest',n,x,y)
for k,bg,_,body in slides:
    n=int(k.split('-')[-1])
    tail=None
    if n in tips:
        tx,ty=tips[n]
        tail=f'[{tx},{ty}]'
    open(H+k+'.html','w').write(page(body,bg,tail))
    r=subprocess.run(['node',H+'render_a.mjs',H+k+'.html',O+k+'.jpg','1080','1350'],capture_output=True,text=True)
    print(k,r.stdout.strip(),r.stderr.strip()[:200])
