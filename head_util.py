import pathlib
import numpy as np
from PIL import Image
BASE = pathlib.Path(__file__).parent


def head_of(art):
    """Topo da cabeca da mascote (x, y) em coordenadas 1080x1920, achado pelo primeiro pixel azul/vermelho saturado na faixa central."""
    im = Image.open(BASE / "stories_base" / art).convert("RGB").resize((1080, 1920))
    a = np.asarray(im).astype(float) / 255
    mx, mn = a.max(2), a.min(2)
    sat = (mx - mn) / np.maximum(mx, 1e-6)
    blue = (a[..., 2] > a[..., 0] + 0.25) & (sat > 0.55)
    red = (a[..., 0] > a[..., 2] + 0.35) & (sat > 0.6)
    m = (blue | red)[:, 300:800]
    ys = np.where(m.any(axis=1))[0]
    y = int(ys[0])
    xs = np.where(m[y:y + 40].any(axis=0))[0]
    return [int(xs.mean()) + 300, y + 10]
