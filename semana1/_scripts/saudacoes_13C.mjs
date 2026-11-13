// Carrossel de saudações (13C, Dia Mundial da Saudação, sáb 21/11): capa em leque + PM01 a PM05, 1080x1350.
import { createRequire } from 'module';
const require = createRequire('/home/rodrigo/moost-projects/devfluent-app/package.json');
const { chromium } = require('playwright');
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const here = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(here, '../..');
const Q = (n) => 'file://' + path.join(root, 'lote13_posts/pelo_mundo_PM', n);
const FONT = (n) => 'file://' + path.join(here, '../_fontes', n);

const CSS = `
@font-face{font-family:'Nunito';src:url('${FONT('Nunito.ttf')}');font-weight:200 1000}
@font-face{font-family:'Mochiy';src:url('${FONT('MochiyPopOne-Regular.ttf')}')}
*{box-sizing:border-box;margin:0;padding:0}
body{background:#000}
#post{position:relative;width:1080px;height:1350px;overflow:hidden;font-family:'Nunito';color:#081226;background:#000}
#post>img.bg{position:absolute;inset:0;width:1080px;height:1350px;object-fit:cover}
.tape{position:absolute;left:50px;top:58px;z-index:9;background:#FFC83D;color:#081226;font-weight:900;font-size:40px;padding:12px 40px;transform:rotate(-2deg);clip-path:polygon(2% 0,98% 6%,100% 94%,0 100%);box-shadow:0 8px 18px rgba(0,0,0,.25)}
.bal{position:absolute;z-index:7;background:#fff;border-radius:46px;border-bottom:16px solid #B9CCF2;padding:30px 44px 26px;box-shadow:0 22px 42px rgba(0,0,0,.28);font-weight:900;font-size:52px;line-height:1.1;letter-spacing:-.01em;text-align:center}
#tails{position:absolute;left:0;top:0;z-index:6}
.bar{position:absolute;left:56px;right:56px;z-index:8;background:#081226;border-radius:32px;padding:22px 30px 26px;text-align:center;font-family:'Mochiy';text-transform:uppercase;font-size:38px;line-height:1.25;color:#fff;box-shadow:0 14px 30px rgba(0,0,0,.35)}
.bar .y{color:#FFC83D}
.bar s{text-decoration-color:#FF5A5F;text-decoration-thickness:6px}
.bar.bottom{bottom:44px}.bar.top{top:150px}
.tile{position:absolute;z-index:7;border-radius:26px;background-repeat:no-repeat;box-shadow:0 6px 16px rgba(0,0,0,.18)}
.tile .muted{position:absolute;right:14px;bottom:14px;width:62px;height:62px;border-radius:50%;background:#E5484D;display:flex;align-items:center;justify-content:center}
.tile .muted svg{width:34px;height:34px;stroke:#fff;fill:none;stroke-width:2.4;stroke-linecap:round;stroke-linejoin:round}
.mic{position:absolute;z-index:7;border-radius:50%;background:#E5484D;border-bottom:14px solid #A92E33;display:flex;align-items:center;justify-content:center;box-shadow:0 18px 36px rgba(0,0,0,.3)}
.mic svg{width:56%;height:56%;stroke:#fff;fill:none;stroke-width:2.2;stroke-linecap:round;stroke-linejoin:round}
/* capa */
#post.cover{background:linear-gradient(165deg,#FF8A78 0%,#FF6B57 55%,#F25744 100%)}
.cover::before{content:"";position:absolute;width:760px;height:760px;border-radius:50%;right:-240px;top:-300px;background:radial-gradient(circle,rgba(255,255,255,.30),rgba(255,255,255,.10) 62%,rgba(255,255,255,0) 70%)}
.cover h1{position:absolute;left:64px;top:158px;z-index:5;font-weight:900;font-size:84px;line-height:1.04;letter-spacing:-.01em;width:950px}
.hl{background:linear-gradient(transparent 52%,#FFC83D 52%,#FFC83D 92%,transparent 92%);padding:0 6px}
.card{position:absolute;left:330px;top:395px;width:600px;height:750px;border-radius:40px;overflow:hidden;border-bottom:16px solid #B9CCF2;box-shadow:0 26px 48px rgba(0,0,0,.32);transform:rotate(2deg);z-index:3}
.card img{width:600px;height:750px;object-fit:cover;display:block}
.go{position:absolute;left:56px;bottom:44px;z-index:5;display:flex;gap:26px;align-items:center;font-weight:800;font-size:36px}
.btn{width:104px;height:104px;border-radius:50%;background:#FFC83D;display:flex;align-items:center;justify-content:center;box-shadow:0 10px 0 rgba(0,0,0,.22)}
.btn svg{width:54px;height:54px;stroke:#081226;fill:none;stroke-width:2.6;stroke-linecap:round;stroke-linejoin:round}
`;

const ICON_ARROW = '<svg viewBox="0 0 24 24"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg>';


const SL = [
  { img: 'PM01_v1.png', word: 'Hello!', lang: 'inglês', bal: { x: 520, y: 56, w: 440 }, tip: [619, 336] },
  { img: 'PM02_v2.png', word: '¡Hola!', lang: 'espanhol', bal: { x: 170, y: 250, w: 440 }, tip: [365, 525] },
  { img: 'PM03_v2.png', word: 'Bonjour!', lang: 'francês', bal: { x: 250, y: 215, w: 520 }, tip: [480, 448] },
  { img: 'PM04_v2.png', word: 'Hallo!', lang: 'alemão', bal: { x: 150, y: 335, w: 440 }, tip: [400, 572] },
  { img: 'PM05_v2.png', word: 'Ciao!', lang: 'italiano', bal: { x: 260, y: 265, w: 440 }, tip: [500, 502], bar: 'Manda pro amigo que só sabe dizer hello' },
];
const EXTRA = `
.bal{font-size:92px;padding:22px 44px 22px}
.bal .lg{font-weight:800;font-size:38px;letter-spacing:.01em;color:#4A5D8F;line-height:1.1;margin-bottom:2px}
.chip{position:absolute;right:56px;bottom:44px;z-index:8;background:#fff;color:#081226;font-weight:900;font-size:42px;padding:12px 34px;border-radius:999px;box-shadow:0 10px 22px rgba(0,0,0,.28)}
.fan{position:absolute;z-index:3;width:340px;height:425px;border-radius:30px;overflow:hidden;border-bottom:14px solid #B9CCF2;box-shadow:0 22px 40px rgba(0,0,0,.32)}
.fan img{width:340px;height:425px;object-fit:cover;display:block}
.bar.bottom{bottom:130px}
`;
function cover() {
  // Cinco cartões lado a lado em duas fileiras suaves, cada um mostrando a Rara inteira (recorte centrado nela).
  const pos = [[50,455,-5],[405,440,3],[760,455,-3],[225,825,4],[590,825,-4]];
  const cards = SL.map((s, i) => `<div class="fan" style="left:${pos[i][0]}px;top:${pos[i][1]}px;width:270px;height:338px;transform:rotate(${pos[i][2]}deg);z-index:${3 + i}"><img style="width:270px;height:338px;object-fit:cover;object-position:50% 55%" src="${Q(s.img)}"></div>`).join('');
  return `<div id="post" class="cover"><div class="tape">rara pelo mundo</div><h1>Como dizer oi em <span class="hl">5 idiomas</span></h1>${cards}<div class="go"><span>Arrasta para o lado</span><div class="btn">${ICON_ARROW}</div></div></div>`;
}
function slide(s) {
  let h = `<div id="post"><img class="bg" src="${Q(s.img)}"><div class="tape">rara pelo mundo</div><svg id="tails" width="1080" height="1350"></svg>`;
  h += `<div class="bal" data-tip="${s.tip.join(',')}" style="left:${s.bal.x}px;top:${s.bal.y}px;width:${s.bal.w}px"><div class="lg">em ${s.lang}</div>${s.word}</div>`;
  if (s.bar) h += `<div class="bar bottom">${s.bar}</div>`;
  h += `<script>document.fonts.ready.then(()=>{const ns='http://www.w3.org/2000/svg';const sv=document.getElementById('tails');
document.querySelectorAll('.bal').forEach(b=>{const t=b.dataset.tip.split(',').map(Number),x=b.offsetLeft,y=b.offsetTop,w=b.offsetWidth,hh=b.offsetHeight;
const bx=Math.min(Math.max(t[0]-60,x+50),x+w-130);const p=document.createElementNS(ns,'polygon');
p.setAttribute('points',\`\${bx},\${y+hh-18} \${bx+80},\${y+hh-18} \${t[0]},\${t[1]}\`);p.setAttribute('fill','#fff');sv.appendChild(p)});});</script></div>`;
  return h;
}
const outDir = path.join(root, 'semana1/grupo3_feed/saudacoes');
fs.mkdirSync(outDir, { recursive: true });
const b = await chromium.launch();
const p = await b.newPage({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: 1 });
const slides = [cover(), ...SL.map(slide)];
for (let i = 0; i < slides.length; i++) {
  const f = path.join(outDir, `_s${i}.html`);
  fs.writeFileSync(f, `<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>${CSS}${EXTRA}</style></head><body>${slides[i]}</body></html>`);
  await p.goto('file://' + f);
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(500);
  await (await p.$('#post')).screenshot({ path: path.join(outDir, `s${i}.png`) });
  fs.unlinkSync(f);
}
console.log('ok', slides.length);
await b.close();
