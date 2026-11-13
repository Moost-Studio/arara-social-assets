import numpy as np
from PIL import Image
S=0.8; YS_SRC=900
src=Image.open('../recortes/C01.png').convert('RGBA')
W0,H0=src.size
im=src.resize((round(W0*S),round(H0*S)),Image.LANCZOS)
A=np.asarray(im).astype(float); H,W,_=A.shape
ys=round(YS_SRC*S)
al=A[...,3]
# centro e meia largura da cauda por linha
xc=np.zeros(H); hw=np.zeros(H)
for y in range(ys-6,H):
    cols=np.where(al[y]>60)[0]
    if len(cols): xc[y]=(cols.min()+cols.max())/2; hw[y]=(cols.max()-cols.min())/2
    else: xc[y]=xc[y-1]; hw[y]=0
Ls=H-ys
print('cauda: raiz y',ys,'x',xc[ys],'largura',2*hw[ys],'comprimento',Ls)
DX,DY,CY=430,120,200
R=np.array([xc[ys],float(ys)]); E=R+np.array([DX,DY]); C=R+np.array([0,CY])
t=np.linspace(0,1,1200)[:,None]
P=(1-t)**2*R+2*(1-t)*t*C+t**2*E
T=np.gradient(P,axis=0); T/=np.linalg.norm(T,axis=1,keepdims=True)
N=np.stack([-T[:,1],T[:,0]],1)   # normal: para a direita do sentido do percurso
seg=np.linalg.norm(np.diff(P,axis=0),axis=1); s=np.concatenate([[0],np.cumsum(seg)]); Lc=s[-1]
print('arco',Lc,'estica',Lc/Ls)
# regiao de saida
x0,x1=int(R[0]-90),int(E[0]+110); y0,y1=int(ys-12),int(P[:,1].max()+110)
gx,gy=np.meshgrid(np.arange(x0,x1),np.arange(y0,y1)); pts=np.stack([gx.ravel(),gy.ravel()],1).astype(float)
out=np.zeros((len(pts),4))
def bil(Ay,Ax):
    x=np.clip(Ax,0,W-1.001); y=np.clip(Ay,0,H-1.001); xi=x.astype(int); yi=y.astype(int); fx=(x-xi)[:,None]; fy=(y-yi)[:,None]
    a=A[yi,xi]*(1-fx)*(1-fy)+A[yi,xi+1]*fx*(1-fy)+A[yi+1,xi]*(1-fx)*fy+A[yi+1,xi+1]*fx*fy
    return a
for i in range(0,len(pts),15000):
    p=pts[i:i+15000]
    d2=((p[:,None,:]-P[None,:,:])**2).sum(2); k=d2.argmin(1)
    rel=p-P[k]; v=(rel*N[k]).sum(1); along=(rel*T[k]).sum(1)
    sk=s[k]
    ok=~((k==0)&(along<-7))&~((k==len(P)-1)&(along>1))
    u=sk/Lc; kw=1+0.3*u
    ysrc=ys+u*Ls+np.where(k==0,np.minimum(along,0),0); xsrc=xc[np.clip(ysrc.astype(int),0,H-1)]+v/kw
    inb=ok&(ysrc<H-1)&(xsrc>=0)&(xsrc<W-1)
    res=np.zeros((len(p),4))
    if inb.any(): res[inb]=bil(ysrc[inb],xsrc[inb])
    out[i:i+15000]=res
tail=out.reshape(y1-y0,x1-x0,4)
# canvas final: corpo (sem a cauda) + cauda curva
CW=x1+10; CH=y1+10
can=np.zeros((CH,CW,4)); body=A.copy(); body[ys-3:,:,3]=0
can[:H,:W]=body
# composita cauda por cima (alfa normal)
reg=can[y0:y1,x0:x1]; a=tail[...,3:4]/255; ra=reg[...,3:4]/255
oa=a+ra*(1-a); rgb=(tail[...,:3]*a+reg[...,:3]*ra*(1-a))/np.maximum(oa,1e-6)
can[y0:y1,x0:x1]=np.concatenate([rgb,oa*255],2)
res=Image.fromarray(np.clip(can,0,255).astype('uint8'),'RGBA')
bb=res.getbbox(); res=res.crop(bb); print('bbox',bb,res.size,'raiz relativa',R[0]-bb[0],R[1]-bb[1],'corpo centro x',(W/2)-bb[0])
res.save('../recortes/C01_cauda_curva.png')
bg=Image.new('RGBA',res.size,(8,18,38,255)); bg.alpha_composite(res); bg.convert('RGB').save('../recortes/_previa_cauda.png')
