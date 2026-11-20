import { createRequire } from 'module';
const require = createRequire('/home/rodrigo/moost-projects/devfluent-app/package.json');
const { chromium } = require('playwright');
const jobs = JSON.parse(process.argv[2]);
const b = await chromium.launch();
for (const [f,out,w,h] of jobs){ const p = await b.newPage({viewport:{width:w,height:h}});
 await p.goto('file://'+f); await p.evaluate(()=>document.fonts.ready); await p.waitForTimeout(500);
 const r = await p.evaluate(()=>[...document.querySelectorAll('.bal,.card,.sup,.word,.punch,h1,.pill,svg.tail path')].map(e=>{const b=e.getBoundingClientRect();return [e.className&&e.className.baseVal!==undefined?'tail':e.className||e.tagName,Math.round(b.left),Math.round(b.top),Math.round(b.right),Math.round(b.bottom)]}));
 console.log('RECTS '+out+' '+JSON.stringify(r));
 await (await p.$('#post')).screenshot({path:out, type:'png'}); await p.close(); }
await b.close();