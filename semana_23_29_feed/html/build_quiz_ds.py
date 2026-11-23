import subprocess, json
import ds
G='/home/rodrigo/.openclaw/workspace/arara_social/semana_23_29_feed/gen/'
H='/home/rodrigo/.openclaw/workspace/arara_social/semana_23_29_feed/html/'
O='/home/rodrigo/.openclaw/workspace/arara_social/semana_23_29_feed/final/'
TH=dict(ink='#081226',acc='#FFC83D',hl='#1B4FE0',under='#E6C65A',hltext=1,ctaacc='#1B4FE0')
LB=ds.label('Quiz da Rara')
def opt(l,t,dim=False,ok=False):
    st='opacity:.55;' if dim else ''
    if ok: return f'<div class="ds-card" data-box="card" style="background:#2FB45A;border-bottom-color:#1E8A40;color:#fff;display:flex;gap:20px;align-items:center;padding:18px 34px"><div style="width:54px;height:54px;border-radius:50%;background:rgba(255,255,255,.28);display:flex;align-items:center;justify-content:center;font-weight:900;font-size:30px;flex:none">{l}</div><div><div class="ct" style="color:#fff;font-size:44px">{t}</div><div class="cs" style="color:#E8FFEF">Quer dizer “está na ponta da língua”</div></div></div>'
    return f'<div class="ds-chip" style="{st}"><span class="ib" style="background:#081226;color:#fff;font-weight:900;font-size:22px">{l}</span>{t}</div>'
def pair(lang,t,s): return ds.badge(lang)+ds.card(t,s)+'<div class="gap" style="--g:24px"></div>'
S=[(1,ds.zone(LB,ds.title('A palavra <span class="hl">sumiu</span> na hora de falar?'),ds.sub('Em inglês, o que você diz? Escolhe uma letra e comenta antes de arrastar'),
     '<div style="display:flex;flex-direction:column;gap:12px">'+opt('A','It’s on the tip of my tongue')+opt('B','My head is empty')+opt('C','I lost my words')+'</div>')+ds.nav()),
(2,ds.zone(LB,ds.status('Resposta certa, letra A'),ds.badge('Em inglês'),opt('A','It’s on the tip of my tongue',ok=True),'<div class="gap" style="--g:14px"></div><div style="display:flex;flex-direction:column;gap:10px">'+opt('B','My head is empty',dim=True)+opt('C','I lost my words',dim=True)+'</div>','<div class="gap" style="--g:20px"></div>'+ds.sub('É igualzinho ao português, dá pra acreditar?'))+ds.nav()),
(3,ds.zone(LB,ds.badge('Em espanhol'),ds.card('Lo tengo en la punta de la lengua','Eu tenho na ponta da língua'))+ds.nav()),
(4,ds.zone(LB,ds.badge('Em francês'),ds.card('Je l’ai sur le bout de la langue','Eu tenho na ponta da língua'))+ds.nav()),
(5,ds.zone(LB,pair('Em alemão','Es liegt mir auf der Zunge','Está na minha língua'),pair('Em italiano','Ce l’ho sulla punta della lingua','Eu tenho na ponta da língua'))+ds.nav()),
(6,ds.zone(LB,ds.title('Deu branco? <span class="hl">Acontece</span> com todo mundo'),ds.cta('Comenta qual idioma <b>te surpreendeu</b> mais',ds.MSG)))]
for n,body in S:
    k=f'traduz-ponta-lingua-{n}'
    open(H+k+'.html','w').write(ds.doc(TH,G+f'ta_bg_{n}.jpg',body))
    r=subprocess.run(['node',H+'render_a.mjs',H+k+'.html',O+k+'.jpg','1080','1350'],capture_output=True,text=True)
    z=json.loads(r.stdout.strip().splitlines()[-1]).get('zone') if r.stdout.strip() else None
    print(n,'zona',z,r.stderr[:100])
