# 数据库覆盖率

更新日期：2026-09-23

| 数据库／来源 | 覆盖范围 | 本次深度 | 状态与限制 |
|---|---|---|---|
| SAE Mobilus | 1953–2025 核心 DOI 与方法节点 | 逐条核验 14 个原始条目页面／摘要 | 多数全文受限；只记录元数据与摘要证据 |
| TRID | 1968、1979 DOT 历史节点 | 核验 2 个记录；DOT-HS-805-079 页面抓取失败 | 未完成系统分页检索 |
| ISO | ISO 12021:2010 与前版生命周期 | 官方页面核验 | 正文付费；仅使用公开元数据与摘要 |
| Chalmers Research | 2023 博士论文及派生论文线索 | 机构元数据页核验 | 全文存在但本轮未逐页抽取 |
| ScienceDirect | 2014、2016 关键论文线索 | 搜索摘要／片段核验 | 页面访问有 403；全文验证待权限 |
| Crossref/OpenAlex/Semantic Scholar | 尚未系统检索 | 0 页 | 后续用于 DOI 去重和 cited-by |
| Google Scholar/WoS/Scopus/CNKI | 尚未执行 | 0 页 | 权限与自动检索可用性待确认 |

“尚未搜索完成”不得解释为“没有研究”。1953 年以前、1981–1995、2001–2013 仍是明显覆盖缺口。

## source_type 覆盖统计（2026-09-23）

统计来自 `sources/index.csv`，不是数据库总体数量：

| source_type | 当前记录数 | 覆盖判断 |
|---|---:|---|
| `journal_article` | 6 | 已有代表性条目，未系统搜索 |
| `sae_technical_paper` | 11 | 本轮重点覆盖，引用网络未完成 |
| `conference_paper` | 0 | 需检索其他会议库；SAE 会议出版物归 SAE 技术论文类型 |
| `standard` | 1 | 仅 ISO 12021 正式版本 |
| `government_report` | 1 | 仅 DOT-HS-805-078，卷 II 待补 |
| `institutional_report` | 0 | 机构页面尚未筛选报告类型 |
| `doctoral_thesis` | 1 | 仅 Chalmers 博士论文 |
| `master_thesis` | 0 | 未系统检索学位库 |
| `dataset` | 0 | 未系统检索开放数据仓库 |
| `facility_documentation` | 0 | 风洞／发生器设施资料待检索 |

目前为已纳入记录的类型计数；0 表示本库当前无记录，不表示该类型确实不存在。其它规范类型也按索引中的实际记录统计。

## 2026-09-25 Benner 1958 全文增量

用户提供一份已出版 AMS 期刊全文；Crossref 精确 DOI 核验 1 条，筛选 1、纳入 1，无题名/DOI 真重复。此次 `journal_article` +1。索引当前 25 条：`journal_article` 9、`sae_technical_paper` 12、`government_report` 2、`standard` 1、`doctoral_thesis` 1。`conference_paper`、`institutional_report`、`master_thesis`、`dataset`、`facility_documentation` 仍为 0；这反映本库检索覆盖不足，不是该领域不存在这些资料。未额外搜索上述空缺类型，不能把本次 PDF 阅读记为其检索完成。

## 2026-09-24 增量覆盖与断点

- TRID：卷 II 144116 的书目和目录摘要可访问；原报告未取得。政府报告新增 1 条 metadata_verified，不能把目录摘要当已核验全文。
- SAE：1953 页面复核；1967 Beauvais DOI 670608 的原页/DOI抓取失败，本机 HTTP 25 秒超时。670100 为另文，当前摘要缺少瞬态关联，排除。
- SAGE：2001 Passmore 原始出版者摘要和完整公开参考文献 1–10 核查；新建 1 条 journal_article、核验 2 条 references。正文未取得。
- OpenAlex：仅 seed DOI 元数据（W1518832512；引用计数 30）；0 个 cited-by 分页。
- Semantic Scholar：seed DOI 返回 30 条 cited-by 标题/DOI，已全部筛题并留候选；不宣称跨数据库完整覆盖。剩余三个核心 DOI 的 API cited-by 未执行。
- Loughborough 作者书目：发现 Windsor 数据集 DOI 10.17028/rd.lboro.13161284，未检索数据本体/说明；不得当作阵风验证数据。
- 2026 中英文检索：保留 4 条候选线索；中文原始页打开失败。范围非穷尽，未知结果总数留空。

### 当前类型覆盖与本次新增

| source_type | 当前 | 本次新增 | 缺口判断 |
|---|---:|---:|---|
| journal_article | 7 | 1 | 2001 频率响应节点已补；全文和 2026 原始资料待核验 |
| sae_technical_paper | 11 | 0 | 1967 原始页访问受限；1953 references 未补齐 |
| conference_paper | 0 | 0 | 2001 原始参考文献列出 Bearman/Mullarkey 1994 会议，尚未核验原始出版物；覆盖不足 |
| standard | 1 | 0 | 仅现有 ISO 条目，历史版本与国家标准覆盖不足；本日未重新检索状态 |
| government_report | 2 | 1 | 卷 II 书目已补，原报告可访问性待解决；两个记录属同项目 |
| institutional_report | 0 | 0 | 机构报告专门检索未执行，覆盖不足 |
| doctoral_thesis | 1 | 0 | 新线索 Mullarkey 1990，原机构记录未核验；覆盖不足 |
| master_thesis | 0 | 0 | 学位库专门检索未执行，覆盖不足 |
| dataset | 0 | 0 | 作者书目已提供 DOI 线索，阵风适用性与开放许可未检索完成 |
| facility_documentation | 0 | 0 | 历史论文中的设施不自动改分类；独立设施资料检索不足 |

本日无 source_type 枚举变化。A–M 主题与 source_type 保持独立。所有零项均无“不存在”的证据；不能把未执行解释成检索无结果。

### 2026 候选（不进入规范来源索引）

- https://pubs.cstam.org.cn/article/doi/10.7638/kqdlxxb-2025.0207 — 某三厢轿车的侧风敏感性仿真研究；发现于原出版网站搜索片段，打开失败，待核验瞬态输入、闭环状态、验证等级。
- https://doi.org/10.3390/fluids11050119 — 重卡合流/编队侧风 CFD；仅聚合器搜索线索，原文未查。
- https://doi.org/10.3389/ffutr.2026.1871420 — 厢式货车侧风稳定性；原站搜索片段，原文未查。
- https://doi.org/10.1061/JSDCCC.SCENG-1766 — 桥梁耦合/行驶轨迹；原站搜索片段，原文未查。

## 2026-09-25 学习访问审计
本日未收集新来源，各source_type新增均0。Passmore全文通过Loughborough/Figshare精确标题API定位9225113，已核读10页原文；源索引升级full_text_verified。1953/1973/1996/1998/2017 SAE均仅有公开摘要，ISO仅公开目录范围；KTH确认2016作者但单篇入口受anti-bot阻断。不是全部机构仓储穷尽搜索，未取得不等于不存在。既有14条达标学习未重做。

## 2026-09-25 DOI/PDF 全量核对

22 条来源中 SAE Technical Paper 11、journal_article 7、government_report 2、standard 1、doctoral_thesis 1；其他重点类型仍 0，本次未新增 source_type 或研究来源。17 DOI 经 Crossref 精确解析并匹配标题/出版年份；ISO 官方目录未列 DOI，另 4 条暂待跨库 DOI 搜索。合法 OA 入口 4 条，已在本机留存 2 份；0 份有足够再分发许可证据可提交 GitHub。OpenAlex 无 PDF URL 的 OA 标记只是线索，不能算下载。历史/引文/方法谱系仍沿用本日早间断点；本轮优先 v4 任务，不制造新边。

## 2026-09-25 后续增量覆盖判断

总数 **23**：journal_article **8**（今日后续新增 `jfe-2013-volpe` 1）、sae_technical_paper **11**、government_report **2**、standard **1**、doctoral_thesis **1**。其余强制检查类型 conference_paper、institutional_report、master_thesis、dataset、facility_documentation 均仍为 **0**；对应缺口分别是会议原始出版物核验不足、机构报告专项检索不足、硕士学位库专项检索不足、开放阵风数据适用性和许可未查清、独立设施文档尚未核验。零不等于不存在。2013 年设施论文仍归 `journal_article`，不能因内容涉及设施就重复计入 `facility_documentation`；A–M 主题标签与发布类型独立。

## 2026-09-25 v5 后单篇历史补入

已用 SAE 出版页、Crossref 精确 DOI 和 OpenAlex 精确 DOI 核验 `sae-670608`（Beauvais 1967），作为 SAE Technical Paper 入库；公开摘要能确认准稳态/瞬态阵风风洞载荷比较的研究问题，但未取得全文，不臆测峰值结果。当前总数 **24**：sae_technical_paper **12**、journal_article **8**、government_report **2**、standard **1**、doctoral_thesis **1**。本次 source_type 新增 SAE 1，其它类型 0；conference_paper、institutional_report、master_thesis、dataset、facility_documentation 缺口仍在。Crossref/OpenAlex 已从早期“0页”逐步用于 DOI/合法 OA 核验；上表保留历史快照，不能读作当前完全未检索。

DOI 状态：18 verified、4 暂时 no_doi_confirmed、1 missing_to_search，覆盖率 18/23 = 78.26%。本机有效 PDF 3，SAE 2025 出版者 CC BY PDF 可上传 GitHub 1；Durham 和 HAL 2013 是 OA 页面线索，不计 PDF。此次历史/方法检索新增 2014 → 2013、2013 → 1996、2013 → 2001 三条 verified references 边，以及 2013 → 2000 Durham 的**概念方法继承**边；后者由 2013 作者摘要与 2018 Springer 原始研究交叉支持，不冒充 2013 原文的直接 references 边或硬件复用证明。

1953 SAE Crossref 现有 5 条参考元数据，含 1951 Lett 学位论文、Stuttgart Huber No.44 与 Sawatzki No.50；Stuttgart 官方档案另列 1941 No.50 和 1942 突发侧风 film report。它们是 pre-1953 来源/类型候选，**尚未入规范索引**：Lett 缺大学原馆藏，Huber No.44 标题/年代版本冲突，Sawatzki 报告与 1953 引文标题不同，1942 film report 未取得内容。`institutional_report`、`doctoral_thesis` 当前总量不据线索虚增；后者仍仅 Brandt 2023 一条。后续优先核实原始档案单项和报告全文。

## 2026-09-26 DOI/PDF access audit

Existing25 sources audited; new sources0. Five Crossref exact DOI refreshed; remaining primary proofs retained. Seven missing full texts searched; DOT I/II HathiTrust/Google Books and Volpe OATAO leads added. No new PDF; local18/GitHub1/local-only17. Unpaywall deferred without configured contact email. Learning backlog10; source-type coverage unchanged.

## 2026-10-13 existing-source access check

Two existing canonical targets only: Crossref DOI/title/author/year reverified; OpenAlex and Semantic Scholar read, one OATAO PDF request timed out. Exact-title/domain discovery did not yield an acquired primary original. No new source/PDF or claim. Unpaywall deferred without configured contact; protected endpoints not retried. This does not establish exhaustive absence of OA.

## 2026-10-14 existing-source catalog lookup

ISO12021 paid/preview catalog;DOT I/II TRID metadata and NASA indexed bibliography only. Added VolII retrieval identifierPB80-118383/N80-21219; no original PDF. Search limited to three existing targets;prior protected endpoints not retried;other sources not freshly searched. No new source/claim/evidence grade.

## 2026-10-15 existing-source evidence search

Bell/Milner originals and existing raw-data requests pursued;no newsource/PDF. DataCite exact relatedIdentifier searches forWinkler/Lewington/Nakasato returned0;this excludes neither unregistered nor unlinked data. BellOpenAlexclosed/S2 429 stopped;DLR nofulltext. Gnadler/Sorgatz original not acquired. Existing protected URLs not retried. Details inaccess_check JSON.
