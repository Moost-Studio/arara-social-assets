import subprocess, json
from PIL import Image
R='/home/rodrigo/.openclaw/workspace/arara_social/semana1/recortes/'
F='/home/rodrigo/.openclaw/workspace/arara_social/semana1/_fontes/'
H='/home/rodrigo/.openclaw/workspace/arara_social/semana_23_29_feed/html/'
O='/home/rodrigo/.openclaw/workspace/arara_social/semana_23_29_feed/final/'
SC=0.72; BOT=1292
IC={'mic':'<path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3Z"/><path d="M19 10v2a7 7 0 0 1-14 0v-2"/><line x1="12" x2="12" y1="19" y2="22"/>',
'target':'<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/>',
'check':'<path d="M20 6 9 17l-5-5"/>',
'kb':'<path d="M10 8h.01"/><path d="M12 12h.01"/><path d="M14 8h.01"/><path d="M16 12h.01"/><path d="M18 8h.01"/><path d="M6 8h.01"/><path d="M7 16h10"/><path d="M8 12h.01"/><rect width="20" height="16" x="2" y="4" rx="2"/>',
'slow':'<path d="M3 12a9 9 0 1 0 9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"/><path d="M3 3v5h5"/>',
'msg':'<path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z"/>',
'lang':'<path d="m5 8 6 6"/><path d="m4 14 6-6 2-3"/><path d="M2 5h12"/><path d="M7 2h1"/><path d="m22 22-5-10-5 10"/><path d="M14 18h6"/>',
'arr':'<path d="M5 12h14"/><path d="m12 5 7 7-7 7"/>'}
def ic(n,sz=56,col='#fff',sw=2.4): return f'<svg width="{sz}" height="{sz}" viewBox="0 0 24 24" fill="none" stroke="{col}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round">{IC[n]}</svg>'
CSS=f"""
@font-face{{font-family:'Nunito';src:url('file://{F}Nunito.ttf');font-weight:200 1000}}
@font-face{{font-family:'Mochiy';src:url('file://{F}MochiyPopOne-Regular.ttf')}}
*{{box-sizing:border-box;margin:0;padding:0}} body{{background:#000}}
#post{{position:relative;width:1080px;height:1350px;overflow:hidden;font-family:'Nunito';color:#081226;background:linear-gradient(180deg,#3F73F2 0%,#2457E6 55%,#1F4FD6 100%)}}
.blob{{position:absolute;border-radius:50%;background:radial-gradient(circle,rgba(255,255,255,.20),rgba(255,255,255,0) 70%)}}
.floor{{position:absolute;left:0;top:1150px;width:1080px;height:200px;background:linear-gradient(180deg,#1B43B8,#17399B);border-top:6px solid rgba(255,255,255,.22)}}
.rara{{position:absolute;z-index:3}}
.lbl{{position:absolute;left:64px;top:58px;display:flex;align-items:center;gap:16px;font-weight:900;font-size:34px;letter-spacing:.22em;text-transform:uppercase;color:#fff;z-index:6}}
.lbl::after{{content:'';width:56px;height:5px;border-radius:3px;background:#FFC83D}}
h1{{position:absolute;left:64px;top:116px;width:950px;font-weight:900;font-size:68px;line-height:1.05;letter-spacing:-.01em;color:#fff;z-index:6}}
.y{{color:#FFC83D}}
.sub{{position:absolute;left:64px;width:950px;font-weight:800;font-size:42px;line-height:1.2;color:#EAF1FF;z-index:6}}
.card{{position:absolute;left:64px;width:952px;z-index:6;background:#FFF5E1;border-radius:40px;border-bottom:14px solid #E6D3AA;padding:24px 34px;box-shadow:0 14px 30px rgba(5,20,80,.28)}}
.row{{display:flex;align-items:center;gap:22px}}
.ib{{width:76px;height:76px;border-radius:50%;background:#2457E6;display:flex;align-items:center;justify-content:center;flex:none}}
.ch{{display:flex;align-items:center;gap:18px;background:#fff;border-radius:999px;padding:8px 28px 8px 12px;font-weight:900;font-size:40px;border-bottom:8px solid #DCEBFF;box-shadow:0 8px 18px rgba(5,20,80,.2)}}
.ch .ib{{width:56px;height:56px;background:#FFC83D}}
.num{{width:50px;height:50px;border-radius:50%;background:#FFC83D;font-weight:900;font-size:30px;display:flex;align-items:center;justify-content:center;flex:none}}
.pill{{position:absolute;left:44px;bottom:36px;z-index:7;display:flex;gap:22px;align-items:center;font-weight:800;font-size:36px;background:rgba(255,255,255,.94);padding:10px 14px 10px 30px;border-radius:999px}}
.btn{{width:76px;height:76px;border-radius:50%;background:#FFC83D;display:flex;align-items:center;justify-content:center;box-shadow:0 6px 0 #D9A21A}}
.punch{{position:absolute;left:64px;width:950px;font-family:'Mochiy';font-size:104px;line-height:1.05;color:#FFC83D;text-transform:uppercase;z-index:6;text-shadow:0 8px 0 #1A3FA5}}
"""
def page(rara,flip,body):
    im=Image.open(R+rara); w,h=im.size; bb=im.getbbox(); 
    W=int(w*SC); Hh=int(h*SC)
    bbw=(bb[2]-bb[0])*SC
    x=int(540-(bb[0]*SC+bbw/2)) if not flip else int(540-((w-bb[2])*SC+bbw/2))
    y=int(BOT-bb[3]*SC)
    top=y+int(bb[1]*SC)
    fl='transform:scaleX(-1);' if flip else ''
    blobs='<div class="blob" style="left:-160px;top:560px;width:620px;height:620px"></div><div class="blob" style="left:620px;top:380px;width:560px;height:560px"></div>'
    html=f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body><div id="post">{blobs}<div class="floor"></div><img class="rara" data-top="{top}" src="file://{R}{rara}" style="left:{x}px;top:{y}px;width:{W}px;height:{Hh}px;{fl}">{body}</div></body></html>'
    return html,top
LB='<div class="lbl">Conheça a Rara</div>'
S=[]
S.append(('G07_cx.png',False,LB+'<h1 data-box="h1">Toda conversa comigo começa com uma <span class="y">missão</span></h1><div class="sub" data-box="sub" style="top:316px;width:760px">É assim que a gente treina sem enrolar</div><div class="pill">Arrasta para o lado<div class="btn">'+ic('arr',42,'#081226',3)+'</div></div>'))
S.append(('G02_cx.png',False,LB+'<h1 data-box="h1" style="font-size:60px">Antes de começar, eu te passo <span class="y">3 expressões</span></h1><div class="sub" data-box="sub" style="top:262px;font-size:40px">A sua missão é usar as três na conversa</div>'
 '<div class="card" data-box="card" style="top:336px"><div class="row" style="margin-bottom:14px"><div class="ib">'+ic('target',44)+'</div><div><div style="font-weight:900;font-size:46px;line-height:1">Sua missão</div><div style="font-weight:800;font-size:40px;color:#46557a">3 expressões para tentar usar</div></div></div>'
 +'<div class="row" style="margin-top:6px;gap:22px">'+''.join(f'<div class="row" style="gap:12px"><div class="num">{i}</div><div style="font-weight:800;font-size:40px;color:#46557a">expressão</div></div>' for i in (1,2,3))+'</div></div>'))
S.append(('G01_cx.png',False,LB+'<h1 data-box="h1" style="font-size:60px">Depois a gente conversa <span class="y">por voz</span>, numa situação de verdade</h1><div class="sub" data-box="sub" style="top:262px;font-size:40px">Pode ser um check-in no hotel ou uma<br>reunião do seu trabalho</div>'
 '<div class="card" data-box="card" style="top:376px;padding:18px 34px"><div class="row" style="gap:26px"><div class="ib" style="width:92px;height:92px;background:#FF6B57">'+ic('mic',52)+'</div>'
 '<div style="display:flex;align-items:center;gap:10px;height:92px">'+''.join(f'<div style="width:14px;height:{hh}px;border-radius:7px;background:#2457E6"></div>' for hh in (26,54,80,44,70,34,58,84,38,64,28,48,74,36,22))+'</div></div>'
 '<div class="row" style="margin-top:12px;gap:16px;flex-wrap:wrap"><div class="ch" style="padding:10px 28px">check-in no hotel</div><div class="ch" style="padding:10px 28px">reunião do trabalho</div></div></div>'))
S.append(('G09_cx.png',False,LB+'<h1 data-box="h1">E se você travar no meio?</h1><div class="sub" data-box="sub" style="top:200px;font-size:42px">Eu repito mais devagar, explico em português ou traduzo a minha última fala</div>'
 '<div style="position:absolute;left:64px;top:326px;z-index:6;display:flex;flex-direction:column;gap:12px;align-items:flex-start" data-box="card"><div class="ch"><div class="ib">'+ic('slow',34,'#081226')+'</div>repetir mais devagar</div><div class="ch"><div class="ib">'+ic('msg',34,'#081226')+'</div>explicar em português</div><div class="ch"><div class="ib">'+ic('lang',34,'#081226')+'</div>traduzir a minha última fala</div></div>'))
S.append(('G01_cx.png',True,LB+'<h1 data-box="h1" style="font-size:62px">Não deu pra usar as três?</h1><div class="sub" data-box="sub" style="top:200px">Tudo bem, na próxima conversa tem outra chance</div><div class="punch" data-box="punch" style="top:330px">Bora de novo?</div>'))
S.append(('G06_cx.png',False,LB+'<h1 data-box="h1" style="font-size:62px"><span class="y">Salva</span> esse post pra lembrar como funciona</h1><div class="sub" data-box="sub" style="top:268px">E se você preferir, também dá pra responder escrevendo</div>'
 '<div class="card" data-box="card" style="top:400px;width:560px"><div class="row"><div class="ib">'+ic('kb',40)+'</div><div style="font-weight:900;font-size:46px;line-height:1.05">responder escrevendo</div></div></div>'))
res={}
for i,(rara,flip,body) in enumerate(S,1):
    html,top=page(rara,flip,body)
    open(H+f'como-funciona-1-{i}.html','w').write(html)
    r=subprocess.run(['node',H+'render_a.mjs',H+f'como-funciona-1-{i}.html',O+f'como-funciona-1-{i}.jpg','1080','1350'],capture_output=True,text=True)
    boxes=json.loads(r.stdout.strip().splitlines()[-1]) if r.stdout.strip() else {}
    low=max([b[3] for b in boxes.values()] or [0])
    print(i,'rara_top',top,'conteudo_baixo',low,'folga',top-low,r.stderr[:150])
