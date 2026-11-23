import subprocess, json, numpy as np
from PIL import Image
import ds
G='/home/rodrigo/.openclaw/workspace/arara_social/semana_23_29_feed/gen/'
H='/home/rodrigo/.openclaw/workspace/arara_social/semana_23_29_feed/html/'
O='/home/rodrigo/.openclaw/workspace/arara_social/semana_23_29_feed/final/'
TH=dict(ink='#3A1620',acc='#FFC83D',hl='#FFD25E',under='#F2C9D2',ctaacc='#C81E3A')
WASH='<div style="position:absolute;left:0;top:0;width:1080px;height:640px;background:linear-gradient(180deg,rgba(242,201,210,.78),rgba(242,201,210,.35) 62%,rgba(242,201,210,0));z-index:1"></div>'
def crest(bg):
    a=np.array(Image.open(G+bg).convert('RGB')).astype(int)
    m=(a[...,2]>170)&(a[...,0]<70)&(a[...,1]<140)
    ys,xs=np.where(m[:900]); y=ys.min(); x=int(np.median(xs[ys<y+6])); return x,y
S=[]
S.append(('pio-japones-1','seg_s1_base.jpg',
  ds.zone(ds.label('Pio da Semana'),ds.title('Hoje é feriado no Japão, e o motivo é <span class="hl">lindo</span>'),ds.sub('É o dia de agradecer quem trabalha, e eu trouxe 3 frases que você ouve em qualquer escritório japonês'))+ds.nav()))
def frase(n,jp,ro,tr,ap):
    x,y=crest(f'seg_s{n}_base.jpg')
    main=f'<div style="font-family:JP,Nunito;font-size:1.12em;line-height:1.1;white-space:nowrap">{jp}</div><div style="font-size:.56em;line-height:1.2;color:#C81E3A;font-weight:900;margin-top:3px">{ro}</div><div style="font-size:.86em;margin-top:2px">{tr}</div>'
    body=ds.zone(ds.label('Pio da Semana'))+ds.fala(main,ap,idx=n,hx=x,cy=y,top_min=104,extra_main_css='font-size:50px')+ds.nav()
    return (f'pio-japones-{n}',f'seg_s{n}_base.jpg',body)
S.append(frase(2,'お疲れ様です','otsukaresama desu','Obrigado pelo seu esforço','Serve pra cumprimentar e pra fechar o dia'))
S.append(frase(3,'よろしくお願いします','yoroshiku onegaishimasu','Conto com você','A gente diz no começo de um projeto'))
S.append(frase(4,'お先に失礼します','osaki ni shitsurei shimasu','Com licença, vou sair antes','Pra sair sem parecer que fugiu, hahaha'))
S.append(('pio-japones-5','seg_s5_base.jpg',
  ds.zone(ds.label('Pio da Semana'),ds.title('Salva pra usar no seu <span class="hl">primeiro dia</span> de trabalho'),ds.cta('Manda pro colega que sonha em conhecer o <b>Japão</b>'))))
for k,bg,body in S:
    open(H+k+'.html','w').write(ds.doc(TH,G+bg,WASH+body))
    r=subprocess.run(['node',H+'render_a.mjs',H+k+'.html',O+k+'.jpg','1080','1350'],capture_output=True,text=True)
    print(k,r.stdout.strip()[-260:],r.stderr[:150])
