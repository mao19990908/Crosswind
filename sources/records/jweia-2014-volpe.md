# jweia-2014-volpe — Forces and Flow Structures Evolution on a Car Body in a Sudden Crosswind

## Bibliographic
- ID: `jweia-2014-volpe`; Authors: Raffaele Volpe; Valérie Ferrand; Arthur Da Silva; Luis Le Moyne
- Year / venue: 2014, Journal of Wind Engineering and Industrial Aerodynamics 128:114–125
- DOI / URL: [10.1016/j.jweia.2014.03.006](https://doi.org/10.1016/j.jweia.2014.03.006)
- GB/T 7714: VOLPE R, FERRAND V, DA SILVA A, et al. Forces and flow structures evolution on a car body in a sudden crosswind[J]. Journal of Wind Engineering and Industrial Aerodynamics, 2014, 128:114-125.
- BibTeX: `@article{Volpe2014,author={Volpe, Raffaele and Ferrand, Valerie and Da Silva, Arthur and Le Moyne, Luis},title={Forces and flow structures evolution on a car body in a sudden crosswind},journal={Journal of Wind Engineering and Industrial Aerodynamics},volume={128},pages={114--125},year={2014},doi={10.1016/j.jweia.2014.03.006}}`

## Access / verification
- access_status: abstract; full_text_source: publisher page; copyright_status: publisher-controlled
- verification_status: abstract_verified; access_level: abstract; evidence_type: dynamic_wind_tunnel

## Classification
- source_type: journal_article
- publisher_or_institution: Elsevier
- report_or_standard_number: not_applicable
- primary_category: F; secondary_categories: C,J; tags: `sudden_crosswind`, `PIV`, `rear_geometry`, `overshoot`

## Physical problem and method
- Two Windsor-type bodies with squareback/fastback rear geometries in double-wind-tunnel sudden-yaw setup.
- TR-PIV and stereoscopic PIV connect side force/yaw moment to evolving flow.
- Detailed scale, Reynolds number, gust gradient, coordinates and normalization: not yet extracted.

## Results / validation / evidence
- Publisher highlights report yaw-moment transient coefficient up to 16% above steady counterpart; transient changes concentrated on rear leeward flank and correlated with leeward-vortex circulation.
- Rear geometry changed established lateral coefficients but not significantly transient duration/overshoot in tested cases.

## Limitations / relevance / follow-up
- Limitation: abstract/highlights verified, not full methods.
- Relevance: flow-physics bridge from Durham-type gust tests to vortex-based ROM candidates.
- Follow-up: lawful full text; establish direct facility/method citation to `sae-2000-01-0874`.

## DOI / PDF registry (2026-09-25)

- DOI: `10.1016/j.jweia.2014.03.006`; doi_status: `verified`; doi_source: https://api.crossref.org/works/10.1016/j.jweia.2014.03.006; doi_verified_date: 2026-09-25.
- pdf_status: `paywalled`; pdf_source: https://doi.org/10.1016/j.jweia.2014.03.006; pdf_path: `none`; pdf_sha256: `not applicable`; pdf_bytes: not applicable; pdf_license: publisher_or_standard_restricted; other OA locations not exhausted; github_pdf: false.
- PDF 状态为本轮已检查入口的状态；未穷尽全部机构仓储或作者版本，不将当前未找到写成永久不存在。

## Bibliography and abstract provenance (2026-09-25)

- Canonical Bib key: `jweia-2014-volpe` in `sources/bibliography/references.bib`.
- abstract_status: `available_not_copied`; abstract_source: Official source or catalog abstract noted in source record; abstract_source_url: https://doi.org/10.1016/j.jweia.2014.03.006.
- Full-text check: No full text has been validated; do not promote claims beyond the current evidence level.

## User-provided PDF receipt (2026-09-25)

- The earlier PDF/access note above is superseded for file availability. `volpe2014.pdf` matches this source by title and/or SAE number/DOI; 12 pages opened and text-extracted without errors.
- pdf_status: `user_provided`; pdf_path: `sources\pdfs\jweia-2014-volpe__volpe__2014.pdf`; pdf_source: `user_provided_local:Downloads/PDF/volpe2014.pdf`.
- pdf_sha256: `36644f7834c969b6a1816f0d4d8a9fb303d577b9fe85e75c2653ec4dd7cd04be`; pdf_bytes: 5203302; pdf_checked_date: 2026-09-25.
- pdf_license: Elsevier publisher PDF; redistribution permission not verified; github_pdf: false. The file stays local; only metadata is committed.
- Verification status remains `abstract_verified` pending substantive full-text reading and revision of abstract-based claims.

## Full-text Pass 2 review (2026-09-25)

- `verification_status=full_text_verified`; old abstract-only statements are superseded. All 12 publisher PDF pages read, including Figs.2–16 and Table 1. The apparatus is explicitly *adapted from* Ryan/Dominy 2000, not hardware-identical: 20 paired-shutter channels in a 30° double-tunnel arrangement, longitudinal tunnel 9 m/s and auxiliary 10.39 m/s (article pp.114,117). Actual established yaw at the model is ~21° because the main flow straightens the auxiliary flow (p.119); 30° is apparatus orientation, not measured model-relative yaw.
- Windsor reference length 0.25 m, frontal area 0.00644 m², 12 mm ground clearance; squareback and 25° rear-slant fastback variants. `t+=t U_main/L_ref`; therefore establishment at `t+≈7` corresponds to ~0.194 s at 9 m/s for this 0.25 m model, while the example `t+_gust=10` is ~0.278 s (pp.117–120). This normalization is not interchangeable with other studies' model lengths or inlet speeds.
- Empty-bench TR-PIV repeated 15 events and reported velocity SD 0.8% of main speed; force traces phase-average 50 events. Horizontal TR-PIV 500 Hz, vertical stereoscopic PIV has low intrinsic frame rate and reconstructs selected phases across repeated gusts, not a simultaneous high-speed 3-D time series. Balance signal was low-pass filtered at 35 Hz and instrument response corrected (pp.117–120).
- Both car shapes' side-force peak was ~7% above each own established value at `t+≈1.7`; yaw moment peaks differ: squareback ~16% at the first peak near `t+≈1`, fastback ~10% with strongest second peak near `t+≈3`. Coefficients settle around `t+≈7` for the tested arrangements (pp.120–121, Fig.9). Rear leeward flow is most time sensitive. Table 1 p.124 reports correlation of vortex ΓA circulation with side force `r=0.806/0.883` and yaw moment `r=0.551/0.758` (squareback/fastback). Correlation and flow visualization support a mechanism hypothesis but do not independently establish causal contribution or full vehicle response.
- Reference list p.125 directly includes `sae-2000-01-0874` and `jfe-2013-volpe`; no duplicate record or exact apparatus identity is inferred. The publisher PDF lacks confirmed public redistribution authorization and remains local only.
