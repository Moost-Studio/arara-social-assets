#!/usr/bin/env python3
"""Cores por idioma para as artes da Arara (prototipo de 04/11/2026, aguardando aprovacao do Rodrigo).

A mascote nunca muda (azul, barriga amarela, cauda verde). O que muda por idioma:
- o fundo claro da ilustracao (o azul palido vira a cor do idioma);
- o destaque dos titulos, o selo do topo, o icone de som e os botoes (cor de acento).
O verde de "acertou" continua verde em todos os idiomas, porque e um sinal de interface.
Temas sem idioma (humor, tutora, testes, Arara) usam o padrao azul.
"""
import numpy as np
from PIL import Image


def rgba(h, a=255):
    h = h.lstrip("#")
    return (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16), a)


# bg_hue: matiz do fundo em graus; bg_sat: multiplicador da saturacao do fundo original (palido)
THEMES = {
    "padrao": dict(bg_hue=None, accent="#1E6FD9", dark="#124EA5", border="#BED2EC", navy="#152642", muted="#607494"),
    "en": dict(bg_hue=None, accent="#D62839", dark="#9E1B2A", border="#BED2EC", navy="#152642", muted="#607494"),
    "es": dict(bg_hue=44, bg_sat=1.55, accent="#C8102E", dark="#8F0B21", border="#F1D79A", navy="#3A1A12", muted="#8A6A4A"),
    "fr": dict(bg_hue=246, bg_sat=0.95, accent="#2540B8", dark="#1A2D86", border="#CFCBF2", navy="#1B1D4A", muted="#6A6F9E"),
    "it": dict(bg_hue=142, bg_sat=1.0, accent="#0A8F4B", dark="#066B38", border="#BFE3CC", navy="#12351F", muted="#5C8068"),
    "de": dict(bg_hue=48, bg_sat=1.0, accent="#1F1F24", dark="#000000", border="#E6D79E", navy="#1F1F24", muted="#7A7357"),
    "pt": dict(bg_hue=78, bg_sat=1.2, accent="#2E9B1F", dark="#1F7013", border="#D5E8A8", navy="#1A3312", muted="#6B7F4E"),
    "ja": dict(bg_hue=348, bg_sat=0.9, accent="#D6203F", dark="#9C1630", border="#F2C9D2", navy="#3A1620", muted="#8E6470"),
    "zh": dict(bg_hue=8, bg_sat=1.25, accent="#D0211C", dark="#8F1612", border="#F2C7BA", navy="#3A1512", muted="#8E6458"),
}


def recolor(img, theme):
    """Troca so o fundo palido azulado da ilustracao pela cor do idioma (a mascote e saturada e fica como esta)."""
    t = THEMES[theme]
    if t.get("bg_hue") is None:
        return img
    a = np.asarray(img.convert("RGB"), dtype=np.float32) / 255.0
    mx, mn = a.max(axis=2), a.min(axis=2)
    v = mx
    s = np.where(mx > 0, (mx - mn) / np.maximum(mx, 1e-6), 0)
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    d = np.maximum(mx - mn, 1e-6)
    h = np.where(mx == r, ((g - b) / d) % 6, np.where(mx == g, (b - r) / d + 2, (r - g) / d + 4)) * 60.0
    in_blue = np.clip((h - 170) / 12, 0, 1) * np.clip((256 - h) / 12, 0, 1)
    pale = np.clip((0.62 - s) / 0.18, 0, 1) * np.clip((v - 0.80) / 0.08, 0, 1)
    w = (in_blue * pale)[..., None]
    th = t["bg_hue"] / 360.0
    ns = np.clip(s * t.get("bg_sat", 1.0), 0, 1)
    # conversao vetorizada hsv -> rgb
    hh = np.full_like(v, th) * 6.0
    i = np.floor(hh).astype(int) % 6
    f = hh - np.floor(hh)
    p, q, tt = v * (1 - ns), v * (1 - ns * f), v * (1 - ns * (1 - f))
    choices = [(v, tt, p), (q, v, p), (p, v, tt), (p, q, v), (tt, p, v), (v, p, q)]
    out = np.zeros_like(a)
    for k, (cr, cg, cb) in enumerate(choices):
        m = (i == k)
        out[..., 0] = np.where(m, cr, out[..., 0])
        out[..., 1] = np.where(m, cg, out[..., 1])
        out[..., 2] = np.where(m, cb, out[..., 2])
    res = a * (1 - w) + out * w
    return Image.fromarray((np.clip(res, 0, 1) * 255).astype(np.uint8))


def apply_ui(sc, theme):
    """Pinta a interface (selo, destaque do titulo, icone de som, botoes) com as cores do idioma."""
    t = THEMES[theme]
    sc.BLUE, sc.DARKBLUE, sc.BORDER = rgba(t["accent"]), rgba(t["dark"]), rgba(t["border"])
    sc.NAVY, sc.MUTED = rgba(t["navy"]), rgba(t["muted"])
