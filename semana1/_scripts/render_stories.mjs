import { createRequire } from 'module';
const require = createRequire('/home/rodrigo/moost-projects/devfluent-app/package.json');
const { chromium } = require('playwright');
import path from 'path'; import fs from 'fs'; import { fileURLToPath } from 'url';
const here = path.dirname(fileURLToPath(import.meta.url));
const ids = JSON.parse(fs.readFileSync(path.join(here,'stories_ids.json')));
const out = process.argv[2];
const b = await chromium.launch();
const p = await b.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
await p.goto('file://' + path.join(here,'stories.html'));
await p.evaluate(() => document.fonts.ready);
await p.waitForFunction(()=>window.__done===true); await p.waitForTimeout(500);
const only=process.argv[3]?process.argv[3].split(','):ids; for (const id of only) { await (await p.$('#'+id)).screenshot({ path: path.join(out, id+'.png') }); }
await b.close();
