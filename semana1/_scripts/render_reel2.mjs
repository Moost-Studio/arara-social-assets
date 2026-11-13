import { createRequire } from 'module';
const require = createRequire('/home/rodrigo/moost-projects/devfluent-app/package.json');
const { chromium } = require('playwright');
import path from 'path'; import fs from 'fs'; import { fileURLToPath } from 'url';
const here = path.dirname(fileURLToPath(import.meta.url));
const [,, outDir, scale, ...rest] = process.argv;
const from = +(process.env.FROM||0), to = +(process.env.TO||525), only = process.env.ONLY ? process.env.ONLY.split(',').map(Number) : null;
const b = await chromium.launch(); const p = await b.newPage({ viewport:{width:1080,height:1920}, deviceScaleFactor:+scale });
p.on('pageerror',e=>console.log('PAGEERR',e.message)); p.on('console',m=>{if(m.type()==='error')console.log('CONERR',m.text())});
await p.goto('file://'+path.join(here,'reel2.html')); await p.waitForFunction(()=>window.__done===true,{timeout:120000}); await p.waitForTimeout(600);
const times = only ? only : Array.from({length:to-from},(_,i)=>(from+i)/30);
let n=from;
for (const t of times) { await p.evaluate(tt=>window.setT(tt),t); await p.evaluate(()=>new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r))));
  const name = only ? 't_'+t.toFixed(2) : 'f_'+String(n).padStart(4,'0'); await p.screenshot({path:path.join(outDir,name+'.jpg'),type:'jpeg',quality:92}); n++; }
await b.close(); console.log('frames',times.length);
