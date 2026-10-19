# jcp-2016-tunay — Coupling Aerodynamics to Vehicle Dynamics in Transient Crosswinds Including a Driver Model

## Bibliographic
- ID: `jcp-2016-tunay`; Authors: Niklas Winkler; Lars Drugge; Annika Stensson Trigell; Gunilla Efraimsson
- Year / venue: 2016, Computers & Fluids 138:26–34
- DOI / URL: [10.1016/j.compfluid.2016.08.006](https://doi.org/10.1016/j.compfluid.2016.08.006)
- GB/T 7714: WINKLER N, DRUGGE L, STENSSON TRIGELL A, et al. Coupling aerodynamics to vehicle dynamics in transient crosswinds including a driver model[J]. Computers & Fluids, 2016, 138:26-34.
- BibTeX: `@article{Winkler2016,author={Winkler, Niklas and Drugge, Lars and Stensson Trigell, Annika and Efraimsson, Gunilla},title={Coupling aerodynamics to vehicle dynamics in transient crosswinds including a driver model},journal={Computers and Fluids},volume={138},pages={26--34},year={2016},doi={10.1016/j.compfluid.2016.08.006}}`

## Current access / verification (2026-10-09)

- verification_status: full_text_verified; access_level: full_text; full_text_verified_date: 2026-10-09.
- local_pdf_path: sources/pdfs/jcp-2016-tunay__winkler__2016.pdf; SHA-256 045e005eeaa5984d1192ece1e99bfbbcb118d40aceb23398d14c7325311fe9b6.
- P2 complete after reading all 38 pages of accepted manuscript; P3 pending. PDF stays local (github_pdf=false).
- Current structured full-text analysis and evidence map follow the dated history below.

## Historical abstract/access record (through 2026-09-25; superseded by full text)

### Access / verification
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

## Bibliography and abstract provenance (2026-09-25)

- Canonical Bib key: `jcp-2016-tunay` in `sources/bibliography/references.bib`.
- abstract_status: `available_not_copied`; abstract_source: Official source or catalog abstract noted in source record; abstract_source_url: https://doi.org/10.1016/j.compfluid.2016.08.006.
- Full-text check: No full text has been validated; do not promote claims beyond the current evidence level.

## User-provided PDF receipt (2026-09-25)

- The earlier PDF/access note above is superseded for file availability. `winkler2016.pdf` matches this source by title and/or SAE number/DOI; 38 pages opened and text-extracted without errors.
- pdf_status: `user_provided`; pdf_path: `sources\pdfs\jcp-2016-tunay__winkler__2016.pdf`; pdf_source: `user_provided_local:Downloads/PDF/winkler2016.pdf`.
- pdf_sha256: `045e005eeaa5984d1192ece1e99bfbbcb118d40aceb23398d14c7325311fe9b6`; pdf_bytes: 4821113; pdf_checked_date: 2026-09-25.
- pdf_license: Elsevier accepted manuscript; redistribution permission not verified; github_pdf: false. The file stays local; only metadata is committed.
- Verification status remains `abstract_verified` pending substantive full-text reading and revision of abstract-based claims.

## Full-text structured reading (2026-10-09)

## Research question / physical problem

研究车辆姿态反馈是否改变瞬态横风中的载荷与车辆响应。虚拟道路上的简化客车以恒定纵向速度穿越有限横风，比较单向预计算载荷和逐时刻双向耦合；驾驶员模型改变返回原路径的过程。创新定位是这种方法组合和反馈比较，不作未经检索的“首次”判断。

## Gust / crosswind definition

PDF8、13/Fig2：整车速度25 m/s（90 km/h），横风9 m/s，名义最大相对入流角约20°。作者称阵风长度5L，升降沿各对应1.5L并使用余弦函数；不随高度变化。这是规定输入，不是本次实测自然阵风。作者据外部来源选择5L以避免稳态建立，不证明所有车辆7L都能达到稳态。

Fig2横坐标零点附近已处于上升沿，而正文称从零开始；精确空间零点/分段函数须在P3核对，不能直接把图改成从0到5的矩形窗。

## Coordinate system and normalization / important equations

PDF11–13 Eqs1–5：Cs=Fya/(0.5 rho u_inf² A)，Cyaw=Mza/(0.5 rho u_inf² A L)，St=L/(u_inf t)。u_inf为free-stream velocity、A前面积、L车长、t时间；St按本文原定义保存，不替换为其他文献的pi*f*L/U。Fya、Mza进入单轨模型，psi为车辆横摆，delta为车轮转角，不能与气动入流角混用。

PDF12–13：线性轮胎Fi=−Ci alpha_i，两自由度侧向/横摆；Eqs4–5给出载荷到加速度/横摆角加速度的关系。PDF17–20 Eqs6–14给驾驶员路径/横摆反馈及预瞄增益；Eq11与Eq12的曲率、误差、转向正负号需独立P3推导后才可用于可执行控制器，不能默默纠正原文。PDF26 Eq15：方向盘/车轮角比20。

## Vehicle / model geometry and important parameters

PDF8/16 Table1：SANDIA GTS牵引车挂车简化模型缩短成客车；整车长12.2 m、宽2.6 m、高3.6 m、轴距5.9 m；前轴至重心f=3.7 m、后轴b=2.2 m；质量13650 kg；Jz表列200000 kg m²/rad（保留印刷单位，量纲约定待P3）；前/后轴侧偏刚度250000/450000 N/rad。气动力重心标在距车头6.5 m/53.4%车长处，动力学标准重心63%轴距；两种参考长度不能混用。重心前移43%/23%的参数研究无驾驶员。

## Experimental setup / validation method

本文未开展该客车横风轨迹的实测试验。PDF10说明网格设置参考GTS既有风洞/计算：阻力系数高估12%，增减单元尺度未改善，作者讨论几何不确定性与耗散但未继续匹配。不能记作该瞬态客车已通过网格独立性或载荷验证。

PDF21–24 §3用重心前移后的响应趋势展示robustness，原因是难以获得横风中的运动测量；这不是独立Level C。驾驶员模型原先在电动轿车单轮电机故障模拟器中验证（本文二手说明ref23），不等于本客车横风驾驶员验证。未建立同车同事件A/B/C完整链。

## CFD setup

PDF9–11 §2.1：IDDES、overset、非结构六面体trimmed grid，总2400万单元，其中overlap900万；20层棱柱，总厚0.0141 m、拉伸1.25，y+<11。背景域22.5×6×1.5L、重叠域5.5×2.5×1L。1/8模型在气动域以91.6 m/s运动，Re=2×10^6；整车动力学速度25 m/s，不能把二者当同一物理尺度。气动步长6×10^-5 s，近车RANS区对流Courant<1，波动区偶达5。STAR-CCM+9.02，二阶时间、二阶迎风/有界中心混合空间离散。overset每步最小二乘插值；过粗背景网格曾引起压力伪振荡。约2500步、192核、12小时为原作者算例成本，不是本次执行成本。

## Vehicle-dynamics model / coupling method

PDF7/11–13：单向先计算不含运动反馈的CFD载荷，再驱动车辆模型；双向每个时刻更新车位姿，载荷/运动按系数和速度/长度尺度双向换算。没有报告可直接运行的完整耦合代码或迭代收敛容差；不能凭“real-time”推断强耦合子迭代。

PDF17–20：正文实际有无驾驶员、轿车参数、客车参数三种情形；不是三套非零驾驶员增益。表2两套(ky,kpsi)=(1.0,15.6)、(1.2,30.9)，均t_delta=0.55s、t_s=0.52s；一秒预瞄/25m；司机开始感知时间0.37s。表中增益未单列单位，角度及转向误差约定留给P3。同步时间用于限制不现实转向输入，不能直接臆造饱和实现。

## Main quantitative results / flow mechanisms

- PDF26–27、32 Fig17：无驾驶员、x/L=7时双向预测累积偏离8.3 m，基于侧向速度的偏移0.8 m，横摆约0.21 rad/12.2°。单向累积偏离较双向高7.3%，侧向速度积分量高3.9%，横摆高9.8%。三者不是同一指标。
- 驾驶员轿车/客车参数下，原文报告单向累积路径偏差较双向高6.3%/3.9%。这些是数值方案比较，非对实测的误差；未给通用“大偏航角”阈值或置信区间。
- PDF25–27、30 Fig12/13：顺风偏转使双向载荷衰减；驾驶员回转迎风时力矩后段重新上升。出口后负力矩不足以因惯性让无驾驶员车辆回原路。尾流波动起因是作者解释，未证明一般因果规律。
- PDF21：前移重心至23%时虽全浸没阶段力矩接近零，仍发生约9.7°横摆；标准约12.2°。作者归因于前后轮胎刚度不对称。参数趋势检查不能替代实测验证。

## Main conclusions / limitations / reproducibility

车体姿态反馈和驾驶员动作会改变本工况的气动载荷与路径。摘要“静态耦合高估”须限定模型、输入、控制器和评价量；不是所有时刻每个带符号载荷都严格更高，更不是对所有车辆的必要性定理。简化几何、固定纵向速度、线性轮胎、两自由度、无高度风梯度；缺原始网格、时程、完整驱动代码及匹配瞬态实测。P2完成；P3控制器符号/增益、尺度时间与重心变换核对仍待执行，不宣称数值输出复现。

## Relation to previous / subsequent work

PDF35 ref6直接引用既有Ryan1998，PDF36 refs7/8引用Volpe2013和Chadwick2000。仅确认references，不推断硬件/代码继承。ref12是Nakashima2013方法前作，尚未作为新source入库；ref16 Ryan2000博士论文不能错配SAE2000-01-0874。与Nakasato2017、Lewington2017可作条件化方法比较，直接继承关系仍未核；不自行扩库。

## Relevance / follow-up questions

为Level7/8/9提供“输入—姿态反馈—驾驶员—路径指标”的可追溯示例。下一轮同source Pass3：核Eq8–14符号/增益单位、按St复核时间换算、重心参考点转换和Fig2零点；有代码/时程/匹配实测再检验输出。NC-2016-VALIDATION请求原始代码/数据及同条件验证，不请求重复PDF。暂不进入proposal或research-gap写作。

## Evidence map

| Evidence | PDF locator | Knowledge |
|---|---|---|
| E-2016-01（升级/收窄） | 26–27,32; §4; Fig17 | 路径偏差对比及指标分离 |
| E-2016-02 | 7–13; §2/2.1/2.2; Eqs1–3 | 逐步反馈、模型尺度与规范化 |
| E-2016-03 | 17–20,25–27; §2.3/4; Table2 | 两套增益加无驾驶员、响应条件 |
| E-2016-04 | 10,21–24; §2.1/3; Figs6–10 | 阻力对照与趋势检查的验证边界 |

## 2026-10-10 Pass3 controller/scaling checkpoint

Targeted original-PDF review plus independent equation checks completed; no new full read or grade upgrade. [Detailed audit](../../learning/audits/winkler_2016_controller_scaling.md): full/model time29.312 gives fullscale step0.00175872s; equal-density force/moment factors4.76726226/38.1380981 require corresponding origins. All are ANALYST_INFERENCE, not verified simulation settings. Bus steady-bicycle reduction gives gain magnitudes0.021553rad/m and0.538836rad/rad;degree-output conversion1.23492deg/m and30.8730deg/rad matches roundedTable2, but code units unproven. PrintedEq11 negative versus Eq12 positive remains unresolved;do not silently repair/control from it. CG nominal shifts1.18/2.36m and half-ramp0.366s are conditional arithmetic, not definitive geometry/input timing. ExistingNC-2016-VALIDATION expanded;P3partial still pending original implementation/data. Next available source sae-2017-01-1515 Pass3 axis/spline/uncertainty audit.

## 2026-10-18 numerical-method evidence

Existing local original sections rechecked for CFD discretization/interface/refinement evidence. Source-specific new E2 claims and locators are indexed in the [four-source audit](../../learning/audits/cfd_coupling_evidence.md);formal orders,reported CFL and interface artifacts do not establish converged transient accuracy. No new source/PDF,external DOI query,grade upgrade,Pass completion or author-output replay. Historical access/abstract and earlier checkpoints remain dated snapshots.

## 2026-10-20 neutral-steer/tyre evidence

Targeted originalPDF12-13/16/21 visually checked. E-2016-08 records reported near-zero fully immersed aero moment but9.7deg yaw atCG23percent versus12.2standard;E-2016-09 records linear axle-sum tyre parameters/force-moment inputs. Analyst fixed-steer zero-yaw trim from standardTable1 gives xn=-0.092857m,not source-reported NSP or9.7deg replay. Existing source grade/raw-replay request unchanged. See [audit](../../learning/audits/neutral_steer_point.md).
