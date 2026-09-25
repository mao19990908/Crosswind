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

合法取得、供本机研究的 PDF 放在 `D:\GEELY\Crosswind\local_fulltext\`。该目录被 `.gitignore` 排除，不会随 GitHub 仓库同步；其他电脑克隆仓库时需按来源记录的仓储链接自行获取。

2026-09-25 已在本机保存 `pimeche-2001-passmore.pdf`（Loughborough 作者存档）和 `brandt-2023-thesis.pdf`（Chalmers 博士论文）。前者已完成全文核读；后者仅完成下载与文件格式检查，不能据此把记录升级为全文核验。受限 SAE 论文和 ISO 标准仍只有元数据／摘要记录。
