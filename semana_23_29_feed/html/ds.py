"""Sistema de layout do feed e dos stories da Arara (23/11/2026). Tokens e componentes padronizados.
Regras: leitura da esquerda para a direita e de cima para baixo; hierarquia titulo > subtitulo > status; quando ha fala, a fala e o foco;
balao so para conversa; botao de seta unico e redondo (sem texto); badge de idioma padronizado; CTA sem balao, em cor que contrasta."""
import os
HERE=os.path.dirname(os.path.abspath(__file__))
F=os.path.join(HERE,'..','..','semana1','_fontes')+'/'
# ---- tokens (px em 1080 de largura)
T=dict(label=28,title=66,sub=38,status=24,fala=58,fala_apoio=36,card_t=46,card_s=36,badge=24,cta=42)
TS=dict(label=32,title=74,sub=42,status=26,fala=62,fala_apoio=40,card_t=50,card_s=40,badge=26,cta=46)  # stories (1080x1920)
def css(theme, story=False):
    t=TS if story else T
    HLTXT='.hl{{background:none!important;color:var(--hl);padding:0!important;margin:0!important}}\n'.format() if theme.get('hltext') else ''
    ink,acc,hl,under=theme['ink'],theme['acc'],theme['hl'],theme['under']
    return f"""
@font-face{{font-family:'Nunito';src:url('file://{F}Nunito.ttf');font-weight:200 1000}}
@font-face{{font-family:'Mochiy';src:url('file://{F}MochiyPopOne-Regular.ttf')}}
@font-face{{font-family:'JP';src:url('file://{F}NotoSansJP.ttf');font-weight:100 900}}
@font-face{{font-family:'NSC';src:url('file://{F}NotoSansSC.ttf');font-weight:100 900}}
@font-face{{font-family:'NAR';src:url('file://{F}NotoSansArabic.ttf');font-weight:100 900}}
*{{box-sizing:border-box;margin:0;padding:0}} body{{background:#000}}
#post{{position:relative;width:1080px;height:{1920 if story else 1350}px;overflow:hidden;font-family:'Nunito','JP','Noto Color Emoji';color:{ink};--ink:{ink};--acc:{acc};--hl:{hl};--under:{under};--ctaacc:{theme.get('ctaacc',acc)}}}
.bg{{position:absolute;inset:0;width:1080px;height:{1920 if story else 1350}px;object-fit:cover}}
.zone{{position:absolute;left:64px;right:64px;top:{240 if story else 56}px;z-index:8;display:flex;flex-direction:column;align-items:flex-start}}
.ds-label{{font-weight:900;font-size:{t['label']}px;line-height:1;letter-spacing:.2em;text-transform:uppercase;display:flex;align-items:center;gap:14px;margin-bottom:{26 if not story else 30}px;color:var(--lbl,var(--ink))}}
.ds-label::after{{content:'';width:48px;height:4px;border-radius:2px;background:currentColor}}
.ds-status{{font-weight:800;font-size:{t['status']}px;line-height:1;letter-spacing:.16em;text-transform:uppercase;opacity:.78;margin-bottom:{22 if not story else 26}px}}
.ds-title{{font-weight:900;font-size:{t['title']}px;line-height:1.2;letter-spacing:-.01em;max-width:950px;margin-bottom:24px;color:var(--ttl,var(--ink))}}
.ds-title.small{{font-size:{int(t['title']*0.78)}px}}
.hl{{background:linear-gradient(transparent 58%,var(--hl) 58%,var(--hl) 94%,transparent 94%);-webkit-box-decoration-break:clone;box-decoration-break:clone;padding:0 8px;margin:0 -8px}}
{HLTXT}.ds-sub{{font-weight:800;font-size:{t['sub']}px;line-height:1.3;max-width:900px;margin-bottom:30px;color:var(--sub,var(--ink));opacity:.94}}
.ds-fala{{position:relative;z-index:8;background:transparent;padding:30px 56px 34px;filter:drop-shadow(0 16px 22px rgba(8,18,38,.24));--rad:58px 124px 66px 132px / 92px 58px 112px 62px;max-width:940px}}
.ds-fala.r0{{transform:rotate(-1.6deg)}}.ds-fala.r1{{transform:rotate(1.3deg)}}
.ds-fala::before{{content:'';position:absolute;inset:0;top:10px;border-radius:var(--rad);background:var(--under);z-index:-2}}
.ds-fala::after{{content:'';position:absolute;inset:0;border-radius:var(--rad);background:#fff;z-index:-1}}
.ds-fala .main{{font-weight:900;font-size:{t['fala']}px;line-height:1.15;color:#081226}}
.ds-fala .apoio{{font-weight:700;font-size:{t['fala_apoio']}px;line-height:1.25;margin-top:8px;color:#4A5D8F}}
.ds-fala .tail{{position:absolute;bottom:-88px;width:112px;height:100px;z-index:-1;overflow:visible}}
.ds-card{{background:#fff;border-radius:34px;border-bottom:12px solid var(--under);padding:24px 38px 26px;box-shadow:0 14px 30px rgba(8,18,38,.16);max-width:952px;color:#081226}}
.ds-card .ct{{font-weight:900;font-size:{t['card_t']}px;line-height:1.16}}
.ds-card .cs{{font-weight:800;font-size:{t['card_s']}px;line-height:1.25;margin-top:6px;color:#4A5D8F}}
.ds-badge{{display:inline-flex;align-items:center;justify-content:center;height:48px;padding:0 24px;border-radius:24px;font-weight:900;font-size:{t['badge']}px;letter-spacing:.14em;text-transform:uppercase;background:#081226;color:#fff;margin-bottom:14px;white-space:nowrap}}
.ds-title,.ds-sub,.ds-cta>div:last-child,.ds-fala .main{{text-wrap:balance}}
.ds-cta{{display:flex;align-items:center;gap:18px;font-weight:900;font-size:{t['cta']}px;line-height:1.22;color:var(--cta,var(--ink));max-width:900px}}
.ds-cta .ic{{flex:none;width:64px;height:64px;border-radius:50%;background:var(--acc);display:flex;align-items:center;justify-content:center}}
.ds-cta .ic svg{{width:34px;height:34px;stroke:#081226;fill:none;stroke-width:2.6;stroke-linecap:round;stroke-linejoin:round}}
.ds-cta b{{color:var(--ctaacc,var(--acc))}}
.ds-nav{{position:absolute;right:36px;bottom:36px;z-index:9;width:68px;height:68px;border-radius:50%;background:#FFC83D;display:flex;align-items:center;justify-content:center;border:3px solid #081226;box-shadow:0 5px 0 rgba(8,18,38,.28),0 10px 18px rgba(0,0,0,.14)}}
.ds-nav svg{{width:36px;height:36px;stroke:#081226;fill:none;stroke-width:3;stroke-linecap:round;stroke-linejoin:round}}
.ds-punch{{font-family:'Mochiy';font-size:{int(t['title']*1.5)}px;line-height:1.1;text-transform:uppercase;color:var(--acc);margin-bottom:20px;max-width:950px}}
.ds-chip{{display:inline-flex;align-items:center;gap:14px;height:62px;padding:0 26px 0 12px;border-radius:31px;background:#fff;color:#081226;font-weight:900;font-size:{t['card_s']}px;border-bottom:6px solid var(--under);box-shadow:0 8px 16px rgba(8,18,38,.14);white-space:nowrap}}
.ds-chip .ib{{width:42px;height:42px;border-radius:50%;background:#FFC83D;display:flex;align-items:center;justify-content:center}}
.ds-chip .ib svg{{width:24px;height:24px;stroke:#081226;fill:none;stroke-width:2.6;stroke-linecap:round;stroke-linejoin:round}}
.ds-scrim{{position:absolute;left:0;right:0;bottom:0;height:430px;background:linear-gradient(0deg,rgba(8,18,38,.78),rgba(8,18,38,0));z-index:7}}
.ds-caption{{position:absolute;left:64px;bottom:58px;max-width:800px;z-index:8;font-weight:900;font-size:{int(t['title']*0.82)}px;line-height:1.2;color:#fff;text-shadow:0 2px 12px rgba(0,0,0,.35);text-wrap:balance}}
.ds-caption b{{color:#FFC83D}}
.gap{{height:var(--g,24px)}}
"""
ARR='<svg viewBox="0 0 24 24"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg>'
SEND='<svg viewBox="0 0 24 24"><path d="M14.536 21.686a.5.5 0 0 0 .937-.024l6.5-19a.496.496 0 0 0-.635-.635l-19 6.5a.5.5 0 0 0-.024.937l7.93 3.18a2 2 0 0 1 1.112 1.11z"/><path d="m21.854 2.147-10.94 10.939"/></svg>'
SAVE='<svg viewBox="0 0 24 24"><path d="m19 21-7-4-7 4V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2v16z"/></svg>'
MSG='<svg viewBox="0 0 24 24"><path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z"/></svg>'
TAILSVG='<svg class="tail" viewBox="0 0 112 100"><path d="M8 0 C 8 44 40 80 106 96 C 66 70 62 34 94 0 Z" fill="#fff"/></svg>'
def label(t): return f'<div class="ds-label">{t}</div>'
def status(t): return f'<div class="ds-status">{t}</div>'
def title(t,small=False): return f'<div class="ds-title{" small" if small else ""}" data-box="title">{t}</div>'
def sub(t): return f'<div class="ds-sub" data-box="sub">{t}</div>'
def badge(t): return f'<div class="ds-badge">{t}</div>'
def card(t,s='',extra=''): return f'<div class="ds-card" data-box="card">{extra}<div class="ct">{t}</div>'+(f'<div class="cs">{s}</div>' if s else '')+'</div>'
def cta(text,icon=SEND): return f'<div class="ds-cta" data-box="cta"><div class="ic">{icon}</div><div>{text}</div></div>'
def punch(t): return f'<div class="ds-punch" data-box="punch">{t}</div>'
def chip(t,icon=''): return f'<div class="ds-chip">'+(f'<span class="ib">{icon}</span>' if icon else '')+f'{t}</div>'
def caption(t): return '<div class="ds-scrim"></div><div class="ds-caption" data-box="caption">'+t+'</div>'
def nav(): return f'<div class="ds-nav">{ARR}</div>'
def zone(*items): return '<div class="zone" data-box="zone">'+''.join(items)+'</div>'
def fala(main,apoio='',idx=0,hx=540,cy=500,top_min=112,extra_main_css=''):
    """balao de conversa ancorado na cabeca: ponta do rabinho ~52 px acima do topo (cy), rabinho apontando para hx"""
    ap=f'<div class="apoio">{apoio}</div>' if apoio else ''
    return (f'<div class="ds-fala r{idx%2}" data-box="fala" data-hx="{hx}" data-cy="{cy}" data-min="{top_min}" style="position:absolute;left:64px;width:952px"><div class="main" style="{extra_main_css}">{main}</div>{ap}{TAILSVG}</div>')
FIT_JS='''<script>document.fonts.ready.then(()=>{document.querySelectorAll('.ds-fala').forEach(b=>{const hx=+b.dataset.hx,cy=+b.dataset.cy,mn=+b.dataset.min;const L=b.offsetLeft;const kids=[...b.querySelectorAll('.main,.apoio,.main *')].map(e=>[e,parseFloat(getComputedStyle(e).fontSize)]);let k=1;function fit(){kids.forEach(([e,f])=>e.style.fontSize=(f*k)+'px');b.style.top=((cy-136)-b.offsetHeight)+'px'}fit();while(b.offsetTop<mn&&k>0.8){k-=0.04;fit()}const t=b.querySelector('.tail');const flip=b.classList.contains('r1');t.style.left=Math.max(30,Math.min(b.offsetWidth-150,flip?(hx+14-L):(hx-126-L)))+'px';if(flip)t.style.transform='scaleX(-1)'})})</script>'''
def doc(theme,bg,body,story=False,extra_css=''):
    img=f'<img class="bg" src="file://{bg}">' if bg and not bg.startswith('<') else (bg or '')
    return f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>{css(theme,story)}{extra_css}</style></head><body><div id="post">{img}{body}</div>{FIT_JS}</body></html>'
