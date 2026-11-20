import sys, glob, colorsys, numpy as np
from PIL import Image, ImageFilter
G='/home/rodrigo/.openclaw/workspace/arara_social/semana_23_29_feed/gen/'
M='/home/rodrigo/.openclaw/media/tool-image-generation/'
def run(src,out,y0,x0=0,x1=10**6):
    im=Image.open(src).convert('RGB'); a=np.asarray(im).astype(float)/255
    mx=a.max(2); mn=a.min(2); d=mx-mn+1e-6
    r,g,b=a[...,0],a[...,1],a[...,2]
    h=np.where(mx==r,((g-b)/d)%6,np.where(mx==g,(b-r)/d+2,(r-g)/d+4))/6
    s=d/(mx+1e-6)
    yellow=(h>0.09)&(h<0.18)&(s>0.55)&(mx>0.55)
    claw=(h>0.58)&(h<0.72)&(s>0.3)&(mx<0.45)
    m=(yellow|claw); H,W=m.shape
    m[:y0,:]=False; m[:,:x0]=False; m[:,x1:]=False
    foot=Image.fromarray((m*255).astype('uint8')).filter(ImageFilter.MaxFilter(3))
    sh=Image.new('L',(W,H),0); sh.paste(foot.transform((W,H),Image.AFFINE,(1,0,-6,0,1,-8)),(0,0))
    sh=sh.filter(ImageFilter.GaussianBlur(5))
    sa=np.asarray(sh).astype(float)/255*0.62
    foota=np.asarray(foot.filter(ImageFilter.GaussianBlur(1))).astype(float)/255
    k=sa*(1-foota)
    dark=np.array([0.10,0.06,0.12])
    res=a*(1-k[...,None])+dark*k[...,None]
    Image.fromarray((res*255).astype('uint8')).save(out)
import glob
def f(n): return glob.glob(M+n+'---*.jpg')[0]
jobs=[(f('fb_thanks_s1'),'thanks1',1050),(f('fb_thanks_s2'),'thanks2',1050),(f('fb_thanks_s3b'),'thanks3',1050),(f('fb_thanks_s4'),'thanks4',1050),(f('fb_thanks_s5'),'thanks5',1050),
 (f('fb_fa_s1'),'fa1',1040),(G+'fa_sale_eyes.png','fa_sale',1040),(G+'fa_receipt_eyes.png','fa_receipt',1040),(f('fb_fa_collar'),'fa_collar',1030)]
for src,n,y0 in jobs: run(src,G+n+'_sh.png',y0)
print('ok')
