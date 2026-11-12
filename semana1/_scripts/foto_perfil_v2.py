#!/usr/bin/env python3
"""Foto de perfil do @falearara, v2 (dinâmica): 3 opções 1080x1080 com a Rara recortada do acervo aprovado, contorno de adesivo, fundo com movimento.
Saída em ../../perfil/ (foto_perfil_v2_{A,B,C}_1080.png e prévia circular)."""
import sys, math, random, pathlib
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageChops
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from cutout import cutout, bbox
BASE = pathlib.Path(__file__).resolve().parents[2]
OUT = BASE / 'perfil'
N = 1080; C = N // 2
YEL, BLU, GRN, COR, NOITE, CREME, CEU = '#FFC83D', '#2457E6', '#22B573', '#FF6B57', '#081226', '#FFF5E1', '#DCEBFF'
def rgb(h): h = h.lstrip('#'); return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))

def radial(inner, outer, cx=C, cy=C, r=N * 0.75):
    yy, xx = np.mgrid[0:N, 0:N]
    d = np.clip(np.sqrt((xx - cx) ** 2 + (yy - cy) ** 2) / r, 0, 1)[..., None]
    a = np.array(rgb(inner)); b = np.array(rgb(outer))
    return Image.fromarray((a * (1 - d) + b * d).astype('uint8')).convert('RGBA')

def rays(img, color, n=18, alpha=46, rot=0, cx=C, cy=C):
    lay = Image.new('RGBA', (N, N), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    for i in range(n):
        a0 = math.radians(rot + i * 360 / n); a1 = math.radians(rot + (i + .5) * 360 / n)
        d.polygon([(cx, cy), (cx + 1600 * math.cos(a0), cy + 1600 * math.sin(a0)), (cx + 1600 * math.cos(a1), cy + 1600 * math.sin(a1))], fill=rgb(color) + (alpha,))
    img.alpha_composite(lay)

def star(d, x, y, r, fill):
    d.polygon([(x, y - r), (x + r * .22, y - r * .22), (x + r, y), (x + r * .22, y + r * .22), (x, y + r), (x - r * .22, y + r * .22), (x - r, y), (x - r * .22, y - r * .22)], fill=fill)

def confetti(img, seed, cols, count=34, rmin=330, rmax=500):
    random.seed(seed); lay = Image.new('RGBA', (N, N), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    for _ in range(count):
        a = random.uniform(0, 2 * math.pi); r = random.uniform(rmin, rmax)
        x, y = C + r * math.cos(a), C + r * math.sin(a); col = rgb(random.choice(cols)) + (235,); s = random.uniform(10, 24)
        k = random.random()
        if k < .4: d.ellipse([x - s, y - s, x + s, y + s], fill=col)
        elif k < .75:
            tmp = Image.new('RGBA', (int(s * 3), int(s * 3)), (0, 0, 0, 0)); ImageDraw.Draw(tmp).rounded_rectangle([s * .8, s * .2, s * 2.2, s * 2.8], radius=int(s * .4), fill=col)
            tmp = tmp.rotate(random.uniform(0, 180), expand=True); lay.alpha_composite(tmp, (int(x - tmp.width / 2), int(y - tmp.height / 2)))
        else: star(d, x, y, s * 1.5, col)
    img.alpha_composite(lay)

def sticker(arq, frac=.66, height=760, tilt=0, border=16, bcol='#FFFFFF'):
    rgba, _ = cutout(str(BASE / arq)); x0, y0, x1, y1 = bbox(rgba)
    ch = int((y1 - y0) * frac); crop = rgba.crop((x0, y0, x1, y0 + ch))
    s = min(height / ch, 940 / (x1 - x0)); crop = crop.resize((int((x1 - x0) * s), int(ch * s)), Image.LANCZOS)
    pad = border * 3 + 20; canvas = Image.new('RGBA', (crop.width + pad * 2, crop.height + pad * 2), (0, 0, 0, 0)); canvas.alpha_composite(crop, (pad, pad))
    al = canvas.getchannel('A'); size = border * 2 + 1
    halo = al.filter(ImageFilter.MaxFilter(size if size % 2 else size + 1)).filter(ImageFilter.GaussianBlur(1.2))
    ring = Image.new('RGBA', canvas.size, rgb(bcol) + (0,)); ring.putalpha(halo)
    out = Image.alpha_composite(ring, canvas)
    if tilt: out = out.rotate(tilt, resample=Image.BICUBIC, expand=True)
    return out

def put(img, st, cx, cy, shadow=70):
    a = st.getchannel('A'); sh = Image.new('RGBA', st.size, (0, 0, 0, 0)); sh.putalpha(a.point(lambda v: int(v * shadow / 255)))
    lay = Image.new('RGBA', (N, N), (0, 0, 0, 0)); lay.alpha_composite(sh.filter(ImageFilter.GaussianBlur(20)), (int(cx - st.width / 2), int(cy - st.height / 2 + 26)))
    img.alpha_composite(lay); img.alpha_composite(st, (int(cx - st.width / 2), int(cy - st.height / 2)))

def finish(img, nome):
    p = OUT / f'foto_perfil_v2_{nome}_1080.png'; img.convert('RGB').save(p)
    m = Image.new('L', (N, N), 0); ImageDraw.Draw(m).ellipse([0, 0, N - 1, N - 1], fill=255)
    pv = Image.new('RGB', (N, N), (238, 238, 238)); pv.paste(img.convert('RGB'), (0, 0), m); return pv.resize((420, 420), Image.LANCZOS)

def opt_A():  # noite, raios amarelos, Rara eufórica
    img = radial('#2A55D6', NOITE, r=N * .72); rays(img, '#6F95FF', 20, 70, rot=-8)
    glow = radial('#FFC83D', '#FFC83D', r=1).convert('RGBA'); gl = Image.new('RGBA', (N, N), (0, 0, 0, 0)); ImageDraw.Draw(gl).ellipse([C - 330, C - 200, C + 330, C + 460], fill=rgb(YEL) + (95,)); img.alpha_composite(gl.filter(ImageFilter.GaussianBlur(70)))
    d = ImageDraw.Draw(img); 
    for r, al in ((330, 40), (390, 28)): d.ellipse([C - r, C - r, C + r, C + r], outline=rgb(YEL) + (al * 3,), width=6)
    confetti(img, 7, [YEL, GRN, COR, '#FFFFFF'], 38, 360, 505)
    st = sticker('personagens/rara/expressoes/E02_euforia.png', .46, 980, tilt=-3); put(img, st, C, 175 + st.height / 2)
    fg = Image.new('RGBA', (N, N), (0, 0, 0, 0)); fd = ImageDraw.Draw(fg)
    fd.ellipse([C - 640, 800, C + 640, 1700], fill=rgb(NOITE) + (255,)); fd.ellipse([C - 640, 800, C + 640, 1700], outline=rgb(YEL) + (255,), width=14)
    for i in range(9): star(fd, 110 + i * 107, 900 + (i % 3) * 55, 12 + (i % 2) * 6, rgb(YEL if i % 2 else '#FFFFFF') + (235,))
    img.alpha_composite(fg)
    return finish(img, 'A')

def opt_B():  # amarelo-laranja, equalizador de voz, Rara acenando
    img = radial('#FFD76A', '#F7861F', r=N * .8)
    lay = Image.new('RGBA', (N, N), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    cols = [BLU, GRN, '#FFFFFF', COR, NOITE]; random.seed(3)
    for i in range(23):
        x = 40 + i * 44; h = 120 + 260 * abs(math.sin(i * .55 + .4)) + random.uniform(-30, 30)
        top = C + 120 - h * .5; d.rounded_rectangle([x, top, x + 26, top + h * .9], radius=13, fill=rgb(cols[i % len(cols)]) + (215,))
    img.alpha_composite(lay)
    confetti(img, 11, [BLU, '#FFFFFF', GRN], 22, 380, 510)
    st = sticker('personagens/rara/gestos/G06_aceno.png', .64, 900, tilt=5); put(img, st, C + 10, N + 120 - st.height / 2)
    return finish(img, 'B')

def opt_C():  # céu claro, ondas de voz a partir do bico, Rara falando
    img = radial('#FFFFFF', CEU, r=N * .7)
    lay = Image.new('RGBA', (N, N), (0, 0, 0, 0)); d = ImageDraw.Draw(lay); ox, oy = C + 150, C - 20
    for k, (r, col, w) in enumerate(((220, YEL, 26), (320, BLU, 22), (420, GRN, 20), (520, COR, 18), (620, YEL, 16))):
        d.arc([ox - r, oy - r, ox + r, oy + r], -60, 60, fill=rgb(col) + (235,), width=w)
    img.alpha_composite(lay)
    confetti(img, 21, [YEL, BLU, GRN, COR], 24, 400, 510)
    st = sticker('personagens/rara/expressoes/E01_alegria.png', .66, 900, tilt=-5); put(img, st, C - 60, N + 120 - st.height / 2, shadow=55)
    return finish(img, 'C')

if __name__ == '__main__':
    OUT.mkdir(exist_ok=True)
    pvs = [opt_A(), opt_B(), opt_C()]
    sh = Image.new('RGB', (420 * 3 + 40, 440), (30, 30, 36))
    for i, p in enumerate(pvs): sh.paste(p, (10 + i * 430, 10))
    sh.save(OUT / '_previa_v2.png'); print('ok')
