#!/usr/bin/env python3
"""Estilo v2 (sticker + balao de fala), sem badges/cartoes.
Uso: story_compose_v2.py <id> <base.png> <head_x> <head_y> [saida.png]
head_x/head_y = topo da cabeca da mascote (onde a ponta do balao aponta)."""
import json, sys, pathlib
from PIL import Image, ImageDraw, ImageFont

D = "/tmp/arara_fonts"
BASE = pathlib.Path(__file__).parent
W, H = 1080, 1920
NAVY, DEEP, WHITE = (21, 38, 66, 255), (11, 22, 44, 255), (255, 255, 255, 255)
YELLOW, BLUE, MUTED = (255, 201, 64, 255), (30, 111, 217, 255), (84, 104, 140, 255)


def F(name, size, weight=None):
    f = ImageFont.truetype(f"{D}/{name}", size)
    if weight:
        f.set_variation_by_name(weight)
    return f


def cjk(t): return any(ord(c) > 0x2E80 for c in t)
def head(s, t=""): return F("MPLUSRounded1c-ExtraBold.ttf", s) if cjk(t) else F("Baloo2.ttf", s, "ExtraBold")
def body(s, t=""): return F("MPLUSRounded1c-ExtraBold.ttf", s) if cjk(t) else F("Nunito.ttf", s, "ExtraBold")


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


def sticker_text(im, cx, top, text, size, max_w):
    d = ImageDraw.Draw(im)
    f = head(size, text)
    lines = wrap(d, text, f, max_w)
    step = int(size * 1.0)
    y = top
    for l in lines:
        d.text((cx, y + 12), l, font=f, fill=DEEP, anchor="ma", stroke_width=14, stroke_fill=DEEP)
        d.text((cx, y), l, font=f, fill=WHITE, anchor="ma", stroke_width=14, stroke_fill=NAVY)
        y += step
    return y + 24


def tag(im, cx, cy, text):
    f = body(40, text)
    tmp = Image.new("RGBA", (700, 160), (0, 0, 0, 0))
    td = ImageDraw.Draw(tmp)
    w = int(td.textlength(text, font=f)) + 80
    x0 = (700 - w) // 2
    td.rounded_rectangle([x0, 30, x0 + w, 120], radius=45, fill=YELLOW, outline=NAVY, width=7)
    td.text((350, 76), text, font=f, fill=NAVY, anchor="mm")
    tmp = tmp.rotate(4, resample=Image.BICUBIC, expand=True)
    im.alpha_composite(tmp, (int(cx - tmp.width / 2), int(cy - tmp.height / 2)))


def bubble(im, top, phrase, trans, tx, ty):
    d = ImageDraw.Draw(im)
    fp, ft = head(66, phrase), body(40, trans)
    inner = W - 2 * 90 - 2 * 44
    pl, tl = wrap(d, phrase, fp, inner), wrap(d, trans, ft, inner)
    ps, ts = int(66 * 1.08), int(40 * 1.25)
    h = ps * len(pl) + ts * len(tl) + 2 * 40 + 18
    w = max(max(int(d.textlength(l, font=fp)) for l in pl), max(int(d.textlength(l, font=ft)) for l in tl)) + 2 * 56
    w = max(w, 560)
    x0, x1, y0, y1 = W / 2 - w / 2, W / 2 + w / 2, top, top + h
    bx = min(max(tx, x0 + 90), x1 - 90)
    pts = [(bx - 34, y1 - 6), (bx + 34, y1 - 6), (tx, ty)]
    d.polygon(pts, fill=WHITE, outline=NAVY)
    d.line([pts[0], pts[2]], fill=NAVY, width=8)
    d.line([pts[1], pts[2]], fill=NAVY, width=8)
    d.rounded_rectangle([x0, y0 + 8, x1, y1 + 8], radius=56, fill=DEEP)
    d.polygon([(a, b + 8) for a, b in pts], fill=DEEP)
    d.polygon(pts, fill=WHITE)
    d.line([pts[0], pts[2]], fill=NAVY, width=8)
    d.line([pts[1], pts[2]], fill=NAVY, width=8)
    d.rounded_rectangle([x0, y0, x1, y1], radius=56, fill=WHITE, outline=NAVY, width=8)
    d.line([(pts[0][0] + 4, y1 - 4), (pts[1][0] - 4, y1 - 4)], fill=WHITE, width=12)
    y = y0 + 40
    for l in pl:
        d.text((W / 2, y), l, font=fp, fill=BLUE, anchor="ma")
        y += ps
    y += 18
    for l in tl:
        d.text((W / 2, y), l, font=ft, fill=MUTED, anchor="ma")
        y += ts
    return y1


def compose(sid, src, hx, hy, out):
    s = next(x for x in json.loads((BASE / "stories.json").read_text())["stories"] if x["id"] == sid)
    im = Image.open(src).convert("RGB").resize((W, H), Image.LANCZOS).convert("RGBA")
    tag(im, W / 2, 296, s["tag"])
    y = sticker_text(im, W / 2, 352, s["title"], 84, W - 130)
    phrase = next((t for k, t in s["blocks"] if k == "phrase"), None)
    trans = next((t for k, t in s["blocks"] if k == "trans"), "")
    end = bubble(im, y + 36, phrase, trans, hx, hy) if phrase else y
    im.convert("RGB").save(out, quality=95)
    return end


if __name__ == "__main__":
    sid, src, hx, hy = int(sys.argv[1]), sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
    out = sys.argv[5] if len(sys.argv) > 5 else str(BASE / "stories_img_v2" / f"story_{sid:02d}.png")
    pathlib.Path(out).parent.mkdir(parents=True, exist_ok=True)
    print("fim do balao em y =", compose(sid, src, hx, hy, out), "cabeca em y =", hy)
