import { createRequire } from 'module';
const require = createRequire('/home/rodrigo/moost-projects/devfluent-app/package.json');
const { chromium } = require('playwright');
import path from 'path';
const [,, outDir, scale] = process.argv;
const FPS = +(process.env.FPSV||60), from = +(process.env.FROM||0), to = +(process.env.TO||1080), only = process.env.ONLY ? process.env.ONLY.split(',').map(Number) : null;
const PORT = process.env.PORT || 8765, q = +(process.env.Q||88), hud = process.env.HUD ?? '1';
const b = await chromium.launch({args:['--enable-unsafe-swiftshader','--ignore-gpu-blocklist','--disable-gpu-rasterization']});
const p = await b.newPage({ viewport:{width:1080,height:1920}, deviceScaleFactor:+scale });
p.on('pageerror',e=>console.log('PAGEERR',e.message.slice(0,500))); p.on('console',m=>{if(m.type()==='error')console.log('CONERR',m.text().slice(0,300))});
await p.goto(`http://127.0.0.1:${PORT}/grupo5_apresenta/animatic.html?hud=${hud}`); await p.waitForFunction(()=>window.__done===true,null,{timeout:240000}); await p.waitForTimeout(400);
const times = only ? only : Array.from({length:to-from},(_,i)=>(from+i)/FPS);
let n=from;
for (const t of times) { await p.evaluate(tt=>window.setT(tt),t); await p.evaluate(()=>new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r))));
  const name = only ? 't_'+t.toFixed(2) : 'f_'+String(n).padStart(4,'0'); await p.screenshot({timeout:180000,path:path.join(outDir,name+'.jpg'),type:'jpeg',quality:q}); n++; }
await b.close(); console.log('frames',times.length);
