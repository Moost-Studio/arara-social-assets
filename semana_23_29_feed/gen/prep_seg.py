import numpy as np
from PIL import Image, ImageFilter, ImageDraw
D='/home/rodrigo/.openclaw/workspace/arara_social/semana_23_29_feed/gen/'
# (arquivo, pés: lista de (x,y) centros dos dedos em coordenadas originais 928x1152)
cfg={'seg_s1':('seg_s1_v3f.jpg',[(420,1046),(520,1046)]),
     'seg_s2':('seg_s2.jpg',[(415,1038),(525,1038)]),
     'seg_s3':('seg_s3.jpg',[(412,1040),(525,1040)]),
     'seg_s4':('seg_s4.jpg',[(430,1040),(500,1048)]),
     'seg_s5':('seg_s5.jpg',[(415,1040),(525,1040)])}
S=0.98
for k,(f,feet) in cfg.items():
    im=Image.open(D+f).convert('RGB'); W,H=im.size
    # sombra de contato (multiplica) na imagem original antes de escalar
    sh=Image.new('L',(W,H),0); d=ImageDraw.Draw(sh)
    for (x,y) in feet: d.ellipse((x-70,y-4,x+70,y+16),fill=150)
    sh=sh.filter(ImageFilter.GaussianBlur(5))
    a=np.array(im).astype(float); m=np.array(sh).astype(float)/255*0.62
    a=a*(1-m[...,None])+np.array([35,18,10])*m[...,None]
    im=Image.fromarray(a.astype(np.uint8))
    # canvas 1080x1350: fundo desfocado + imagem escalada ancorada na base
    w=int(1080*S); h=int(w*H/W)
    sm=im.resize((w,h),Image.LANCZOS)
    x0=(1080-w)//2; y0=1350-h
    cv=Image.new('RGB',(1080,1350))
    cv.paste(sm,(x0,y0))
    # preenche as sobras por espelhamento (fundo desfocado, sem faixa visivel)
    L=sm.crop((0,0,x0+4,h)).transpose(Image.FLIP_LEFT_RIGHT); cv.paste(L,(0,y0))
    R=sm.crop((w-x0-4,0,w,h)).transpose(Image.FLIP_LEFT_RIGHT); cv.paste(R,(1080-x0-4,y0))
    T=cv.crop((0,y0,1080,y0+y0+4)).transpose(Image.FLIP_TOP_BOTTOM); cv.paste(T,(0,0))
    cv.paste(sm,(x0,y0)) if False else None
    bg=cv
    bg.save(D+k+'_base.jpg',quality=95)
    print(k,'x0',x0,'y0',y0,'w',w,'h',h)
