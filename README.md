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
- [方法谱系](citations/method_lineages.md)
- [研究现状](synthesis/state_of_the_art.md)
- [研究空白](synthesis/research_gaps.md)
- [当日日志](logs/2026-09-25.md)

当前处于 Phase I：先建立可追溯的历史与方法地图，不把初步线索包装成成熟综述结论。

## 本地全文 PDF

合法取得的 PDF 登记在 `D:\GEELY\Crosswind\sources\pdfs\`。旧 `local_fulltext\` 副本保留。两目录默认被 `.gitignore` 排除；只有明确允许再分发的 PDF 才逐个 `git add -f` 纳入 GitHub。

Passmore 作者存档与 Brandt Chalmers 学位论文仅本机留存；前者已核读全文，后者已核读仓储 PDF 的扩展摘要页段（其 Paper A–E 附录原篇不在该 92 页文件内）。SAE 2025 出版者 PDF 首页明确 CC BY 4.0，已核验并纳入 GitHub。当前 **本机 PDF 3 份、GitHub PDF 1 份、仅本机 2 份**。

## DOI / 合法全文台账（2026-09-25）

现有 23 条来源全部纳入 [DOI 总账](sources/doi_registry.csv)：18 条 DOI 经 Crossref 精确核验，4 条按当前官方目录与 Crossref/DataCite 题名检索暂列 `no_doi_confirmed`（ISO 原标准、1979 两卷 DOT 报告、Chalmers 学位论文），1968 Milner 期刊条目仍为 `missing_to_search`。原始题名页或新登记可改变无 DOI 判断；BS ISO 采用版 DOI 不归给原 ISO 记录。**DOI 覆盖率 18/23 = 78.26%**。

公开全文已验证 3 份：Passmore 作者版、Brandt 学位论文、SAE 2025 出版者版。Durham 2000 与 HAL 2013 有开放仓储页面，但直接文档请求分别返回 403 和 bot challenge，本机未取得 PDF，也未绕过访问控制。其余条目的付费或未找到状态只描述已查入口，不能解释为永久无 OA。Passmore 封面与仓储许可版本不一致、Brandt 仅明确可公开访问，两份仅本机保留；SAE 2025 许可 CC BY 4.0，允许署名再分发。来源、大小、SHA-256 和许可边界以 DOI 总账为准。

### 2026-09-25 追加：出版者 CC BY 全文

[SAE 2025 风洞阵风发生系统论文](https://doi.org/10.4271/15-18-01-0005)的出版者 PDF 首页明确标示 CC BY 4.0，已核对题名、DOI、16 页和 SHA-256，并按署名许可纳入 GitHub。其余本机 PDF 仍不推送；实时数量以 DOI 总账为准。
