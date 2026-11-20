import numpy as np
from PIL import Image, ImageFilter, ImageDraw
D='/home/rodrigo/.openclaw/workspace/arara_social/semana_23_29_feed/gen/'
cfg={'st216':('ter_story216.jpg',[(309,1208),(464,1202)]),'st218':('ter_story218_v2.jpg',[(309,1193),(470,1168)])}
S=0.92
for k,(f,feet) in cfg.items():
    im=Image.open(D+f).convert('RGB'); W,H=im.size
    sh=Image.new('L',(W,H),0); d=ImageDraw.Draw(sh)
    for (x,y) in feet: d.ellipse((x-72,y-3,x+72,y+16),fill=150)
    sh=sh.filter(ImageFilter.GaussianBlur(4))
    a=np.array(im).astype(float); m=np.array(sh).astype(float)/255*0.6
    im=Image.fromarray((a*(1-m[...,None])+np.array([35,18,10])*m[...,None]).astype(np.uint8))
    w=int(1080*S); h=int(w*H/W)
    if h<1920*S: h=int(1920*S)
    sm=im.resize((w,int(w*H/W)),Image.LANCZOS); h=sm.size[1]
    x0=(1080-w)//2; y0=1920-h
    cv=Image.new('RGB',(1080,1920))
    cv.paste(sm,(x0,y0))
    top=sm.crop((0,0,w,y0+6)).transpose(Image.FLIP_TOP_BOTTOM); cv.paste(top,(x0,0))
    for side in (0,1):
        col=cv.crop((x0 if side==0 else x0+w-1,0,(x0+1) if side==0 else x0+w,1920))
        strip=col.resize((x0,1920)).filter(ImageFilter.GaussianBlur(10))
        cv.paste(strip,(0 if side==0 else x0+w,0))
    cv.save(D+k+'_base.jpg',quality=95); print(k,x0,y0,w,h)
