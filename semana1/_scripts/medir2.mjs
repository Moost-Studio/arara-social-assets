import { createRequire } from 'module';
const require = createRequire('/home/rodrigo/moost-projects/devfluent-app/package.json');
const { chromium } = require('playwright');
import path from 'path'; import { fileURLToPath } from 'url';
const here = path.dirname(fileURLToPath(import.meta.url));
const b = await chromium.launch(); const p = await b.newPage({ viewport:{width:1080,height:1920} });
await p.goto('file://'+path.join(here,'stories.html')); await p.waitForFunction(()=>window.__done===true);
const r = await p.evaluate(()=>[...document.querySelectorAll('.st')].map(s=>{const st=s.getBoundingClientRect();const bl=s.querySelector('.blk').getBoundingClientRect();const bal=[...s.querySelectorAll('.bal')].map(x=>{const r=x.getBoundingClientRect();return Math.round(r.bottom-st.top)});const head=+s.dataset.head;const bot=Math.round(bl.bottom-st.top);let minfs=99;s.querySelectorAll('.blk *, .bal *').forEach(e=>{if(e.children.length===0||e.tagName==='P'||e.tagName==='H1'){const f=parseFloat(getComputedStyle(e).fontSize);if(f<minfs)minfs=f}});return `${s.id} blk=${bot} bal=${bal.join(',')||'-'} head=${head} ${bot>head-20?'**SOBREPOE**':''} minfont=${minfs}`}));
console.log(r.join('\n')); await b.close();
