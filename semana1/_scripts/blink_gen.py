"""Gera a variante "piscando" de cada pose de corpo inteiro.

Acha o par de olhos da pose por correlação normalizada com o recorte dos olhos
do K00 (kit, olhos abertos) em várias escalas e cola por cima os olhos do K03
(kit, olhos fechados), com máscara suave. Poses com cabeça virada ficam sem
variante (correlação abaixo do limite).
Uso: python3 blink_gen.py   (lê ../recortes, grava ../recortes/blink e blink_report.json)
"""
import json, os, sys
import numpy as np
from PIL import Image, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
REC = os.path.join(HERE, '..', 'recortes')
OUT = os.path.join(REC, 'blink')
os.makedirs(OUT, exist_ok=True)
POSES = ["C01", "E01", "E02", "E04", "E06", "E08", "E09", "G01", "G02", "G06", "G07", "G09", "G10", "ARDENCIA"]
BOX = (165, 270, 590, 460)  # região dos dois olhos no K00/K03 (x0,y0,x1,y1)
LIMIT = 0.62

BG = (60, 80, 130)


def flat(path):
    im = Image.open(path).convert('RGBA')
    bg = Image.new('RGBA', im.size, BG + (255,))
    bg.alpha_composite(im)
    return im, bg.convert('RGB')


def gray(im):
    return np.asarray(im.convert('L'), dtype=np.float64)


def ncc_map(img, tpl):
    """NCC de tpl sobre img (modo 'valid') via FFT + somas integrais."""
    H, W = img.shape
    h, w = tpl.shape
    t = tpl - tpl.mean()
    tn = np.sqrt((t ** 2).sum())
    shape = (H + h, W + w)
    fi = np.fft.rfft2(img, shape)
    ft = np.fft.rfft2(t[::-1, ::-1], shape)
    corr = np.fft.irfft2(fi * ft, shape)[h - 1:H, w - 1:W]
    ii = np.pad(img, ((1, 0), (1, 0))).cumsum(0).cumsum(1)
    i2 = np.pad(img ** 2, ((1, 0), (1, 0))).cumsum(0).cumsum(1)

    def box(a):
        return a[h:, w:] - a[:-h, w:] - a[h:, :-w] + a[:-h, :-w]

    s = box(ii)
    s2 = box(i2)
    var = np.maximum(s2 - s ** 2 / (h * w), 1e-6)
    return corr / (np.sqrt(var) * tn)


def main():
    _, k0 = flat(os.path.join(REC, 'K', 'K00.png'))
    k3img, k3 = flat(os.path.join(REC, 'K', 'K03.png'))
    t0 = k0.crop(BOX)
    t3 = k3.crop(BOX)
    rep = {}
    for n in POSES:
        pim, pflat = flat(os.path.join(REC, n + '.png'))
        pg = gray(pflat)
        best = (-1, None, None)
        for s in np.arange(0.30, 0.72, 0.02):
            tw, th = int(t0.width * s), int(t0.height * s)
            tg = gray(t0.resize((tw, th), Image.LANCZOS))
            m = ncc_map(pg[:int(pg.shape[0] * 0.55)], tg)
            y, x = np.unravel_index(np.argmax(m), m.shape)
            if m[y, x] > best[0]:
                best = (float(m[y, x]), (x, y), s)
        sc, (x, y), s = best
        rep[n] = {'score': round(sc, 3), 'x': int(x), 'y': int(y), 'scale': round(float(s), 2)}
        print(n, rep[n])
        if sc < LIMIT:
            continue
        tw, th = int(t3.width * s), int(t3.height * s)
        patch = t3.resize((tw, th), Image.LANCZOS)
        mask = Image.new('L', (tw, th), 0)
        # elipse suave cobrindo os dois olhos
        from PIL import ImageDraw
        d = ImageDraw.Draw(mask)
        d.ellipse((tw * 0.03, th * 0.02, tw * 0.97, th * 0.98), fill=255)
        mask = mask.filter(ImageFilter.GaussianBlur(max(2, tw * 0.025)))
        out = pim.copy()
        base = out.crop((x, y, x + tw, y + th)).convert('RGBA')
        comp = Image.composite(patch.convert('RGBA'), base, mask)
        comp.putalpha(base.split()[3])
        out.paste(comp, (x, y))
        out.save(os.path.join(OUT, n + '_blink.png'))
    json.dump(rep, open(os.path.join(OUT, 'blink_report.json'), 'w'), indent=1)


if __name__ == '__main__':
    main()
