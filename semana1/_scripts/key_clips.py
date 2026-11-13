"""Remove o fundo cinza liso dos clipes do Veo (cor-chave com bordas suaves e descontaminação).

Entrada:  grupo4_reel/ia/raw{N}/f_###.png (720x1280, 24 fps)
Saída:    grupo4_reel/ia/clip{N}/f_###.png recortados (RGBA, caixa comum) e clips.js com a geometria.
Uso: python3 key_clips.py N inicio fim   (quadros 1-based, inclusive)
"""
import json, os, sys
import numpy as np
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
IA = os.path.join(HERE, '..', 'grupo4_reel', 'ia')
GX, GY = 360, 921          # âncora do chão e do centro nas imagens iniciais (720x1280)


def smooth(a, b, x):
    p = np.clip((x - a) / (b - a), 0, 1)
    return p * p * (3 - 2 * p)


def key(path):
    im = np.asarray(Image.open(path).convert('RGB'), dtype=np.float64)
    border = np.concatenate([im[:8].reshape(-1, 3), im[-8:].reshape(-1, 3), im[:, :8].reshape(-1, 3), im[:, -8:].reshape(-1, 3)])
    bg = np.median(border, axis=0)
    d = np.abs(im - bg).max(axis=2)
    a = smooth(30, 68, d)
    # descontamina: remove a parcela do cinza nas bordas semitransparentes
    af = np.maximum(a, 1e-3)[..., None]
    col = np.clip(bg + (im - bg) / af, 0, 255)
    col = np.where(a[..., None] > 0.97, im, col)
    out = np.dstack([col, a * 255]).astype(np.uint8)
    return out


def main():
    n, f0, f1 = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    src = os.path.join(IA, f'raw{n}')
    dst = os.path.join(IA, f'clip{n}')
    os.makedirs(dst, exist_ok=True)
    for f in os.listdir(dst):
        os.remove(os.path.join(dst, f))
    frames = []
    bbs = []
    for k in range(f0, f1 + 1):
        arr = key(os.path.join(src, f'f_{k:03d}.png'))
        al = arr[..., 3]
        ys, xs = np.where(al > 8)
        bbs.append((xs.min(), ys.min(), xs.max() + 1, ys.max() + 1))
        frames.append(arr)
    x0 = max(min(b[0] for b in bbs) - 6, 0)
    y0 = max(min(b[1] for b in bbs) - 6, 0)
    x1 = min(max(b[2] for b in bbs) + 6, 720)
    y1 = min(max(b[3] for b in bbs) + 6, 1280)
    names = []
    for i, arr in enumerate(frames):
        nm = f'f_{i:03d}.png'
        Image.fromarray(arr[y0:y1, x0:x1], 'RGBA').save(os.path.join(dst, nm), optimize=False, compress_level=3)
        names.append(nm)
    # altura da personagem no 1º quadro (para escalar até RH)
    b0 = bbs[0]
    meta = {'dir': f'clip{n}', 'frames': names, 'n': len(names), 'fps': 24, 'ox': int(x0), 'oy': int(y0),
            'gx': GX, 'gy': GY, 'ch0': int(b0[3] - b0[1]), 'cw0': int(b0[2] - b0[0])}
    path = os.path.join(IA, 'clips_meta.json')
    allm = json.load(open(path)) if os.path.exists(path) else {}
    allm[f'c{n}'] = meta
    json.dump(allm, open(path, 'w'), indent=1)
    print(n, meta['n'], 'crop', (x0, y0, x1, y1), 'ch0', meta['ch0'])


if __name__ == '__main__':
    main()
