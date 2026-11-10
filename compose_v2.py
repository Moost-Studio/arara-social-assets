#!/usr/bin/env python3
"""Semana 09-15/11, versao 2: cenas novas (expressoes variadas) + cores por idioma. Saida em revisao_v2/ (nao toca nos posts agendados)."""
import json, sys, pathlib
import numpy as np
from PIL import Image, ImageDraw
import post_compose_s3 as pc
import story_compose_v4 as sc
import lang_theme as lt

BASE = pathlib.Path(__file__).parent
OUT = BASE / "revisao_v2"; OUT.mkdir(exist_ok=True)
posts = json.load(open(BASE / "posts_semana3.json"))
ORIG = {k: getattr(sc, k) for k in ("BLUE", "DARKBLUE", "BORDER", "NAVY", "MUTED")}


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


def render(spec, theme, out):
    for k, v in ORIG.items(): setattr(sc, k, v)
    lt.apply_ui(sc, theme)
    pc.RECOLOR = lambda im: lt.recolor(im, theme)
    spec = dict(spec)
    if spec["type"] == "phrase" and "head_auto" in spec:
        spec["head"] = head_of(spec["art"])
    pc.slide(spec, out)
    return out


def phrase(art, tag, title, phr, trans, scale=0.75, **kw):
    return dict(type="phrase", art=art, scale=scale, tag=tag, title=title, phrase=phr, trans=trans, head_auto=1, **kw)


JOBS = []  # (arquivo, spec, tema)
c = posts["conta"]["slides"]
JOBS += [
    ("conta_1", c[0], "padrao"),
    ("conta_2", phrase("v2_conta_en.png", "Frase útil · Inglês", "Pedir a *conta*", "Can I have the check, please?", "Posso pedir a conta, por favor?"), "en"),
    ("conta_3", phrase("v2_conta_es.png", "Frase útil · Espanhol", "Pedir a *conta*", "La cuenta, por favor.", "A conta, por favor."), "es"),
    ("conta_4", phrase("v2_conta_fr.png", "Frase útil · Francês", "Pedir a *conta*", "L'addition, s'il vous plaît.", "A conta, por favor."), "fr"),
    ("conta_5", phrase("v2_conta_it.png", "Frase útil · Italiano", "Pedir a *conta*", "Il conto, per favore.", "A conta, por favor."), "it"),
]
b = posts["banheiro"]["slides"]
q = dict(b[0]); q.update(art="v2_banheiro_pergunta.png", scale=0.42, oy=36, btn_y=800)
r = dict(b[1]); r.update(art="v2_banheiro_resposta.png", scale=0.40, oy=165, btn_y=900)
JOBS += [("banheiro_1", q, "en"), ("banheiro_2", r, "en")]
f = posts["falsos"]["slides"]
JOBS += [
    ("falsos_1", f[0], "en"),
    ("falsos_2", phrase("v2_falsos_actually.png", "Falso amigo 1", "*Actually* não é atualmente", "Actually", f[1]["trans"]), "en"),
    ("falsos_3", phrase("v2_falsos_pretend.png", "Falso amigo 2", "*Pretend* não é pretender", "Pretend", f[2]["trans"]), "en"),
    ("falsos_4", phrase("v2_falsos_library.png", "Falso amigo 3", "*Library* não é livraria", "Library", f[3]["trans"]), "en"),
    ("falsos_5", f[4], "en"),
]

only = sys.argv[1] if len(sys.argv) > 1 else None
paths = {}
for name, spec, theme in JOBS:
    if only and not name.startswith(only): continue
    paths[name] = render(spec, theme, OUT / f"{name}.png")
    print("ok", name, theme, spec.get("head") or "")

# folha de revisao: uma linha por post
w, h = 360, 450
rows = {}
for n, p in paths.items(): rows.setdefault(n.split("_")[0], []).append(p)
sheet = Image.new("RGB", (5 * w + 6 * 16, len(rows) * (h + 16) + 16), "white")
for ri, (k, ps) in enumerate(rows.items()):
    for ci, p in enumerate(ps):
        sheet.paste(Image.open(p).convert("RGB").resize((w, h), Image.LANCZOS), (16 + ci * (w + 16), 16 + ri * (h + 16)))
sheet.save(OUT / "folha_v2.png")
print("folha", OUT / "folha_v2.png")
