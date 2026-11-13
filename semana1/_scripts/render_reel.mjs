import { createRequire } from 'module';
const require = createRequire('/home/rodrigo/moost-projects/devfluent-app/package.json');
const { chromium } = require('playwright');
import path from 'path'; import fs from 'fs'; import { fileURLToPath } from 'url';
const here = path.dirname(fileURLToPath(import.meta.url));
const [,, outDir, fps, tot, ...only] = process.argv;
const b = await chromium.launch(); const p = await b.newPage({ viewport:{width:1080,height:1920}, deviceScaleFactor:1 });
await p.goto('file://'+path.join(here,'reel.html')); await p.waitForFunction(()=>window.__done===true,{timeout:60000}); await p.waitForTimeout(500);
const times = only.length ? only.map(Number) : Array.from({length:Math.round(+tot*+fps)},(_,i)=>i/ +fps);
let n=+(process.env.FROM||0); const TO=process.env.TO?+process.env.TO:1e9; const times2=times.slice(n,TO);
for (const t of (only.length?times:times2)) { await p.evaluate(tt=>window.setT(tt),t); await p.evaluate(()=>new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r))));
  const name = only.length ? 't_'+t.toFixed(2) : 'f_'+String(n).padStart(4,'0'); await p.screenshot({path:path.join(outDir,name+'.jpg'),type:'jpeg',quality:93}); n++; }
await b.close(); console.log('frames',n);
