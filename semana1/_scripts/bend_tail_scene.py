"""Curva o rabo da Rara numa IMAGEM DE CENA (rabo reto sobre fundo liso ou suave): extrai o rabo pela cor, preenche o fundo onde ele estava
(difusão a partir dos pixels vizinhos) e redesenha o rabo curvo por cima.
Uso: /tmp/camenv/bin/python bend_tail_scene.py <entrada> <saida> <lado d|e> <y_garras> <x0> <x1> [dxr=0.95 dyr=0.8 cyr=0.5]
y_garras = linha onde terminam as garras (o rabo é refeito dali para baixo); x0..x1 = faixa horizontal onde está o rabo.
Limite: só funciona bem onde o fundo atrás do rabo é liso/gradiente; em cenas com objetos, confira o resultado ampliado."""
import sys, os
import numpy as np
from PIL import Image
from scipy import ndimage as ndi
sys.path.insert(0, os.path.dirname(__file__))
from bend_tail_gen import bend_core
src, dst, lado = sys.argv[1], sys.argv[2], sys.argv[3]
yc, X0, X1 = int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6])
dxr, dyr, cyr = (float(v) for v in sys.argv[7:10]) if len(sys.argv) >= 10 else (0.95, 0.8, 0.5)
satmin = float(sys.argv[10]) if len(sys.argv) >= 11 else 0.18   # cenas escuras: use ~0.10
im = Image.open(src).convert('RGB'); F = np.asarray(im).astype(float); H, W, _ = F.shape
ys = yc + 10; Y0 = ys - 40                                   # recorte do rabo: 40 px acima da raiz até a base
roi = F[Y0:H, X0:X1]; h, w, _ = roi.shape
rgb = roi / 255; mx, mn = rgb.max(2), rgb.min(2); d = mx - mn + 1e-9; r, g, b = rgb[..., 0], rgb[..., 1], rgb[..., 2]
hue = np.where(mx == r, ((g - b) / d) % 6, np.where(mx == g, (b - r) / d + 2, (r - g) / d + 4)) * 60; sat = d / (mx + 1e-9)
cor = (hue >= 70) & (hue <= 255)
alpha = np.clip((sat - satmin) / 0.22, 0, 1) * cor * (mx > (0.2 if satmin >= 0.18 else 0.10))
# só o componente ligado à raiz, e só da raiz para baixo
lab, k = ndi.label(alpha > 0.35); yy = ys - Y0
raiz = lab[yy + 6, :]; ids = np.unique(raiz[raiz > 0]); assert len(ids), 'não achei o rabo na faixa x0..x1 / y_garras'
comp = np.isin(lab, ids); comp[: yy - 3] = False
comp = ndi.binary_fill_holes(ndi.binary_closing(comp, iterations=3)); comp[: yy - 3] = False
alpha = np.maximum(alpha * ndi.binary_dilation(comp, iterations=2), ndi.binary_erosion(comp, iterations=2).astype(float))   # miolo opaco: sem buracos
alpha[: yy - 3] = 0
# 1) fundo sem o rabo: difusão a partir dos vizinhos conhecidos
fill = ndi.binary_dilation(alpha > 0.02, iterations=12)
# sombra do rabo no chão: apaga também uma faixa suave sob a ponta do rabo antigo (a sombra ficaria órfã)
rows = np.where(comp.any(1))[0]; yb = rows.max(); cx_b = int(np.where(comp[max(yb - 10, 0)])[0].mean()) if comp[max(yb - 10, 0)].any() else (X1 - X0) // 2
fill[max(yb - 40, 0): min(yb + 70, h), max(cx_b - 75, 0): cx_b + 75] = True
fill[: yy - 3] = False
known = ~fill; idx = ndi.distance_transform_edt(fill, return_distances=False, return_indices=True)
bgr = roi[idx[0], idx[1]]; kern = np.array([[0, .25, 0], [.25, 0, .25], [0, .25, 0]])
for _ in range(250):
    nb = np.stack([ndi.convolve(bgr[..., c], kern, mode='nearest') for c in range(3)], -1); bgr[fill] = nb[fill]
F2 = F.copy(); F2[Y0:H, X0:X1][fill] = bgr[fill]
# 2) rabo curvo
A = np.dstack([roi, alpha * 255]); can, ox = bend_core(A, yy, lado, dxr, dyr, cyr)
can[: yy - 3] = 0                                            # acima da raiz o rabo original já está na cena
ch, cw, _ = can.shape; px = X0 - ox; py = Y0
for y in range(ch):
    Y = py + y
    if Y < 0 or Y >= H: continue
    xs = np.arange(cw) + px; ok = (xs >= 0) & (xs < W)
    a = can[y, ok, 3:4] / 255; F2[Y, xs[ok]] = can[y, ok, :3] * a + F2[Y, xs[ok]] * (1 - a)
Image.fromarray(np.clip(F2, 0, 255).astype('uint8')).save(dst); print('ok', dst)
