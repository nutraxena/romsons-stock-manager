import {copyFileSync,existsSync,statSync,mkdirSync} from 'node:fs';
mkdirSync('dist',{recursive:true});
for (const filename of ['seed.json','sw.js','icon.svg','manifest.webmanifest']) {
 if(!existsSync(filename)) throw new Error(`Required deployment asset missing: ${filename}`);
 copyFileSync(filename,`dist/${filename}`);
 console.log(`Copied ${filename} (${statSync(filename).size} bytes) to dist/`);
}
