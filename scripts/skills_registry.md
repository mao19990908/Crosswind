# 第三方学术 Skill 评估（2026-09-25）

本轮没有安装或运行第三方 Skill，未向其提供凭据。实际 DOI 核验使用 Crossref REST；OA 入口筛查使用 OpenAlex；本地 PDF 校验使用 Codex 自带 `pdf` skill 和本机 pypdf。GitHub 访问只读。

| Skill | 来源与检查时 main SHA | 用途 / 已读范围 | 访问域名与脚本审查结论 | 状态 |
|---|---|---|---|---|
| academic-search v1.4.0 | https://github.com/ustc-ai4science/academic-search ; `b9b692ed1334c858eb42d1f2710ccfcae1a43eb8` | 已读公开 SKILL.md；元数据核验、OA PDF 工作流与批量记录 | SKILL.md 提及 Crossref、OpenAlex、Unpaywall、Semantic Scholar、PMC、机构仓储及本机独立 Chrome profile；脚本 `oa-pdf-download.mjs` 尚未逐行审计，故未安装/运行。说明文档明确禁止 Sci-Hub、LibGen 和挑战绕过。 | evaluated_only |
| pdf-paper-ingestion v1.5.0 | https://github.com/hideshi/scholarly-agent-skills ; `3ef50b4c6a12240a768e7a70ef5b57f2906f10a1` | 已读公开 SKILL.md；PDF 下载后转 Markdown/抽取图 | SKILL.md 提及 OpenAlex、Semantic Scholar、出版者和作者来源；`download_literature_pdf.py` 尚未逐行审计，故未安装/运行。其建议将下载 PDF 版本控制，与本库许可不明确则只存本机的规则冲突；后者优先。挑战页需停下交由用户处理。 | evaluated_only |

如将来安装，必须先审查对应 SHA 的全部可执行脚本、依赖与网络目标，禁用任何绕过访问控制方案；不得输入 GitHub token、企业账号或 cookie。本轮用官方 API 的轻量只读核验即可完成 DOI 总账初版，不需要运行第三方代码。

## 2026-09-26 本轮工具审计

最新 TASK 提及 jxtse/scientific-research-skills 的 literature-search/paper-fulltext-harvest；本轮没有安装、下载或运行其代码，未完成可执行代码和域名审计，不标为已启用。使用内置 web、Python 标准库官方 API 和已有校验器完成有界访问审计。内置 PDF skill 已读；无新 PDF 取得，无全文重读。Unpaywall 因未配置联系邮箱跳过，不伪造邮箱。SAE/ASME/HathiTrust/HAL/OATAO/Google Books 的失败均记录，未绕过访问限制。
