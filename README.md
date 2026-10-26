# ROMSONS Stock Manager — Alias reconciliation update

Upload the files in this ZIP to the GitHub repository root; Vercel builds using `npm run build` and publishes `dist`.

## Fixed
- Paramount Rehab aliases: ANKEL -> Ankle; ARM SLING POUCH / POUCH ARM SILNG -> Pouch Arm Sling; CERVICAL COLLER / CERVIVAL -> Cervical Collar; CLAVICAL -> Clavicle; CONTOURED LUMBO SACRAL BELT -> Contoured Lumbo Sacral Support; FOREARM SPILNT -> Forearm Splint; WRIST FOREAM SPLINT Left/Right -> Wrist And Forearm Splint; XL (RMS) interpreted as XL, with RMS ignored.
- Removed the Unmatched Review download button. No source financial amounts are silently dropped: statement-only items appear in an explicit reconciliation row in Product Wise until the catalogue owner confirms the proper family.
- Existing Graph Selection, report exports, monthly closing balance semantics, and Paramount Rehab-only upload rule retained.

## Requires catalogue owner confirmation
The 49-name master does not include distinct names present in the 21 Excel statements: Taylor's Brace Long (UNI/SPL), Paediatric Soft Collar, Relief Eye Care Pack. These cannot be accurately merged into other catalogue products without a documented rule. A zero-value RN Enterprise 'ROMSONS ORTHO' heading is also present. Do not use the 49-row product totals as a fully reconciled 49-SKU ledger until these are resolved. Historical statement financials have not been independently validated against each Excel source.

## Verification
JavaScript syntax check passed. The Vite production build could not be executed in this runtime because node dependencies (vite) are not installed. Vercel should run npm install automatically on deployment.

## Size normalization (26 Oct 2026)
LARGE -> L, MEDIUM -> M, SMALL -> S, EXTRA LARGE -> XL, DOUBLE EXTRA -> XXL. RMS/Romsons stockist suffixes are removed before size extraction. Product Wise merges sizes; Product Size Wise keeps normalized sizes.


### Excluded product rule (26 Oct 2026)
Paediatric/Pediatric Soft Collar and statement misspellings PEADIATRIC, PEADIETRIC, PEADRIC are explicitly excluded from seeded data, existing browser imports and all future Excel uploads. Original 3 excluded seed rows each had zero purchase, sale and closing quantities and values. This is an intentional exclusion, not an alias to Cervical Collar Soft. Other unmatched lines remain unresolved; this release does not claim 49-product reconciliation.
