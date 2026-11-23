import json, os, subprocess, html
H=os.path.dirname(os.path.abspath(__file__)); F=os.path.join(H,'..','final')
CSS='''
@font-face{font-family:'Nunito';src:url('../../semana1/_fontes/Nunito.ttf');font-weight:200 1000}
@font-face{font-family:'Mochiy';src:url('../../semana1/_fontes/MochiyPopOne-Regular.ttf')}
@font-face{font-family:'NSC';src:url('../../semana1/_fontes/NotoSansSC.ttf');font-weight:100 900}
@font-face{font-family:'NAR';src:url('../../semana1/_fontes/NotoSansArabic.ttf');font-weight:100 900}
*{box-sizing:border-box;margin:0;padding:0}body{background:#000}
#post{position:relative;width:1080px;height:1920px;overflow:hidden;font-family:'Nunito';color:#081226;background-size:cover}
.tapew{position:absolute;left:70px;top:250px;z-index:8;filter:drop-shadow(0 5px 7px rgba(0,0,0,.28));transform:rotate(-4deg)}
.tape{display:inline-block;font-family:'Mochiy';text-transform:lowercase;font-size:44px;line-height:1;color:#081226;background:#FFC83D;padding:16px 46px 16px 42px;clip-path:polygon(1% 6%,0 28%,2% 52%,0 76%,1% 96%,99% 100%,100% 74%,98% 50%,100% 24%,98% 2%)}
h1{position:absolute;left:64px;top:350px;z-index:8;font-weight:900;font-size:80px;line-height:1.04;letter-spacing:-.01em;width:950px}
.hl{background:linear-gradient(transparent 50%,#FF9B47 50%,#FF9B47 92%,transparent 92%);padding:0 8px}
.sup{position:absolute;left:64px;z-index:8;font-weight:800;font-size:46px;line-height:1.22}
.bal{position:absolute;z-index:8;background:transparent;padding:30px 52px 32px;filter:drop-shadow(0 18px 24px rgba(8,18,38,.25));text-align:left;--rad:58px 124px 66px 132px / 92px 58px 112px 62px}
.bal.r0{transform:rotate(-1.6deg)}.bal.r1{transform:rotate(1.3deg)}
.bal::before{content:'';position:absolute;inset:0;top:10px;border-radius:var(--rad);background:#B9CCF2;z-index:-2}
.bal::after{content:'';position:absolute;inset:0;border-radius:var(--rad);background:#fff;z-index:-1}
.tail{position:absolute;bottom:-88px;width:112px;height:100px;z-index:-1;overflow:visible}
.bal .i{font-weight:800;font-size:42px;line-height:1.2;color:#2b3a5c}
.bal .k{display:inline-block;font-weight:900;font-size:84px;line-height:1.25;margin:6px 0 2px;background:linear-gradient(transparent 52%,#FFC83D 52%,#FFC83D 92%,transparent 92%);padding:0 8px}
.bal .r{font-weight:800;font-size:44px;line-height:1.2}
.bal .a{font-weight:800;font-size:42px;line-height:1.2;color:#2b3a5c;margin-top:4px}
.card{position:absolute;left:130px;top:700px;width:820px;height:1025px;border-radius:44px;overflow:hidden;box-shadow:0 30px 60px rgba(0,0,0,.35);z-index:6;border:10px solid #fff}
.card img{width:100%;height:100%;object-fit:cover}
'''
JS='''<script>document.fonts.ready.then(()=>{document.querySelectorAll('.bal[data-bot]').forEach(b=>{const bot=+b.dataset.bot,hx=+b.dataset.hx;b.style.top=(bot-b.offsetHeight)+'px';const L=b.offsetLeft;const t=b.querySelector('.tail');const flip=b.classList.contains('r1');t.style.left=(flip?(hx+14-L):(hx-126-L))+'px';if(flip)t.style.transform='scaleX(-1)'})})</script>'''
TS='''<svg class="tail" viewBox="0 0 112 100"><path d="M8 0 C 8 44 40 80 106 96 C 66 70 62 34 94 0 Z" fill="#fff"/></svg>'''
def tail(bx,by,tx,ty,w=80): return f'<svg class="tail" width="1080" height="1920"><path d="M{bx-w//2},{by-6} L{bx+w//2},{by-6} L{tx},{ty} Z" fill="#fff"/></svg>'
def pg(name,bg,body):
    s=f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>{CSS}</style></head><body><div id="post" style="background-image:url(../gen/{bg})">{body}</div>'+JS+'</body></html>'
    p=os.path.join(H,name+'.html'); open(p,'w').write(s); return p
E=html.escape
jobs=[]
# 219
body=('<div class="tapew"><span class="tape">Bom dia da Rara</span></div><h1 style="font-size:68px">Fala, mestre! Hoje a gente agradece quem <span class="hl">recebe</span></h1>'
 '<div class="bal r0" data-bot="901" data-hx="498" style="left:90px;width:900px"><div class="i">em mandarim, a frase de hoje é</div><div class="k" style="font-family:NSC,Nunito">谢谢你的款待</div><div class="r">xièxie nǐ de kuǎndài</div><div class="a">Quer dizer “obrigado pela hospitalidade”</div>'+TS+'</div>')
jobs.append((pg('story-219','st219_bg.png',body),'story-219',1920,(375,1033,750,1420)))
# 220
body=('<div class="tapew"><span class="tape">Rara reage</span></div><h1 style="font-size:72px">O meu primeiro <span class="hl">Thanksgiving</span> já está no feed</h1>'
 '<div class="sup" style="top:622px;font-size:42px;max-width:880px;background:#fff;padding:12px 28px;border-radius:28px">Confesso que exagerei na torta, por isso eu disse “I’m stuffed”</div>'
 '<div class="card" style="top:770px;height:1000px"><img src="../final/thanksgiving-5.jpg"></div>')
jobs.append((pg('story-220','st220_bg.png',body),'story-220',1920,None))
# 221
body=('<div class="tapew"><span class="tape">Rara pelo mundo</span></div><h1 style="font-size:60px">Hoje foi dia de agradecer, e eu fecho com mais um <span class="hl">obrigado</span></h1>'
 '<div class="bal r1" data-bot="901" data-hx="498" style="left:90px;width:900px"><div class="i">em árabe, a frase é</div><div class="k" dir="rtl" lang="ar" style="font-family:NAR;font-size:92px;line-height:1.5">شكرًا جزيلًا</div><div class="r" style="display:block">shukran jazeelan</div><div class="a">Quer dizer “muito obrigado”, a primeira frase de qualquer viagem</div>'+TS+'</div>')
jobs.append((pg('story-221','st221_bg.png',body),'story-221',1920,(375,1033,750,1420)))
js=os.path.join(H,'render.mjs')
J=[[p,os.path.join(H,'_'+o+'.png'),1080,1920] for p,o,h,f in jobs]
res=subprocess.run(['node',js,json.dumps(J)],check=True,capture_output=True,text=True)
for line in res.stdout.splitlines():
    if not line.startswith('RECTS'): continue
    _,o,r=line.split(' ',2); name=os.path.basename(o)[1:-4]; face=[j[3] for j in jobs if j[1]==name][0]
    bad=[]
    if face:
        for c,l,t,rr,b in json.loads(r):
            if c=='pill': continue
            if l<face[2] and rr>face[0] and t<face[3] and b>face[1]: bad.append((c,l,t,rr,b))
    print(name,'rosto',face,'INTERSECTA' if bad else 'livre',bad)
from PIL import Image
for p,o,w,h in J:
    Image.open(o).convert('RGB').save(os.path.join(F,os.path.basename(o)[1:-4]+'.jpg'),quality=92)
print('ok')
