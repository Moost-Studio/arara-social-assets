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
    w=int(1080*S); sm=im.resize((w,int(w*H/W)),Image.LANCZOS); h=sm.size[1]
    x0=(1080-w)//2; y0=1920-h
    # fundo desfocado (cover) + imagem nitida com borda suave
    sc=max(1080/W,1920/H); bgim=im.resize((int(W*sc)+2,int(H*sc)+2),Image.LANCZOS)
    bgim=bgim.crop(((bgim.size[0]-1080)//2,(bgim.size[1]-1920)//2,(bgim.size[0]-1080)//2+1080,(bgim.size[1]-1920)//2+1920)).filter(ImageFilter.GaussianBlur(16))
    cv=bgim.copy()
    m=Image.new('L',(w,h),255); md=ImageDraw.Draw(m); F=26
    for i in range(F):
        v=int(255*i/F); md.rectangle((i,0,i,h),fill=v) ; md.rectangle((w-1-i,0,w-1-i,h),fill=v)
    # topo
    for i in range(F):
        v=int(255*i/F)
        for x in range(w):
            if m.getpixel((x,i))>v: m.putpixel((x,i),v)
    cv.paste(sm,(x0,y0),m)
    cv.save(D+k+'_base.jpg',quality=95); print(k,x0,y0,w,h)
