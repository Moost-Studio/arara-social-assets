#!/usr/bin/env python3
"""Compõe as 15 telas (5 episódios x 3) do Diário da Rara e da História do Raro, semana 23 a 29/11/2026.
Texto por código sobre a cena gerada. Uso: python3 compor_telas.py  (gera HTML em semana1/_scripts/diario_*.html e PNGs em telas/)."""
import json, pathlib, subprocess, html
HERE = pathlib.Path(__file__).resolve().parent
SC = HERE.parent / 'semana1' / '_scripts'
# topo do personagem em px (1920): onde o balão NÃO pode chegar
EPS = {
 'seg': dict(img='seg_escritorio_v1.jpg', sel='DIÁRIO DA RARA', topo=613, titulo='Segunda e eu cheguei primeiro', kw='primeiro',
   telas=[ ['são 7h e o escritório inteiro é meu'],
           ['ensaiei o japonês do trabalho em voz alta', '<small>お疲れ様です (otsukaresama desu) pra cadeira, e ela nem respondeu</small>'],
           ['só tem um detalhe', '<small>amanhã eu conto por que ninguém chegou</small>'] ]),
 'qua': dict(img='qua_call_v2.jpg', sel='DIÁRIO DA RARA', topo=589, titulo='A call que só eu ouvi', kw='só eu',
   telas=[ ['10h, call importante, eu estava inspirada'],
           ['falei por dez minutos', '<small>o microfone estava no mudo</small>'],
           ['errou? treinou', '<small>agora eu confiro antes de falar</small>'] ]),
 'sex': dict(img='sex_fila_v1.jpg', sel='DIÁRIO DA RARA', topo=819, titulo='A fila da Black Friday', kw='fila',
   telas=[ ['a fila dá duas voltas no poleiro'],
           ['aprendi duas palavras na fila', '<small>sale, liquidação</small><small>discount, desconto</small>'],
           ['no fim saí com um suporte de microfone', '<small>amanhã o primo liga</small>'] ]),
 'sab': dict(img='sab_raro_v3.jpg', sel='HISTÓRIA DO RARO', topo=669, titulo='De onde vem sábado', kw='sábado',
   telas=[ ['bah, prima, hoje é sábado e tu sabe de onde vem essa palavra'],
           ['vem do hebraico, onde quer dizer descanso', '<small>passou pelo grego e pelo latim até chegar no nosso português</small>'],
           ['por isso sábado combina com rede', '<small>devagar se vai ao longe, tchê</small>'] ]),
 'dom': dict(img='dom_resumo_v2.jpg', sel='DIÁRIO DA RARA', topo=648, titulo='O resumo da semana', kw='resumo',
   telas=[ ['domingo é dia de contar os micos'],
           ['errei na call, errei na fila e errei a hora de chegar'],
           ['e tudo bem, errou? treinou', '<small>segunda tem mais</small>'] ]),
}
CSS = """@font-face{font-family:'Nunito';src:url('../_fontes/Nunito.ttf');font-weight:200 1000}
@font-face{font-family:'Mochiy';src:url('../_fontes/MochiyPopOne-Regular.ttf')}
@font-face{font-family:'JP';src:url('../_fontes/NotoSansJP.ttf')}
*{box-sizing:border-box;margin:0;padding:0}
#post{position:relative;width:1080px;height:1920px;overflow:hidden;font-family:'Nunito','JP';color:#081226;background:#222}
.bg{position:absolute;inset:0;background-size:cover;background-position:center}
.veil{position:absolute;left:0;right:0;top:0;height:640px;background:linear-gradient(180deg,rgba(255,255,255,.55),rgba(255,255,255,0))}
.sel{position:absolute;left:72px;top:92px;font-weight:900;font-size:38px;letter-spacing:.2em;display:flex;align-items:center;gap:16px}
.sel::after{content:'';width:56px;height:5px;border-radius:3px;background:currentColor}
.pg{position:absolute;right:72px;top:96px;font-weight:900;font-size:34px;letter-spacing:.12em;opacity:.7}
.tit{position:absolute;left:72px;right:72px;top:168px;font-family:'Mochiy';font-size:74px;line-height:1.12}
.tit b{font-weight:400;background:linear-gradient(transparent 55%,#FFC83D 55%,#FFC83D 94%,transparent 94%);padding:0 6px;margin-left:-6px}
.bal{position:absolute;left:72px;right:72px;background:#fff;border-radius:38px;padding:34px 42px;box-shadow:0 18px 40px rgba(0,0,0,.22);font-weight:800;font-size:50px;line-height:1.22}
.bal small{display:block;font-weight:700;font-size:40px;line-height:1.25;color:#2E3A55;margin-top:12px}
.bal::after{content:'';position:absolute;left:210px;bottom:-34px;width:0;height:0;border-left:30px solid transparent;border-right:30px solid transparent;border-top:36px solid #fff}
"""
def tela(ep, d, i, linhas):
    t = d['titulo'].replace(d['kw'], f"<b>{d['kw']}</b>")
    bal = ''.join(f'<div>{l}</div>' if not l.startswith('<small') else l for l in linhas)
    titulo = f'<div class="tit">{t}</div>' if i == 0 else ''
    return f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>{CSS}</style></head><body><div id="post">
<div class="bg" style="background-image:url('../../semana_23_29_diario/geradas/{d['img']}')"></div><div class="veil"></div>
<div class="sel">{d['sel']}</div><div class="pg">{i+1} DE 3</div>{titulo}
<div class="bal" id="bal">{bal}</div></div>
<script>
const b=document.getElementById('bal');const topo={d['topo']};const bottomMax=topo-80;
// ancora o balão logo acima do topo do personagem (rabinho 36 px) e deixa crescer para cima
b.style.top=(bottomMax-36-b.offsetHeight)+'px';
</script></body></html>"""
def main():
    medidas = {}
    for ep, d in EPS.items():
        for i, linhas in enumerate(d['telas']):
            n = SC / f'diario_{ep}_{i+1}.html'
            n.write_text(tela(ep, d, i, linhas), encoding='utf-8')
            out = HERE / 'telas' / f'{ep}_{i+1}.png'
            subprocess.run(['node', 'render_post.mjs', n.name, str(out), '1080', '1920'], cwd=SC, check=True)
    print('ok')
main()
