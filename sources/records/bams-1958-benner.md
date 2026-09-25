# bams-1958-benner — Engineering Meteorology: Wind Effects on Motor Vehicle Stability

## Bibliographic information

- William Benner, 1958, *Bulletin of the American Meteorological Society* 39(8):421–426.
- DOI: [10.1175/1520-0477-39.8.421](https://doi.org/10.1175/1520-0477-39.8.421). Crossref exact DOI metadata and the PDF title page agree; the superscript 1 after the printed title is a footnote marker.
- source_type: journal_article
- publisher_or_institution: American Meteorological Society
- report_or_standard_number: not_applicable
- Canonical Bib key: `bams-1958-benner` in `sources/bibliography/references.bib`.

## Access / verification

- `verification_status=full_text_verified`; complete article pp. 421–426 read on 2026-09-25. The unrelated *News and Notes* after the references on p. 426 is excluded.
- `pdf_status=user_provided`; `pdf_source=user_provided_local:Downloads/PDF/1520-0477-39_8_421.pdf`; `pdf_path=sources\pdfs\bams-1958-benner__benner__1958.pdf`.
- `pdf_sha256=069ffaad12dd0f0c64242c08881e399e8cea0d434bcb5cf3485435ec748893aa`; `pdf_bytes=6562510`; PDF has six readable pages.
- `pdf_license=public redistribution permission not verified`; `github_pdf=false`. The local research copy must not be pushed as a GitHub PDF.
- The printed abstract was read locally but is not copied into Bib; `abstract_status=full_text_supersedes_abstract`.

## Research question

How do wind direction and gusts affect vehicle stability, and how should wind and vehicle response be measured on the road?

## Physical problem

The article relates relative wind direction, aerodynamic side force and yaw tendency to tire lateral response and driver steering correction. It is a 1958 engineering-meteorology synthesis with examples and a description of Lay and Lett's earlier instrumented road car, not a new controlled transient test series.

## Gust / crosswind definition

It distinguishes steady sidewinds from natural gusts and describes an oblique gust striking a moving car. No controlled gust waveform, rise time, spatial profile, spectrum, or repeat count is reported in full text.

## Coordinate system and normalization

Fig. 1 sketches vehicle velocity, ambient wind and resultant relative wind; Fig. 2 sketches yaw and lateral translation. A full sign convention and aerodynamic coefficient normalization are not reported in full text.

## Vehicle / model geometry

A 1955 Ford is used for stationary wind-tunnel examples. The road-test vehicle described in Sec. 5 is Lay and Lett's car; its exact geometry is not reported in this article.

## Experimental setup

Sec. 5 describes the *Lay and Lett* road setup: wind vane and bridled anemometer on a forward/upper boom, photographed indicator readouts, and body-to-frame pillars with strain gauges. Body-force gauges were calibrated by incremental tilt and the wind sensors in a wind tunnel (pp. 424–425, Figs. 3–4). This is a description of cited earlier work, not an independent 1958 measurement campaign. The 1955 Ford wind-tunnel examples use fixed headwind/15° yaw at 100 mph (pp. 421, 423); they are steady aerodynamic examples, not transient gust validation.

## CFD setup

not applicable.

## Vehicle-dynamics model

Qualitative discussion of center of pressure, center of gravity, tire slip angle, understeer and driver response; no governing dynamic equations or identified driver model are reported in full text.

## Coupling method

not applicable. Driver action is discussed qualitatively; the article does not present a coupled aerodynamic–vehicle simulation.

## Important equations

not reported in full text. Fig. 1 gives a vector sketch, not a quantitative dynamic response equation.

## Important parameters

Fixed wind-tunnel examples: 1955 Ford, 100 mph tunnel stream, with a 15° right-of-center yaw case (pp. 421, 423). These values must not be transferred to natural-road gust experiments.

## Main quantitative results

The fixed wind-tunnel examples report wheel load and side-force percentages on pp. 421 and 423. They are not a measured transient gust-response series. No quantified natural-gust peak, steering input, displacement, uncertainty or statistical distribution is reported in full text.

## Flow / aerodynamic mechanisms

The author discusses the pressure-center/center-of-gravity lever arm and the opposing design effects of shifting side area rearward versus increasing total sail area (p. 423). These are conceptual design arguments, not a universal sign or magnitude prediction for present vehicle shapes.

## Validation method

The described road setup includes instrument calibration; the article provides no independent validation dataset for an aerodynamic or vehicle-dynamics model. `validation_level=none` for this source's own transient claims.

## Main conclusions

- Natural oblique gusts can induce lateral displacement and heading change; driver steering to recover course may increase body-to-frame forces during the gust interval (p. 425, Sec. 6). This is Benner's summary of the road-test line; do not count it as independent replication of Lay and Lett.
- Road-gust work needs continuous wind speed/direction measurement, preferably ahead of vehicle flow disturbance, and information on natural wind distribution (pp. 424–425, Secs. 5–6).
- The paper explicitly cites Lay and Lett (1953) as reference 5 on p. 425, so `bams-1958-benner -> sae-530255` is a verified `references` edge.

## Limitations

Natural road-wind time histories, vehicle response series, driver-steering measurements, sensor frequency response, uncertainties and raw data are not reported. The paper mixes author synthesis, descriptions of prior work and stationary wind-tunnel examples; those evidence kinds must remain separate. OCR ambiguities in p. 423 tables should not be used for new numerical conclusions without visual recheck.

## Relation to previous work

Lay & Lett 1953 is directly cited and its road instrumentation described (p. 425 ref. 5; pp. 424–425). References 3 and 9 give Huber 1940 and Sawatzki 1941, but Sawatzki is labeled series 44 here, while another official catalog records report 50; resolve against originals before creating canonical records or merging report identities.

## Relation to subsequent work

The paper documents an early need to separate aerodynamic disturbance, measured vehicle response and driver correction. Any direct citation or method inheritance into later Beauvais/DOT/ISO work remains unverified.

## Relevance to 车辆侧风模拟及实验验证

Historical evidence for the road measurement chain and for treating the driver as a separate response loop. It does not establish transient CFD, a controlled gust profile or a Level B/C validation benchmark.

## Follow-up questions

- Obtain Lay & Lett 1953 full text to compare the apparatus and the claim about driver correction with the original measurements.
- Verify Huber and Sawatzki report numbers/titles against original archive items.
- Check whether Benner's cited 1955 Ford steady-wind data came from a separately published primary report.

## Evidence map

| Claim | PDF page | Section / figure | Evidence boundary |
|---|---|---|---|
| Relative wind and yaw/lateral-motion sketch | printed 422 | Sec. 4, Figs. 1–2 | Conceptual vector diagrams |
| Fixed Ford 100 mph examples | printed 421, 423 | Secs. 2, 4 | Steady headwind/yaw, not a gust test |
| Lay/Lett boom sensors and strain-gauge car | printed 424–425 | Sec. 5, Figs. 3–4 | Secondary description of 1953 cited work |
| Oblique gust and driver correction | printed 425 | Sec. 6, point 2 | Narrative result; no time series |
| Direct Lay/Lett 1953 citation | printed 425 | References, no. 5 | Bibliographic edge verified |
| Huber/Sawatzki historical leads | printed 425–426 | References, nos. 3 and 9 | Report-number conflict unresolved |
