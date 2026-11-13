import json, html
G='../grupo2_stories/geradas/'
CIRC='<div class="c" style="width:760px;height:760px;left:-220px;top:380px"></div><div class="c" style="width:700px;height:700px;right:-260px;top:880px"></div>'
def B(intro,key,after,x,y,w,tip,side='bottom'): return dict(intro=intro,key=key,after=after,x=x,y=y,w=w,tip=tip,side=side)
S=[
 dict(id='BD01',img=G+'BD01_segunda.png',theme='light',pill='Bom dia da Rara',title='Bom dia, presidente',lines=['a expressão de hoje é'],key='I’m running on coffee',after=['tô funcionando à base de café'],head=768),
 dict(id='BD02',img=G+'BD02_terca.png',theme='light',pill='Bom dia da Rara',title='Terça é dia de soltar o bico',hs=64,lines=[],key=None,after=[],head=9999,bal=B('a expressão de hoje é','rise and shine','levanta e brilha',24,430,640,(520,742))),
 dict(id='BD03',img=G+'BD03_quarta.png',theme='light',pill='Bom dia da Rara',title='Meio da semana, topete no lugar',hs=58,lines=['a expressão de hoje é'],key='looking sharp',after=['visual em dia'],head=696),
 dict(id='BD04',img=G+'BD04_quinta.png',theme='dark',pill='Bom dia da Rara',title='Quinta é dia de aquecer',hs=62,lines=[],key=None,after=[],head=9999,bal=B('repete comigo em voz alta','let’s warm up','a gente aquece junto',24,436,620,(505,690))),
 dict(id='BD05',img=G+'BD05_sexta.png',theme='light',pill='Bom dia da Rara',title='Sextou, mas antes uma frase',lines=['a expressão de hoje é'],key='that Friday feeling',after=['aquela sensação boa de fim de semana'],head=800),
 dict(id='BD06',img=G+'BD06_sabado.png',theme='light',pill='Bom dia da Rara',title='Sábado com calma',hs=70,lines=[],key=None,after=[],head=9999,bal=B('a expressão de hoje é','take it easy','hoje a gente só desacelera',24,450,660,(440,748))),
 dict(id='BD07',img=G+'BD07_domingo.png',theme='light',pill='Bom dia da Rara',title='Domingo leve, amanhã a gente volta',lines=['a expressão de hoje é'],key='lazy Sunday',after=['domingo preguiçoso, do jeito que tem que ser'],head=800),
 dict(id='QZ01',img=G+'QZ01_pergunta.png',theme='light',pill='Traduz aí, presidente',title='Como você diria “eu tô com fome” em inglês?',lines=[],key=None,after=['escolhe uma opção aí embaixo'],head=760),
 dict(id='QZ02',img=G+'QZ02_suspense.png',theme='light',pill='Traduz aí, presidente',title='E aí, qual você marcou?',lines=['eu tô roendo uma pena aqui'],key=None,after=[],head=728),
 dict(id='QZ03',cut='E02',bg='linear-gradient(170deg,#3FD493,#14935A)',theme='light',pill='Traduz aí, presidente',title=None,punch='Acertou',lines=['até meu topete ficou em pé'],key='I’m hungry',after=['em inglês, fome a gente é, não tem'],cutstyle='height:820px;left:190px;top:880px',head=860),
 dict(id='QZ04',cut='E08',bg='linear-gradient(170deg,#FF8A78,#E5503C)',theme='light',pill='Traduz aí, presidente',title='Errou? Treinou',lines=['a resposta certa é'],key='I’m hungry',after=['em inglês, fome a gente é, não tem'],cutstyle='height:820px;left:250px;top:900px',head=880),
 dict(id='QZ05',img=G+'QZ05_placar.png',theme='dark',pill='Traduz aí, presidente',title='X% acertaram',lines=['que coisa Rara!'],key=None,after=[],note='X = número real da enquete, preencher antes de publicar',head=700),
 dict(id='M01',cut='E09',bg='linear-gradient(170deg,#6D3DB8,#D26AA8)',theme='dark',pill='Modo carente',title=None,punch=None,lines=[],key=None,after=[],title2='E aí, meu chapa, já fez a lição hoje?',cutstyle='height:900px;left:300px;top:700px',head=690),
 dict(id='M02',img=G+'M02_espiando.png',theme='light',pill='Modo carente',title=None,punch='Já treinou hoje?',lines=['só dando uma espiadinha'],key=None,after=[],head=930),
 dict(id='M03',img=G+'M03_cha.png',theme='dark',pill='Modo carente',title='Fiz até um chazinho pra gente treinar',lines=['esfriou'],key=None,after=[],head=800),
 dict(id='M04',img=G+'M04_drama.png',theme='dark',pill='Modo carente',title=None,punch='Esperando',lines=['eu tô aqui, sozinha, com o fone'],key=None,after=[],head=630),
 dict(id='M05',img=G+'M05_cartaz.png',theme='light',pill='Modo carente',title=None,punch='Responde',lines=['só um oi, pode ser em inglês','pode ser errado'],key=None,after=[],sign='oi?',head=670),
 dict(id='M06',img=G+'M06_abdominal.png',theme='light',pill='Modo carente',title='Presidente, 3 minutinhos',lines=['eu conto como abdominal'],key=None,after=[],head=810),
]
def block(s):
    o=[]; b=s.get('bal'); hs=s.get('hs',80)
    if s['pill'].startswith('Traduz'): o.append(f'<div class="lbl">{html.escape(s["pill"])}</div>')
    else: o.append(f'<div class="tapew"><span class="tape">{html.escape(s["pill"])}</span></div>')
    if s.get('title2'): o.append(f'<h1 style="font-size:{hs}px">{html.escape(s["title2"])}</h1>')
    if s.get('title'): o.append(f'<h1 style="font-size:{hs}px">{html.escape(s["title"])}</h1>')
    if s.get('punch'): o.append(f'<div class="punch">{html.escape(s["punch"])}</div>')
    if s['lines']: o.append('<p class="sup">'+'<br>'.join(html.escape(x) for x in s['lines'])+'</p>')
    if s.get('key') and not b: o.append(f'<div class="key"><span class="k">{html.escape(s["key"])}</span></div>')
    if s['after'] and not b: o.append('<p class="sup a">'+'<br>'.join(html.escape(x) for x in s['after'])+'</p>')
    return '<div class="blk">'+''.join(o)+'</div>'
def story(s):
    bg=f'background-image:url({s["img"]})' if 'img' in s else f'background:{s["bg"]}'
    inner=''
    if 'cut' in s: inner+=CIRC+f'<img class="cut" src="../recortes/{s["cut"]}.png" style="{s["cutstyle"]}">'
    inner+=block(s)
    if s.get('bal'):
        b=s['bal']; inner+=f'<div class="bal" data-tip="{b["tip"][0]},{b["tip"][1]}" data-side="{b["side"]}" style="left:{b["x"]}px;top:{b["y"]}px;width:{b["w"]}px"><p class="i">{html.escape(b["intro"])}</p><div class="kk"><span class="k">{html.escape(b["key"])}</span></div><p class="a">{html.escape(b["after"])}</p></div>'
    if s.get('sign'): inner+=f'<div class="sign">{html.escape(s["sign"])}</div>'
    return f'<div class="st {s["theme"]}" id="{s["id"]}" data-head="{s.get("head",9999)}" style="{bg}">{inner}</div>'
CSS='''
@font-face{font-family:'Nunito';src:url('../_fontes/Nunito.ttf');font-weight:200 1000}
@font-face{font-family:'Mochiy';src:url('../_fontes/MochiyPopOne-Regular.ttf')}
*{box-sizing:border-box;margin:0;padding:0}
body{background:#000;width:1080px}
.st{position:relative;width:1080px;height:1920px;overflow:hidden;background-size:cover;background-position:center;font-family:'Nunito'}
.st.light{color:#081226}.st.dark{color:#fff}
.c{position:absolute;border-radius:50%;background:radial-gradient(circle,rgba(255,255,255,.28),rgba(255,255,255,.10) 62%,rgba(255,255,255,0) 70%)}
.cut{position:absolute;filter:drop-shadow(0 30px 34px rgba(0,0,0,.28))}
.lbl{display:flex;align-items:center;gap:16px;font-family:'Nunito';font-weight:900;font-size:40px;letter-spacing:.16em;text-transform:uppercase;margin-bottom:30px}
.lbl::after{content:'';width:56px;height:4px;border-radius:2px;background:currentColor}
.tapew{display:block;margin:0 0 34px 6px;filter:drop-shadow(0 5px 7px rgba(0,0,0,.28));display:inline-block;transform:rotate(-4deg)}
.tape{display:inline-block;font-family:'Mochiy';text-transform:lowercase;font-size:40px;line-height:1;color:#081226;background:#FFC83D;padding:14px 42px 14px 38px;clip-path:polygon(1% 6%,0 28%,2% 52%,0 76%,1% 96%,99% 100%,100% 74%,98% 50%,100% 24%,98% 2%)}
.blk{position:absolute;left:64px;right:64px;top:250px;z-index:5}
h1{font-weight:900;line-height:1.04;letter-spacing:-.01em;max-width:950px}
.punch{font-family:'Mochiy';text-transform:uppercase;font-size:118px;line-height:1.18}
.dark .punch{color:#FFC83D}
.sup{font-weight:800;font-size:46px;line-height:1.26;margin-top:20px}
.sup.a{margin-top:16px;font-size:42px}
.key{margin-top:14px}
.key .k{font-weight:900;font-size:84px;line-height:1.1;letter-spacing:-.01em}
.light .key .k{background:linear-gradient(transparent 50%,#FFC83D 50%,#FFC83D 92%,transparent 92%);padding:0 8px;margin-left:-8px}
.dark .key .k{color:#FFC83D}
.bal{position:absolute;z-index:6;background:#fff;color:#081226;border-radius:44px;border-bottom:16px solid #B9CCF2;padding:28px 40px 26px;box-shadow:0 22px 44px rgba(0,0,0,.26);transform:rotate(-1.2deg);word-break:keep-all;overflow-wrap:normal}
.bal .i,.bal .a{font-weight:800;font-size:40px;line-height:1.2}
.bal .kk{margin:6px 0 4px}
.bal .k{font-weight:900;font-size:76px;line-height:1.1;letter-spacing:-.01em;white-space:nowrap;background:linear-gradient(transparent 50%,#FFC83D 50%,#FFC83D 92%,transparent 92%);padding:0 6px;margin-left:-6px}
.sign{position:absolute;left:344px;top:1160px;width:368px;height:232px;display:flex;align-items:center;justify-content:center;font-weight:900;font-size:120px;color:#081226;z-index:5;transform:rotate(-2deg)}
'''
SV='<svg style="display:none"><symbol id="mic" viewBox="0 0 24 24" fill="none" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3Z"/><path d="M19 10v2a7 7 0 0 1-14 0v-2"/><line x1="12" x2="12" y1="19" y2="22"/></symbol></svg>'
SCRIPT="""<script>document.fonts.ready.then(()=>{
 const ns='http://www.w3.org/2000/svg';
 document.querySelectorAll('.st').forEach(st=>{
  const out={};
  st.querySelectorAll('.bal').forEach(b=>{
   const tip=b.dataset.tip.split(',').map(Number),x=b.offsetLeft,y=b.offsetTop,w=b.offsetWidth,h=b.offsetHeight;
   const pts=`${x+w*0.30},${y+h-12} ${x+w*0.30+110},${y+h-12} ${tip[0]},${tip[1]}`;
   let sv=st.querySelector('svg.t'); if(!sv){sv=document.createElementNS(ns,'svg');sv.setAttribute('class','t');sv.setAttribute('width',1080);sv.setAttribute('height',1920);sv.style.cssText='position:absolute;left:0;top:0;z-index:5';st.appendChild(sv)}
   const p=document.createElementNS(ns,'polygon');p.setAttribute('points',pts);p.setAttribute('fill','#fff');sv.appendChild(p);
  });
 });
 window.__done=true;});</script>"""
open('stories.html','w').write(f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>{CSS}</style></head><body>{SV}'+''.join(story(s) for s in S)+SCRIPT+'</body></html>')
json.dump([s['id'] for s in S],open('stories_ids.json','w'))
with open('../grupo2_stories/textos_stories.md','w') as f:
    f.write('# Textos dos stories da semana 1 (tom 3.1b, mínimo de 40 px)\n\n')
    for s in S:
        f.write(f'## {s["id"]} ({s["pill"]})\n')
        for k in ('title2','title','punch'):
            if s.get(k): f.write(f'- {k}: {s[k]}\n')
        for l in s['lines']: f.write(f'- apoio: {l}\n')
        if s.get('key'): f.write(f'- destaque: {s["key"]}\n')
        for l in s['after']: f.write(f'- depois: {l}\n')
        if s.get('bal'): f.write(f'- balão: {s["bal"]["intro"]} / {s["bal"]["key"]} / {s["bal"]["after"]}\n')
        if s.get('sign'): f.write(f'- no cartaz: {s["sign"]}\n')
        if s.get('note'): f.write(f'- nota: {s["note"]}\n')
        f.write('\n')
print(len(S))
