import numpy as np, subprocess, os
from PIL import Image, ImageFilter
HERE=os.path.dirname(os.path.abspath(__file__))
K=0.78
def bg(src,out):
    im=Image.open(src).convert('RGB'); w,h=int(1080*K),int(1350*K); im=im.resize((w,h),Image.LANCZOS)
    L=(1080-w)//2; T=1350-h
    a=np.pad(np.array(im),((T,0),(L,1080-w-L),(0,0)),mode='edge')
    base=Image.fromarray(a).filter(ImageFilter.GaussianBlur(40))
    mask=Image.new('L',(1080,1350),0); m=np.zeros((1350,1080),np.float32)
    m[T:,L:L+w]=1
    mk=Image.fromarray((m*255).astype('uint8')).filter(ImageFilter.GaussianBlur(14))
    # reforco: dentro do retangulo, mascara 1 (apos blur perde nas bordas internas; mistura com o blur do fundo e ok)
    full=Image.new('RGB',(1080,1350)); full.paste(im,(L,T))
    # padded sharp para evitar halo
    sharp=Image.fromarray(a)
    comp=Image.composite(sharp,base,mk)
    comp.save(out,quality=95)
FONTS="""@font-face{font-family:'Nunito';src:url('../../semana1/_fontes/Nunito.ttf');font-weight:200 1000}
@font-face{font-family:'Mochiy';src:url('../../semana1/_fontes/MochiyPopOne-Regular.ttf')}"""
CSS=FONTS+"""
*{box-sizing:border-box;margin:0;padding:0}body{background:#000}
#post{position:relative;width:1080px;height:1350px;overflow:hidden;font-family:'Nunito';color:#081226}
.bg{position:absolute;inset:0;width:1080px;height:1350px}
.lbl{position:absolute;left:64px;top:62px;display:flex;align-items:center;gap:16px;font-weight:900;font-size:32px;letter-spacing:.2em;text-transform:uppercase}
.lbl::after{content:'';width:56px;height:4px;border-radius:2px;background:currentColor}
h1{position:absolute;left:64px;font-weight:900;line-height:1.04;letter-spacing:-.01em}
.bl{color:#1B4FE0}
.card{position:absolute;left:64px;width:952px;background:#fff;border-radius:34px;border-bottom:12px solid #D9B63A;padding:26px 40px 24px;box-shadow:0 14px 30px rgba(120,80,0,.18)}
.chip{display:inline-flex;align-items:center;gap:10px;background:#081226;color:#fff;font-weight:900;font-size:28px;letter-spacing:.14em;text-transform:uppercase;padding:8px 22px;border-radius:999px;margin-bottom:14px}
.ph{font-weight:900;font-size:64px;line-height:1.06;letter-spacing:-.01em}
.pt{font-weight:800;font-size:40px;line-height:1.2;margin-top:10px;color:#2b3a5c}
.opt{position:absolute;left:64px;display:flex;align-items:center;gap:16px;background:#fff;border-radius:20px;height:60px;padding:0 24px 0 10px;font-weight:800;font-size:36px;box-shadow:0 8px 0 rgba(120,80,0,.22)}
.opt b{width:42px;height:42px;border-radius:50%;background:#081226;color:#fff;display:flex;align-items:center;justify-content:center;font-weight:900;font-size:26px}
.pill{position:absolute;display:flex;gap:18px;align-items:center;background:rgba(255,255,255,.92);border-radius:999px;font-weight:800;font-size:30px;padding:8px 10px 8px 26px}
.btn{width:54px;height:54px;border-radius:50%;background:#FFC83D;display:flex;align-items:center;justify-content:center;box-shadow:0 5px 0 rgba(0,0,0,.22)}
svg.i{width:30px;height:30px;stroke:#081226;fill:none;stroke-width:2.6;stroke-linecap:round;stroke-linejoin:round}
"""
ARR='<svg class="i" viewBox="0 0 24 24"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg>'
CHK='<svg class="i" viewBox="0 0 24 24" style="stroke:#fff;width:34px;height:34px"><path d="M20 6 9 17l-5-5"/></svg>'
MSG='<svg class="i" viewBox="0 0 24 24" style="width:40px;height:40px"><path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z"/></svg>'
def page(n,img,body):
    html=f"<!doctype html><html lang='pt-BR'><head><meta charset='utf-8'><style>{CSS}</style></head><body><div id='post'><img class='bg' src='../gen/{img}'><div class='lbl'>Traduz aí, presidente</div>{body}</div></body></html>"
    open(f'{HERE}/html/ta_{n}.html','w').write(html)
    subprocess.check_call(['node','/home/rodrigo/.openclaw/workspace/arara_social/semana1/_scripts/render_post.mjs',f'{HERE}/html/ta_{n}.html',f'{HERE}/gen/ta_final_{n}.png','1080','1350'])
    Image.open(f'{HERE}/gen/ta_final_{n}.png').convert('RGB').save(f'{HERE}/final/traduz-ponta-lingua-{n}.jpg',quality=92)
srcs={1:'ta_s1_estudio.jpg',2:'ta_s2.jpg',3:'ta_s3.jpg',4:'ta_s4.jpg',5:'ta_s5.jpg',6:'ta_s6.jpg'}
for n,s in srcs.items(): bg(f'{HERE}/gen/{s}',f'{HERE}/gen/ta_bg_{n}.jpg')
pill=f'<div class="pill" style="right:44px;bottom:16px"><span>Arrasta para o lado</span><div class="btn">{ARR}</div></div>'
page(1,'ta_bg_1.jpg',f"""<h1 style="top:112px;font-size:76px;width:960px">Sabe a palavra, mas ela <span class="bl">sumiu</span>?</h1>
<div style="position:absolute;left:64px;top:280px;font-weight:800;font-size:38px">em inglês, o que você diz?</div>
<div style="position:absolute;left:64px;top:332px;font-weight:900;font-size:34px;background:#081226;color:#fff;padding:6px 22px;border-radius:999px">Comenta a letra antes de arrastar</div>
<div class="opt" style="top:410px"><b>A</b>It’s on the tip of my tongue</div>
<div class="opt" style="top:482px"><b>B</b>My head is empty</div>
<div class="opt" style="top:554px"><b>C</b>I lost my words</div>{pill}""")
page(2,'ta_bg_2.jpg',f"""<div class="chip" style="position:absolute;left:64px;top:118px">Inglês</div>
<div class="card" style="top:178px;background:#2FB45A;border-bottom-color:#1E8A40;color:#fff;padding:20px 40px 20px;display:flex;gap:22px;align-items:center"><div style="width:62px;height:62px;border-radius:50%;background:rgba(255,255,255,.25);display:flex;align-items:center;justify-content:center;flex:none"><span style="font-weight:900;font-size:36px">A</span></div><div><div class="ph" style="font-size:54px">It’s on the tip of my tongue</div><div class="pt" style="color:#E8FFEF;margin-top:4px;font-size:38px">tá na ponta da língua</div></div></div>
<div class="opt" style="top:372px;opacity:.55"><b>B</b>My head is empty</div>
<div class="opt" style="top:444px;opacity:.55"><b>C</b>I lost my words</div>
<div style="position:absolute;left:64px;top:536px;font-weight:900;font-size:40px">igualzinho ao português, acredita?</div>{pill}""")
page(3,'ta_bg_3.jpg',f"""<div class="card" style="top:140px"><div class="chip">Espanhol</div><div class="ph">Lo tengo en la punta de la lengua</div><div class="pt">eu tenho na ponta da língua</div></div>{pill}""")
page(4,'ta_bg_4.jpg',f"""<div class="card" style="top:140px"><div class="chip">Francês</div><div class="ph">Je l’ai sur le bout de la langue</div><div class="pt">eu tenho na ponta da língua</div></div>{pill}""")
page(5,'ta_bg_5.jpg',f"""<div class="card" style="top:116px;padding:20px 40px 18px"><div class="chip" style="margin-bottom:8px">Alemão</div><div class="ph" style="font-size:56px">Es liegt mir auf der Zunge</div><div class="pt" style="margin-top:4px">está na minha língua</div></div>
<div class="card" style="top:352px;padding:20px 40px 18px"><div class="chip" style="margin-bottom:8px">Italiano</div><div class="ph" style="font-size:56px">Ce l’ho sulla punta della lingua</div><div class="pt" style="margin-top:4px">eu tenho na ponta da língua</div></div>{pill}""")
page(6,'ta_bg_6.jpg',f"""<h1 style="top:120px;font-size:84px;width:940px">Deu branco? <span class="bl">Acontece</span> com todo mundo</h1>
<div class="card" style="top:400px;display:flex;gap:22px;align-items:center;padding:22px 34px"><div style="width:64px;height:64px;border-radius:50%;background:#FFC83D;display:flex;align-items:center;justify-content:center;flex:none">{MSG}</div><div style="font-weight:900;font-size:44px;line-height:1.1">comenta qual idioma te surpreendeu</div></div>""")
