import subprocess, json
import ds
Q='/home/rodrigo/.openclaw/workspace/arara_social/lote13_posts/tirinhas_13B/'
H='/home/rodrigo/.openclaw/workspace/arara_social/semana_23_29_feed/html/'
O='/home/rodrigo/.openclaw/workspace/arara_social/semana_23_29_feed/final/'
TH=dict(ink='#081226',acc='#FFC83D',hl='#FFC83D',under='#B9CCF2')
THD=dict(ink='#FFFFFF',acc='#FFC83D',hl='#FFC83D',under='#B9CCF2',hltext=1)
MIC='<svg viewBox="0 0 24 24" style="width:56%;height:56%;stroke:#fff;fill:none;stroke-width:2.2;stroke-linecap:round;stroke-linejoin:round"><line x1="2" x2="22" y1="2" y2="22"/><path d="M18.89 13.23A7.12 7.12 0 0 0 19 12v-2"/><path d="M5 10v2a7 7 0 0 0 12 5"/><path d="M15 9.34V5a3 3 0 0 0-5.68-1.33"/><path d="M9 9v3a3 3 0 0 0 5.12 2.12"/><line x1="12" x2="12" y1="19" y2="22"/></svg>'
def img(n): return f'<img class="bg" src="file://{Q}{n}.png">'
LB=ds.label('Mico da Rara')
cover=('<div style="position:absolute;inset:0;background:linear-gradient(165deg,#FF8A78 0%,#FF6B57 55%,#F25744 100%)"></div>'
 '<div style="position:absolute;width:760px;height:760px;border-radius:50%;right:-240px;top:-300px;background:radial-gradient(circle,rgba(255,255,255,.30),rgba(255,255,255,.10) 62%,rgba(255,255,255,0) 70%)"></div>'
 f'<div style="position:absolute;left:330px;top:420px;width:600px;height:750px;border-radius:40px;overflow:hidden;border-bottom:16px solid #B9CCF2;box-shadow:0 26px 48px rgba(0,0,0,.32);transform:rotate(2deg);z-index:3"><img src="file://{Q}T2Q1_v1.png" style="width:600px;height:750px;object-fit:cover"></div>')
tile=(f'<div style="position:absolute;left:163px;top:565px;width:396px;height:347px;border-radius:26px;overflow:hidden;z-index:7;box-shadow:0 6px 16px rgba(0,0,0,.18);background-image:url(file://{Q}T2Q1_v1.png);background-repeat:no-repeat;background-size:800px auto;background-position:-238px -170px">'
 f'<div style="position:absolute;right:14px;bottom:14px;width:62px;height:62px;border-radius:50%;background:#E5484D;display:flex;align-items:center;justify-content:center">{MIC}</div></div>')
mic=f'<div style="position:absolute;left:775px;top:225px;width:210px;height:210px;border-radius:50%;background:#E5484D;border-bottom:14px solid #A92E33;display:flex;align-items:center;justify-content:center;box-shadow:0 18px 36px rgba(0,0,0,.3);z-index:7">{MIC}</div>'
S=[(1,TH,cover+ds.zone(LB,ds.title('O mico do <span class="hl">microfone mudo</span>'))+ds.nav()),
(2,TH,img('T2Q1_v1')+ds.zone(LB)+ds.caption('Eu na call, falando o melhor inglês da minha vida')+ds.nav()),
(3,TH,img('T2Q2_v2')+tile+ds.zone(LB)+ds.caption('Só que o meu microfone estava <b>no mudo</b>')+ds.nav()),
(4,TH,img('T2Q3_v1')+mic+ds.zone(LB)+ds.caption('Foi aí que eu percebi')+ds.nav()),
(5,TH,img('T2Q4_v3')+ds.zone(LB)+ds.caption('Falei bonito, mas <b>ninguém escutou nada</b>'))]
for n,th,body in S:
    k=f'mico-t2-{n}'
    open(H+k+'.html','w').write(ds.doc(th,None,body))
    r=subprocess.run(['node',H+'render_a.mjs',H+k+'.html',O+k+'.jpg','1080','1350'],capture_output=True,text=True)
    print(n,r.stdout.strip()[-120:],r.stderr[:100])
