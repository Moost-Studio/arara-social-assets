#!/usr/bin/env python3
"""Estilo v3, inspirado nos exercicios do app (cabecalho, balao com alto-falante, botao de microfone).
Uso: story_compose_v3.py <id> <base.png> <head_x> <head_y> [saida.png]"""
import json, sys, pathlib
from PIL import Image, ImageDraw, ImageFont

D = "/tmp/arara_fonts"
BASE = pathlib.Path(__file__).parent
W, H = 1080, 1920
NAVY, BLUE, DARKBLUE = (21, 38, 66, 255), (30, 111, 217, 255), (18, 78, 165, 255)
WHITE, MUTED, BORDER = (255, 255, 255, 255), (96, 116, 148, 255), (190, 210, 236, 255)
SHADOW = (21, 38, 66, 40)
MX = 80


def F(name, size, weight=None):
    f = ImageFont.truetype(f"{D}/{name}", size)
    if weight:
        f.set_variation_by_name(weight)
    return f


def cjk(t): return any(ord(c) > 0x2E80 for c in t)
def head(s, t=""): return F("MPLUSRounded1c-ExtraBold.ttf", s) if cjk(t) else F("Baloo2.ttf", s, "ExtraBold")
def body(s, t=""): return F("MPLUSRounded1c-ExtraBold.ttf", s) if cjk(t) else F("Nunito.ttf", s, "ExtraBold")
def soft(s, t=""): return F("MPLUSRounded1c-ExtraBold.ttf", s) if cjk(t) else F("Nunito.ttf", s, "SemiBold")


def wrap(d, text, f, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=f) <= max_w:
            cur = t
        else:
            lines.append(cur)
            cur = w
    lines.append(cur)
    return lines


def icon_mic(d, cx, cy, s, color, width):
    k = s / 24
    d.rounded_rectangle([cx - 4 * k, cy - 11 * k, cx + 4 * k, cy + 3 * k], radius=4 * k, outline=color, width=width)
    d.arc([cx - 8 * k, cy - 7 * k, cx + 8 * k, cy + 9 * k], 0, 180, fill=color, width=width)
    d.line([(cx, cy + 9 * k), (cx, cy + 12 * k)], fill=color, width=width)


def icon_speaker(d, cx, cy, s, color, width):
    k = s / 24
    pts = [(cx - 10 * k, cy - 4 * k), (cx - 5 * k, cy - 4 * k), (cx + 1 * k, cy - 9 * k), (cx + 1 * k, cy + 9 * k),
           (cx - 5 * k, cy + 4 * k), (cx - 10 * k, cy + 4 * k)]
    d.polygon(pts, fill=color)
    d.arc([cx - 4 * k, cy - 6 * k, cx + 8 * k, cy + 6 * k], -50, 50, fill=color, width=width)
    d.arc([cx - 4 * k, cy - 11 * k, cx + 13 * k, cy + 11 * k], -50, 50, fill=color, width=width)


def dashed_underline(d, x0, x1, y, color):
    x = x0
    while x < x1:
        d.line([(x, y), (min(x + 12, x1), y)], fill=color, width=4)
        x += 20


def header(im, label, y):
    d = ImageDraw.Draw(im)
    d.ellipse([MX, y, MX + 64, y + 64], fill=BLUE)
    icon_mic(d, MX + 32, y + 32, 34, WHITE, 5)
    d.text((MX + 84, y + 34), label.upper(), font=body(36, label), fill=BLUE, anchor="lm")
    return y + 64


def title(im, text, y):
    d = ImageDraw.Draw(im)
    f = head(84, text)
    lines = wrap(d, text, f, W - 2 * MX)
    for l in lines:
        d.text((MX, y), l, font=f, fill=NAVY, anchor="la")
        y += 88
    return y


def bubble(im, top, phrase, trans, tx, ty):
    d = ImageDraw.Draw(im, "RGBA")
    fp, ft = body(64, phrase), soft(40, trans)
    icon_w = 90
    inner = W - 2 * MX - 2 * 44 - icon_w
    pl = wrap(d, phrase, fp, inner)
    tl = wrap(d, trans, ft, inner)
    ps, ts = 82, 52
    h = ps * len(pl) + 14 + ts * len(tl) + 2 * 40
    x0, x1, y0, y1 = MX, W - MX, top, top + h
    bx = min(max(tx, x0 + 120), x1 - 120)
    for off, col in ((10, SHADOW),):
        d.rounded_rectangle([x0, y0 + off, x1, y1 + off], radius=44, fill=col)
    tail = [(bx - 30, y1 - 4), (bx + 30, y1 - 4), (tx, ty)]
    d.polygon(tail, fill=WHITE)
    d.line([tail[0], tail[2]], fill=BORDER, width=4)
    d.line([tail[1], tail[2]], fill=BORDER, width=4)
    d.rounded_rectangle([x0, y0, x1, y1], radius=44, fill=WHITE, outline=BORDER, width=4)
    d.line([(tail[0][0] + 3, y1 - 2), (tail[1][0] - 3, y1 - 2)], fill=WHITE, width=8)
    icon_speaker(d, x0 + 44 + 30, y0 + 40 + 36, 54, BLUE, 6)
    tx0 = x0 + 44 + icon_w
    y = y0 + 40
    for l in pl:
        d.text((tx0, y), l, font=fp, fill=NAVY, anchor="la")
        x = tx0
        for w in l.split(" "):
            ww = d.textlength(w, font=fp)
            dashed_underline(d, x, x + ww, y + 76, (150, 170, 200, 255))
            x += ww + d.textlength(" ", font=fp)
        y += ps
    y += 14
    for l in tl:
        d.text((tx0, y), l, font=ft, fill=MUTED, anchor="la")
        y += ts
    return y1


def mic_button(im, cy):
    d = ImageDraw.Draw(im, "RGBA")
    w, h = 260, 100
    x0, x1 = W / 2 - w / 2, W / 2 + w / 2
    d.rounded_rectangle([x0, cy - h / 2 + 10, x1, cy + h / 2 + 10], radius=40, fill=DARKBLUE)
    d.rounded_rectangle([x0, cy - h / 2, x1, cy + h / 2], radius=40, fill=BLUE)
    icon_mic(d, W / 2, cy, 54, WHITE, 7)


def compose(sid, src, hx, hy, out):
    s = next(x for x in json.loads((BASE / "stories.json").read_text())["stories"] if x["id"] == sid)
    im = Image.open(src).convert("RGB").resize((W, H), Image.LANCZOS).convert("RGBA")
    y = header(im, s["tag"] if s["hl"] != "Frases" else f"Frase útil · {s['tag']}", 290) + 28
    y = title(im, s["title"], y) + 56
    phrase = next((t for k, t in s["blocks"] if k == "phrase"), None)
    trans = next((t for k, t in s["blocks"] if k == "trans"), "")
    end = bubble(im, y, phrase, trans, hx, hy) if phrase else y
    if phrase:
        mic_button(im, 1722)
    im.convert("RGB").save(out, quality=95)
    return end


if __name__ == "__main__":
    sid, src, hx, hy = int(sys.argv[1]), sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
    out = sys.argv[5] if len(sys.argv) > 5 else str(BASE / "stories_img_v3" / f"story_{sid:02d}.png")
    pathlib.Path(out).parent.mkdir(parents=True, exist_ok=True)
    print("fim do balao em y =", compose(sid, src, hx, hy, out), "cabeca em y =", hy)
