#!/usr/bin/env python3
"""Compõe as 15 telas (5 episódios x 3) do Diário da Rara e da História do Raro, semana 23 a 29/11/2026.
Texto por código sobre a cena gerada. Uso: python3 compor_telas.py  (gera HTML em semana1/_scripts/diario_*.html e PNGs em telas/)."""
import json, pathlib, subprocess, html
HERE = pathlib.Path(__file__).resolve().parent
SC = HERE.parent / 'semana1' / '_scripts'
# topo do personagem em px (1920): onde o balão NÃO pode chegar
HX = {'seg':[540,540,540],'qua':[560,560,560],'sex':[470,480,480],'sab':[590,590,780],'dom':[570,570,570]}
EPS = {
 'seg': dict(img=['seg_escritorio_v1.jpg', 'seg_2.jpg', 'seg_3.jpg'], sel='DIÁRIO DA RARA', topo=[613, 613, 470], titulo='Cheguei primeiro', kw='primeiro',
   telas=[ ['Hoje eu cheguei às 7h e o escritório inteiro estava vazio, só pra mim'],
           ['Aproveitei pra treinar o japonês do trabalho em voz alta. Falei <span style="white-space:nowrap">「お疲れ様です」</span>, que quer dizer “obrigada pelo esforço”, pra uma cadeira vazia', '<small>e a cadeira, claro, não respondeu</small>'],
           ['Aí eu descobri por que ninguém veio... é feriado no Japão...'] ]),
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
.bal{position:absolute;left:84px;right:92px;background:transparent;padding:40px 58px 42px;font-weight:800;font-size:50px;line-height:1.22;filter:drop-shadow(0 16px 22px rgba(8,18,38,.22));z-index:3;--rad:58px 124px 66px 132px / 92px 58px 112px 62px}
.bal.r0{transform:rotate(-2deg)}.bal.r1{transform:rotate(1.6deg)}
.bal::before{content:'';position:absolute;inset:0;top:10px;border-radius:var(--rad);background:#BCD0F5;z-index:-2}
.bal::after{content:'';position:absolute;inset:0;border-radius:var(--rad);background:#fff;z-index:-1}
.bal small{display:block;font-weight:700;font-size:40px;line-height:1.25;color:#2E3A55;margin-top:12px}
.tail{position:absolute;bottom:-88px;width:112px;height:100px;z-index:-1;overflow:visible}
"""
def tela(ep, d, i, linhas):
    t = d['titulo'].replace(d['kw'], f"<b>{d['kw']}</b>")
    bal = ''.join(f'<div>{l}</div>' if not l.startswith('<small') else l for l in linhas)
    titulo = f'<div class="tit">{t}</div>' if i == 0 else ''
    hx = HX[ep][i]
    esq = (i % 2 == 0)
    cauda = (max(40, min(660, hx - 210)), '') if esq else (max(40, min(660, hx - 70)), 'transform:scaleX(-1);')
    return f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>{CSS}</style></head><body><div id="post">
<div class="bg" style="background-image:url('../../semana_23_29_diario/geradas/{d['img'][i]}')"></div><div class="veil"></div>
<div class="sel">{d['sel']}</div><div class="pg">{i+1} DE 3</div>{titulo}
<div class="bal r{i%2}" id="bal">{bal}<svg class="tail" viewBox="0 0 112 100" style="left:{cauda[0]}px;{cauda[1]}"><path d="M8 0 C 8 44 40 80 106 96 C 66 70 62 34 94 0 Z" fill="#fff"/></svg></div></div>
<script>
const b=document.getElementById('bal');const topo={d['topo'][i]};const bottomMax=topo-80;
// ancora o balão logo acima do topo do personagem (rabinho 36 px) e deixa crescer para cima
const tit=document.querySelector('.tit');const minTop=tit?(tit.offsetTop+tit.offsetHeight+28):150;
let fs=50,sm=40;
function ajusta(){{b.style.fontSize=fs+'px';b.querySelectorAll('small').forEach(e=>{{e.style.fontSize=sm+'px'}});b.style.top=(topo-124-b.offsetHeight)+'px';}}
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
