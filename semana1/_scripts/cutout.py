from PIL import Image
import numpy as np
def cutout(path, bg=(140,140,140), lo=14, hi=34):
    im=np.asarray(Image.open(path).convert('RGB')).astype(float)
    H,W,_=im.shape
    # fundo real: mediana das bordas
    edge=np.concatenate([im[0],im[-1],im[:,0],im[:,-1]]); bgc=np.median(edge,axis=0)
    dist=np.abs(im-bgc).max(axis=2)
    cand=dist<hi
    reach=np.zeros((H,W),bool)
    reach[0,:]|=cand[0,:]; reach[-1,:]|=cand[-1,:]; reach[:,0]|=cand[:,0]; reach[:,-1]|=cand[:,-1]
    while True:
        n=reach.copy()
        n[1:]|=reach[:-1]; n[:-1]|=reach[1:]; n[:,1:]|=reach[:,:-1]; n[:,:-1]|=reach[:,1:]
        n&=cand
        if (n==reach).all(): break
        reach=n
    a=np.ones((H,W))
    soft=np.clip((dist-lo)/(hi-lo),0,1)
    a[reach]=soft[reach]
    # descontaminar o cinza nas bordas semitransparentes
    out=im.copy(); m=(a<1)&(a>0.02)
    out[m]=np.clip((im[m]-(1-a[m,None])*bgc)/a[m,None],0,255)
    rgba=np.dstack([out,a*255]).astype('uint8')
    return Image.fromarray(rgba,'RGBA'), bgc
def bbox(img):
    a=np.asarray(img)[...,3]; ys,xs=np.where(a>20); return xs.min(),ys.min(),xs.max()+1,ys.max()+1

def cutout_pockets(path, minpix=120, tol=24, sat_max=14):
    """Como cutout(), mas também remove bolsões de cinza do fundo cercados pelo personagem."""
    import numpy as np
    from PIL import Image
    rgba,bgc=cutout(path)
    im=np.asarray(Image.open(path).convert('RGB')).astype(float)
    a=np.asarray(rgba)[...,3].astype(float)
    dist=np.abs(im-bgc).max(axis=2); sat=im.max(axis=2)-im.min(axis=2)
    cand=(a>200)&(dist<tol)&(sat<sat_max)
    H,W=cand.shape; seen=np.zeros((H,W),bool); out=np.zeros((H,W),bool)
    from collections import deque
    ys,xs=np.where(cand)
    for y0,x0 in zip(ys,xs):
        if seen[y0,x0]: continue
        q=deque([(y0,x0)]); seen[y0,x0]=True; pts=[]
        while q:
            y,x=q.popleft(); pts.append((y,x))
            for dy,dx in ((1,0),(-1,0),(0,1),(0,-1)):
                ny,nx=y+dy,x+dx
                if 0<=ny<H and 0<=nx<W and cand[ny,nx] and not seen[ny,nx]: seen[ny,nx]=True; q.append((ny,nx))
        if len(pts)>=minpix:
            for y,x in pts: out[y,x]=True
    # alarga 2 px para pegar a borda do bolsão
    for _ in range(2):
        n=out.copy(); n[1:]|=out[:-1]; n[:-1]|=out[1:]; n[:,1:]|=out[:,:-1]; n[:,:-1]|=out[:,1:]
        out=n&(dist<tol+14)
    arr=np.asarray(rgba).copy(); arr[...,3][out]=0
    return Image.fromarray(arr,'RGBA'),int(out.sum())
