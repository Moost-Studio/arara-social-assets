import subprocess, json
import ds
G='/home/rodrigo/.openclaw/workspace/arara_social/semana_23_29_feed/gen/'
H='/home/rodrigo/.openclaw/workspace/arara_social/semana_23_29_feed/html/'
O='/home/rodrigo/.openclaw/workspace/arara_social/semana_23_29_feed/final/'
DARK=dict(ink='#FFFFFF',acc='#FFC83D',hl='#FFC83D',under='#D9CCF2',hltext=1,sub='#F1EAFF')
LIGHT=dict(ink='#081226',acc='#FFC83D',hl='#FFC83D',under='#F3C9B8')
FACE={'fa1':548,'fa07':579,'sale':551,'receipt':548,'collar':560}
def scrim(h): return f'<div style="position:absolute;left:0;top:0;width:1080px;height:{h}px;background:linear-gradient(180deg,#5A2FA0 0%,#5A2FA0 62%,rgba(90,47,160,0) 100%);z-index:2"></div>'
def pair(a,b): return f'{a} <span style="opacity:.8">→</span> <span class="hl">{b}</span>'
LB=ds.label('Falso amigo')
def slide(n,img,th,body,face,sc=''):
    return (n,img,th,sc,body,face)
S=[slide(1,'fa1_sh.png',DARK,ds.zone(LB,ds.title('Black Friday em inglês tem <span class="hl">pegadinha</span>'),ds.sub('4 palavras que parecem português, mas não são'))+ds.nav(),'fa1'),
slide(2,'fa07_sh.png',LIGHT,ds.zone(LB,ds.title(pair('PUSH','EMPURRAR')),ds.card('Na porta da loja, é pra empurrar','Pra puxar, a palavra é pull'))+ds.nav(),'fa07'),
slide(3,'fa_sale_sh.png',DARK,ds.zone(LB,ds.title(pair('SALE','LIQUIDAÇÃO')),ds.card('Na vitrine, quer dizer promoção','Não tem nada a ver com sala'))+ds.nav(),'sale'),
slide(4,'fa_receipt_sh.png',DARK,ds.zone(LB,ds.title(pair('RECEIPT','NOTA')),ds.card('É a nota, o comprovante da compra','Receita de bolo, em inglês, é recipe'))+ds.nav(),'receipt'),
slide(5,'fa_collar_sh.png',DARK,ds.zone(LB,ds.title(pair('COLLAR','GOLA')),ds.card('É a gola de camisa ou a coleira','Colar de enfeite é necklace'))+ds.nav(),'collar',scrim(520)),
slide(6,'fa1_sh.png',DARK,ds.zone(LB,ds.punch('Bora de novo?'),ds.cta('Manda pro amigo que vai <b>às compras</b> lá fora')),'fa1',scrim(470))]
for n,img,th,sc,body,face in S:
    html=ds.doc(th,None,f'<img class="bg" src="file://{G}{img}">'+sc+body)
    k=f'falso-blackfriday-{n}'
    open(H+k+'.html','w').write(html)
    r=subprocess.run(['node',H+'render_a.mjs',H+k+'.html',O+k+'.jpg','1080','1350'],capture_output=True,text=True)
    z=json.loads(r.stdout.strip().splitlines()[-1])['zone'] if r.stdout.strip() else None
    print(n,'zona',z,'folga p/ rosto',(FACE[face]-z[3]) if z else None,r.stderr[:100])
