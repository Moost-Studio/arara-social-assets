"""Remove o balao de fala vazio das ilustracoes 15 e 27 (interpola o fundo na vertical)."""
import numpy as np
from PIL import Image, ImageFilter

def clean(src, dst, rect):
    im = Image.open(src).convert("RGB").resize((1080, 1920), Image.LANCZOS)
    a = np.array(im).astype(int)
    x0, y0, x1, y1 = rect
    sub = a[y0:y1, x0:x1]
    r, g, b = sub[..., 0], sub[..., 1], sub[..., 2]
    white = (r > 225) & (g > 225) & (b > 225)
    outline = (b > 170) & (r < 90) & (g > 80) & (g < 150)   # azul do contorno
    mask = Image.fromarray(((white | outline) * 255).astype("uint8")).filter(ImageFilter.MaxFilter(15))
    m = np.array(mask) > 0
    out = a.copy()
    for xi in range(x1 - x0):
        col = m[:, xi]
        if not col.any():
            continue
        ys = np.where(col)[0]
        top, bot = max(ys.min() - 1, 0), min(ys.max() + 1, y1 - y0 - 1)
        ctop, cbot = sub[top, xi], sub[bot, xi]
        for yi in ys:
            t = (yi - top) / max(bot - top, 1)
            out[y0 + yi, x0 + xi] = (1 - t) * ctop + t * cbot
    Image.fromarray(out.astype("uint8")).filter(ImageFilter.GaussianBlur(0)).save(dst)

clean("stories_base/story_27.png", "stories_base/story_27_clean.png", (740, 1030, 1000, 1240))
clean("stories_base/story_15.png", "stories_base/story_15_clean.png", (700, 860, 1030, 1100))
print("ok")
