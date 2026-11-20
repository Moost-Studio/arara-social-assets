import sys, numpy as np
from PIL import Image, ImageFilter, ImageDraw
src,dst,x0,y0,x1,y1=sys.argv[1],sys.argv[2],*map(int,sys.argv[3:7])
im=Image.open(src).convert('RGB'); a=np.array(im).astype(float)
reg=a[y0:y1,x0:x1]
r,g,b=reg[...,0],reg[...,1],reg[...,2]
mx=reg.max(-1); mn=reg.min(-1); sat=(mx-mn)/(mx+1e-6)
# cinza arroxeado: b >= r-6, r,g baixos, sat baixa; exclui garras azul-marinho (muito escuras) e chão laranja
m=(b>=r-12)&(mx>48)&(mx<195)&(sat<0.45)&((b-r)<24)&((r-b)<14)
mm=Image.fromarray((m*255).astype(np.uint8)).filter(ImageFilter.MaxFilter(3)).filter(ImageFilter.GaussianBlur(1))
mk=np.array(mm).astype(float)/255
lum=np.clip((0.3*r+0.59*g+0.11*b)/110.0,0.45,1.15)
yel=np.stack([np.clip(255*lum,0,255),np.clip(205*lum,0,255),np.clip(55*lum,0,255)],-1)
reg2=reg*(1-mk[...,None])+yel*mk[...,None]
a[y0:y1,x0:x1]=reg2
im2=Image.fromarray(a.astype(np.uint8))
im2.save(dst,quality=95)
