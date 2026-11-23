import subprocess, json
from PIL import Image
import ds
R='/home/rodrigo/.openclaw/workspace/arara_social/semana1/recortes/'
H='/home/rodrigo/.openclaw/workspace/arara_social/semana_23_29_feed/html/'
O='/home/rodrigo/.openclaw/workspace/arara_social/semana_23_29_feed/final/'
TH=dict(ink='#FFFFFF',acc='#FFC83D',hl='#FFC83D',under='#DCEBFF',hltext=1,sub='#EAF1FF')
SC=0.66; BOT=1292
IC={'mic':'<path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3Z"/><path d="M19 10v2a7 7 0 0 1-14 0v-2"/><line x1="12" x2="12" y1="19" y2="22"/>',
'target':'<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/>',
'kb':'<path d="M10 8h.01"/><path d="M12 12h.01"/><path d="M14 8h.01"/><path d="M16 12h.01"/><path d="M18 8h.01"/><path d="M6 8h.01"/><path d="M7 16h10"/><path d="M8 12h.01"/><rect width="20" height="16" x="2" y="4" rx="2"/>',
'slow':'<path d="M3 12a9 9 0 1 0 9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"/><path d="M3 3v5h5"/>',
'msg':'<path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z"/>',
'lang':'<path d="m5 8 6 6"/><path d="m4 14 6-6 2-3"/><path d="M2 5h12"/><path d="M7 2h1"/><path d="m22 22-5-10-5 10"/><path d="M14 18h6"/>'}
def ic(n): return f'<svg viewBox="0 0 24 24">{IC[n]}</svg>'
def bgpage(rara,flip):
    im=Image.open(R+rara); w,h=im.size; bb=im.getbbox(); W=int(w*SC); Hh=int(h*SC); bbw=(bb[2]-bb[0])*SC
    x=int(540-(bb[0]*SC+bbw/2)) if not flip else int(540-((w-bb[2])*SC+bbw/2)); y=int(BOT-bb[3]*SC); top=y+int(bb[1]*SC)
    fl='transform:scaleX(-1);' if flip else ''
    bg=('<div style="position:absolute;inset:0;background:linear-gradient(180deg,#3F73F2 0%,#2457E6 55%,#1F4FD6 100%)"></div>'
        '<div style="position:absolute;left:-160px;top:560px;width:620px;height:620px;border-radius:50%;background:radial-gradient(circle,rgba(255,255,255,.20),rgba(255,255,255,0) 70%)"></div>'
        '<div style="position:absolute;left:620px;top:380px;width:560px;height:560px;border-radius:50%;background:radial-gradient(circle,rgba(255,255,255,.20),rgba(255,255,255,0) 70%)"></div>'
        '<div style="position:absolute;left:0;top:1150px;width:1080px;height:200px;background:linear-gradient(180deg,#1B43B8,#17399B);border-top:6px solid rgba(255,255,255,.22)"></div>'
        f'<img src="file://{R}{rara}" style="position:absolute;z-index:3;left:{x}px;top:{y}px;width:{W}px;height:{Hh}px;{fl}">')
    return bg,top
LB=ds.label('Conheça a Rara')
mission=('<div class="ds-card" data-box="card" style="display:flex;align-items:center;gap:22px;padding:20px 34px"><div class="ds-chip" style="padding:0;width:72px;height:72px;border-radius:50%;justify-content:center;background:#2457E6"><span class="ib" style="background:none;width:44px;height:44px"><svg viewBox="0 0 24 24" style="stroke:#fff;width:40px;height:40px">'+IC['target']+'</svg></span></div>'
 '<div><div class="ct" style="font-size:40px">Sua missão</div><div class="cs" style="font-size:32px">3 expressões para tentar usar</div></div></div>')
voz=('<div class="ds-card" data-box="card" style="padding:20px 34px;display:flex;flex-direction:column;gap:14px"><div style="display:flex;align-items:center;gap:22px"><div style="width:72px;height:72px;border-radius:50%;background:#FF6B57;display:flex;align-items:center;justify-content:center;flex:none"><svg viewBox="0 0 24 24" style="stroke:#fff;fill:none;stroke-width:2.4;stroke-linecap:round;width:40px;height:40px">'+IC['mic']+'</svg></div>'
 '<div style="display:flex;align-items:center;gap:9px;height:72px">'+''.join(f'<div style="width:12px;height:{hh}px;border-radius:6px;background:#2457E6"></div>' for hh in (22,44,64,36,56,28,48,66,30,52,24,40,60,30,18))+'</div></div>'
 '<div style="display:flex;gap:14px">'+ds.chip('check-in no hotel')+ds.chip('reunião do trabalho')+'</div></div>')
S=[('G07_cx.png',False,ds.zone(LB,ds.title('Toda conversa comigo começa com uma <span class="hl">missão</span>'),ds.sub('É assim que a gente treina sem enrolar'))+ds.nav()),
('G02_cx.png',False,ds.zone(LB,ds.title('Antes de começar, eu te passo <span class="hl">3 expressões</span>'),ds.sub('A sua missão é usar as três na conversa'),mission)+ds.nav()),
('G01_cx.png',False,ds.zone(LB,ds.title('E a conversa é <span class="hl">por voz</span>'),ds.sub('Numa situação de verdade, como um check-in no hotel ou uma reunião do seu trabalho'),voz)+ds.nav()),
('G09_cx.png',False,ds.zone(LB,ds.title('E se você <span class="hl">travar</span> no meio?'),ds.sub('Eu repito mais devagar, explico em português ou traduzo a minha última fala'),'<div style="display:flex;flex-direction:column;gap:12px">'+ds.chip('repetir mais devagar',ic('slow'))+ds.chip('explicar em português',ic('msg'))+ds.chip('traduzir a minha última fala',ic('lang'))+'</div>')+ds.nav()),
('G01_cx.png',True,ds.zone(LB,ds.title('Não deu pra usar as três?'),ds.sub('Tudo bem, na próxima conversa tem outra chance'),ds.punch('Bora de novo?'))+ds.nav()),
('G06_cx.png',False,ds.zone(LB,ds.title('<span class="hl">Salva</span> esse post pra lembrar como funciona'),ds.sub('E se você preferir, também dá pra responder escrevendo'),ds.chip('responder escrevendo',ic('kb'))))]
for i,(rara,flip,body) in enumerate(S,1):
    bg,top=bgpage(rara,flip)
    open(H+f'como-funciona-1-{i}.html','w').write(ds.doc(TH,bg,body))
    r=subprocess.run(['node',H+'render_a.mjs',H+f'como-funciona-1-{i}.html',O+f'como-funciona-1-{i}.jpg','1080','1350'],capture_output=True,text=True)
    z=json.loads(r.stdout.strip().splitlines()[-1])['zone'] if r.stdout.strip() else None
    print(i,'rara_top',top,'zona',z,'folga',(top-z[3]) if z else None,r.stderr[:100])
