"""Apoia a Rara no chão em imagem de cena com fundo liso/degradê: extrai a Rara (diferença para o fundo), reconstrói o fundo por difusão em baixa resolução,
desce a Rara `dy` pixels e desenha uma sombra de contato sob os pés.
Uso: /tmp/camenv/bin/python ground_scene.py <entrada> <saida> <dy> <y_pes> <x_centro_pes> [y_barriga]
y_pes = linha do fundo dos pés na imagem de entrada; x_centro_pes = centro dos pés (para a sombra)."""
import sys
import numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage as ndi
src, dst = sys.argv[1], sys.argv[2]; dy, yp, xp = int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
im = Image.open(src).convert('RGB'); F = np.asarray(im).astype(float); H, W, _ = F.shape
L = F[:, :12].mean(1); Rr = F[:, -12:].mean(1); t = (np.arange(W) / (W - 1))[None, :, None]
bg0 = L[:, None, :] * (1 - t) + Rr[:, None, :] * t
d = np.abs(F - bg0).mean(2)
m = ndi.binary_opening(d > 30, iterations=2); m[yp + 22:, :] = False   # abaixo dos pés só há sombra antiga: não é a Rara
lab, k = ndi.label(m); tam = ndi.sum(m, lab, range(1, k + 1))
m = np.isin(lab, [i + 1 for i in range(k) if tam[i] > 3000]); m = ndi.binary_fill_holes(ndi.binary_closing(m, iterations=3))
soft = ndi.gaussian_filter(m.astype(float), 0.9)
# fundo sem a Rara: difusão em 1/4 de resolução (fundo é liso), recolocada só onde havia Rara
S = 4; sm = np.asarray(im.resize((W // S, H // S), Image.BILINEAR)).astype(float); mk = ndi.binary_dilation(np.asarray(Image.fromarray((m * 255).astype('uint8')).resize((W // S, H // S))) > 0, iterations=3)
idx = ndi.distance_transform_edt(mk, return_distances=False, return_indices=True); bg = sm[idx[0], idx[1]]; kern = np.array([[0, .25, 0], [.25, 0, .25], [0, .25, 0]])
for _ in range(600):
    nb = np.stack([ndi.convolve(bg[..., c], kern, mode='nearest') for c in range(3)], -1); bg[mk] = nb[mk]
bg = np.asarray(Image.fromarray(np.clip(bg, 0, 255).astype('uint8')).resize((W, H), Image.BICUBIC)).astype(float)
area = ndi.gaussian_filter(ndi.binary_dilation(m, iterations=6).astype(float), 3)[..., None]
base = F * (1 - area) + bg * area
# suaviza o chão abaixo dos pés (apaga bordas de remendos antigos)
y0 = yp + dy + 14; zone = np.zeros((H, W)); zone[y0:, :] = 1; zone = ndi.gaussian_filter(zone, 6)[..., None]
blur = np.stack([ndi.gaussian_filter(base[..., c], 18) for c in range(3)], -1); base = base * (1 - zone) + blur * zone
# sombra de contato projetada: faixa escura colada na base dos pés e do rabo (luz do alto à esquerda: 6 px à direita)
yb_ = int(sys.argv[6]) if len(sys.argv) > 6 else yp - 50
sh = np.zeros((H, W)); ar = np.arange(H)
for x in range(W):
    col = m[:, x]
    if not col.any(): continue
    low = H - 1 - np.argmax(col[::-1])
    foot = abs(x - xp) <= 170 and low >= yp - 10
    tail = abs(x - xp) > 165 and low >= yb_ - 20 and col[yb_ - 20: yp + 30].any()
    if foot or tail:
        sh[:, x] = (1.0 if foot else 0.8) * np.exp(-((ar - (low + 2)) / 6.0) ** 2) * (ar >= low - 4)
sh = ndi.gaussian_filter(sh, 3.0); sh = np.roll(sh, 7, axis=1) * 0.65 + ndi.gaussian_filter(np.roll(sh, 7, axis=1), 10) * 0.40
sh = np.pad(sh, ((dy, 0), (0, 0)))[:H][..., None]
k = np.clip(sh * 1.9, 0, 0.82); base = base * (1 - k) + np.array([70, 20, 26]) * k
# Rara deslocada para baixo (dy)
sa = np.zeros((H, W, 1)); sa[dy:, :, 0] = soft[: H - dy]; sf = np.zeros_like(F); sf[dy:] = F[: H - dy]
out = sf * sa + base * (1 - sa)
Image.fromarray(np.clip(out, 0, 255).astype('uint8')).save(dst); print('ok', dst, '| Rara descida', dy, 'px; pés em y =', yp + dy)
