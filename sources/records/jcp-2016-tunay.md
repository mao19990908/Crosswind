# jcp-2016-tunay — Coupling Aerodynamics to Vehicle Dynamics in Transient Crosswinds Including a Driver Model

## Bibliographic
- ID: `jcp-2016-tunay`; Authors: Tural Tunay; Niklas Winkler; Ciarán J. O'Reilly; Lars Drugge
- Year / venue: 2016, Computers & Fluids 138:26–34
- DOI / URL: [10.1016/j.compfluid.2016.08.006](https://doi.org/10.1016/j.compfluid.2016.08.006)
- GB/T 7714: TUNAY T, WINKLER N, O'REILLY C J, et al. Coupling aerodynamics to vehicle dynamics in transient crosswinds including a driver model[J]. Computers & Fluids, 2016, 138:26-34.
- BibTeX: `@article{Tunay2016,author={Tunay, Tural and Winkler, Niklas and O'Reilly, Ciaran J. and Drugge, Lars},title={Coupling aerodynamics to vehicle dynamics in transient crosswinds including a driver model},journal={Computers and Fluids},volume={138},pages={26--34},year={2016},doi={10.1016/j.compfluid.2016.08.006}}`

## Access / verification
- access_status: abstract; full_text_source: ScienceDirect; copyright_status: publisher-controlled
- verification_status: abstract_verified; access_level: abstract; evidence_type: coupled_simulation

## Classification
- source_type: journal_article
- publisher_or_institution: Elsevier
- report_or_standard_number: not_applicable
- primary_category: I; secondary_categories: H,E,J; tags: `level_5`, `DES`, `overset`, `single_track`, `closed_loop_driver`

## Physical problem and method
- Simplified bus in transient crosswind; DES with overset mesh coupled to two-DOF single-track model (lateral translation, yaw).
- Driver model evaluated with three controller parameter sets; one-way/static and full dynamic/two-way coupling compared.
- Detailed gust, mesh, timestep, coordinates and normalization: not extracted from full text.

## Results / validation / evidence
- Abstract reports full dynamic coupling becomes necessary for large vehicle yaw angles; static coupling overpredicts aerodynamic loads and motion.
- Validation level: not reported in abstract.

## Limitations / relevance / follow-up
- Limitation: simplified bus and abstract-level evidence; threshold for “large” yaw not extracted.
- Relevance: explicit Level 5 necessity study with driver-in-loop.
- Follow-up: extract feedback variables, numerical coupling interval, validation and driver gains.
