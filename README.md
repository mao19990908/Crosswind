# 车辆瞬态侧风（阵风）知识库

本仓库持续整理道路车辆瞬态侧风／阵风的历史、理论、实验、CFD、车辆动力学与耦合验证证据。研究主线是：

> 阵风输入 → 非定常气动载荷 → 横向／横摆／侧倾响应 → 驾驶员或控制器修正

## 证据边界

- 瞬态阵风与固定偏航角稳态侧风分开记录；稳态结果仅作为基线或准稳态输入。
- open-loop、closed-loop driver、closed-loop controller 与 autonomous control 分开比较。
- `metadata_only`、`abstract_verified` 与 `full_text_verified` 不混用。
- 未报告参数写“未报告”；分析者推断显式标为 `analyst_inference`。
- 仓库不保存未获授权的受版权保护全文、内部数据或大型计算文件。
- 每条资料同时记录研究主题类别 A–M 与规范发布类型 `source_type`；资料不只限于论文。

## 资料类型覆盖

来源总数和各 `source_type` 数量以 `sources/index.csv` 为准。v3 强制检查的类型包括：

`journal_article`、`sae_technical_paper`、`conference_paper`、`standard`、`government_report`、`institutional_report`、`doctoral_thesis`、`master_thesis`、`dataset`、`facility_documentation`。

当前索引共 23 条；分类型覆盖与尚未检索的类别判断见 [database_coverage.md](search/database_coverage.md)。

## 导航

- [任务书](TASK.md)
- [历史时间线](history/timeline.md)
- [分类体系](taxonomy.md)
- [检索覆盖率](search/database_coverage.md)
- [来源索引](sources/index.csv)
- [规范 Bib 文献库](sources/bibliography/references.bib)与[元数据、摘要来源台账](sources/bibliography/bib_sources.csv)
- [需要用户手动查找的全文](sources/manual_retrieval_queue.md)
- [全库去重复核](sources/dedup_report.csv)与[旧 ID 映射](sources/aliases.csv)
- [方法谱系](citations/method_lineages.md)
- [研究现状](synthesis/state_of_the_art.md)
- [研究空白](synthesis/research_gaps.md)
- [当日日志](logs/2026-09-25.md)

当前处于 Phase I：先建立可追溯的历史与方法地图，不把初步线索包装成成熟综述结论。

## v5 书目、去重和补档（2026-09-25）

现有 23 条资料均有稳定 ID 对应的 Bib 条目；[Bib 来源台账](sources/bibliography/bib_sources.csv)逐条给出元数据和摘要来源。仅有明确 CC BY 4.0 再利用依据的 SAE 2025 摘要复制进 Bib；其他官方/仓储摘要仅标明可得来源，未整段复制。`abstract_status` 与 `verification_status` 分开：有摘要不代表已核读全文。

首次全量检查 DOI、SAE/标准/报告号、规范化题名和近似题名后，没有确认的真重复项，因此没有删除旧记录，[aliases.csv](sources/aliases.csv)目前只有表头。3 对相关版本/设施延续来源保留为不同资料，判定理由见[去重报告](sources/dedup_report.csv)；报告 Volume I/II 新增 `companion_report` 边。现有 3 份本机 PDF 重新核对文件头、可读页数、题名和 SHA-256；Passmore、SAE 2025 两条为 `full_text_verified`，Brandt 92 页学位论文 PDF 只有扩展摘要与文献目录、不含 Paper A–E 原篇，保持保守的 `abstract_verified`。

[人工补档清单](sources/manual_retrieval_queue.md)现列 20 条仍无已校验本机全文的资料，按 P0/P1 标明原始入口、为何需要全文和已查渠道。付费/未找到只代表当前已核验入口；Unpaywall、受限机构仓储与其他合法 OA 搜索仍可继续。拿到 PDF 后请放入 `sources/pdfs/`，后续运行会核验并更新 DOI/PDF、学习与综合结论。

## 本地全文 PDF

合法取得的 PDF 登记在 `D:\GEELY\Crosswind\sources\pdfs\`。旧 `local_fulltext\` 副本保留。两目录默认被 `.gitignore` 排除；只有明确允许再分发的 PDF 才逐个 `git add -f` 纳入 GitHub。

Passmore 作者存档与 Brandt Chalmers 学位论文仅本机留存；前者已核读全文，后者已核读仓储 PDF 的扩展摘要页段（其 Paper A–E 附录原篇不在该 92 页文件内）。SAE 2025 出版者 PDF 首页明确 CC BY 4.0，已核验并纳入 GitHub。当前 **本机 PDF 3 份、GitHub PDF 1 份、仅本机 2 份**。

## DOI / 合法全文台账（2026-09-25）

现有 23 条来源全部纳入 [DOI 总账](sources/doi_registry.csv)：18 条 DOI 经 Crossref 精确核验，5 条按当前官方目录及 Crossref/DataCite 题名检索暂列 `no_doi_confirmed`（ISO 原标准、1979 两卷 DOT 报告、Chalmers 学位论文、1968 Milner 期刊条目），`missing_to_search` 为 0。原始题名页或新登记可改变无 DOI 判断；BS ISO 采用版 DOI 不归给原 ISO 记录。**DOI 覆盖率 18/23 = 78.26%**。

公开全文已验证 3 份：Passmore 作者版、Brandt 学位论文、SAE 2025 出版者版。Durham 2000 与 HAL 2013 有开放仓储页面，但直接文档请求分别返回 403 和 bot challenge，本机未取得 PDF，也未绕过访问控制。其余条目的付费或未找到状态只描述已查入口，不能解释为永久无 OA。Passmore 封面与仓储许可版本不一致、Brandt 仅明确可公开访问，两份仅本机保留；SAE 2025 许可 CC BY 4.0，允许署名再分发。来源、大小、SHA-256 和许可边界以 DOI 总账为准。

### 2026-09-25 追加：出版者 CC BY 全文

[SAE 2025 风洞阵风发生系统论文](https://doi.org/10.4271/15-18-01-0005)的出版者 PDF 首页明确标示 CC BY 4.0，已核对题名、DOI、16 页和 SHA-256，并按署名许可纳入 GitHub。其余本机 PDF 仍不推送；实时数量以 DOI 总账为准。
