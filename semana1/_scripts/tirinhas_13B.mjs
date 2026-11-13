// Compõe os carrosséis das tirinhas T2 a T5 (13B): capa + 4 quadros, 1080x1350.
// Uso: node tirinhas_13B.mjs [T2 T3 ...]  (sem argumentos compõe todas)
import { createRequire } from 'module';
const require = createRequire('/home/rodrigo/moost-projects/devfluent-app/package.json');
const { chromium } = require('playwright');
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const here = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(here, '../..');
const Q = (n) => 'file://' + path.join(root, 'lote13_posts/tirinhas_13B', n + '.png');
const FONT = (n) => 'file://' + path.join(here, '../_fontes', n);

// Regras: balões e rabinhos ficam fora do rosto (a ponta termina acima da cabeça).
// Coordenadas finais (1080x1350). kind: bal (balão), bar (faixa de legenda), mic (ícone de microfone mudo).
const SERIES = {
  T2: {
    title: 'O mico do <span class="hl">microfone mudo</span>',
    cover: 'T2Q1_v1',
    frames: [
      { img: 'T2Q1_v1', over: [{ kind: 'bar', pos: 'bottom', html: 'Eu falando o melhor inglês<br>da minha vida' }] },
      { img: 'T2Q2_v2', over: [{ kind: 'tile', x: 163, y: 565, w: 396, h: 347, src: 'T2Q1_v1', bx: -238, by: -170, bw: 800 }] },
      { img: 'T2Q3_v1', over: [{ kind: 'mic', cx: 880, cy: 330, d: 210 }] },
      { img: 'T2Q4_v3', over: [{ kind: 'bar', pos: 'top', html: 'Ficou <s>fluente</s><br><span class="y">no mudo</span>' }] },
    ],
  },
  T3: {
    title: 'Calma na <span class="hl">entrevista</span>',
    cover: 'T3Q1_v1',
    frames: [
      { img: 'T3Q1_v1', over: [] },
      { img: 'T3Q2_v1', over: [{ kind: 'bal', x: 90, y: 150, w: 760, html: 'E se perguntarem meus pontos fracos?', tip: [430, 352] }] },
      { img: 'T3Q3_v2', over: [{ kind: 'bal', x: 420, y: 120, w: 580, html: 'Respira,<br>solta o bico', tip: [668, 372] }] },
      { img: 'T3Q4_v3', over: [] },
    ],
  },
  T4: {
    title: 'O elogio do <span class="hl">tucano</span>',
    cover: 'T4Q1_v2',
    frames: [
      { img: 'T4Q1_v2', over: [] },
      { img: 'T4Q2_v1', over: [{ kind: 'bal', x: 90, y: 150, w: 820, html: 'This food is very EXQUISITE!', tip: [470, 465] }] },
      { img: 'T4Q3_v3', over: [] },
      { img: 'T4Q4_v3', over: [{ kind: 'bar', pos: 'top', html: 'Exquisite é requintado<br>Esquisito é weird<br><span class="y">Errou? Treinou</span>' }] },
    ],
  },
  T5: {
    title: 'O mico do <span class="hl">tapas bar</span>',
    cover: 'T5Q1_v1',
    frames: [
      { img: 'T5Q1_v1', over: [] },
      { img: 'T5Q2_v3_recorte4x5', over: [{ kind: 'bal', x: 190, y: 190, w: 640, html: 'Estoy embarazada', tip: [330, 566] }] },
      { img: 'T5Q3_v2', over: [] },
      { img: 'T5Q4_v2', over: [{ kind: 'bar', pos: 'top', html: 'Embarazada é grávida<br><span class="y">Envergonhada é avergonzada</span>' }] },
    ],
  },
};

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

const ICON_MIC_OFF =
  '<svg viewBox="0 0 24 24"><line x1="2" x2="22" y1="2" y2="22"/><path d="M18.89 13.23A7.12 7.12 0 0 0 19 12v-2"/><path d="M5 10v2a7 7 0 0 0 12 5"/><path d="M15 9.34V5a3 3 0 0 0-5.68-1.33"/><path d="M9 9v3a3 3 0 0 0 5.12 2.12"/><line x1="12" x2="12" y1="19" y2="22"/></svg>';
const ICON_ARROW = '<svg viewBox="0 0 24 24"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg>';

function coverHtml(s) {
  return `<div id="post" class="cover">
  <div class="tape">mico da rara</div>
  <h1>${s.title}</h1>
  <div class="card"><img src="${Q(s.cover)}"></div>
  <div class="go"><span>Arrasta para o lado</span><div class="btn">${ICON_ARROW}</div></div>
</div>`;
}

function frameHtml(f) {
  let h = `<div id="post"><img class="bg" src="${Q(f.img)}"><div class="tape">mico da rara</div><svg id="tails" width="1080" height="1350"></svg>`;
  for (const o of f.over) {
    if (o.kind === 'bal') {
      h += `<div class="bal" data-tip="${o.tip.join(',')}" style="left:${o.x}px;top:${o.y}px;width:${o.w}px">${o.html}</div>`;
    } else if (o.kind === 'bar') {
      h += `<div class="bar ${o.pos}">${o.html}</div>`;
    } else if (o.kind === 'tile') {
      h += `<div class="tile" style="left:${o.x}px;top:${o.y}px;width:${o.w}px;height:${o.h}px;background-image:url('${Q(o.src)}');background-size:${o.bw}px auto;background-position:${o.bx}px ${o.by}px"><div class="muted">${ICON_MIC_OFF}</div></div>`;
    } else if (o.kind === 'mic') {
      h += `<div class="mic" style="left:${o.cx - o.d / 2}px;top:${o.cy - o.d / 2}px;width:${o.d}px;height:${o.d}px">${ICON_MIC_OFF}</div>`;
    }
  }
  h += `<script>document.fonts.ready.then(()=>{const ns='http://www.w3.org/2000/svg';const sv=document.getElementById('tails');
document.querySelectorAll('.bal').forEach(b=>{const t=b.dataset.tip.split(',').map(Number),x=b.offsetLeft,y=b.offsetTop,w=b.offsetWidth,hh=b.offsetHeight;
const bx=Math.min(Math.max(t[0]-60,x+50),x+w-130);const p=document.createElementNS(ns,'polygon');
p.setAttribute('points',\`\${bx},\${y+hh-18} \${bx+80},\${y+hh-18} \${t[0]},\${t[1]}\`);p.setAttribute('fill','#fff');sv.appendChild(p)});window.__done=true;});</script></div>`;
  return h;
}

const only = process.argv.slice(2);
const names = only.length ? only : Object.keys(SERIES);
const b = await chromium.launch();
const p = await b.newPage({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: 1 });
for (const n of names) {
  const s = SERIES[n];
  const outDir = path.join(root, 'semana1/grupo3_feed/tirinhas', n);
  fs.mkdirSync(outDir, { recursive: true });
  const slides = [coverHtml(s), ...s.frames.map(frameHtml)];
  for (let i = 0; i < slides.length; i++) {
    const htmlFile = path.join(outDir, `_s${i}.html`);
    fs.writeFileSync(htmlFile, `<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>${CSS}</style></head><body>${slides[i]}</body></html>`);
    await p.goto('file://' + htmlFile);
    await p.evaluate(() => document.fonts.ready);
    await p.waitForTimeout(500);
    await (await p.$('#post')).screenshot({ path: path.join(outDir, `s${i}.png`) });
    fs.unlinkSync(htmlFile);
  }
  console.log('ok', n, slides.length, 'slides');
}
await b.close();
