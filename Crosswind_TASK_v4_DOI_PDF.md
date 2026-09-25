# Crosswind TASK v4 — DOI / PDF 版

本文件用于标记车辆瞬态侧风知识库任务书的 **v4（DOI / PDF）版本**。

完整执行规则已同步到仓库根目录：

- `TASK.md`
- 对应更新提交：`0ead48bc8e4f1a4b64307fe4aa34e3a338c908d9`

## 本版新增核心要求

1. 对现有及新增资料统一统计 DOI，并维护 `sources/doi_registry.csv`。
2. DOI 状态区分 `verified`、`no_doi_confirmed`、`missing_to_search`、`invalid_or_conflict`、`not_applicable`。
3. 对已验证 DOI 自动检索合法开放全文，优先顺序为 publisher/official → Unpaywall → OpenAlex → Semantic Scholar → institutional/author repository → Crossref resource links。
4. 新建本机 `sources/pdfs/` 保存合法获得的全文。
5. 每个 PDF 记录 `pdf_status`、来源、路径、SHA-256、许可和检查日期。
6. GitHub 可以存 PDF，但仅上传明确允许再分发的 OA/public-domain 全文；机构订阅或许可不明的 PDF 只保存在本机。
7. 可评估 `ustc-ai4science/academic-search` 与 `hideshi/scholarly-agent-skills` 的 `pdf-paper-ingestion`，安装前必须检查 `SKILL.md` 和脚本，禁止任何绕过 paywall/captcha 的 fallback。
8. 每日日报增加 DOI 覆盖率、OA PDF 数量、paywalled/not-found/download-failed 等统计。
9. “资料”继续覆盖期刊、SAE Technical Paper、标准、政府/机构报告、学位论文、数据集与设施资料，不能退化为论文收藏夹。

> 后续 Codex 执行以当前 `TASK.md` 为唯一完整规范；本文件仅作为 v4 版本标记和变更摘要。