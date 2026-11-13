import { createRequire } from 'module';
const require = createRequire('/home/rodrigo/moost-projects/devfluent-app/package.json');
const { chromium } = require('playwright');
import path from 'path'; import { fileURLToPath } from 'url';
const here = path.dirname(fileURLToPath(import.meta.url));
const [,, htmlFile, outDir, prefix, ...ids] = process.argv;
const b = await chromium.launch();
const p = await b.newPage({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: 1 });
await p.goto('file://' + path.resolve(here, htmlFile));
await p.evaluate(() => document.fonts.ready);
await p.waitForTimeout(500);
for (const id of ids) {
  const el = await p.$('#' + id);
  await el.screenshot({ path: path.join(outDir, `${prefix}_${id}.png`) });
}
await b.close();
