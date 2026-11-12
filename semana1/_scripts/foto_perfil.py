#!/usr/bin/env python3
"""Foto de perfil do @falearara: selo oficial da Rara sobre Azul-Noite, tudo dentro do círculo do Instagram (1080x1080)."""
import numpy as np, pathlib
from PIL import Image, ImageDraw
BASE = pathlib.Path(__file__).resolve().parents[2]
N = 1080
selo = Image.open(BASE / 'logotipo/selo/png/arara_selo_transparente_1024.png').convert('RGBA')
a = np.asarray(selo)[..., 3]
ys, xs = np.where(a > 20)
x0, y0, x1, y1 = xs.min(), ys.min(), xs.max() + 1, ys.max() + 1
selo = selo.crop((x0, y0, x1, y1)); a = np.asarray(selo)[..., 3]
h, w = a.shape
# menor círculo que envolve o selo inteiro (inclui o rabinho), para ocupar o máximo do círculo do Instagram
yy, xx = np.nonzero(a > 20)
pts = np.stack([xx, yy], 1).astype(float)[:: max(1, len(xx) // 6000)]
c = pts.mean(0)
for i in range(1500):
    far = pts[np.argmax(((pts - c) ** 2).sum(1))]
    c = c + (far - c) / (i + 2)
R = 478
dist = np.sqrt(((pts - c) ** 2).sum(1)).max()
s = R / dist
selo = selo.resize((int(w * s), int(h * s)), Image.LANCZOS)
# fundo Azul-Noite com brilho suave no centro
yy2, xx2 = np.mgrid[0:N, 0:N]
d = np.sqrt((xx2 - N / 2) ** 2 + (yy2 - N / 2) ** 2) / (N * 0.7)
k = np.clip(1 - d, 0, 1)[..., None] * 0.16
base = np.zeros((N, N, 3)) + (8, 18, 38)
img = Image.fromarray((base * (1 - k) + np.array([36, 87, 230]) * k).clip(0, 255).astype('uint8')).convert('RGBA')
img.alpha_composite(selo, (int(N / 2 - c[0] * s), int(N / 2 - c[1] * s)))
out = BASE / 'perfil' / 'foto_perfil_1080.png'
img.convert('RGB').save(out)
# prévia circular
m = Image.new('L', (N, N), 0); ImageDraw.Draw(m).ellipse([0, 0, N - 1, N - 1], fill=255)
pv = Image.new('RGB', (N, N), (240, 240, 240)); pv.paste(img.convert('RGB'), (0, 0), m)
pv.resize((540, 540), Image.LANCZOS).save(BASE / 'perfil' / '_previa_circulo.png')
print(out, selo.size)
