#!/usr/bin/env python3
"""Monta slides 4:5 (1080x1350) para o feed, reaproveitando as ilustracoes dos stories."""
import json, sys, pathlib
from PIL import Image, ImageDraw, ImageFilter
import story_compose_v4 as sc

BASE = pathlib.Path(__file__).parent
PW, PH = 1080, 1350
sc.W = PW


def canvas(art, scale, oy=None, mode="edge"):
    src = Image.open(BASE / "stories_base" / art).convert("RGB").resize((1080, 1920), Image.LANCZOS)
    w, h = int(1080 * scale), int(1920 * scale)
    y = PH - h + 40 if oy is None else oy
    # fundo: gradiente do topo + versao esticada e desfocada da propria arte (cobre as laterais sem emenda)
    bg = src.crop((0, 0, 1080, 360)).resize((PW, PH), Image.BICUBIC).convert("RGBA")
    if mode == "stretch":
        wide = src.resize((PW, h), Image.LANCZOS).filter(ImageFilter.GaussianBlur(30)).convert("RGBA")
    else:
        col = src.crop((2, 0, 6, 1920)).resize((1, h), Image.BILINEAR)
        colr = src.crop((1074, 0, 1078, 1920)).resize((1, h), Image.BILINEAR)
        wide = Image.new("RGB", (PW, h))
        left = col.resize((PW // 2, h), Image.NEAREST)
        right = colr.resize((PW // 2, h), Image.NEAREST)
        wide.paste(left, (0, 0)); wide.paste(right, (PW // 2, 0))
        wide = wide.filter(ImageFilter.GaussianBlur(20)).convert("RGBA")
    wmask = Image.new("L", (PW, h), 255)
    ImageDraw.Draw(wmask).rectangle([0, 0, PW, 60], fill=0)
    wmask = wmask.filter(ImageFilter.GaussianBlur(25))
    bg.paste(wide, (0, y), wmask)
    il = src.resize((w, h), Image.LANCZOS).convert("RGBA")
    x = (PW - w) // 2
    mask = Image.new("L", (w, h), 255)
    md = ImageDraw.Draw(mask)
    f = 90
    for i in range(f):
        a = int(255 * (i / f) ** 1.5)
        md.line([(i, 0), (i, h)], fill=a)
        md.line([(w - 1 - i, 0), (w - 1 - i, h)], fill=a)
    top = Image.new("L", (w, h), 255)
    td = ImageDraw.Draw(top)
    for i in range(f):
        td.line([(0, i), (w, i)], fill=int(255 * (i / f) ** 1.5))
    from PIL import ImageChops
    mask = ImageChops.multiply(mask, top)
    bg.paste(il, (x, y), mask)
    return bg, x, y


def head_pt(hx, hy, scale, x, y):
    return int(hx * scale + x), int(hy * scale + y)


def slide(spec, out):
    sc.H = PH
    im, ox, oy = canvas(spec["art"], spec.get("scale", 0.75), spec.get("oy"), spec.get("bg", "edge"))
    sc_ = spec.get("scale", 0.75)
    t = spec["type"]
    y = spec.get("top", 60)
    y = sc.header(im, spec["tag"], y) + 24
    y = sc.title(im, spec["title"], y, spec.get("tsize", 84)) + 40
    hp = head_pt(*spec["head"], sc_, ox, oy) if spec.get("head") else (None, None)
    if t == "phrase":
        sc.bubble_phrase(im, y, spec["phrase"], spec["trans"], *hp)
    elif t == "plain":
        sc.bubble_plain(im, y, spec["body"], *hp)
    elif t == "cheat":
        sc.cheat_card(im, y, spec["likes"], spec["dislikes"])
    elif t == "rows":
        sc.rows_card(im, y, spec["rows"], spec.get("slang", False), spec.get("row_h", 70))
    elif t in ("exercise", "answer"):
        ans = t == "answer"
        end = (y - 16) if spec.get("hide_prompt") else sc.bubble_plain(im, y, spec["prompt"], None, None)
        by = spec.get("btn_y", end + 40)
        if ans:
            d = ImageDraw.Draw(im, "RGBA")
            f = sc.body(40)
            lines = sc.wrap(d, spec["feedback"], f, PW - 2 * sc.MX - 2 * 40 - 70)
            h = 56 * len(lines) + 56
            y0 = end + 24
            d.rounded_rectangle([sc.MX, y0 + 8, PW - sc.MX, y0 + h + 8], radius=40, fill=sc.DGREEN)
            d.rounded_rectangle([sc.MX, y0, PW - sc.MX, y0 + h], radius=40, fill=sc.LGREEN, outline=sc.GREEN, width=5)
            d.ellipse([sc.MX + 34, y0 + h / 2 - 28, sc.MX + 90, y0 + h / 2 + 28], fill=sc.GREEN)
            sc.icon_check(d, sc.MX + 62, y0 + h / 2, 30, sc.WHITE, 7)
            for i, l in enumerate(lines):
                d.text((sc.MX + 112, y0 + 28 + i * 56), l, font=f, fill=sc.DGREEN, anchor="la")
        sc.option_buttons(im, spec.get("btn_y", 880), spec["options"], spec["correct"], ans)
    im.convert("RGB").save(out, quality=95)


def quiz_cover(out, arts):
    sc.H = PH
    im = Image.open(BASE / "stories_base" / arts[0]).convert("RGB").resize((1080, 1920))
    im = im.crop((0, 0, 1080, 360)).resize((PW, PH), Image.BICUBIC).convert("RGBA")
    y = sc.header(im, "Teste rápido", 60) + 24
    y = sc.title(im, "Que tipo de *arara* você é?", y, 84) + 30
    tw, th, gap = 380, 470, 24
    x0 = (PW - 2 * tw - gap) // 2
    for k, a in enumerate(arts):
        src = Image.open(BASE / "stories_base" / a).convert("RGB").resize((1080, 1920))
        crop = src.crop((190, 950, 890, 1816)).resize((tw, th), Image.LANCZOS)
        card = Image.new("RGBA", (tw, th), (255, 255, 255, 255))
        card.paste(crop.crop((0, 0, tw, th)), (0, 0))
        m = Image.new("L", (tw, th), 0)
        ImageDraw.Draw(m).rounded_rectangle([0, 0, tw, th], radius=36, fill=255)
        bx = x0 + (k % 2) * (tw + gap)
        by = y + (k // 2) * (th + gap)
        d = ImageDraw.Draw(im, "RGBA")
        d.rounded_rectangle([bx, by + 8, bx + tw, by + th + 8], radius=36, fill=sc.SHADOW)
        im.paste(card, (bx, by), m)
        d.rounded_rectangle([bx, by, bx + tw, by + th], radius=36, outline=sc.BORDER, width=4)
    im.convert("RGB").save(out, quality=95)


if __name__ == "__main__":
    posts = json.load(open(BASE / "posts_semana2.json"))
    outdir = BASE / "posts_img"
    outdir.mkdir(exist_ok=True)
    only = sys.argv[1] if len(sys.argv) > 1 else None
    for pid, p in posts.items():
        if pid.startswith("_") or (only and pid != only):
            continue
        for i, s in enumerate(p["slides"], 1):
            out = outdir / f"{pid}_{i}.png"
            if s["type"] == "quiz_cover":
                quiz_cover(out, s["arts"])
            else:
                slide(s, out)
            print("ok", out.name)
