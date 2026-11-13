"""Junta os JSON de pontos (personagens/rara/rig/*.json) e o relatório de variantes em rig_data.js, lido pelo reel4.html."""
import json, os, glob
H = os.path.dirname(os.path.abspath(__file__))
R = os.path.join(H, '..', '..', 'personagens', 'rara', 'rig')
V = os.path.join(H, '..', 'recortes', 'rig')
data = {}
for f in sorted(glob.glob(os.path.join(R, '*.json'))):
    d = json.load(open(f))
    data[d['pose']] = {'bbox': d['bbox'], 'points': {k: v for k, v in d['points'].items()}}
blink = sorted(p for p in data if os.path.exists(os.path.join(V, p + '_blink.png')))
beak = sorted(p for p in data if os.path.exists(os.path.join(V, p + '_beak.png')))
open(os.path.join(H, 'rig_data.js'), 'w').write('window.RIGDATA=' + json.dumps(data) + ';\nwindow.RIGVAR=' + json.dumps({'blink': blink, 'beak': beak}) + ';\n')
print('poses', len(data), 'blink', blink, 'beak', beak)
