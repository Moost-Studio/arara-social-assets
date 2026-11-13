import { createRequire } from 'module';
const require = createRequire('/home/rodrigo/moost-projects/devfluent-app/package.json');
const { chromium } = require('playwright');
import path from 'path'; import { fileURLToPath } from 'url';
const here = path.dirname(fileURLToPath(import.meta.url));
const [,, htmlFile, outFile, w, h] = process.argv;
const b = await chromium.launch(); const p = await b.newPage({ viewport:{width:+w,height:+h}, deviceScaleFactor: 1 });
await p.goto('file://'+path.resolve(here,htmlFile)); await p.evaluate(()=>document.fonts.ready); await p.waitForTimeout(600);
await (await p.$('#post')).screenshot({ path: outFile }); await b.close();
