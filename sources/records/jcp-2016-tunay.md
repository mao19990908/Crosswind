# jcp-2016-tunay — Coupling Aerodynamics to Vehicle Dynamics in Transient Crosswinds Including a Driver Model

## Bibliographic
- ID: `jcp-2016-tunay`; Authors: Niklas Winkler; Lars Drugge; Annika Stensson Trigell; Gunilla Efraimsson
- Year / venue: 2016, Computers & Fluids 138:26–34
- DOI / URL: [10.1016/j.compfluid.2016.08.006](https://doi.org/10.1016/j.compfluid.2016.08.006)
- GB/T 7714: WINKLER N, DRUGGE L, STENSSON TRIGELL A, et al. Coupling aerodynamics to vehicle dynamics in transient crosswinds including a driver model[J]. Computers & Fluids, 2016, 138:26-34.
- BibTeX: `@article{Winkler2016,author={Winkler, Niklas and Drugge, Lars and Stensson Trigell, Annika and Efraimsson, Gunilla},title={Coupling aerodynamics to vehicle dynamics in transient crosswinds including a driver model},journal={Computers and Fluids},volume={138},pages={26--34},year={2016},doi={10.1016/j.compfluid.2016.08.006}}`

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

## 2026-09-25 bibliographic correction

KTH author publication record confirms the four authors above: https://kth.diva-portal.org/smash/person.jsf?pid=authority-person%3A31208 . Earlier author attribution was erroneous; stable ID `jcp-2016-tunay` is retained per TASK.md §17. Journal is Computers & Fluids, not Journal of Computational Physics. Linked record diva2:1047242 returned an anti-bot page; no full text inspected or evidence upgrade. Pass 3 remains pending.

## DOI / PDF registry (2026-09-25)

- DOI: `10.1016/j.compfluid.2016.08.006`; doi_status: `verified`; doi_source: https://api.crossref.org/works/10.1016/j.compfluid.2016.08.006; doi_verified_date: 2026-09-25.
- pdf_status: `paywalled`; pdf_source: https://doi.org/10.1016/j.compfluid.2016.08.006; pdf_path: `none`; pdf_sha256: `not applicable`; pdf_bytes: not applicable; pdf_license: publisher_or_standard_restricted; other OA locations not exhausted; github_pdf: false.
- PDF 状态为本轮已检查入口的状态；未穷尽全部机构仓储或作者版本，不将当前未找到写成永久不存在。
