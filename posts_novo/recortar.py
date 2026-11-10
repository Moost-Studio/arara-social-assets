#!/usr/bin/env python3
"""Recorta a mascote das ilustracoes de fundo liso azul-palido (stories_base) e remove brilhos soltos. Saida: cutouts/<nome>.png"""
import sys, pathlib
import numpy as np
from PIL import Image, ImageFilter
from collections import deque
SB = pathlib.Path(__file__).resolve().parent.parent / "stories_base"
OUT = pathlib.Path(__file__).resolve().parent / "cutouts"
def components(mask):
    h, w = mask.shape; lab = np.zeros((h, w), np.int32); sizes = [0]; cur = 0
    for y in range(h):
        for x in range(w):
            if mask[y, x] and not lab[y, x]:
                cur += 1; q = deque([(y, x)]); lab[y, x] = cur; n = 0
                while q:
                    cy, cx = q.popleft(); n += 1
                    for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        ny, nx = cy + dy, cx + dx
                        if 0 <= ny < h and 0 <= nx < w and mask[ny, nx] and not lab[ny, nx]:
                            lab[ny, nx] = cur; q.append((ny, nx))
                sizes.append(n)
    return lab, sizes
def cut(name):
    im = Image.open(SB / (name + ".png")).convert("RGB")
    im = im.crop((3, 0, im.width - 3, im.height - 10)).resize((1080, 1920), Image.LANCZOS)
    a = np.asarray(im).astype(np.float32) / 255
    mx, mn = a.max(2), a.min(2)
    s = np.where(mx > 0, (mx - mn) / np.maximum(mx, 1e-6), 0)
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    d = np.maximum(mx - mn, 1e-6)
    h = np.where(mx == r, ((g - b) / d) % 6, np.where(mx == g, (b - r) / d + 2, (r - g) / d + 4)) * 60
    bg_like = (h > 190) & (h < 238) & (s < 0.62) & (mx > 0.78)
    small = bg_like[::2, ::2]; reach = np.zeros_like(small)
    reach[0, :] = small[0, :]; reach[-1, :] = small[-1, :]; reach[:, 0] = small[:, 0]; reach[:, -1] = small[:, -1]
    while True:
        n = reach.copy()
        n[1:, :] |= reach[:-1, :]; n[:-1, :] |= reach[1:, :]; n[:, 1:] |= reach[:, :-1]; n[:, :-1] |= reach[:, 1:]
        n &= small
        if (n == reach).all(): break
        reach = n
    bg = np.asarray(Image.fromarray((reach * 255).astype(np.uint8)).resize((1080, 1920), Image.BILINEAR)) > 127
    alpha = Image.fromarray(((~bg) * 255).astype(np.uint8), "L").filter(ImageFilter.MinFilter(5)).filter(ImageFilter.GaussianBlur(1.3))
    rgba = im.convert("RGBA"); rgba.putalpha(alpha)
    # remove brilhos e confetes soltos: mantem so componentes grandes (props presos ao corpo ficam)
    al = np.array(alpha)[::4, ::4] > 20
    dl = al.copy()
    for _ in range(3): dl = dl | np.roll(dl, 1, 0) | np.roll(dl, -1, 0) | np.roll(dl, 1, 1) | np.roll(dl, -1, 1)
    lab, sizes = components(dl); big = max(sizes[1:]); keep = [i for i, sz in enumerate(sizes) if i > 0 and sz > 0.06 * big]
    mk = np.isin(lab, keep)
    mk_full = np.array(Image.fromarray((mk * 255).astype(np.uint8)).resize((1080, 1920), Image.NEAREST)) > 0
    arr = np.array(rgba); arr[..., 3] = np.where(mk_full, arr[..., 3], 0)
    out = Image.fromarray(arr); out = out.crop(out.getbbox()); out.save(OUT / (name + ".png")); return out.size
if __name__ == "__main__":
    for n in sys.argv[1:]:
        try: print(n, cut(n))
        except Exception as e: print(n, "ERRO", e)
