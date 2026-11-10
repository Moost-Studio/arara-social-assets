#!/usr/bin/env python3
"""Gancho do Enem (04/11/2026): carrossel de 5 telas + story de sabado 07/11. Saida em revisao_enem/ (nada publicado)."""
import pathlib
from PIL import Image, ImageDraw
import post_compose_s3 as pc
import story_compose_v4 as sc
import lang_theme as lt
from head_util import head_of

BASE = pathlib.Path(__file__).parent
OUT = BASE / "revisao_enem"; OUT.mkdir(exist_ok=True)
lt.apply_ui(sc, "padrao"); pc.RECOLOR = None


def plain(art, tag, title, body, scale=0.75, **kw):
    return dict(type="plain", art=art, scale=scale, tag=tag, title=title, body=body, head=head_of(art), **kw)


SLIDES = [
    plain("v2_enem_pronto.png", "Enem 2026", "Só 5 questões de *idioma*, mas dá pra se preparar",
          "No primeiro dia, 8/11, o Enem traz 5 questões de inglês ou espanhol. Arrasta para o lado e veja 3 dicas rápidas.", tsize=66, top=40),
    plain("v2_enem_ler.png", "Dica 1", "Leia o *enunciado* primeiro",
          "Ele diz o que a questão pede e ajuda a achar a resposta no texto sem se perder."),
    plain("v2_enem_prof.png", "Dica 2", "Cace as palavras *parecidas*",
          "Muita palavra em inglês ou espanhol lembra o português. Aproveite, mas fique de olho nos falsos amigos."),
    plain("v2_enem_calma.png", "Dica 3", "Travou numa *palavra*? Siga em frente",
          "Você não precisa entender tudo. Busque o sentido geral do texto e volte depois se sobrar tempo."),
    plain("v2_enem_torcida.png", "Boa prova", "Respira e *voa*, bando!",
          "Salva este post e marca quem faz o Enem neste domingo. Boa prova para vocês!"),
]
paths = []
for i, s in enumerate(SLIDES, 1):
    p = OUT / f"enem_{i}.png"; pc.slide(s, p); paths.append(p); print("ok", p.name)

# story 9:16 (sabado 07/11): reaproveita o desenho da mascote com sono, mas como lembrete de vespera
art = "v2_enem_sono.png"
im = Image.open(BASE / "stories_base" / art).convert("RGB").resize((1080, 1920), Image.LANCZOS).convert("RGBA")
y = sc.header(im, "Véspera do Enem", 290) + 28
y = sc.title(im, "Amanhã é dia de *Enem*", y) + 52
hx, hy = head_of(art)
sc.bubble_plain(im, y, "Durma cedo, separe o documento com foto e chegue com folga. Os portões fecham às 13h, no horário de Brasília. Boa prova!", hx, hy)
im.convert("RGB").save(OUT / "enem_story.png"); print("ok story")

w, h = 360, 450
sheet = Image.new("RGB", (5 * w + 6 * 16, h + 32), "white")
for i, p in enumerate(paths):
    sheet.paste(Image.open(p).convert("RGB").resize((w, h), Image.LANCZOS), (16 + i * (w + 16), 16))
st = Image.open(OUT / "enem_story.png").convert("RGB").resize((int(h * 1080 / 1920), h), Image.LANCZOS)
sheet2 = Image.new("RGB", (sheet.width + st.width + 16, h + 32), "white")
sheet2.paste(sheet, (0, 0)); sheet2.paste(st, (sheet.width, 16))
sheet2.save(OUT / "folha_enem.png"); print("folha ok")
