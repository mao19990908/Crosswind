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

当前索引共 22 条；分类型覆盖与尚未检索的类别判断见 [database_coverage.md](search/database_coverage.md)。

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

合法取得、供本机研究的 PDF 统一登记在 `D:\GEELY\Crosswind\sources\pdfs\`。原有 `local_fulltext\` 副本保留；两目录均被 `.gitignore` 排除，不会随 GitHub 仓库同步。其他电脑克隆仓库时需按来源记录的仓储链接自行获取。

2026-09-25 已在本机保存 `pimeche-2001-passmore.pdf`（Loughborough 作者存档）和 `brandt-2023-thesis.pdf`（Chalmers 博士论文）。前者已完成全文核读；后者仅完成下载与文件格式检查，不能据此把记录升级为全文核验。受限 SAE 论文和 ISO 标准仍只有元数据／摘要记录。

## DOI / 合法全文台账（2026-09-25）

现有 22 条来源已逐条纳入 [DOI 总账](sources/doi_registry.csv)。Crossref DOI 精确查询核验 17 条；ISO 官方目录未列 DOI，暂列 `no_doi_confirmed`（仅对当前官方目录而言）；TRID 的 1968 期刊条目、1979 两卷政府报告及 Chalmers 学位论文仍列 `missing_to_search`，不猜测 DOI。DOI 覆盖率按 verified / total = **17/22 = 77.27%**；状态或 DOI 与题名/年份冲突应在总账保留，不因字段为空推断无资料。

合法全文筛查已对 17 条 verified DOI 做 Crossref/OpenAlex 精确查询，并查核出版者/官方入口。现有已确认可打开的公开全文 PDF 2 条：Passmore 作者存档、Brandt 官方学位仓储。另有 Durham 作者存档和 SAE 2025 开放出版入口 2 条 OA landing page 线索，尚未核实直接 PDF。其中前两份已复制到本机 `sources/pdfs/`，核验 PDF 文件头、可打开页数、题名、来源和 SHA-256；另外两条仅有 OA landing page，不能计为已下载。其余仍按当前入口记录付费或未找到状态；未穷尽所有大学/作者仓储、Unpaywall（需联系方式）与 Semantic Scholar，不把当前状态当永久定论。

`D:\GEELY\Crosswind\sources\pdfs\` 与旧 `local_fulltext\` 均被 `.gitignore` 排除。两份本地 PDF 的再分发许可未充分确认（Passmore 仓储 API 与封面 CC 版本不一致；Brandt 仅明确公开访问），因此本轮 **GitHub PDF 数为 0**。来源记录与总账可帮助其他电脑合法重新获取，下载文件本体不随 Git 同步。具体 SHA、字节和许可边界以总账为准。
