#!/usr/bin/env python3
"""Prototipo: o post 'conta' (en, es, fr, it) com as cores de cada idioma. Saida: proto_cores/ (nao toca nos posts agendados)."""
import json, pathlib, sys
from PIL import Image, ImageDraw
import post_compose_s3 as pc
import story_compose_v4 as sc
import lang_theme as lt

BASE = pathlib.Path(__file__).parent
OUT = BASE / "proto_cores"; OUT.mkdir(exist_ok=True)
posts = json.load(open(BASE / "posts_semana3.json"))
slides = posts["conta"]["slides"]
langs = {1: "en", 2: "es", 3: "fr", 4: "it"}
orig = {k: getattr(sc, k) for k in ("BLUE", "DARKBLUE", "BORDER", "NAVY", "MUTED")}
paths = []
for idx, th in langs.items():
    for k, v in orig.items(): setattr(sc, k, v)
    lt.apply_ui(sc, th)
    pc.RECOLOR = lambda im, th=th: lt.recolor(im, th)
    out = OUT / f"conta_{th}.png"
    pc.slide(slides[idx], out)
    paths.append(out)
# folha: antes (azul) em cima, depois (por idioma) embaixo
for k, v in orig.items(): setattr(sc, k, v)
pc.RECOLOR = None
antes = []
for idx in langs:
    out = OUT / f"conta_antes_{langs[idx]}.png"; pc.slide(slides[idx], out); antes.append(out)
w, h = 540, 675
sheet = Image.new("RGB", (4 * w + 5 * 20, 2 * h + 3 * 20 + 40), "white")
d = ImageDraw.Draw(sheet)
for i, p in enumerate(antes):
    sheet.paste(Image.open(p).convert("RGB").resize((w, h), Image.LANCZOS), (20 + i * (w + 20), 20))
for i, p in enumerate(paths):
    sheet.paste(Image.open(p).convert("RGB").resize((w, h), Image.LANCZOS), (20 + i * (w + 20), 20 + h + 20))
sheet.save(OUT / "folha_conta.png")
print("ok", OUT / "folha_conta.png")
