import subprocess, json, os, sys, numpy as np
from PIL import Image, ImageFilter
import ds
G='/home/rodrigo/.openclaw/workspace/arara_social/semana_23_29_feed/gen/'
H='/home/rodrigo/.openclaw/workspace/arara_social/semana_23_29_feed/html/'
O='/home/rodrigo/.openclaw/workspace/arara_social/semana_23_29_feed/final/'
K=0.84
def bg(src,out):
    im=Image.open(src).convert('RGB'); w,h=int(1080*K),int(1350*K); im=im.resize((w,h),Image.LANCZOS)
    L=(1080-w)//2; T=1350-h
    arr=np.array(im); a=np.pad(arr,((0,0),(L,1080-w-L),(0,0)),mode='reflect'); a=np.pad(a,((T,0),(0,0),(0,0)),mode='edge')
    base=Image.fromarray(a).filter(ImageFilter.GaussianBlur(24))
    m=np.zeros((1350,1080),np.float32); m[T:,L:L+w]=1
    mk=Image.fromarray((m*255).astype('uint8')).filter(ImageFilter.GaussianBlur(14))
    comp=Image.composite(Image.fromarray(a),base,mk); comp.save(out,quality=95)
def crest(path):
    a=np.array(Image.open(path).convert('RGB')).astype(int)
    m=(a[...,2]>170)&(a[...,0]<70)&(a[...,1]<140)
    ys,xs=np.where(m[:900]); y=ys.min(); x=int(np.median(xs[ys<y+8])); return x,y
TH=dict(ink='#4A2410',acc='#FFC83D',hl='#FFB066',under='#F0C7A0',ctaacc='#C2410C')
src={1:'t1.jpg',2:'t2.jpg',3:sys.argv[1] if len(sys.argv)>1 else 't3.jpg',4:'t4.jpg',5:'t5.jpg',6:'t1.jpg'}
paths={}
for n,s in src.items():
    p=G+f'thx2/bg_{n}.jpg'; bg(G+'thx2/'+s,p); paths[n]=p
LB=ds.label('Rara pelo mundo')
def frase(n,uso,en,pt):
    x,y=crest(paths[n])
    return ds.zone(LB,ds.status(uso))+ds.fala(en,pt,idx=n,hx=x,cy=y,top_min=150)+ds.nav()
S=[(1,ds.zone(LB,ds.title('Fui convidada pro <span class="hl">Thanksgiving</span>'),ds.sub('O Dia de Ação de Graças nos Estados Unidos. Separei 4 frases pra ninguém ficar em silêncio na mesa'))+ds.nav()),
(2,frase(2,'Quando você chega','Thanks for having me!','Obrigada por me receber')),
(3,frase(3,'Pra pedir comida','Could you pass the potatoes, please?','Você me passa as batatas, por favor?')),
(4,frase(4,'A pergunta clássica do jantar','What are you thankful for this year?','Pelo que você é grato este ano?')),
(5,frase(5,'Quando você já comeu demais','I’m stuffed!','Não cabe mais nada')),
(6,ds.zone(LB,ds.title('<span class="hl">Salva</span> pra quando te convidarem'),ds.sub('O Thanksgiving é sempre na quarta quinta-feira de novembro, então dá tempo de treinar')))]
for n,body in S:
    k=f'thanksgiving-{n}'
    open(H+k+'.html','w').write(ds.doc(TH,paths[n],body))
    r=subprocess.run(['node',H+'render_a.mjs',H+k+'.html',O+k+'.jpg','1080','1350'],capture_output=True,text=True)
    print(n,r.stdout.strip()[-200:],r.stderr[:100])
