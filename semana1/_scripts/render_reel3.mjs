import { createRequire } from 'module';
const require = createRequire('/home/rodrigo/moost-projects/devfluent-app/package.json');
const { chromium } = require('playwright');
import path from 'path'; import { fileURLToPath } from 'url';
const here = path.dirname(fileURLToPath(import.meta.url));
const [,, outDir, scale] = process.argv;
const FPS = 60, from = +(process.env.FROM||0), to = +(process.env.TO||1050), only = process.env.ONLY ? process.env.ONLY.split(',').map(Number) : null;
const q = +(process.env.Q||88);
const b = await chromium.launch(); const p = await b.newPage({ viewport:{width:1080,height:1920}, deviceScaleFactor:+scale });
p.on('pageerror',e=>console.log('PAGEERR',e.message)); p.on('console',m=>{if(m.type()==='error'||m.type()==='log')console.log('CON',m.text())});
await p.goto('file://'+path.join(here,'reel3.html')); await p.waitForFunction(()=>window.__done===true,null,{timeout:180000}); await p.waitForTimeout(500);
const times = only ? only : Array.from({length:to-from},(_,i)=>(from+i)/FPS);
let n=from;
for (const t of times) { await p.evaluate(tt=>window.setT(tt),t); await p.evaluate(()=>new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r))));
  const name = only ? 't_'+t.toFixed(2) : 'f_'+String(n).padStart(4,'0'); await p.screenshot({timeout:180000,path:path.join(outDir,name+(process.env.PNG?'.png':'.jpg')),...(process.env.PNG?{type:'png'}:{type:'jpeg',quality:q})}); n++; }
await b.close(); console.log('frames',times.length);
