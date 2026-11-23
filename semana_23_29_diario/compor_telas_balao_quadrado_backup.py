#!/usr/bin/env python3
"""Compõe as 15 telas (5 episódios x 3) do Diário da Rara e da História do Raro, semana 23 a 29/11/2026.
Texto por código sobre a cena gerada. Uso: python3 compor_telas.py  (gera HTML em semana1/_scripts/diario_*.html e PNGs em telas/)."""
import json, pathlib, subprocess, html
HERE = pathlib.Path(__file__).resolve().parent
SC = HERE.parent / 'semana1' / '_scripts'
# topo do personagem em px (1920): onde o balão NÃO pode chegar
EPS = {
 'seg': dict(img=['seg_escritorio_v1.jpg', 'seg_2.jpg', 'seg_3.jpg'], sel='DIÁRIO DA RARA', topo=[613, 613, 470], titulo='Cheguei primeiro', kw='primeiro',
   telas=[ ['Hoje eu cheguei às 7h e o escritório inteiro estava vazio, só pra mim'],
           ['Aproveitei pra treinar o japonês do trabalho em voz alta. Falei <span style="white-space:nowrap">「お疲れ様です」</span>, que quer dizer “obrigada pelo esforço”, pra uma cadeira vazia', '<small>e a cadeira, claro, não respondeu</small>'],
           ['Aí eu descobri por que ninguém veio, hoje é feriado no Japão'] ]),
 'qua': dict(img=['qua_call_v5.jpg', 'qua_2_v4.jpg', 'qua_3_v5.jpg'], sel='DIÁRIO DA RARA', topo=[589, 520, 589], titulo='A call que só eu ouvi', kw='só eu',
   telas=[ ['Hoje às 10h eu tinha uma call importante e acordei muito inspirada'],
           ['Falei por dez minutos seguidos. Só que o meu microfone estava no mudo, então ninguém me ouviu'],
           ['Agora, antes de falar, eu sempre confiro o ícone do microfone', '<small>E se eu errar de novo, é só tentar outra vez. Bora de novo?</small>'] ]),
 'sex': dict(img=['sex_fila_v1.jpg', 'sex_2.jpg', 'sex_3.jpg'], sel='DIÁRIO DA RARA', topo=[819, 819, 819], titulo='A fila da Black Friday', kw='fila',
   telas=[ ['A fila da loja deu duas voltas no quarteirão, e eu fiquei nela'],
           ['Enquanto esperava, aprendi duas palavras em inglês', '<small>“sale” quer dizer liquidação</small><small>“discount” quer dizer desconto</small>'],
           ['No fim, saí da fila só com um suporte de microfone', '<small>Amanhã o meu primo Raro conta uma história</small>'] ]),
 'sab': dict(img=['sab_raro_v3.jpg', 'sab_2.jpg', 'sab_3.jpg'], sel='HISTÓRIA DO RARO', topo=[669, 669, 780], titulo='De onde vem sábado', kw='sábado',
   telas=[ ['Ooooopaaa, bão? Eu sou o Raro, primo da Rara. Hoje é sábado, uai, e ocê sabe de onde vem essa palavra?'],
           ['Ela vem do hebraico, sô, e lá quer dizer “descanso”', '<small>Passou pelo grego e pelo latim até chegar no nosso português</small>'],
           ['Por isso sábado combina tanto com rede, uai', '<small>Devagar se vai ao longe, sô. Amanhã a Rara volta com o resumo da semana</small>'] ]),
 'dom': dict(img=['dom_resumo_v2.jpg', 'dom_2.jpg', 'dom_3.jpg'], sel='DIÁRIO DA RARA', topo=[648, 429, 648], titulo='O resumo da semana', kw='resumo',
   telas=[ ['Domingo é dia de contar os micos da semana'],
           ['Essa semana falei no mudo, comprei só um suporte e cheguei num escritório vazio'],
           ['E tudo bem, porque é errando que a gente aprende', '<small>Segunda tem mais. Bora de novo?</small>'] ]),
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
<div class="bg" style="background-image:url('../../semana_23_29_diario/geradas/{d['img'][i]}')"></div><div class="veil"></div>
<div class="sel">{d['sel']}</div><div class="pg">{i+1} DE 3</div>{titulo}
<div class="bal" id="bal" style="">{bal}</div></div>
<script>
const b=document.getElementById('bal');const topo={d['topo'][i]};const bottomMax=topo-80;
// ancora o balão logo acima do topo do personagem (rabinho 36 px) e deixa crescer para cima
const tit=document.querySelector('.tit');const minTop=tit?(tit.offsetTop+tit.offsetHeight+28):150;
let fs=50,sm=40;
function ajusta(){{b.style.fontSize=fs+'px';b.querySelectorAll('small').forEach(e=>{{e.style.fontSize=sm+'px'}});b.style.top=(bottomMax-36-b.offsetHeight)+'px';}}
ajusta();
while(b.offsetTop<minTop&&fs>40){{fs-=2;sm=Math.max(36,sm-2);ajusta();}}
if(b.offsetTop<minTop){{b.style.padding='22px 40px';ajusta();}}
document.title='fs='+fs+' top='+b.offsetTop+' min='+minTop;
</script></body></html>"""
def main():
    medidas = {}
    import sys
    only = sys.argv[1:]
    for ep, d in EPS.items():
        if only and ep not in only: continue
        for i, linhas in enumerate(d['telas']):
            n = SC / f'diario_{ep}_{i+1}.html'
            n.write_text(tela(ep, d, i, linhas), encoding='utf-8')
            out = HERE / 'telas' / f'{ep}_{i+1}.png'
            subprocess.run(['node', 'render_post.mjs', n.name, str(out), '1080', '1920'], cwd=SC, check=True)
    print('ok')
main()
