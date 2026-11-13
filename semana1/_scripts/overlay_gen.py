"""Gera as variantes de textura do rig: olhos fechados (K03) e bico aberto (K01), por pose.

Alinha os olhos do K00 (kit, 1254 px) em cada pose do quadro de 1254 px por correlação normalizada
e cola só a região que muda entre K00 e K03 / K00 e K01 (máscara por diferença, suavizada).
Só gera a variante quando a correlação passa do limite (cabeça e expressão compatíveis com o kit).

Saídas: semana1/recortes/rig/{pose}_blink.png, {pose}_beak.png e overlay_report.json
Uso: python3 overlay_gen.py [poses...]
"""
import json, os, sys
import numpy as np
from PIL import Image, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from blink_gen import ncc_map  # noqa: E402

PERS = os.path.join(HERE, '..', '..', 'personagens', 'rara')
RIG = os.path.join(HERE, '..', 'recortes', 'rig')
BG = (60, 80, 130)
LIM_EYE, LIM_MOUTH = 0.62, 0.78


def flat(im):
    im = im.convert('RGBA')
    b = Image.new('RGBA', im.size, BG + (255,))
    b.alpha_composite(im)
    return b.convert('RGB')


def gray(im):
    return np.asarray(im.convert('L'), dtype=np.float64)


def diff_box(a, b, thr=14, grow=10):
    d = np.abs(np.asarray(a.convert('RGB'), dtype=int) - np.asarray(b.convert('RGB'), dtype=int)).max(2) > thr
    ys, xs = np.where(d)
    return d, (max(xs.min() - grow, 0), max(ys.min() - grow, 0), min(xs.max() + grow, a.width), min(ys.max() + grow, a.height))


def soft_mask(d, box, grow=7, blur=5):
    m = Image.fromarray((d * 255).astype(np.uint8)).filter(ImageFilter.MaxFilter(2 * grow + 1)).filter(ImageFilter.GaussianBlur(blur))
    return m.crop(box)


def main(poses):
    from PIL import ImageDraw
    KD = os.path.join(HERE, '..', 'recortes', 'K')
    k0, k1, k3 = [flat(Image.open(os.path.join(KD, f'{n}.png'))) for n in ('K00', 'K01', 'K03')]
    EYE = (165, 270, 590, 460)       # os dois olhos (K00/K03), em px do kit alinhado
    MOUTH = (275, 375, 490, 615)     # bico e boca (K00/K01)
    t0 = k0.crop(EYE)
    rep = {'eye_box_kit': EYE, 'mouth_box_kit': MOUTH}
    def emask(w, h):
        m = Image.new('L', (w, h), 0)
        ImageDraw.Draw(m).ellipse((w * 0.03, h * 0.02, w * 0.97, h * 0.98), fill=255)
        return m.filter(ImageFilter.GaussianBlur(max(2, w * 0.03)))
    for n in poses:
        p = Image.open(os.path.join(RIG, n + '.png')).convert('RGBA')
        pg = gray(flat(p))
        H = int(pg.shape[0] * 0.55)
        best = (-1, None, None)
        for s in np.arange(0.50, 0.76, 0.02):
            tw, th = int(t0.width * s), int(t0.height * s)
            tg = gray(t0.resize((tw, th), Image.LANCZOS))
            m = ncc_map(pg[:H], tg)
            y, x = np.unravel_index(np.argmax(m), m.shape)
            if m[y, x] > best[0]:
                best = (float(m[y, x]), (int(x), int(y)), float(s))
        sc, (x, y), s = best
        r = {'eye_score': round(sc, 3), 'x': x, 'y': y, 'scale': round(s, 2)}
        if sc >= LIM_EYE:
            for tag, kimg, bx in (('blink', k3, EYE), ('beak', k1, MOUTH)):
                x0, y0 = int(x + (bx[0] - EYE[0]) * s), int(y + (bx[1] - EYE[1]) * s)
                w, h = int((bx[2] - bx[0]) * s), int((bx[3] - bx[1]) * s)
                if tag == 'beak':
                    ref = gray(k0.crop(bx).resize((w, h), Image.LANCZOS))
                    cur = gray(flat(p).crop((x0, y0, x0 + w, y0 + h)))
                    a_, b_ = ref - ref.mean(), cur - cur.mean()
                    ms = float((a_ * b_).sum() / (np.sqrt((a_ ** 2).sum() * (b_ ** 2).sum()) + 1e-9))
                    r['mouth_score'] = round(ms, 3)
                    if ms < LIM_MOUTH:
                        continue
                patch = kimg.crop(bx).resize((w, h), Image.LANCZOS)
                out = p.copy()
                base = out.crop((x0, y0, x0 + w, y0 + h)).convert('RGBA')
                comp = Image.composite(patch.convert('RGBA'), base, emask(w, h))
                comp.putalpha(base.split()[3])
                out.paste(comp, (x0, y0))
                out.save(os.path.join(RIG, f'{n}_{tag}.png'))
                r[tag] = True
        rep[n] = r
        print(n, r, flush=True)
    path = os.path.join(RIG, 'overlay_report.json')
    old = json.load(open(path)) if os.path.exists(path) else {}
    old.update(rep)
    json.dump(old, open(path, 'w'), indent=1)


if __name__ == '__main__':
    poses = sys.argv[1:] or ['C01', 'E01', 'E02', 'E03', 'E04', 'E06', 'E08', 'E09', 'E11', 'E13', 'G01', 'G02', 'G03', 'G05', 'G06', 'G07', 'G09', 'G10']
    main(poses)
