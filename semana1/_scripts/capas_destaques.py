#!/usr/bin/env python3
"""Capas dos destaques do @falearara (1080x1920, sem texto). Rara/Raro recortados do acervo aprovado, busto dentro de um círculo.
Uso: python3 capas_destaques.py   (saída em ../../destaques/capas/)"""
import sys, pathlib
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from cutout import cutout, bbox

BASE = pathlib.Path(__file__).resolve().parents[2]
OUT = BASE / 'destaques' / 'capas'
W, H = 1080, 1920
CX, CY, D = 540, 960, 900
CAPAS = [
    # nome, arquivo, fundo, palco (círculo)
    ('sobre', 'personagens/rara/gestos/G06_aceno.png', '#DCEBFF', '#FFFFFF'),
    ('como-funciona', 'personagens/rara/gestos/G07_apontando.png', '#22B573', '#7FE0B0'),
    ('frases', 'personagens/rara/expressoes/E01_alegria.png', '#F7861F', '#FFB866'),
    ('diario', 'personagens/rara/expressoes/E07_pensativa.png', '#7B4DD6', '#B89BF0'),
    ('historias', 'personagens/raro/raro_canonica_frente_v2.png', '#FFF5E1', '#FFE0A3'),
    ('lancamento', 'personagens/rara/expressoes/E02_euforia.png', '#081226', '#1B3470'),
]

def hexrgb(h): h = h.lstrip('#'); return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def radial(color, size=(W, H)):
    base = np.zeros((size[1], size[0], 3), float) + hexrgb(color)
    yy, xx = np.mgrid[0:size[1], 0:size[0]]
    d = np.sqrt(((xx - CX) / (W * .75)) ** 2 + ((yy - CY) / (H * .55)) ** 2)
    k = np.clip(1 - d, 0, 1)[..., None] * 0.10
    base = base * (1 - k) + 255 * k
    return Image.fromarray(base.clip(0, 255).astype('uint8'), 'RGB')

def feita(nome, arq, fundo, palco):
    img = radial(fundo)
    stage = Image.new('RGBA', (D, D), (0, 0, 0, 0))
    ImageDraw.Draw(stage).ellipse([0, 0, D - 1, D - 1], fill=hexrgb(palco) + (255,))
    rgba, _ = cutout(str(BASE / arq))
    x0, y0, x1, y1 = bbox(rgba)
    ch = int((y1 - y0) * 0.62)
    crop = rgba.crop((x0, y0, x1, y0 + ch))
    s = min(730 / ch, 840 / (x1 - x0))
    crop = crop.resize((int((x1 - x0) * s), int(ch * s)), Image.LANCZOS)
    px = (D - crop.width) // 2
    py = 96
    stage.alpha_composite(crop, (px, py))
    mask = Image.new('L', (D, D), 0)
    ImageDraw.Draw(mask).ellipse([0, 0, D - 1, D - 1], fill=255)
    stage.putalpha(Image.fromarray(np.minimum(np.asarray(stage)[..., 3], np.asarray(mask))))
    # anel e sombra suave
    sh = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(sh).ellipse([CX - D // 2, CY - D // 2 + 14, CX + D // 2, CY + D // 2 + 14], fill=(0, 0, 0, 55))
    img = Image.alpha_composite(img.convert('RGBA'), sh.filter(ImageFilter.GaussianBlur(22)))
    img.alpha_composite(stage, (CX - D // 2, CY - D // 2))
    ring = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(ring).ellipse([CX - D // 2, CY - D // 2, CX + D // 2, CY + D // 2], outline=(255, 255, 255, 235), width=12)
    img.alpha_composite(ring)
    out = OUT / f'CAPA_{nome}_1080x1920.png'
    img.convert('RGB').save(out)
    return out

if __name__ == '__main__':
    OUT.mkdir(parents=True, exist_ok=True)
    fs = [feita(*c) for c in CAPAS]
    # prévia: círculo como o Instagram mostra (recorte central redondo, 270 px)
    S = 270
    sheet = Image.new('RGB', (S * 6 + 70, S + 40), (30, 30, 36))
    for i, f in enumerate(fs):
        im = Image.open(f).crop((0, 420, 1080, 1500)).resize((S, S), Image.LANCZOS)
        m = Image.new('L', (S, S), 0); ImageDraw.Draw(m).ellipse([0, 0, S - 1, S - 1], fill=255)
        sheet.paste(im, (10 + i * (S + 10), 20), m)
    sheet.save(OUT / '_previa_circulo.png')
    print([f.name for f in fs])
