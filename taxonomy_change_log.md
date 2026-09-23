# 分类变更日志

2026-09-23：按 v2 初始化 A–M 研究主题类别。

2026-09-23（v3）：新增与主题类别正交的规范 `source_type` 资料类型维度，采用 v3 任务书第 12.1 节的 21 个枚举。原因：来源包含标准、SAE 技术论文、政府报告、学位论文、数据集及设施资料，不能以“论文”统称。旧字段 `source_type` 原先混用 `technical_paper`、`journal_article`、`government_report`、`standard`、`doctoral_thesis`；现映射为 v3 规范类型，并在索引中新增 `publisher_or_institution`、`report_or_standard_number`。研究类别 A–M 保持不变。
