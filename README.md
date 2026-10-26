# ROMSONS Stock Management PWA

Vercel-ready Vite PWA with initial April–October 2026 stock statement data.

## Deploy to Vercel
1. Unzip this project and push folder contents to a GitHub repository.
2. Import repository in Vercel.
3. Framework: Vite; Build command: `npm run build`; Output directory: `dist`.
4. Deploy. Open the HTTPS link, then use browser Install App / Add to Home Screen.

## Local development
`npm install` then `npm run dev`. For production run `npm run build`.

## Notes
- Initial 21 stock files were parsed to seed.json. Paramount Remedies August 2026 data has been rebuilt from the corrected standard-format workbook in `reference/`. New Excel uploads are parsed client-side and saved to browser localStorage only. Browser storage is not a durable database and can be cleared. Export backups regularly.
- New uploads do not sync between different devices. Add hosted database and authentication for true multi-device cloud synchronization.
- Service worker caches visited assets for offline access after first online visit; PWA installation depends on browser support.
- Print / PDF opens browser print dialog (choose Save as PDF). CSV and XLSX download directly. Image export is not included yet.
- Data parser is best-effort; validate totals against source statements before business reporting. Negative and missing numeric fields may require manual verification.
- Monthly Closing Total uses the latest month with data rather than sum of all monthly closing balances.
