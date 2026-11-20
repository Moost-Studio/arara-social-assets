import html, json, subprocess, os
H=os.path.dirname(os.path.abspath(__file__)); F=os.path.join(H,'..','final')
CSS='''
@font-face{font-family:'Nunito';src:url('../../semana1/_fontes/Nunito.ttf');font-weight:200 1000}
@font-face{font-family:'Mochiy';src:url('../../semana1/_fontes/MochiyPopOne-Regular.ttf')}
@font-face{font-family:'NJP';src:url('../../semana1/_fontes/NotoSansJP.ttf');font-weight:100 900}
@font-face{font-family:'NSC';src:url('../../semana1/_fontes/NotoSansSC.ttf');font-weight:100 900}
@font-face{font-family:'NAR';src:url('../../semana1/_fontes/NotoSansArabic.ttf');font-weight:100 900}
*{box-sizing:border-box;margin:0;padding:0}
body{background:#000}
#post{position:relative;width:1080px;height:1350px;overflow:hidden;font-family:'Nunito';color:#081226}
#post>img.bg{position:absolute;left:0;top:0;width:1080px;height:1350px;object-fit:cover;object-position:center}
.scrim{position:absolute;left:0;top:0;width:1080px;z-index:2}
.lbl{position:absolute;left:64px;top:62px;z-index:8;display:flex;align-items:center;gap:16px;font-weight:900;font-size:40px;letter-spacing:.18em;text-transform:uppercase}
.lbl::after{content:'';width:56px;height:5px;border-radius:3px;background:currentColor}
h1{position:absolute;left:64px;z-index:8;font-weight:900;line-height:1.06;letter-spacing:-.01em}
.hl{padding:0 8px;border-radius:10px}
.sup{position:absolute;left:64px;z-index:8;font-weight:800;font-size:44px;line-height:1.2;padding:16px 30px;border-radius:30px}
.bal{position:absolute;z-index:8;background:#fff;border-radius:46px;border-bottom:16px solid #B9CCF2;padding:22px 40px 20px;box-shadow:0 20px 40px rgba(0,0,0,.24);display:flex;flex-direction:column;justify-content:center}
.bal .en{font-weight:900;font-size:64px;line-height:1.08;letter-spacing:-.01em}
.bal .pt{font-weight:800;font-size:42px;line-height:1.18;margin-top:10px;color:#2b3a5c}
.pill{position:absolute;z-index:9;display:flex;gap:18px;align-items:center;font-weight:800;font-size:40px;line-height:1.1;background:rgba(255,255,255,.93);padding:12px 12px 12px 26px;border-radius:44px;right:30px;bottom:44px;width:320px}
.btn{width:90px;height:90px;border-radius:50%;display:flex;align-items:center;justify-content:center;box-shadow:0 8px 0 rgba(0,0,0,.2)}
.btn svg{width:48px;height:48px;stroke:#081226}
svg.tail{position:absolute;left:0;top:0;z-index:7}
.word{position:absolute;z-index:8;left:64px;display:flex;align-items:center;gap:26px;font-family:'Mochiy';font-size:92px;line-height:1;padding:20px 40px;border-radius:36px;box-shadow:0 10px 0 rgba(0,0,0,.2)}
.word svg{width:1em;height:1em;stroke:currentColor;flex:none}
.card{position:absolute;z-index:8;left:64px;background:#fff;border-radius:34px;padding:22px 36px;font-weight:900;font-size:46px;line-height:1.16;box-shadow:0 14px 30px rgba(0,0,0,.2);border-bottom:12px solid #D9CCF2}
.card small{display:block;font-weight:800;font-size:42px;margin-top:6px;color:#4b3b73}
.punch{position:absolute;z-index:8;left:64px;font-family:'Mochiy';font-size:110px;line-height:1.1}
'''
ARR='<svg viewBox="0 0 24 24" fill="none" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg>'
def page(key,n,img,body,extra_css=''):
    s=f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>{CSS}{extra_css}</style></head><body><div id="post"><img class="bg" src="../gen/{img}">{body}</div></body></html>'
    p=os.path.join(H,f'{key}-{n}.html'); open(p,'w').write(s); return p
def tail(bx,by,tx,ty,w=70):
    # triangulo do balao (base em by) ate a ponta (tx,ty)
    return f'<svg class="tail" width="1080" height="1350"><path d="M{bx-w//2},{by-8} L{bx+w//2},{by-8} L{tx},{ty} Z" fill="#fff"/><path d="M{bx-w//2},{by-8} L{bx+w//2},{by-8} L{tx},{ty+0} Z" fill="none"/></svg>'
def bal(en,pt,top,h,tx,ty,left=100,w=880):
    bx=min(max(tx,left+90),left+w-90)
    return f'<div class="bal" style="left:{left}px;top:{top}px;width:{w}px;height:{h}px"><div class="en">{html.escape(en)}</div><div class="pt">{html.escape(pt)}</div></div>'+tail(bx,top+h+16,tx,ty)
jobs=[]  # (html, out, w, h)
# ---------- THANKSGIVING
OR='#F5873A'
T=[ ('thanks1_sh.png',457,540),('thanks2_sh.png',457,540),('thanks3_sh.png',457,540),('thanks4_sh.png',457,540),('thanks5_sh.png',457,540),('thanks1_sh.png',457,540)]
def lbl(txt,color='#081226'): return f'<div class="lbl" style="color:{color}">{html.escape(txt)}</div>'
extra_t='.hl{background:linear-gradient(transparent 50%,#FF9B47 50%,#FF9B47 92%,transparent 92%)}'
body=lbl('Rara pelo mundo')+'<h1 style="top:124px;font-size:70px;width:940px">Fui convidada pro <span class="hl">Thanksgiving</span></h1><div class="sup" style="top:296px;background:#F5873A;color:#fff;width:900px;font-size:42px;padding:12px 28px">e separei 4 frases pra ninguém ficar quieto na mesa</div><div class="pill"><span>Arrasta para o lado</span><div class="btn" style="background:#F5873A">'+ARR+'</div></div>'
jobs.append((page('thanksgiving',1,T[0][0],body,extra_t),'thanksgiving-1'))
phr=[('Thanks for having me!','obrigada por me receber',None),('Could you pass the potatoes, please?','você me passa as batatas, por favor?',None),('What are you thankful for this year?','pelo que você é grato este ano?','é a pergunta mais clássica da noite'),('I’m stuffed!','não cabe mais nada',None)]
for i,(en,pt,ap) in enumerate(phr):
    n=i+2; h=262 if len(en)>24 else 240
    b=lbl('Rara pelo mundo')+bal(en,pt,118,h,T[i+1][2],T[i+1][1]-26)
    if ap: b+=f'<div class="sup" style="left:auto;right:40px;top:1090px;width:300px;font-size:40px;background:#F5873A;color:#fff;padding:14px 24px;border-radius:26px;line-height:1.15">{html.escape(ap)}</div>'
    jobs.append((page('thanksgiving',n,T[i+1][0],b,extra_t),f'thanksgiving-{n}'))
# final
b=lbl('Rara pelo mundo')+'<div style="position:absolute;left:0;top:0;width:1080px;height:430px;z-index:3;background:linear-gradient(180deg,#F5873A 0%,#F5873A 84%,rgba(245,135,58,0) 100%)"></div><h1 style="top:128px;font-size:62px;width:940px;color:#fff;z-index:8">Salva pro dia em que te chamarem pra um jantar desses</h1><div class="sup" style="top:318px;background:#fff;color:#081226;width:940px;font-size:42px;padding:12px 28px">o Thanksgiving cai sempre na 4ª quinta de novembro</div>'
b=b.replace('class="lbl" style="color:#081226"','class="lbl" style="color:#fff"')
jobs.append((page('thanksgiving',6,T[5][0],b,extra_t),'thanksgiving-6'))
# ---------- FALSO AMIGO
V='#6D3DB8'
extra_f='.hl{background:#FFC83D;color:#081226}'
def word_slide(n,img,word,meaning,card1,card2,crest,tipx,bgc,txtc,scrim=None,fs=92):
    b=lbl('Falso amigo','#fff' if txtc=='w' else '#081226')
    if scrim: b+=scrim
    b+=f'<div class="word" style="top:128px;background:{bgc};color:#fff;font-size:{fs}px;gap:{fs//4}px;padding:18px 34px">{word}{ARR}{meaning}</div>'
    b+=f'<div class="card" style="top:300px;width:940px">{html.escape(card1)}<small>{html.escape(card2)}</small></div>'
    return page('falso-blackfriday',n,img,b,extra_f)
cover=lbl('Falso amigo','#fff')+'<h1 style="top:128px;font-size:72px;width:950px;color:#fff">Black Friday em inglês tem <span class="hl">pegadinha</span></h1><div class="sup" style="top:330px;background:#FFC83D;color:#081226;width:760px;font-size:42px">4 palavras que parecem português, mas não são</div><div class="pill"><span>Arrasta para o lado</span><div class="btn" style="background:#FFC83D">'+ARR+'</div></div>'
jobs.append((page('falso-blackfriday',1,'fa1_sh.png',cover,extra_f),'falso-blackfriday-1'))
jobs.append((word_slide(2,'fa07_sh.png','PUSH','EMPURRAR','na porta da loja é empurrar','puxar é pull',580,484,'#6D3DB8','d',None,72),'falso-blackfriday-2'))
jobs.append((word_slide(3,'fa_sale_sh.png','SALE','LIQUIDAÇÃO','na vitrine, é liquidação','nada a ver com sala',551,500,'#6D3DB8','w',None,62),'falso-blackfriday-3'))
jobs.append((word_slide(4,'fa_receipt_sh.png','RECEIPT','NOTA','é a nota, o comprovante da compra','receita de bolo é recipe',548,524,'#6D3DB8','w',None,84),'falso-blackfriday-4'))
scr='<div class="scrim" style="height:520px;background:linear-gradient(180deg,#5A2FA0 0%,#5A2FA0 62%,rgba(90,47,160,0) 100%)"></div>'
jobs.append((word_slide(5,'fa_collar_sh.png','COLLAR','GOLA','gola de camisa ou coleira de bicho','colar de enfeite é necklace',560,330,'#6D3DB8','w',scr,88),'falso-blackfriday-5'))
fin=lbl('Falso amigo','#fff')+'<div class="scrim" style="height:470px;background:linear-gradient(180deg,#5A2FA0 0%,#5A2FA0 80%,rgba(90,47,160,0) 100%)"></div><div class="punch" style="top:128px;color:#FFC83D">Bora de novo?</div><div class="sup" style="top:300px;background:#fff;color:#081226;width:950px;font-size:42px;padding:12px 28px">manda pro amigo que vai às compras lá fora</div>'
jobs.append((page('falso-blackfriday',6,'fa1_sh.png',fin,extra_f),'falso-blackfriday-6'))
# render
js=os.path.join(H,'render.mjs')
open(js,'w').write('''import { createRequire } from 'module';
const require = createRequire('/home/rodrigo/moost-projects/devfluent-app/package.json');
const { chromium } = require('playwright');
const jobs = JSON.parse(process.argv[2]);
const b = await chromium.launch();
for (const [f,out,w,h] of jobs){ const p = await b.newPage({viewport:{width:w,height:h}});
 await p.goto('file://'+f); await p.evaluate(()=>document.fonts.ready); await p.waitForTimeout(500);
 const r = await p.evaluate(()=>[...document.querySelectorAll('.bal,.card,.sup,.word,.punch,h1,.pill,svg.tail path')].map(e=>{const b=e.getBoundingClientRect();return [e.className&&e.className.baseVal!==undefined?'tail':e.className||e.tagName,Math.round(b.left),Math.round(b.top),Math.round(b.right),Math.round(b.bottom)]}));
 console.log('RECTS '+out+' '+JSON.stringify(r));
 await (await p.$('#post')).screenshot({path:out, type:'png'}); await p.close(); }
await b.close();''')
import sys
sel=sys.argv[1:] 
J=[[p,os.path.join(H,'_'+o+'.png'),1080,1350] for p,o in jobs if not sel or any(s in o for s in sel)]
res=subprocess.run(['node',js,json.dumps(J)],check=True,capture_output=True,text=True)
FACE={'thanksgiving':(375,457,750,845),'fa1':(393,548,697,844),'fa07':(349,579,641,844),'sale':(387,551,692,844),'receipt':(393,548,692,844),'collar':(217,560,545,890)}
FK={'thanksgiving-1':'thanksgiving','thanksgiving-2':'thanksgiving','thanksgiving-3':'thanksgiving','thanksgiving-4':'thanksgiving','thanksgiving-5':'thanksgiving','thanksgiving-6':'thanksgiving','falso-blackfriday-1':'fa1','falso-blackfriday-2':'fa07','falso-blackfriday-3':'sale','falso-blackfriday-4':'receipt','falso-blackfriday-5':'collar','falso-blackfriday-6':'fa1'}
for line in res.stdout.splitlines():
    if not line.startswith('RECTS'): continue
    _,o,js_=line.split(' ',2); name=os.path.basename(o)[1:-4]; fx=FACE[FK[name]]; bad=[]
    for c,l,t,r,b in json.loads(js_):
        if c in ('lbl',) or c=='pill': continue
        if l<fx[2] and r>fx[0] and t<fx[3] and b>fx[1]: bad.append((c,l,t,r,b))
    mx=max([b for c,l,t,r,b in json.loads(js_) if c!='pill'] or [0])
    print(name,'face',fx,'INTERSECTA' if bad else 'livre',bad,'| maior base do texto',mx)
from PIL import Image
for p,o,w,h in J:
    name=os.path.basename(o)[1:-4]
    Image.open(o).convert('RGB').save(os.path.join(F,name+'.jpg'),quality=92)
print('ok',len(J))
