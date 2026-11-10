#!/usr/bin/env python3
"""Estilo v4 (estilo app). Le stories.json e monta todos os tipos:
phrase, plain, cheat, exercise, exercise_answer, rows.
Uso: story_compose_v4.py <id> <base.png> [head_x head_y] [saida.png]
head_x/head_y = topo da cabeca da mascote (ponta do balao). Titulo aceita *palavra* em destaque azul."""
import json, sys, pathlib, re
from PIL import Image, ImageDraw, ImageFont

D = "/tmp/arara_fonts"
BASE = pathlib.Path(__file__).parent
W, H = 1080, 1920
NAVY, BLUE, DARKBLUE = (21, 38, 66, 255), (30, 111, 217, 255), (18, 78, 165, 255)
WHITE, MUTED, BORDER = (255, 255, 255, 255), (96, 116, 148, 255), (190, 210, 236, 255)
GREEN, DGREEN, LGREEN = (88, 190, 20, 255), (60, 150, 10, 255), (222, 246, 205, 255)
RED = (230, 70, 70, 255)
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
    d.polygon([(cx - 10 * k, cy - 4 * k), (cx - 5 * k, cy - 4 * k), (cx + 1 * k, cy - 9 * k), (cx + 1 * k, cy + 9 * k),
               (cx - 5 * k, cy + 4 * k), (cx - 10 * k, cy + 4 * k)], fill=color)
    d.arc([cx - 4 * k, cy - 6 * k, cx + 8 * k, cy + 6 * k], -50, 50, fill=color, width=width)
    d.arc([cx - 4 * k, cy - 11 * k, cx + 13 * k, cy + 11 * k], -50, 50, fill=color, width=width)


def icon_check(d, cx, cy, s, color, width):
    k = s / 24
    d.line([(cx - 8 * k, cy), (cx - 2 * k, cy + 6 * k), (cx + 9 * k, cy - 7 * k)], fill=color, width=width, joint="curve")


def icon_x(d, cx, cy, s, color, width):
    k = s / 24
    d.line([(cx - 7 * k, cy - 7 * k), (cx + 7 * k, cy + 7 * k)], fill=color, width=width)
    d.line([(cx - 7 * k, cy + 7 * k), (cx + 7 * k, cy - 7 * k)], fill=color, width=width)


def dashed(d, x0, x1, y, color):
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


def title(im, text, y, size=84):
    d = ImageDraw.Draw(im)
    f = head(size, text)
    toks = []
    for part in re.split(r"(\*[^*]+\*)", text):
        if not part:
            continue
        col = BLUE if part.startswith("*") else NAVY
        words = part.strip("*").split()
        if words and toks and not part[0].isspace() and not part.startswith("*"):
            toks[-1] = (toks[-1][0], toks[-1][1], words[0])
            words = words[1:]
        for w in words:
            toks.append((w, col))
    sp = d.textlength(" ", font=f)
    lines, cur, cw = [], [], 0
    for tk in toks:
        w, col = tk[0], tk[1]
        tail = tk[2] if len(tk) > 2 else ""
        ww = d.textlength(w + tail, font=f)
        if cur and cw + sp + ww > W - 2 * MX:
            lines.append(cur)
            cur, cw = [], 0
        cw += (sp if cur else 0) + ww
        cur.append((w, col, ww, tail))
    lines.append(cur)
    for ln in lines:
        x = MX
        for w, col, ww, tail in ln:
            d.text((x, y), w, font=f, fill=col, anchor="la")
            if tail:
                d.text((x + d.textlength(w, font=f), y), tail, font=f, fill=NAVY, anchor="la")
            x += ww + sp
        y += int(size * 1.05)
    return y


def card_box(d, x0, y0, x1, y1):
    d.rounded_rectangle([x0, y0 + 10, x1, y1 + 10], radius=44, fill=SHADOW)
    d.rounded_rectangle([x0, y0, x1, y1], radius=44, fill=WHITE, outline=BORDER, width=4)


def tail(d, x0, x1, y1, tx, ty):
    bx = min(max(tx, x0 + 120), x1 - 120)
    pts = [(bx - 30, y1 - 4), (bx + 30, y1 - 4), (tx, ty)]
    d.polygon(pts, fill=WHITE)
    d.line([pts[0], pts[2]], fill=BORDER, width=4)
    d.line([pts[1], pts[2]], fill=BORDER, width=4)
    d.line([(pts[0][0] + 3, y1 - 2), (pts[1][0] - 3, y1 - 2)], fill=WHITE, width=8)


def bubble_phrase(im, top, phrase, trans, tx, ty):
    d = ImageDraw.Draw(im, "RGBA")
    fp, ft = body(64, phrase), soft(40, trans)
    inner = W - 2 * MX - 2 * 44 - 90
    pl, tl = wrap(d, phrase, fp, inner), wrap(d, trans, ft, inner)
    ps, ts = 82, 52
    h = ps * len(pl) + 14 + ts * len(tl) + 80
    x0, x1, y0, y1 = MX, W - MX, top, top + h
    card_box(d, x0, y0, x1, y1)
    if tx is not None:
        tail(d, x0, x1, y1, tx, ty)
    icon_speaker(d, x0 + 74, y0 + 76, 54, BLUE, 6)
    tx0, y = x0 + 134, y0 + 40
    for l in pl:
        d.text((tx0, y), l, font=fp, fill=NAVY, anchor="la")
        x = tx0
        for w in l.split(" "):
            ww = d.textlength(w, font=fp)
            dashed(d, x, x + ww, y + 76, (150, 170, 200, 255))
            x += ww + d.textlength(" ", font=fp)
        y += ps
    y += 14
    for l in tl:
        d.text((tx0, y), l, font=ft, fill=MUTED, anchor="la")
        y += ts
    return y1


def bubble_plain(im, top, text, tx, ty):
    d = ImageDraw.Draw(im, "RGBA")
    f = body(46, text)
    pl = wrap(d, text, f, W - 2 * MX - 2 * 44)
    st = 62
    h = st * len(pl) + 80
    x0, x1, y0, y1 = MX, W - MX, top, top + h
    card_box(d, x0, y0, x1, y1)
    if tx is not None:
        tail(d, x0, x1, y1, tx, ty)
    y = y0 + 40
    for l in pl:
        d.text((x0 + 44, y), l, font=f, fill=NAVY, anchor="la")
        y += st
    return y1


def cheat_card(im, top, likes, dislikes):
    d = ImageDraw.Draw(im, "RGBA")
    row, f = 54, body(34)
    n = len(likes) + len(dislikes)
    h = 2 * 62 + n * row + 44
    x0, x1, y0, y1 = MX, W - MX, top, top + h
    card_box(d, x0, y0, x1, y1)
    y = y0 + 28
    for label, items, col, ic in (("GOSTA DE", likes, GREEN, icon_check), ("NÃO GOSTA DE", dislikes, RED, icon_x)):
        d.text((x0 + 44, y + 22), label, font=head(36), fill=col, anchor="lm")
        y += 56
        for t in items:
            d.ellipse([x0 + 44, y + 6, x0 + 84, y + 46], fill=col)
            ic(d, x0 + 64, y + 26, 24, WHITE, 6)
            d.text((x0 + 106, y + 26), t, font=f, fill=NAVY, anchor="lm")
            y += row
        y += 10
    return y1


def rows_card(im, top, rows, slang=False, st=82):
    d = ImageDraw.Draw(im, "RGBA")
    h = st * len(rows) + 60
    x0, x1, y0, y1 = MX, W - MX, top, top + h
    card_box(d, x0, y0, x1, y1)
    y = y0 + 30
    for i, r in enumerate(rows):
        lab, val = [x.strip() for x in r.split("|")]
        if slang:
            d.text((x0 + 44, y + st / 2), lab, font=head(48, lab), fill=NAVY, anchor="lm")
            d.text((x1 - 44, y + st / 2), val, font=soft(38, val), fill=BLUE, anchor="rm")
        else:
            d.text((x0 + 44, y + st / 2), lab, font=soft(34, lab), fill=MUTED, anchor="lm")
            d.text((x1 - 44, y + st / 2), val, font=body(44, val), fill=BLUE, anchor="rm")
        if i < len(rows) - 1:
            d.line([(x0 + 44, y + st), (x1 - 44, y + st)], fill=(225, 234, 246, 255), width=3)
        y += st
    return y1


def option_buttons(im, top, options, correct=None, answer=False):
    d = ImageDraw.Draw(im, "RGBA")
    h, gap = 112, 24
    y = top
    for i, o in enumerate(options):
        x0, x1 = MX, W - MX
        right = answer and i == correct
        fill = LGREEN if right else WHITE
        edge = GREEN if right else BORDER
        d.rounded_rectangle([x0, y + 8, x1, y + h + 8], radius=34, fill=DGREEN if right else (190, 205, 228, 255))
        d.rounded_rectangle([x0, y, x1, y + h], radius=34, fill=fill, outline=edge, width=5)
        col = DGREEN if right else (NAVY if not answer else MUTED)
        d.text((W / 2, y + h / 2), o, font=body(46, o), fill=col, anchor="mm")
        if right:
            d.ellipse([x1 - 90, y + h / 2 - 28, x1 - 34, y + h / 2 + 28], fill=GREEN)
            icon_check(d, x1 - 62, y + h / 2, 30, WHITE, 7)
        y += h + gap
    return y


def mic_button(im, cy):
    d = ImageDraw.Draw(im, "RGBA")
    w, h = 260, 100
    x0, x1 = W / 2 - w / 2, W / 2 + w / 2
    d.rounded_rectangle([x0, cy - h / 2 + 10, x1, cy + h / 2 + 10], radius=40, fill=DARKBLUE)
    d.rounded_rectangle([x0, cy - h / 2, x1, cy + h / 2], radius=40, fill=BLUE)
    icon_mic(d, W / 2, cy, 54, WHITE, 7)


def compose(sid, src, hx, hy, out, off=0, _dry=False):
    s = next(x for x in json.loads((BASE / "stories.json").read_text())["stories"] if x["id"] == sid)
    im = Image.open(src).convert("RGB").resize((W, H), Image.LANCZOS)
    z = s.get("zoom")
    if z:
        from PIL import ImageFilter
        bx0, by0, bx1, by1 = z["box"]
        k2 = z["k"]
        bg = im.crop((0, 0, W, 360)).resize((W, H), Image.BICUBIC)
        part = im.crop((bx0, by0, bx1, by1)).resize((int((bx1 - bx0) * k2), int((by1 - by0) * k2)), Image.LANCZOS)
        mask = Image.new("L", part.size, 0)
        ImageDraw.Draw(mask).rectangle([30, 30, part.width - 30, part.height - 30], fill=255)
        mask = mask.filter(ImageFilter.GaussianBlur(22))
        cx, cy = (bx0 + bx1) // 2, (by0 + by1) // 2
        bg.paste(part, (cx - part.width // 2, cy - part.height // 2 + z.get("dy", 0)), mask)
        im = bg
    k = s.get("shrink")
    if k:
        bg = im.crop((0, 0, W, 360)).resize((W, H), Image.BICUBIC)
        sm = im.resize((int(W * k), int(H * k)), Image.LANCZOS)
        mask = Image.new("L", sm.size, 0)
        ImageDraw.Draw(mask).rectangle([40, 40, sm.width - 40, sm.height], fill=255)
        from PIL import ImageFilter
        mask = mask.filter(ImageFilter.GaussianBlur(26))
        bg.paste(sm, ((W - sm.width) // 2, H - sm.height), mask)
        im = bg
    im = im.convert("RGBA")
    t = s["type"]
    label = f"Frase útil · {s['tag']}" if s.get("hl") == "Frases" and t == "phrase" else s["tag"]
    y = header(im, label, 290 + off) + 28
    y = title(im, s["title"], y) + 52
    if t == "phrase":
        end = bubble_phrase(im, y, s["phrase"], s["trans"], hx, hy)
        if s.get("mic", True):
            mic_button(im, s.get("mic_y", 1690))
    elif t == "plain":
        end = bubble_plain(im, y, s["body"], hx, hy)
    elif t == "cheat":
        end = cheat_card(im, y, s["likes"], s["dislikes"])
    elif t == "rows":
        end = rows_card(im, y, s["rows"], s.get("slang", False), s.get("row_h", 82))
    elif t in ("exercise", "exercise_answer"):
        end = bubble_plain(im, y, s["prompt"], None, None)
        ans = t == "exercise_answer"
        if ans:
            d = ImageDraw.Draw(im, "RGBA")
            f = body(40)
            lines = wrap(d, s["feedback"], f, W - 2 * MX - 2 * 40 - 70)
            h = 56 * len(lines) + 56
            y0 = end + 26
            d.rounded_rectangle([MX, y0 + 8, W - MX, y0 + h + 8], radius=40, fill=DGREEN)
            d.rounded_rectangle([MX, y0, W - MX, y0 + h], radius=40, fill=LGREEN, outline=GREEN, width=5)
            d.ellipse([MX + 34, y0 + h / 2 - 28, MX + 90, y0 + h / 2 + 28], fill=GREEN)
            icon_check(d, MX + 62, y0 + h / 2, 30, WHITE, 7)
            for i, l in enumerate(lines):
                d.text((MX + 112, y0 + 28 + i * 56), l, font=f, fill=DGREEN, anchor="la")
            end = y0 + h
        option_buttons(im, 1380, s["options"], s["correct"], ans)
    if hy is not None and t in ("phrase", "plain") and not _dry and off == 0:
        shift = min(max(0, hy - 120 - end), 280)
        if shift > 40:
            return compose(sid, src, hx, hy, out, off=shift)
    im.convert("RGB").save(out, quality=95)
    return end


if __name__ == "__main__":
    sid, src = int(sys.argv[1]), sys.argv[2]
    rest = sys.argv[3:]
    hx = hy = None
    if len(rest) >= 2 and rest[0].lstrip("-").isdigit():
        hx, hy, rest = int(rest[0]), int(rest[1]), rest[2:]
    out = rest[0] if rest else str(BASE / "stories_final" / f"story_{sid:02d}.png")
    pathlib.Path(out).parent.mkdir(parents=True, exist_ok=True)
    print("fim do bloco de texto em y =", compose(sid, src, hx, hy, out), "| cabeca em y =", hy)
