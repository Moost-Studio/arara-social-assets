"""Rabo da Rara NASCENDO POR TRÁS do corpo, passando atrás dos pés e saindo para o lado (os pés ficam livres na frente, não apoiados no rabo).
Uso: /tmp/camenv/bin/python bend_tail_behind.py <recorte.png> <saida.png> <d|e> [dxr=0.9 dyr=0.5 cxr=0.55 cyr=0.0]
Passos: acha a barriga e as garras; separa o rabo por cor (faixa central); apaga o rabo que aparecia entre os pés; refaz o rabo (Bézier, raiz atrás
da barriga) e o desenha ATRÁS do corpo."""
import sys, os
import numpy as np
from PIL import Image
from scipy import ndimage as ndi
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bend_tail_gen import bend_core

def hsv(A):
    rgb = A[..., :3] / 255; mx, mn = rgb.max(2), rgb.min(2); d = mx - mn + 1e-9; r, g, b = rgb[..., 0], rgb[..., 1], rgb[..., 2]
    h = np.where(mx == r, ((g - b) / d) % 6, np.where(mx == g, (b - r) / d + 2, (r - g) / d + 4)) * 60
    return h, d / (mx + 1e-9), mx

def separar(A):
    H, W, _ = A.shape; al = A[..., 3] / 255; h, s, v = hsv(A)
    ys_, xs_ = np.mgrid[0:H, 0:W]
    amarelo = (al > .8) & (h > 35) & (h < 65) & (s > .55) & (v > .6)
    faixa = (ys_ > H * .42) & (ys_ < H * .62); xc = float(xs_[amarelo & faixa].mean())
    larg = [(y, int(amarelo[y, int(xc) - 95:int(xc) + 95].sum())) for y in range(int(H * .45), int(H * .85))]
    yb = max(y for y, n in larg if n >= 90)                      # última linha com barriga larga
    escuro = (al > .8) & (v * 255 < 75)
    lin = [y for y in range(int(H * .55), int(H * .80)) if escuro[y].sum() >= 6]; yc = max(lin)   # fundo das garras
    baixo = (al > .3) & (h >= 62) & (h <= 235) & (s > .30) & (v > .25) & (ys_ >= yc + 20) & (ys_ <= yc + 120) & (np.abs(xs_ - xc) < 160)
    xt = float(xs_[baixo].mean()) if baixo.any() else xc
    cen = xc + (xt - xc) * np.clip((ys_ - yb) / max(yc + 40 - yb, 1), 0, 1)
    banda = np.abs(xs_ - cen) <= np.where(ys_ <= yc, 82, 120)
    cor = (al > .3) & (h >= 62) & (h <= 235) & (s > .30) & (v > .25) & banda & (ys_ >= yb + 4)
    lab, k = ndi.label(cor); assert k, 'rabo não encontrado'
    tam = ndi.sum(cor, lab, range(1, k + 1)); cor = np.isin(lab, [i + 1 for i in range(k) if tam[i] > 0.04 * tam.max()])
    return xc, yb, yc, cor, cen

def refaz(src, lado, dxr=0.75, dyr=0.8, cxr=0.25, cyr=0.3, verbose=True, sq=1.0, sombra=False):
    im = Image.open(src).convert('RGBA'); A = np.asarray(im).astype(float); H, W, _ = A.shape
    xc, yb, yc, cor, cen = separar(A)
    ys_, xs_ = np.mgrid[0:H, 0:W]
    # rabo-fonte: só o rabo; buracos (escondidos pelas garras) preenchidos com a cor do rabo mais próxima
    ys0 = yb + 4
    banda = (np.abs(xs_ - cen) <= np.where(ys_ <= yc, 82, 120)) & (ys_ >= ys0)
    # contorno do rabo por linha, interpolado nas linhas das garras
    ext = ndi.binary_closing(cor, structure=np.ones((9, 9)), iterations=2) | cor
    ext = ndi.binary_fill_holes(ext) & banda
    iy, ix = ndi.distance_transform_edt(~cor, return_distances=False, return_indices=True)
    T = np.zeros_like(A); T[ext, :3] = A[iy[ext], ix[ext], :3]
    soft = ndi.gaussian_filter(ext.astype(float), 0.8); T[..., 3] = np.where(ext, 255 * np.clip(soft * 1.4, 0, 1), 0)
    low = (ys_ > yc + 6) & (np.abs(xs_ - cen) <= 135) & (A[..., 3] > 0)
    T[low] = A[low]; T[(ys_ > yc + 6) & ~low] = 0
    # raiz escondida: estende o rabo 45 px para cima (fica atrás da barriga) repetindo a primeira linha visível
    EXT = int(os.environ.get("EXT_RAIZ", 45)); topo = ys0 + 2
    for k in range(1, EXT + 1): T[ys0 - k] = T[topo]
    ys_root = ys0 - EXT
    # corpo sem o rabo (inclui o rabo que aparecia entre os pés)
    B = A.copy(); hh, ss, vv = hsv(A); alp = A[..., 3] / 255
    amplo = (alp > .03) & (hh >= 62) & (hh <= 235) & (ss > .22) & (vv > .18) & (ys_ >= yb + 4) & (np.abs(xs_ - cen) <= 135)
    rem = (ndi.binary_dilation(cor, iterations=2) & banda) | (ndi.binary_dilation(amplo, iterations=1) & (ys_ >= yc - 2))
    rem &= ~((ys_ <= yc) & (np.abs(xs_ - cen) > 78) & ~cor)
    rem |= (ys_ > yc + 6)
    rem |= ndi.binary_dilation(amplo, iterations=1) & (ys_ >= yb + 20) & (ys_ <= yc + 6)
    rem &= (A[..., 3] > 0); B[rem, 3] = 0
    # remove o contorno azulado deixado nas pernas pela antialias
    can, ox = bend_core(T, ys_root, lado, dxr, dyr, cyr, verbose=verbose, cxr=cxr, sq=sq)
    CH, CW = max(can.shape[0], H), max(can.shape[1], W + ox)
    out = np.zeros((CH, CW, 4)); out[:can.shape[0], :can.shape[1]] = can          # rabo (atrás)
    Bc = np.zeros((CH, CW, 4)); Bc[:H, ox:ox + W] = B                              # corpo (na frente)
    if sombra:   # sombra de contato projetada: faixa escura colada na base dos pés e do rabo (luz do alto à esquerda: desloca 6 px à direita)
        yy = np.arange(CH)[:, None]; sh = np.zeros((CH, CW))
        pes = (Bc[..., 3] > 128); pes[: yb + 12] = False
        vis = (out[..., 3] > 128) & (Bc[..., 3] < 128)
        for mask, forca in ((pes, 1.0), (vis, 0.8)):
            tem = mask.any(0); low = np.where(tem, CH - 1 - np.argmax(mask[::-1], axis=0), 0)
            for x in np.where(tem)[0]: sh[:, x] = np.maximum(sh[:, x], forca * np.exp(-((np.arange(CH) - (low[x] + 2)) / 5.5) ** 2) * (np.arange(CH) >= low[x] - 4))
        sh = ndi.gaussian_filter(sh, 1.6); sh = np.roll(sh, 6, axis=1) * 0.62 + ndi.gaussian_filter(np.roll(sh, 6, axis=1), 9) * 0.35
        base = np.zeros((CH, CW, 4)); base[..., :3] = (55, 16, 6); base[..., 3] = np.clip(sh, 0, 1) * 255
        o2 = out.copy(); a2 = out[..., 3:4] / 255; b2 = base[..., 3:4] / 255; oa2 = a2 + b2 * (1 - a2)
        o2[..., :3] = (out[..., :3] * a2 + base[..., :3] * b2 * (1 - a2)) / np.maximum(oa2, 1e-6); o2[..., 3:4] = oa2 * 255; out = o2
    a = Bc[..., 3:4] / 255; ra = out[..., 3:4] / 255; oa = a + ra * (1 - a)
    rgb = (Bc[..., :3] * a + out[..., :3] * ra * (1 - a)) / np.maximum(oa, 1e-6)
    if os.environ.get('SO_CORPO'): Image.fromarray(np.clip(Bc, 0, 255).astype('uint8'), 'RGBA').save(os.environ['SO_CORPO'])
    res = Image.fromarray(np.clip(np.concatenate([rgb, oa * 255], 2), 0, 255).astype('uint8'), 'RGBA'); bb = res.getbbox()
    res = res.crop((0, 0, max(bb[2], ox + W), bb[3]))
    if verbose: print(f'{os.path.basename(src)}: centro x={xc:.0f}, barriga até y={yb}, garras até y={yc}, rabo-fonte={int(cor.sum())}px, ox={ox}')
    return res, ox

if __name__ == '__main__':
    src, dst, lado = sys.argv[1:4]
    args = [a for a in sys.argv[4:] if not a.startswith('--')]; par = [float(v) for v in args[:5]]; kw = dict(zip(['dxr', 'dyr', 'cxr', 'cyr', 'sq'], par))
    kw['sombra'] = '--sombra' in sys.argv
    res, ox = refaz(src, lado, **kw); res.save(dst); print('saída', dst, res.size, '| corpo começa em x =', ox)
