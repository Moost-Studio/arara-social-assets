#!/usr/bin/env python3
"""Aplica o texto de um story sobre a ilustracao 9:16.
Uso: story_compose.py <id> <imagem_base> [saida.png]
Fontes em /tmp/arara_fonts (Baloo2.ttf, Nunito.ttf, MPLUSRounded1c-ExtraBold.ttf)."""
import json, sys, pathlib
from PIL import Image, ImageDraw, ImageFont

D = "/tmp/arara_fonts"
BASE = pathlib.Path(__file__).parent
NAVY, NAVY_A = (21, 38, 66, 255), (21, 38, 66, 238)
WHITE, CARD = (255, 255, 255, 255), (255, 255, 255, 240)
YELLOW, BLUE, MUTED = (255, 201, 64, 255), (30, 111, 217, 255), (84, 104, 140, 255)
RADIUS, W, H, MARGIN, SAFE_TOP = 28, 1080, 1920, 64, 270


def F(name, size, weight=None):
    f = ImageFont.truetype(f"{D}/{name}", size)
    if weight:
        f.set_variation_by_name(weight)
    return f


def is_cjk(t):
    return any(ord(c) > 0x2E80 for c in t)


def title_font(s, t=""): return F("MPLUSRounded1c-ExtraBold.ttf", s) if is_cjk(t) else F("Baloo2.ttf", s, "ExtraBold")
def body_font(s, t=""): return F("MPLUSRounded1c-ExtraBold.ttf", s) if is_cjk(t) else F("Nunito.ttf", s, "ExtraBold")
def soft_font(s, t=""): return F("MPLUSRounded1c-ExtraBold.ttf", s) if is_cjk(t) else F("Nunito.ttf", s, "SemiBold")


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


def rrect(im, box, fill):
    ov = Image.new("RGBA", im.size, (0, 0, 0, 0))
    ImageDraw.Draw(ov).rounded_rectangle(box, radius=RADIUS, fill=fill)
    im.alpha_composite(ov)


def metrics(f):
    b = f.getbbox("ÁgçjQ", anchor="ls")
    return -b[1], b[3]


def badge(im, top, text, f, max_w, bg, fg, pad_x=40, pad_y=14):
    d = ImageDraw.Draw(im)
    lines = wrap(d, text, f, max_w - 2 * pad_x)
    up, down = metrics(f)
    step = int((up + down) * 1.05)
    w = max(int(d.textlength(l, font=f)) for l in lines) + 2 * pad_x
    h = step * (len(lines) - 1) + up + down + 2 * pad_y
    rrect(im, [W / 2 - w / 2, top, W / 2 + w / 2, top + h], bg)
    d = ImageDraw.Draw(im)
    for i, l in enumerate(lines):
        d.text((W / 2, top + pad_y + up + i * step), l, font=f, fill=fg, anchor="ms")
    return top + h


def card(im, top, blocks, pad=40, gap=22):
    d = ImageDraw.Draw(im)
    inner = W - 2 * MARGIN - 2 * pad
    items, total = [], 0
    for kind, text in blocks:
        if kind == "chips":
            continue
        if kind == "rows":
            for row in text.split("\n"):
                lab, val = [x.strip() for x in row.split("|")]
                fv = body_font(46, val)
                fl = soft_font(34, lab)
                items.append(("row", lab, val, fl, fv, 70))
                total += 70
            continue
        f, col = {"body": (body_font(44, text), NAVY),
                  "phrase": (title_font(58, text), BLUE),
                  "trans": (soft_font(40, text), MUTED)}[kind]
        lines = wrap(d, text, f, inner)
        step = int(f.size * 1.22)
        items.append((kind, lines, f, col, step))
        total += step * len(lines)
    total += gap * (len(items) - 1)
    h = total + 2 * pad
    rrect(im, [MARGIN, top, W - MARGIN, top + h], CARD)
    d = ImageDraw.Draw(im)
    y = top + pad
    for it in items:
        if it[0] == "row":
            _, lab, val, fl, fv, step = it
            d.text((MARGIN + pad, y + step / 2), lab, font=fl, fill=MUTED, anchor="lm")
            d.text((W - MARGIN - pad, y + step / 2), val, font=fv, fill=BLUE, anchor="rm")
            y += step + gap
        else:
            kind, lines, f, col, step = it
            for l in lines:
                d.text((W / 2, y), l, font=f, fill=col, anchor="ma")
                y += step
            y += gap
    return top + h


def chips(im, top, text):
    items = [x.strip() for x in text.split("|")]
    d = ImageDraw.Draw(im)
    rows = [items[:3], items[3:]]
    y = top
    for row in rows:
        fonts = [body_font(40, t) for t in row]
        widths = [int(d.textlength(t, font=f)) + 56 for t, f in zip(row, fonts)]
        x = W / 2 - (sum(widths) + 20 * (len(row) - 1)) / 2
        for t, f, w in zip(row, fonts, widths):
            rrect(im, [x, y, x + w, y + 76], WHITE)
            ImageDraw.Draw(im).text((x + w / 2, y + 38), t, font=f, fill=BLUE, anchor="mm")
            x += w + 20
        y += 96
    return y


def compose(sid, src, out):
    s = next(x for x in json.loads((BASE / "stories.json").read_text())["stories"] if x["id"] == sid)
    im = Image.open(src).convert("RGB").resize((W, H), Image.LANCZOS).convert("RGBA")
    y = SAFE_TOP
    y = badge(im, y, s["tag"], body_font(36, s["tag"]), W - 200, YELLOW, NAVY, pad_x=36, pad_y=10) + 30
    y = badge(im, y, s["title"], title_font(70, s["title"]), W - 2 * MARGIN, NAVY_A, WHITE) + 34
    blocks = [b for b in s["blocks"] if b[0] != "chips"]
    if blocks:
        y = card(im, y, blocks) + 28
    for k, t in s["blocks"]:
        if k == "chips":
            y = chips(im, y, t)
    im.convert("RGB").save(out, quality=95)
    return y


if __name__ == "__main__":
    sid, src = int(sys.argv[1]), sys.argv[2]
    out = sys.argv[3] if len(sys.argv) > 3 else str(BASE / "stories_img" / f"story_{sid:02d}.png")
    pathlib.Path(out).parent.mkdir(parents=True, exist_ok=True)
    print("fim do texto em y =", compose(sid, src, out), "(ideal ate ~1000)")
