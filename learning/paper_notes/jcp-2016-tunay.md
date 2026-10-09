# jcp-2016-tunay — full-text Pass 2 complete (2026-10-09)

Read all38 PDF pages; accepted manuscript identity/hash verified; full_text_verified/E2. [Structured audit](../audits/winkler_2016_fulltext.md) and source record carry page-level evidence.

- Input: prescribed finite crosswind,25m/s full vehicle/9m/s wind, nominal5L with1.5L cosine ramps; no vertical gradient. Figure2 zero-point requires P3 clarification.
- Method: IDDES/overset24M cells,1/8scale91.6m/s,6e-5s CFD step; two-way pose feedback each step versus offline one-way loads; 2DoF linear-tyre constant-speed dynamics.
- Driver: no-driver plus two gain sets, not three active controllers. Table2 car(1.0,15.6)/bus(1.2,30.9), delays0.55/0.52s.
- Results: one-way accumulated path deviation exceeds two-way7.3% without driver,6.3/3.9% car/bus controller. Distinct from force error or experimental validation. No universal yaw threshold.
- Validation: prior GTS drag +12%; mesh changes did not improve match. CG trends are robustness checks, no measured transient bus trajectory validation.
- Claims E-2016-01 upgraded/narrowed; E-2016-02/03/04 new; M-IDDES-2WAY and EQ-WINKLER-SCALE.
- Pass3 next: Eq8–14 signs/gain units; Strouhal time mapping; CG reference transformations; Fig2 spatial origin. NC-2016-VALIDATION requests original inputs/validation, no duplicate PDF.

## Historical abstract note (superseded)

# jcp-2016-tunay — Pass 2 (publisher abstract)

- Pass 1 / position: two-way aero–vehicle–driver coupling branch (repository Level 5) for transient crosswind.
- Input: transient wind on simplified bus; exact gust waveform, speed and turbulence NEEDS_FULLTEXT.
- Method: DES/overset aerodynamics with two-degree-of-freedom single-track model and three driver-controller parameter sets; one-way/static versus fully dynamic coupling compared.
- Output: aerodynamic loads and vehicle motion; abstract reports static coupling overpredicts both at large vehicle yaw angles.
- Claim/evidence: `E-2016-01`, publisher abstract E1. “Large” threshold and error metrics unavailable.
- Limit: no independent A/B/C validation established from abstract; cannot generalize its coupling need to passenger cars or all wind events.
- Relation: contrast with `sae-2017-01-1515` Level 2 is a method comparison, not an experimentally matched pair.
- Pass 3: NEEDS_FULLTEXT for feedback variables, coupling interval, driver gains, numerical convergence and validation.

## 2026-10-10 Pass3 controller/scaling checkpoint

Targeted original-PDF review plus independent equation checks completed; no new full read or grade upgrade. [Detailed audit](../audits/winkler_2016_controller_scaling.md): full/model time29.312 gives fullscale step0.00175872s; equal-density force/moment factors4.76726226/38.1380981 require corresponding origins. All are ANALYST_INFERENCE, not verified simulation settings. Bus steady-bicycle reduction gives gain magnitudes0.021553rad/m and0.538836rad/rad;degree-output conversion1.23492deg/m and30.8730deg/rad matches roundedTable2, but code units unproven. PrintedEq11 negative versus Eq12 positive remains unresolved;do not silently repair/control from it. CG nominal shifts1.18/2.36m and half-ramp0.366s are conditional arithmetic, not definitive geometry/input timing. ExistingNC-2016-VALIDATION expanded;P3partial still pending original implementation/data. Next available source sae-2017-01-1515 Pass3 axis/spline/uncertainty audit.
