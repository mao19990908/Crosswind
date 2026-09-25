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
