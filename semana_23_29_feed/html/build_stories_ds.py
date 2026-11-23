import subprocess, json
from PIL import Image
import ds
G='/home/rodrigo/.openclaw/workspace/arara_social/semana_23_29_feed/gen/'
R='/home/rodrigo/.openclaw/workspace/arara_social/semana1/recortes/'
H='/home/rodrigo/.openclaw/workspace/arara_social/semana_23_29_feed/html/'
O='/home/rodrigo/.openclaw/workspace/arara_social/semana_23_29_feed/final/'
FIN='/home/rodrigo/.openclaw/workspace/arara_social/semana_23_29_feed/final/'
LIGHT=dict(ink='#081226',acc='#FFC83D',hl='#FFC83D',under='#B9CCF2')
DARK=dict(ink='#FFFFFF',acc='#FFC83D',hl='#FFC83D',under='#B9CCF2',hltext=1,sub='#EAF1FF')
def fala(main,apoio,idx,hx,cy,mn,css=''): return ds.fala(main,apoio,idx=idx,hx=hx,cy=cy,top_min=mn,extra_main_css=css)
P=[]
# 216 bom dia, sueco
P.append(('story-216',LIGHT,'st216_base.jpg',
  ds.zone(ds.label('Bom dia da Rara'),ds.sub('Bom dia! Hoje é a minha frase favorita pra quando alguém erra'))+fala('Ingen fara!','Em sueco, quer dizer “sem problema, relaxa”',0,513,814,300)))
# 218 modo carente (jargao permitido: pedido ao usuario)
P.append(('story-218',DARK,'st218_base.jpg',
  ds.zone(ds.status('Modo carente'))+fala('Faaala, meu campeão! 👀','Separei o cronômetro e o tapete. Bora de 3 minutinhos de conversa?',1,465,668,300)+ds.caption('Eu conto como <b>exercício</b>, prometo')))
# 219 bom dia, mandarim
P.append(('story-219',LIGHT,'st219_bg.png',
  ds.zone(ds.label('Bom dia da Rara'),ds.sub('Bom dia! Hoje é Thanksgiving, o Dia de Ação de Graças nos Estados Unidos, e a gente agradece quem recebe'))+fala('<span style="font-family:NSC,Nunito;font-size:1.25em;line-height:1.3;display:block">谢谢你的款待</span><span style="font-size:.52em;color:#C81E3A;display:block;margin-top:4px">xièxie nǐ de kuǎndài</span>','Em mandarim, quer dizer “obrigado pela hospitalidade”',0,498,1037,360)))
# 221 arabe
P.append(('story-221',LIGHT,'st221_bg.png',
  ds.zone(ds.label('Rara pelo mundo'),ds.sub('Hoje foi Thanksgiving, o Dia de Ação de Graças nos Estados Unidos, então eu fecho o dia com mais um obrigado'))+fala('<span dir="rtl" lang="ar" style="font-family:NAR;font-size:1.3em;line-height:1.5;display:block">شكرًا جزيلًا</span><span style="font-size:.52em;color:#C81E3A;display:block;margin-top:2px">shukran jazeelan</span>','Em árabe, quer dizer “muito obrigado”, a primeira frase de qualquer viagem',1,498,1037,360)))
# 220 reage
P.append(('story-220',LIGHT,'st220_bg.png',
  ds.zone(ds.label('Rara reage'),ds.title('O meu primeiro <span class="hl">Thanksgiving</span> já está no feed',small=True),ds.sub('Confesso que exagerei na torta'))+
  f'<div style="position:absolute;left:130px;top:760px;width:820px;height:960px;border-radius:44px;overflow:hidden;box-shadow:0 30px 60px rgba(0,0,0,.35);z-index:6;border:10px solid #fff"><img src="file://{FIN}thanksgiving-5.jpg" style="width:100%;height:100%;object-fit:cover"></div>'))
# 217 bastidores
SC=0.8; im=Image.open(R+'G07_cx.png'); bb=im.getbbox(); w,h=im.size
x=int(540-(bb[0]*SC+(bb[2]-bb[0])*SC/2)); y=int(1700-bb[3]*SC)
IC_T='<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/>'
card=('<div class="ds-card" data-box="card" style="display:flex;align-items:center;gap:22px;padding:22px 34px;width:900px"><div style="width:76px;height:76px;border-radius:50%;background:#2457E6;display:flex;align-items:center;justify-content:center;flex:none"><svg viewBox="0 0 24 24" style="width:44px;height:44px;stroke:#fff;fill:none;stroke-width:2.4;stroke-linecap:round">'+IC_T+'</svg></div><div><div class="ct">Sua missão</div><div class="cs">3 expressões para tentar usar</div></div></div>')
bg217=('<div style="position:absolute;inset:0;background:linear-gradient(180deg,#3F73F2 0%,#2457E6 55%,#1F4FD6 100%)"></div><div style="position:absolute;left:-200px;top:900px;width:700px;height:700px;border-radius:50%;background:radial-gradient(circle,rgba(255,255,255,.2),rgba(255,255,255,0) 70%)"></div>'
       '<div style="position:absolute;left:0;top:1500px;width:1080px;height:420px;background:linear-gradient(180deg,#1B43B8,#17399B);border-top:6px solid rgba(255,255,255,.22)"></div>'
       f'<img src="file://{R}G07_cx.png" style="position:absolute;z-index:3;left:{x}px;top:{y}px;width:{int(w*SC)}px;height:{int(h*SC)}px">')
P.append(('story-217',DARK,None,bg217+ds.zone(ds.label('Bastidores'),ds.title('Já está no feed como funciona a <span class="hl">missão</span> de cada conversa',small=True),card,'<div class="gap" style="--g:30px"></div>'+ds.sub('Dá uma olhada no post e me conta se ficou claro'))))
for k,th,bg,body in P:
    img=f'<img class="bg" src="file://{G}{bg}">' if bg else ''
    open(H+k+'.html','w').write(ds.doc(th,None,img+body,story=True))
    r=subprocess.run(['node',H+'render_a.mjs',H+k+'.html',O+k+'.jpg','1080','1920'],capture_output=True,text=True)
    print(k,r.stdout.strip()[-200:],r.stderr[:120])
