# pimeche-2001-passmore — An experimental study of unsteady vehicle aerodynamics

## Bibliographic
- ID: `pimeche-2001-passmore`
- Title: An experimental study of unsteady vehicle aerodynamics
- Authors: M. A. Passmore; S. Richardson; A. Imam
- Year / journal: 2001; Proceedings of the Institution of Mechanical Engineers, Part D: Journal of Automobile Engineering, 215(7):779–788
- DOI: 10.1243/0954407011528365
- URL: https://journals.sagepub.com/doi/10.1243/0954407011528365
- GB/T 7714: PASSMORE M A, RICHARDSON S, IMAM A. An experimental study of unsteady vehicle aerodynamics[J]. Proceedings of the Institution of Mechanical Engineers, Part D: Journal of Automobile Engineering, 2001, 215(7):779–788. DOI:10.1243/0954407011528365.
- BibTeX: `@article{Passmore2001,author={Passmore, M. A. and Richardson, S. and Imam, A.},title={An experimental study of unsteady vehicle aerodynamics},journal={Proceedings of the Institution of Mechanical Engineers, Part D: Journal of Automobile Engineering},year={2001},volume={215},number={7},pages={779--788},doi={10.1243/0954407011528365}}`

## Access / verification
- access_status: open_repository; full_text_source: Loughborough author-deposited PDF, file 16804613 (passmore2.pdf)
- verification_status: full_text_verified; access_level: full_text; evidence_type: dynamic_wind_tunnel; last_checked: 2026-09-25
- Repository: https://repository.lboro.ac.uk/articles/journal_contribution/An_experimental_study_of_unsteady_vehicle_aerodynamics/9225113
- Download: https://ndownloader.figshare.com/files/16804613 ; MD5 3715b0721600202700efa05420b11e6c (repository metadata).
- copyright_status: repository API labels CC BY-NC-ND 4.0, PDF cover labels CC BY-NC-ND 2.5; preserve this discrepancy. PDF used locally for research only, not committed. No claim of commercial reuse permission.
- All 10 article pages (779–788; PDF pages 2–11) read; equations/figures inspected visually. PDF page 1 is the repository licence sheet.

## Classification
- source_type: journal_article
- publisher_or_institution: SAGE / Institution of Mechanical Engineers
- report_or_standard_number: not_applicable
- primary_category: D; secondary_categories: B,C,F,J
- tags: sinusoidal_gust;oscillating_aerofoil;aerodynamic_magnification;quasi_steady_comparison

## Physical problem / method
- Fixed Davis bluff body, approximately 1:6 scale, 20° rear slant. Fig. 3: length 625 mm, width 212 mm, height 160 mm; edge radii 10 mm. Ground clearance 40 mm; blockage 2.3%; Reynolds number based on length 1e6 (p.782).
- Closed working section, closed-circuit tunnel: 1.6 m wide × 1 m high × 4.7 m long. Paired NACA0015 aerofoils, 0.3 m chord, in-phase quarter-chord oscillation. Model front is 1.3 model lengths downstream of aerofoil trailing edges; ground board extends 0.6 lengths upstream and 2.4 downstream (pp.781–782).
- CTA split-film calibration at model-front position measures transverse and longitudinal components. Facility capability up to 18 Hz at example 22 m/s is not the actual test-frequency sweep. Actual frequency statement is internally inconsistent: p.784 says 2–8 Hz, Figs.9/11 include 1 Hz. Retain reduced range 0.09–0.71; do not silently correct dimensional frequency.
- 144 taps on one side; four differential pressure transducers repositioned between groups; generator pulse trigger and phase-locked averaging align them. Short tubing, 100 Hz low-pass filter; sample rate, exact averaging count, uncertainty budget and tubing transfer function not reported (pp.782–784).
- Opposite side reconstructed with 180° phase shift, assuming geometric/flow symmetry. Sine fits retain pressure amplitude and phase before area/moment-arm integration. Quasi-steady comparator uses pressure-derived steady data, not balance-derived moment slope (pp.783–785).
- No vehicle motion, driver or controller model; vehicle-motion loop classification not applicable. Closed-circuit tunnel is not closed-loop driver control.

## Coordinates / equations
- Moment reference: mid-model (p.783). Wall static pressure is the pressure reference. Explicit global axis triad, positive moment convention, coefficient reference area/length and dynamic-pressure normalization are not stated; remain UNKNOWN.
- Reduced frequency k_m = pi*f*l/U, f in Hz, l model length (m), U tunnel freestream (m/s), pp.779–780. Source-specific definition; no automatic conversion to 2*pi*f*l/U.
- Ag = v/((u+U)*A0), p.781, with A0 aerofoil maximum angle in radians. Quasi-steady Cy(t) = (dCy/d beta)*Ag*A0*sin(omega*t), p.785. Beta in radians in notation; Table 1 gradient units are not printed and Fig.4 uses degrees: do not reuse slope numbers without conversion audit.
- Magnification chi_a is transient/QS sine-amplitude ratio. Under the same-frequency sine simplification, the paper's power admittance is chi_a squared; neither quantity alone is a complex transfer function (p.785).
- Phase-aware QS pressure uses each tap's longitudinal position and U. Fig.9 pressure phase has gust-convection phase removed; no universal time-delay sign inferred (pp.785–786).

## Results / validation / evidence
- E-2001-02 to E-2001-06 document definitions, measurement logic, baseline phase and uncertainty. Evidence is E2; no E3/E4 upgrade.
- Side force magnification generally below unity, lowest point about 1.5; yaw result depends on phase-aware versus uniform QS comparator (Fig.8). Author summary reports 5–30% yaw amplification. Preserve separate Fig.8 series rather than interpreting this as every uncorrected point exceeding unity (pp.785–787).
- Authors flag low-frequency yaw amplitude below ±2° and resulting signal-to-noise concern; this prevents treating the low-frequency increase as a verified k→0 asymptote (p.785).
- Level A: local gust calibration, not complete spatial field validation. Level B: steady pressure-vs-balance comparison and transient-vs-QS internal comparison; no independent transient force validation. Level C: none.

## Limitations / relevance / follow-up
- Author limitations: low-frequency signal-to-noise; pressure tap resolution/placement and skin-friction contribution in balance comparison. Missing full normalization and raw data prevent exact numerical reconstruction.
- Analyst inference: transferable method is component-wise amplitude/phase and matched pressure baseline, not direct reuse of gains in a passenger-car controller. See Pass 3 note for reproduction design and failure checks.
- References 4 and 6 verified again at p.788, no duplicate citation edges. Smith 1973, Garry/Cooper 1986, Mullarkey 1990 and Bearman/Mullarkey 1994 remain uncollected leads while backlog > 0; discussion of those works here is secondary evidence only.
