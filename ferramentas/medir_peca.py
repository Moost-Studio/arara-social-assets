#!/usr/bin/env python3
"""Mede uma peça recém-gerada: tamanho vs formato, cantos, margens e (opcional) terço de cima livre.
Uso: python3 medir_peca.py PREFIXO FORMATO   (ex.: SI01_v1 1:1  |  TA01_v1 4:5  |  M13_v1 9:16)
Procura o arquivo mais novo em ~/.openclaw/media/tool-image-generation/PREFIXO---*.png"""
import sys, glob, os
from PIL import Image
pref, fmt = sys.argv[1], sys.argv[2]
fs = sorted(glob.glob(os.path.expanduser(f'~/.openclaw/media/tool-image-generation/{pref}---*.png')), key=os.path.getmtime)
if not fs: print('NAO ENCONTRADO'); sys.exit(1)
f = fs[-1]; im = Image.open(f).convert('RGB'); w, h = im.size; px = im.load()
a, b = map(int, fmt.split(':')); alvo = a / b
print('ARQUIVO', f); print('TAMANHO', w, h, 'razao', round(w / h, 4), 'alvo', round(alvo, 4), 'OK' if abs(w / h - alvo) < 0.01 else 'FORMATO ERRADO')
print('cantos', px[5, 5], px[w - 6, 5], px[5, h - 6], px[w - 6, h - 6])
bg = px[5, 5]; d = lambda p: abs(p[0] - bg[0]) + abs(p[1] - bg[1]) + abs(p[2] - bg[2])
rows = [y for y in range(0, h, 2) if any(d(px[x, y]) > 90 for x in range(0, w, 2))]
cols = [x for x in range(0, w, 2) if any(d(px[x, y]) > 90 for y in range(0, h, 2))]
if rows and cols:
    print('margens esq/topo/dir/base', cols[0], rows[0], w - cols[-1], h - rows[-1], '| topo do conteudo a', round(rows[0] / h * 100, 1), '% do alto')
