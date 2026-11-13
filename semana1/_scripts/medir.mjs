import { createRequire } from 'module';
const require = createRequire('/home/rodrigo/moost-projects/devfluent-app/package.json');
const { chromium } = require('playwright');
import path from 'path'; import { fileURLToPath } from 'url';
const here = path.dirname(fileURLToPath(import.meta.url));
const b = await chromium.launch(); const p = await b.newPage({ viewport:{width:1080,height:1920} });
await p.goto('file://'+path.join(here,'stories.html')); await p.evaluate(()=>document.fonts.ready); await p.waitForTimeout(500);
const r = await p.evaluate(()=>[...document.querySelectorAll('.st')].map(s=>{const bl=s.querySelector('.blk').getBoundingClientRect(), st=s.getBoundingClientRect(); return s.id+' '+Math.round(bl.bottom-st.top)}));
console.log(r.join(' | ')); await b.close();
