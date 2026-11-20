import { createRequire } from 'module';
const require = createRequire('/home/rodrigo/moost-projects/devfluent-app/package.json');
const { chromium } = require('playwright'); import path from 'path';
const b = await chromium.launch(); const p = await b.newPage({ viewport:{width:1080,height:1350}});
p.on('pageerror',e=>console.log('ERR',e.message)); p.on('console',m=>console.log('LOG',m.text()));
await p.goto('file://'+path.resolve(process.argv[2])); await p.evaluate(()=>document.fonts.ready); await p.waitForTimeout(500);
console.log(await p.evaluate(()=>document.getElementById('pg').getAttribute('points')));
await b.close();
