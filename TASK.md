# 车辆瞬态侧风（阵风）知识库：Codex 长期执行任务书

> 本任务书用于在用户 Windows 电脑上长期建设道路车辆瞬态侧风知识库。本机工作树：`D:\GEELY\Crosswind`；远端：`https://github.com/mao19990908/Crosswind`。首次执行先建库和历史回溯，此后每日增量收集与整理。时间均按 Asia/Shanghai。

## 1. 总目标与研究边界

建立可溯源、可检索、可持续更新的**道路车辆瞬态侧风／阵风（transient crosswind / crosswind gust）**知识库，服务于“车辆侧风模拟及实验验证”。主因果链为：

**阵风输入 → 非定常气动载荷 → 车辆横向／横摆／侧倾响应 → 驾驶员或控制器修正。**

以乘用车为主；商用车、客车、列车等仅在方法可迁移或作为对照时纳入。不以噪声为研究主题。

必须严格区分：

- 瞬态阵风与固定偏航角稳态侧风；
- 车辆驶入有限侧风区、step/pulse/ramp/sinusoidal/stochastic gust、自然道路阵风、隧道出口／桥梁／会车等瞬态扰动；
- 瞬时相对来流偏航角、车辆航向角、质心侧偏角；
- open-loop 与 closed-loop；
- 标准风发生器工况与真实道路自然阵风。

固定偏航角研究只能作为 steady baseline、准稳态输入、误差比较或机理对照，不能直接写成阵风结论。

## 2. 检索必须沿历史和方法谱系推进

不得随机堆论文。必须同时执行：

1. **历史回溯**：从已确认早期资料向更早来源追溯；
2. **references**：沿参考文献向前追；
3. **cited-by**：沿被引文献一直追到当前年份；
4. **method lineage**：追踪方法继承、改进、分叉、实验设施继承、数据复用和结论冲突；
5. **current update**：补充最新论文、标准、报告、数据和设施资料。

每个关键历史节点都要形成引文链，而不是只保存一篇记录。

当前重要切入点包括但不限于：

- 1953 SAE 530255：Wind Effects on Car Stability；
- 1971 SAE 710287；
- 1973 SAE 730232；
- 1979 DOT-HS-805-078/079；
- 1980 SAE 800848；
- 1996 SAE 960674：static yaw 与 dynamic gust 比较；
- 1997 SAE 970135、970404；
- 1998 SAE 980392；
- ISO 12021-1:1996（已撤销，仅保留历史）；
- ISO 12021:2010（现行基准标准）；
- 后续 transient CFD、DES/DDES/LES、aerodynamic admittance、ROM、CFD–vehicle dynamics coupling、road validation 等路线。

不得预设“第一篇”或“没人做过”，必须记录检索覆盖范围和反证。

## 3. 分类体系

主类别：

- A 历史与定义
- B 阵风输入与环境
- C 非定常气动理论
- D 气动系统响应模型
- E 车辆动力学理论
- F 风洞／移动模型实验
- G 整车／道路实验
- H 气动 CFD
- I 气动—车辆动力学耦合
- J 验证与评价
- K 标准与规范
- L 数据与开放资源
- M 工程应用

每篇资料可有多个标签，但只保留一个规范化主记录。分类改变必须写入 `taxonomy_change_log.md`。

## 4. 资料不等于论文：强制 source_type

所有来源必须赋予 `source_type`：

```text
journal_article
sae_technical_paper
conference_paper
standard
standard_draft
government_report
institutional_report
project_report
doctoral_thesis
master_thesis
book
book_chapter
review_article
dataset
code_repository
facility_documentation
manufacturer_technical_document
patent
regulatory_document
web_primary_source
secondary_web_source
```

优先原则：

- 试验工况／评价方法：正式标准、原始技术报告优先；
- 历史全尺寸侧风试验：政府／研究机构报告、SAE Technical Paper、学位论文优先；
- 理论和模型：原始期刊、SAE、博士论文优先；
- CFD 复现：论文 + 学位论文 + 补充材料；
- 验证：公开数据、原始实验报告、正式论文；
- 标准状态：ISO／国家标准官方源；
- 综述和二手网页主要用于发现原始资料，不能替代原始证据。

README 和 `search/database_coverage.md` 定期统计各 source_type 数量。某类长期为 0 时，必须判断是资料确实少、检索不足、关键词不对还是权限受限。

## 5. 阵风参数标准化

凡研究涉及阵风，尽可能提取：

- 车辆速度 `Uv`；
- 横风速度 `Ug`；
- 合成速度与瞬时相对来流偏航角 `beta(t)`；
- gust rise time、duration、decay time、period、frequency；
- gust-zone length/width/height；
- gust edge thickness、longitudinal/lateral/vertical gradient；
- turbulence intensity；
- integral length scale；
- PSD、coherence、gust factor；
- vehicle residence time；
- sampling frequency / CFD time step；
- road environment、measurement height、terrain。

可比较时记录：

```text
t* = t Uv / L_vehicle
Lg* = Lg / L_vehicle
```

以及作者定义的 reduced frequency、Strouhal number、gust parameter。必须保留原作者定义，不能因为名称相同就假定公式相同。

## 6. 理论主线

重点整理：

- quasi-steady model；
- non-quasi-steady behavior；
- overshoot / undershoot；
- phase lag / hysteresis；
- aerodynamic derivatives；
- aerodynamic admittance；
- transfer / frequency response function；
- weighting function / convolution / impulse response；
- wake memory；
- reduced-order model；
- state-space / system identification；
- POD/DMD、surrogate、ML-ROM。

区分物理可解释 ROM 与纯数据拟合模型。

## 7. 车辆动力学主线

记录：bicycle/four-wheel/multibody、tyre、suspension、roll、steering、driver/controller。

优先输出：yaw rate、lateral acceleration、sideslip angle、roll angle、steering correction、lateral displacement、lane deviation。

每条结果标注：

```text
open_loop
closed_loop_driver
closed_loop_controller
autonomous_control
```

不同闭环类型不得直接合并比较。

## 8. 实验复现信息

### 风洞／移动模型

记录：风洞尺寸、blockage、边界层、地面模拟、车轮、模型比例、Re、模型质量/惯量、天平动态响应、sampling/filtering、压力、PIV、同步、不确定度。

阵风装置分类：side fan array、wind generator、active grid、shutter、moving model through crossflow、moving vehicle through fixed wind zone、oscillating vane、rotating blade、transient inlet。

必须提取风场均匀性、梯度、rise length、edge thickness、TI、重复性和标定方法。

### 道路／整车

记录：场地、风机布置、车辆速度控制、steering constraint、driver participation、IMU、GPS/RTK、方向盘角/力矩、风速测量、环境风、路面坡度、重复次数和不确定度。

## 9. CFD 复现信息

记录：

- geometry simplification、moving ground、wheel rotation；
- domain、blockage、reference area、moment reference point；
- mesh type、cell count、prism layers、y+、wake/gust refinement、grid independence；
- RANS/URANS/DES/DDES/IDDES/LES；
- physical time step、CFL、inner iterations、residual、time-step independence；
- transient inlet、spatial inlet、moving mesh、moving vehicle、moving gust region、synthetic turbulence、precursor/mapped turbulence；
- `CY(t)`、`CN(t)`、`CL(t)`、rolling moment、pressure、vortex/separation/wake、peak、phase lag、rise/relaxation time。

## 10. CFD—车辆动力学耦合等级

统一标记：

- Level 0：稳态系数表；
- Level 1：瞬时相对风角查稳态表；
- Level 2：预计算 transient CFD → load time series → Vehicle Dynamics；
- Level 3：ROM / transfer function 耦合；
- Level 4：在线单向耦合；
- Level 5：CFD 与 vehicle dynamics 双向 fully coupled。

## 11. 三级验证

必须区分：

- Level A：阵风风场验证；
- Level B：气动力／压力／相位／峰值验证；
- Level C：整车 yaw/lateral/sideslip/steering/lane deviation 验证。

“CFD 与风洞气动力一致”不能直接写成“车辆侧风稳定性已验证”。

## 12. 检索数据库

优先：SAE Mobilus、Crossref、OpenAlex、Semantic Scholar、Google Scholar、TRID、ISO、出版社、政府报告、大学机构仓库、学位论文数据库、CNKI；Web of Science/Scopus 可访问时使用。

英文、中文及必要的德文历史术语都要搜索。第三方聚合页面只作线索。

## 13. 引文关系与覆盖率

维护：

```text
citations/citation_edges.csv
citations/citation_graph.md
citations/method_lineages.md
search/search_ledger.csv
search/query_library.md
search/database_coverage.md
```

`citation_edges.csv` 至少包含：

```text
source_id,target_id,relation,verified,note
```

relation 可取：references、cited_by、method_inherits、method_extends、facility_inherits、data_reuses、supports、contradicts、standardizes。

`search_ledger.csv` 至少记录：date,database,query,year_from,year_to,result_count,screened,included,excluded,notes。

不得把“没搜到”写成“没有研究”。

## 14. DOI 总账：强制执行

对所有适用来源检查 DOI。每条记录新增：

```text
doi
doi_status
doi_verified_date
doi_source
```

`doi_status` 只允许：

```text
verified
no_doi_confirmed
missing_to_search
invalid_or_conflict
not_applicable
```

不能因为 DOI 为空就认定资料缺失；标准、政府报告、早期资料和部分学位论文本来可能没有 DOI。

新增：

```text
sources/doi_registry.csv
```

至少包含：

```text
id,title,year,source_type,doi,doi_status,doi_url,doi_source,doi_verified_date,pdf_status,pdf_source,pdf_path,license,notes
```

每次运行统计：

```text
total_sources
sources_with_verified_doi
sources_without_doi_confirmed
sources_missing_doi_to_search
sources_with_doi_conflict
doi_coverage_rate
```

DOI 必须通过 Crossref、出版社、SAE 或其他原始来源核验；不得猜 DOI。

## 15. 合法全文 PDF 检索与下载：强制执行

GitHub 可以存 PDF；当前知识库目标是尽可能保存**合法可获取、可重复核验**的全文，而不是绕过付费墙。

允许自动获取：

- publisher OA PDF；
- Unpaywall 合法 OA location；
- OpenAlex OA full-text；
- Semantic Scholar 合法公开 PDF；
- PubMed Central / arXiv；
- institutional / university repository；
- government repository；
- 作者合法公开 manuscript；
- 用户本人已经合法获得并放入本机目录的文件。

禁止：

- 绕过出版社付费墙；
- 绕过登录、验证码、Cloudflare 或其他访问控制；
- 使用 Sci-Hub 等非授权镜像作为自动下载源；
- 将无再分发授权的付费 PDF 推送到 GitHub；
- 因为网页能显示全文就默认拥有再分发权。

推荐自动检索顺序：

```text
DOI
 ↓
publisher / official source
 ↓
Unpaywall
 ↓
OpenAlex
 ↓
Semantic Scholar
 ↓
institutional / author repository
 ↓
Crossref resource links
```

无 DOI 时用 `title + authors + year` 检索。

每条来源新增：

```text
pdf_status
pdf_source
pdf_path
pdf_sha256
pdf_bytes
pdf_license
pdf_checked_date
```

`pdf_status` 只允许：

```text
oa_downloaded
user_provided
institutional_access
open_repository_available
paywalled
not_found
not_pdf
download_failed
license_unclear
```

下载后必须检查 PDF 文件头、MIME、文件大小、可打开性、题名/DOI 对应关系，并计算 SHA-256；不能把 HTML 错误页误当 PDF。

本机目录：

```text
sources/pdfs/
```

推荐文件名：

```text
<stable_id>__<first-author>__<year>.pdf
```

### GitHub 与本地 PDF 规则

可提交 GitHub：明确 OA、public domain 或明确允许再分发的全文。

只存本机：机构订阅获得但没有再分发权、publisher paid PDF、许可不清楚的 PDF。

只存本机时，在索引记录 `github_pdf=false`，不得提交文件本体。

## 16. 可选学术检索／PDF Skill

Codex 可以使用或参考公开 Skill，但安装前必须审查：

- `ustc-ai4science/academic-search`
- `hideshi/scholarly-agent-skills` 中的 `pdf-paper-ingestion`

目标流程：

```text
Crossref / OpenAlex / Semantic Scholar / Unpaywall
        ↓
verify metadata
        ↓
locate legal OA PDF
        ↓
download
        ↓
validate PDF
        ↓
hash + register
```

安装第三方 Skill 前必须：

1. 阅读 `SKILL.md`；
2. 检查访问域名和脚本；
3. 禁用任何绕过 paywall / captcha 的 fallback；
4. 不向第三方脚本写 GitHub token、企业账号、浏览器 cookie；
5. 在 `scripts/skills_registry.md` 记录 Skill 名、来源、版本／commit SHA 和启用状态。

## 17. 文献去重与版本关系

每次批量入库后检查 verified DOI、SAE paper number、标准号、政府报告号、规范化题名+年份、近似题名+作者+venue、跨数据库别名。本库首次全量迁移记录在 `sources/dedup_report.csv`。真正重复时选择信息最全且验证最高的 canonical record，合并信息并删除冗余记录；旧 ID 写入 `sources/aliases.csv`，同步修正 citation、learning、timeline 和 synthesis 等活跃引用。历史日志不重写。

conference→journal、thesis→paper、preprint→final、ISO→国家采用版、报告 Volume I/II、draft→final 和同一项目不同方法论文，原则上保留为独立资料，用 `version_of`、`derived_from`、`extended_by`、`national_adoption_of`、`companion_report` 等关系连接。不能确定时标记 `needs_manual_review`，不得自动删除。

## 18. 单篇记录

路径：

```text
sources/records/<stable_id>.md
```

至少包括：标准引文（GB/T 7714，可附 BibTeX）、DOI、URL、source_type、access、verification、研究对象、gust parameters、坐标系、参考点、方法、网格/试验设置、观测量、关键结论及页码/图号、验证、局限、课题关联、follow-up。

未知字段写“未报告”；只看摘要时写 `abstract_verified`，不能推断全文细节。

证据字段：

```text
access_level: metadata_only | abstract | full_text
evidence_type: theory | steady_wind_tunnel | dynamic_wind_tunnel | moving_model | CFD | coupled_simulation | full_scale_test | road_test | natural_wind_measurement | standard
validation_level: none | internal_consistency | compared_with_CFD | compared_with_wind_tunnel | compared_with_full_scale | road_validated | multi_level_validated
verification_status: unverified | metadata_verified | abstract_verified | full_text_verified | cross_source_verified
```

## 19. sources/index.csv

至少包含：

```text
id,title,authors,year,doi,doi_status,doi_verified_date,doi_source,url,pdf_status,pdf_source,pdf_path,pdf_sha256,pdf_license,source_type,publisher_or_institution,report_or_standard_number,primary_category,secondary_categories,tags,gust_type,method,vehicle_class,access_status,evidence_type,validation_level,verification_status,added_date,last_checked
```

UTF-8，稳定 ID 不随整理改名。v5 增加 `bib_key`、`abstract_status`；`bib_key` 应与规范 Bib 条目和 `sources/bibliography/bib_sources.csv` 一一对应。`abstract_status` 与 `verification_status` 分开记录，避免把摘要可得误写成已核全文。

## 20. 综合输出

维护：

```text
synthesis/state_of_the_art.md
synthesis/research_gaps.md
synthesis/disputed_findings.md
synthesis/gust_parameter_matrix.csv
synthesis/experiment_matrix.csv
synthesis/simulation_matrix.csv
synthesis/validation_matrix.csv
synthesis/coupled_methods_matrix.csv
synthesis/research_hypotheses.md
```

research gap 必须说明：现有证据、已解决到什么程度、未解决什么、为何重要、如何验证、与博士后课题关系。不能只写“研究较少”。

## 21. 仓库结构

```text
Crosswind/
├─ README.md
├─ TASK.md
├─ Crosswind_TASK_v4_DOI_PDF.md
├─ history/timeline.md
├─ taxonomy.md
├─ taxonomy_change_log.md
├─ search/
│  ├─ search_ledger.csv
│  ├─ query_library.md
│  └─ database_coverage.md
├─ scripts/
│  └─ skills_registry.md
├─ citations/
│  ├─ citation_edges.csv
│  ├─ citation_graph.md
│  └─ method_lineages.md
├─ sources/
│  ├─ index.csv
│  ├─ doi_registry.csv
│  ├─ bibliography/references.bib
│  ├─ bibliography/bib_sources.csv
│  ├─ dedup_report.csv
│  ├─ aliases.csv
│  ├─ manual_retrieval_queue.csv
│  ├─ manual_retrieval_queue.md
│  ├─ records/
│  └─ pdfs/
├─ notes/
├─ standards/
├─ datasets/
├─ synthesis/
├─ logs/YYYY-MM-DD.md
└─ .gitignore
```

## 22. Git 与版权

每天本地整理 → commit → push → 核对 remote SHA 与 local HEAD。一旦 push 失败，保留本地提交并在日志写明，不得声称已双份同步。

禁止提交：token、cookie、密码、吉利内部数据/模型/未授权资料、大型计算输出、无再分发授权的版权 PDF。

## 23. 每日 06:00 与额度

每天 **06:00 Asia/Shanghai** 运行。机器未开机时启用“错过后尽快补跑”，同一自然日只运行一次。

每日使用**可用周额度总量最多 12%**，不要求强行耗满；每周最多 84%，余量约 16%。若额度不可准确读取，记录 `quota_status=unavailable`，不要伪称严格控制了 12%。

## 24. 每日任务优先级

1. 补历史引文链断点；
2. 追核心资料 cited-by；
3. 补理论／实验／CFD 方法谱系；
4. 补 DOI `missing_to_search`；
5. 核验已有 DOI；
6. 为 verified DOI 检索合法 OA PDF；
7. 处理无 DOI 的技术报告／学位论文／标准全文；
8. 搜最新资料；
9. 补全文与旧记录验证；
10. 更新 synthesis。

原则：先提高证据质量，再追求数量。

## 25. 每日运行流程

```text
01 检查周额度
02 检查 Git 状态并同步
03 读取昨日断点
04 检查 timeline / citation graph 缺口
05 历史回溯
06 cited-by 追踪
07 最新资料检索
08 核验 DOI / DOI status
09 检索合法 OA / 授权全文
10 下载并校验 PDF
11 更新 doi_registry / index / records
12 更新 citation_edges / search_ledger / method_lineages / timeline
13 更新 synthesis
14 去重并校验 DOI-author-year-PDF 对应关系；更新 aliases / version edges
15 更新 canonical Bib 与逐条元数据/摘要来源
16 把仍缺重要全文的资料加入人工补档清单
17 更新 DOI / PDF / Bib / 人工补档覆盖统计
18 校验 Bib-DOI-index、别名、引用 ID、PDF/verification 和 learning 状态
19 写日报与持久化断点
20 git commit / push
21 校验本地／远端 SHA
```

## 26. 每日日报

`logs/YYYY-MM-DD.md` 至少包含：数据库和检索式、候选/筛选/纳入/排除、source_type 统计、历史追溯进度、citation edge、新发现 3–5 条及 source ID、矛盾、research gaps、额度、Git SHA、次日断点。

DOI/PDF 额外统计：

```text
DOI
- total_sources
- verified_doi
- no_doi_confirmed
- missing_to_search
- invalid_or_conflict
- doi_coverage_rate

PDF
- oa_downloaded
- user_provided
- open_repository_available
- paywalled
- not_found
- download_failed
- local_pdf_count
- github_pdf_count

new_doi_verified_today
new_pdf_downloaded_today
pdf_download_failures

Bibliography
- total_bib_entries
- entries_with_abstract
- entries_abstract_available_not_copied
- metadata_only_entries

Manual retrieval
- needs_user_search_total
- new_needs_user_search_today
- user_supplied_resolved_today

Dedup
- duplicate_candidates
- merged_and_deleted
- kept_as_version
- needs_manual_review
```

## 27. 阶段目标

- Phase I：历史、术语、timeline、citation graph、taxonomy、method lineage；
- Phase II：quasi-steady、non-quasi-steady、aerodynamic derivatives/admittance、ROM；
- Phase III：wind generator、moving model、full scale、road test、natural gust；
- Phase IV：transient CFD、gust implementation、grid/time-step/validation；
- Phase V：CFD–vehicle dynamics coupling；
- Phase VI：研究现状、方法演化、争议、空白、可验证假设与博士后方案启示。

## 28. 长期原则

1. 从历史源头沿方法演化追到当前，不做随机论文收藏；
2. 阵风与固定偏航角严格区分；
3. 原始来源优先；
4. 综合结论必须追溯到 source record；
5. 未看全文不能写成全文已确认；
6. 未报告的数据不得推测；
7. 证据完整度和可复现性高于论文数量；
8. 建立引用关系和方法谱系，而不是只囤 PDF；
9. “资料”不等于“论文”；
10. DOI 与全文状态必须可统计；
11. 自动下载只允许合法开放或用户有权访问的全文；
12. 每个重要结论都应尽可能关联 DOI、原始入口、全文状态和验证等级。

最终知识库必须能够回答：

> 从道路车辆侧风研究最早可核查的工作开始，这一领域的理论、实验和数值方法怎样一步步发展到今天？

以及：

> 当前“车辆侧风模拟及实验验证”最值得继续解决的科学与工程问题是什么？

## 29. 当前长期执行规则

本文件已吸收 v4 DOI/PDF 与 v5 Bib/人工补档/去重规则，是资料收集的长期唯一主任务书；`Crosswind_TASK_v4_DOI_PDF.md` 和 `Crosswind_TASK_v5_BIB_MISSING_DEDUP.md` 仅作版本审计。开始先读取持久化 learning/state 与当日日志；若已有学习 backlog，按学习任务书从断点继续，清零后才在剩余额度内大规模收集。手动优先任务可覆盖日常顺序，但不得越权获取全文。遇到版权、权限、额度、网络、数据库限制如实记录。**不得编造来源、绕过访问控制、伪称已下载全文或已同步。**

## 30. 规范 Bib 文献库与摘要证据

适合 BibTeX/BibLaTeX 的论文、SAE Technical Paper、学位论文、报告及标准一源一条，写入 `sources/bibliography/references.bib`，稳定 citation key 对应 `sources/index.csv` 的 `id`。尽可能保存 author、title、year、journal/booktitle/institution、volume、number、pages、publisher、DOI、URL、abstract、keywords、note。DOI 必须与 `sources/doi_registry.csv` 中 verified DOI 一致；URL 优先原始出处。策展标签写进 keywords 时必须标明并非作者关键词。

`sources/bibliography/bib_sources.csv` 逐条记录 Bib 来源/URL/核验日期、摘要状态/来源/URL/核验日期、metadata_quality 和备注。摘要状态使用 `full_abstract_saved`、`available_not_copied`、`abstract_not_available`、`abstract_not_checked`、`full_text_supersedes_abstract`。仅在原始来源明确提供且有可保存依据时复制摘要；许可不明时只记录来源与结构化摘要笔记，不按题名编写伪摘要。必须分别区分 metadata only、abstract available、abstract saved、full text available 和 full text verified。Bib 是书目元数据，不替代 `sources/records/` 的研究分析。

## 31. 人工补档清单与用户交接

重要来源已查 DOI、出版社、合法 OA 服务及机构仓储后仍缺全文，或早期/核心方法论文只凭摘要不足以核对公式、实验/CFD 参数时，加入 `sources/manual_retrieval_queue.csv` 和可读的 `.md`。CSV 至少包含 id、题名、作者、年份、source_type、DOI、官方入口、PDF 状态、缺全文的具体原因、已尝试渠道、优先级、请求/检查日期、manual_status、用户提供路径和备注。状态使用 `needs_user_search`、`user_searching`、`user_supplied`、`resolved_elsewhere`、`not_needed`。不能把已查入口的付费/未找到状态写成永久不存在 OA。

每日结束额外汇报“需要用户手动查找的资料”：本次新增与未解决总数，并按优先级列出题名、作者、年份、DOI、官方入口。用户把合法获得的 PDF 放回项目后，下一轮核对题名/DOI/PDF 格式、可读性和 SHA-256，更新 PDF 与 manual_status，阅读真实全文后才升级 `full_text_verified` 并重审以前仅依赖摘要的结论。授权不明的文件仅本机保存。

## 32. v5 一次性迁移与后续校验

首次运行对全部旧来源建立 Bib/摘要来源台账，检查 DOI/编号/题名/作者+venue 等重复候选，把真实重复合并并在 aliases 追溯；相关版本保留且明确关系。对既有 PDF 重新核对格式、题名、DOI（若原件印有）、页数、字节和 SHA-256，特别注意论文汇编摘要与其未附原篇的不同全文范围。更新 README、records、citations 和受影响矩阵，保留历史日志。运行仓库、DOI/PDF、Bib/dedup、learning 校验及 `git diff --check`，再 commit、push、核对本地 HEAD 与远端 SHA。日报必须给出 Bib/摘要、去重、人工补档和全文验证计数。
