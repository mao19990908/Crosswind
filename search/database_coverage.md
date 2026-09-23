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
