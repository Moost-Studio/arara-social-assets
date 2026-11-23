"""Rabo por trás dos pés em IMAGEM DE CENA com fundo liso/degradê (fundo estimado linha a linha entre as bordas da faixa).
Uso: /tmp/camenv/bin/python bend_tail_scene_behind.py <entrada> <saida> <d|e> <y_barriga> <y_garras> <x0> <x1> [dxr=0.75 dyr=0.8 cxr=0.25 cyr=0.3]
y_barriga = fim da barriga (acima das pernas); y_garras = fim das garras; x0..x1 = faixa que contém pés e rabo."""
import sys, os
import numpy as np
from PIL import Image
from scipy import ndimage as ndi
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bend_tail_gen import bend_core
src, dst, lado = sys.argv[1:4]; yb, yc, X0, X1 = (int(v) for v in sys.argv[4:8])
dxr, dyr, cxr, cyr = (float(v) for v in sys.argv[8:12]) if len(sys.argv) >= 12 else (0.75, 0.8, 0.25, 0.3)
sq = float(sys.argv[12]) if len(sys.argv) >= 13 else 1.0   # espessura do rabo (0.8 = deitado no chão)
F = np.asarray(Image.open(src).convert('RGB')).astype(float); H, W, _ = F.shape
Y0 = yb - 150; roi = F[Y0:H, X0:X1].copy(); h, w, _ = roi.shape; yy_b, yy_c = yb - Y0, yc - Y0
rgb = roi / 255; mx, mn = rgb.max(2), rgb.min(2); d = mx - mn + 1e-9; r, g, b = rgb[..., 0], rgb[..., 1], rgb[..., 2]
hue = np.where(mx == r, ((g - b) / d) % 6, np.where(mx == g, (b - r) / d + 2, (r - g) / d + 4)) * 60; sat = d / (mx + 1e-9)
ys_, xs_ = np.mgrid[0:h, 0:w]
# fundo estimado por linha: interpolação entre as bordas esquerda e direita da faixa
L = roi[:, :10].mean(1); Rr = roi[:, -10:].mean(1); t = (xs_ / (w - 1))[..., None]; bg = L[:, None, :] * (1 - t) + Rr[:, None, :] * t
cor = (hue >= 62) & (hue <= 255) & (sat > 0.22) & (mx > 0.2) & (ys_ >= yy_b + 4)
amarelo = (hue > 33) & (hue < 62) & (sat > 0.5) & (mx > 0.6) & (ys_ >= yy_b + 4)
bico = ndi.binary_dilation(amarelo, iterations=9) & (mx < 0.42) & (hue > 190)   # garras: escuras coladas nos dedos
cor &= ~bico
lab, k = ndi.label(cor); tam = ndi.sum(cor, lab, range(1, k + 1)); comp = lab == (np.argmax(tam) + 1)
comp = ndi.binary_fill_holes(ndi.binary_closing(comp, iterations=3))
body = (np.abs(roi - bg).mean(2) > 24) & ~ndi.binary_dilation(comp, iterations=1) & (ys_ <= yy_c + 8)
body = ndi.binary_opening(body, iterations=1)
lb, kb = ndi.label(body); tb = ndi.sum(body, lb, range(1, kb + 1)); body = np.isin(lb, [i + 1 for i in range(kb) if tb[i] > 1500])   # só o corpo grande (barriga, pernas e pés); descarta restos soltos
# rabo-fonte (alfa suave) e extensão da raiz para trás da barriga
alpha = np.clip((sat - 0.18) / 0.22, 0, 1) * ((hue >= 62) & (hue <= 255)) * ndi.binary_dilation(comp, iterations=2)
alpha = np.maximum(alpha, ndi.binary_erosion(comp, iterations=2).astype(float)); alpha[: yy_b + 4] = 0
T = np.dstack([roi, alpha * 255]); ys0 = yy_b + 4; EXT = int(os.environ.get('EXT_RAIZ', 45))
iy, ix = ndi.distance_transform_edt(alpha < 0.5, return_distances=False, return_indices=True)
hole = (alpha < 0.5) & ndi.binary_closing(comp, structure=np.ones((9, 9)), iterations=2) & (ys_ >= ys0); T[hole, :3] = roi[iy[hole], ix[hole]]; T[hole, 3] = 255
for kk in range(1, EXT + 1): T[ys0 - kk] = T[ys0 + 2]
can, ox = bend_core(T, ys0 - EXT, lado, dxr, dyr, cyr, cxr=cxr, sq=sq)
# 1) fundo limpo: onde estava o rabo (e sua sombra) vira fundo estimado
fill = ndi.binary_dilation(comp, iterations=12); rows = np.where(comp.any(1))[0]; yb2 = rows.max()
cx_b = int(np.where(comp[max(yb2 - 10, 0)])[0].mean()) if comp[max(yb2 - 10, 0)].any() else w // 2
fill[max(yb2 - 40, 0): min(yb2 + 70, h), max(cx_b - 75, 0): cx_b + 75] = True; fill &= ~body; fill[: yy_b + 4] &= ndi.binary_dilation(comp, iterations=3)[: yy_b + 4]
unk = fill | ndi.binary_dilation(body, iterations=2); idx = ndi.distance_transform_edt(unk, return_distances=False, return_indices=True)
bgd = roi[idx[0], idx[1]]; kern = np.array([[0, .25, 0], [.25, 0, .25], [0, .25, 0]])
for _ in range(400):
    nb = np.stack([ndi.convolve(bgd[..., c], kern, mode='nearest') for c in range(3)], -1); bgd[unk] = nb[unk]
fs = ndi.gaussian_filter(fill.astype(float), 1.0)[..., None]; base = roi * (1 - fs) + bgd * fs
# 2) rabo novo por cima do fundo, 3) corpo (pés, pernas, barriga) por cima do rabo
ch, cw, _ = can.shape; px = -ox; stage = base.copy()
for y in range(ch):
    Y = y
    if Y >= h: break
    xs = np.arange(cw) + px; ok = (xs >= 0) & (xs < w); a = can[y, ok, 3:4] / 255
    stage[Y, xs[ok]] = can[y, ok, :3] * a + stage[Y, xs[ok]] * (1 - a)
bs = ndi.gaussian_filter(body.astype(float), 0.7)[..., None]; final = stage * (1 - bs) + roi * bs
out = F.copy(); out[Y0:H, X0:X1] = final
Image.fromarray(np.clip(out, 0, 255).astype('uint8')).save(dst); print('ok', dst)
