"""Prepara as poses do rig: recorte em 1254 x 1254 (mesmo quadro do original) e marcação dos 6 pontos.

Saídas:
  semana1/recortes/rig/{pose}.png          RGBA 1254 x 1254
  personagens/rara/rig/{pose}.json         6 pontos de articulação + caixa da figura
  personagens/rara/rig/_verificacao.png    folha com os pontos desenhados

Os pontos são estimados pela geometria (o corpo é o mesmo em todas as poses e só a cabeça, o topete e as
asas mudam) e depois conferidos na folha de verificação. Ajustes manuais ficam em OVERRIDE.
Uso: python3 rig_prep.py
"""
import json, os, sys
import numpy as np
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from cutout import cutout_pockets  # noqa: E402

ROOT = os.path.join(HERE, '..', '..')
PERS = os.path.join(ROOT, 'personagens', 'rara')
SRC = {
    'C01': os.path.join(PERS, 'rara_canonica_frente_v1.png'),
    'E01': 'expressoes/E01_alegria.png', 'E02': 'expressoes/E02_euforia.png', 'E03': 'expressoes/E03_orgulho.png',
    'E04': 'expressoes/E04_vergonha.png', 'E06': 'expressoes/E06_confusao.png', 'E08': 'expressoes/E08_drama.png',
    'E09': 'expressoes/E09_carencia.png', 'E11': 'expressoes/E11_calma.png', 'E13': 'expressoes/E13_tontura.png',
    'G01': 'gestos/G01_joinha.png', 'G02': 'gestos/G02_ok.png', 'G03': 'gestos/G03_hang_loose.png',
    'G05': 'gestos/G05_palmas.png', 'G06': 'gestos/G06_aceno.png', 'G07': 'gestos/G07_apontando.png',
    'G09': 'gestos/G09_suplica.png', 'G10': 'gestos/G10_coracao.png',
    'ARDENCIA': os.path.join(ROOT, 'semana1', 'grupo3_feed', 'pio', 'ardencia_v1.png'),
}
OUT_PNG = os.path.join(ROOT, 'semana1', 'recortes', 'rig')
OUT_JSON = os.path.join(PERS, 'rig')
os.makedirs(OUT_PNG, exist_ok=True)
os.makedirs(OUT_JSON, exist_ok=True)

# pontos do rig.py (poses de pé, 1254 px)
BASE = {'feet': (628, 840), 'neck': (628, 395), 'crest': (600, 150), 'wingL': (505, 445), 'wingR': (752, 445), 'tail': (628, 865)}
OVERRIDE = {'E02': {'feet': (628, 725), 'tail': (615, 752)}}  # pose no ar: pés e cauda 115 px acima das poses de pé


def path_of(k):
    p = SRC[k]
    return p if os.path.isabs(p) else os.path.join(PERS, p)


def estimate(a, name):
    """Ajusta os 6 pontos da base à pose: cabeça (pescoço e topete) e corpo (pés e cauda) pelo alfa."""
    alpha = a[..., 3] > 40
    ys, xs = np.where(alpha)
    x0, y0, x1, y1 = int(xs.min()), int(ys.min()), int(xs.max()) + 1, int(ys.max()) + 1
    pts = {k: list(v) for k, v in BASE.items()}
    # perfil de largura por linha e centro de massa da parte de baixo (cauda) para achar o eixo do corpo
    low = alpha[int(y1 - 0.12 * (y1 - y0)):y1]
    lx = np.where(low.any(0))[0]
    tail_tip_x = float(lx.mean()) if len(lx) else 628
    pts['tail'][0] = float(0.5 * (tail_tip_x + 628)) if abs(tail_tip_x - 628) < 120 else 628
    # topete: ponto mais alto da figura, deslocado 60 px para baixo e 15 px para dentro
    top_row = alpha[y0:y0 + 14]
    tx = np.where(top_row.any(0))[0]
    pts['crest'] = [float(0.5 * (tx.mean() + 628)), float(y0 + 132)]
    # pescoço: x acompanha o meio da cabeça (linhas 230-330), y fixo da base do corpo
    pts['neck'] = [628.0, 395.0]  # o corpo é o mesmo em todas as poses; só a cabeça se inclina
    return {'bbox': [x0, y0, x1, y1], 'points': pts}


def main():
    sheet_items = []
    for name in SRC:
        rgba, _ = cutout_pockets(path_of(name))
        rgba.save(os.path.join(OUT_PNG, name + '.png'))
        arr = np.asarray(rgba)
        info = estimate(arr, name)
        if name in OVERRIDE:
            info['points'].update(OVERRIDE[name])
        info['pose'] = name
        info['image'] = f'semana1/recortes/rig/{name}.png'
        info['size'] = [1254, 1254]
        info['nota'] = 'Pontos em pixels da imagem de 1254 px. feet=pés, neck=pescoço, crest=topete, wingL/wingR=ombros, tail=base da cauda.'
        json.dump(info, open(os.path.join(OUT_JSON, name + '.json'), 'w'), indent=1, ensure_ascii=False)
        sheet_items.append((name, rgba, info))
        print(name, info['bbox'], {k: [round(v[0]), round(v[1])] for k, v in info['points'].items()})
    n = len(sheet_items)
    cols = 6
    rows = (n + cols - 1) // cols
    cw, ch = 330, 330
    S = Image.new('RGB', (cols * cw, rows * ch), (40, 60, 110))
    cols_ = {'feet': (255, 80, 80), 'neck': (80, 255, 80), 'crest': (255, 255, 0), 'wingL': (0, 255, 255), 'wingR': (255, 0, 255), 'tail': (255, 160, 0)}
    for i, (name, rgba, info) in enumerate(sheet_items):
        bg = Image.new('RGBA', rgba.size, (40, 60, 110, 255))
        bg.alpha_composite(rgba)
        d = ImageDraw.Draw(bg)
        for k, (x, y) in info['points'].items():
            d.ellipse((x - 14, y - 14, x + 14, y + 14), outline=cols_[k], width=6)
        d.text((20, 20), name, fill=(255, 255, 255))
        S.paste(bg.convert('RGB').resize((cw, ch)), ((i % cols) * cw, (i // cols) * ch))
    S.save(os.path.join(OUT_JSON, '_verificacao.png'))


if __name__ == '__main__':
    main()
