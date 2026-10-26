# ROMSONS Stock Manager - Vercel root-folder edition

Upload **all files in this folder directly to the root** of your existing GitHub repository. No `public` folder required. Replace `package.json`, `vercel.json`, `src.js` and other matching files. The new `postbuild.mjs` is required.

On Vercel: Root Directory `./`, Framework Vite, Build Command `npm run build`, Output Directory `dist`. Redeploy (clear build cache if available).

After deployment, test `https://YOUR-DOMAIN.vercel.app/seed.json` -- it must show a JSON array, not a 404 or HTML page.

This version packages initial stock data into the deployed site. Browser-uploaded data is stored on that device, not shared across devices. Do not rely on it as the sole backup.
