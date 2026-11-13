import { createRequire } from 'module';
const require = createRequire('/home/rodrigo/moost-projects/devfluent-app/package.json');
const { chromium } = require('playwright');
import path from 'path'; import fs from 'fs'; import { fileURLToPath } from 'url';
const here = path.dirname(fileURLToPath(import.meta.url));
const jobs = [
 ['carrossel_continuo_v3.html',5400,1350,1080,'Conheça a Rara (posts)',34,'#stage'],
 ['pio2.html',7560,1350,1080,'Pio da Semana',34,'#post'],
 ['t1v2.html',1080,1350,1080,'Mico da porta',34,null],
 ['plantao2.html',1080,1350,1080,'Plantão PL01',34,null],
 ['stories.html',1080,1920,1080,'Stories',40,null]];
const b = await chromium.launch();
for (const [f,w,h,sw,name,min] of jobs) {
  const p = await b.newPage({ viewport:{width:w,height:h} });
  await p.goto('file://'+path.join(here,f)); await p.evaluate(()=>document.fonts.ready); await p.waitForTimeout(600);
  const res = await p.evaluate(()=>{
    const out=[]; const walker=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT);
    while(walker.nextNode()){ const n=walker.currentNode; const t=n.textContent.trim(); if(!t) continue; const el=n.parentElement;
      if(el.closest('svg,script,style')) continue; const r=el.getBoundingClientRect(); if(r.width<2||r.height<2) continue;
      const cs=getComputedStyle(el); if(cs.display==='none'||cs.visibility==='hidden') continue;
      let fs=parseFloat(cs.fontSize); const z=parseFloat(getComputedStyle(el.closest('.blk')||el).zoom||1);
      out.push({t:t.slice(0,28),fs:Math.round(fs*10)/10,x:Math.round(r.left+window.scrollX),y:Math.round(r.top+window.scrollY)}); }
    return out;});
  // agrupar por peça
  const groups={};
  for (const r of res){ let key; if(f==='stories.html'){ const ids=JSON.parse(fs.readFileSync(path.join(here,'stories_ids.json'))); key=ids[Math.floor(r.y/1920)];} else if(f==='t1v2.html'){ key=name+' quadro '+['capa','1','2','3','4'][Math.floor(r.y/1350)];} else key=name+' slide '+(Math.floor(r.x/sw)+1); (groups[key] ||= []).push(r); }
  for (const [k,arr] of Object.entries(groups)){ const m=arr.reduce((a,c)=>c.fs<a.fs?c:a); console.log(`${f==='stories.html'?'Story ':''}${k}\tmin ${m.fs}px\t"${m.t}"\t${m.fs<min?'ABAIXO':'ok'}`); }
  await p.close();
}
await b.close();
