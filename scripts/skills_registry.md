# Crosswind Skill Registry

安装日期：2026-09-26（Asia/Shanghai）。本节为当前状态；后面的旧评估只记录历史检查。

| name | source repository | source commit SHA | install scope | install path | install date | enabled status | purpose |
|---|---|---|---|---|---|---|---|
| `literature-search` | https://github.com/jxtse/scientific-research-skills | `68098d5565f423ffcfce1c9936de77ae230843aa` | user | `C:\Users\17984\.agents\skills\literature-search` | 2026-09-26 | enabled for Collect; upstream example scripts unavailable | 在 `TASK.md` 下发现、定位、去重候选来源；使用可用的公开检索工具与官方 API，不做 learning 结论。 |
| `paper-fulltext-harvest` | https://github.com/jxtse/scientific-research-skills | `68098d5565f423ffcfce1c9936de77ae230843aa` + local `SKILL.md` YAML/safety patch | user | `C:\Users\17984\.agents\skills\paper-fulltext-harvest` | 2026-09-26 | enabled for OA guidance only; upstream batch CLI, TDM and browser fallback disabled in this project | 在 `TASK.md` 下核对公开 OA 或用户合法提供的全文入口、许可和 PDF 身份；不绕过访问控制。 |
| `paper-reading` | https://github.com/jxtse/scientific-research-skills | `68098d5565f423ffcfce1c9936de77ae230843aa` | user | `C:\Users\17984\.agents\skills\paper-reading` | 2026-09-26 | enabled for Learn | 在学习任务书下按 P1/P2/P3 阅读现有资料，严格保留实际证据层级。 |
| `crosswind-knowledge-base` | https://github.com/mao19990908/Crosswind | `63379598a06f00d01329122a783222934775ebd3` | project | `D:\GEELY\Crosswind\.agents\skills\crosswind-knowledge-base` | 2026-09-26 | enabled for Learn | 规定 source → atomic claim → evidence → 现有知识节点 → graph edge 的入库与追溯规则。 |

## 依赖与安全配置

- 三个上游 Skill 均从固定 source SHA 复制了完整目录。`literature-search` 和 `paper-reading` 与上游逐文件相同。上游 `paper-fulltext-harvest/SKILL.md` 的单行 `description` 含未转义冒号，YAML 校验失败；安装后仅在该文件修复 frontmatter 并在正文开头加 Crosswind OA 限制，其余 11 个文件逐文件不变。修订后该文件 SHA-256：`FC315E7C96C7C894655D10C9FCC61449405EAF6687F60477692D6668BD68980E`。`paper-reading` 无独立脚本依赖，读取已有 PDF 即可。
- `paper-fulltext-harvest` 的 Python 依赖已装于隔离环境 `C:\Users\17984\.agents\venvs\paper-fulltext-harvest`（Python 3.12；`bs4`、`openpyxl`、`pandas`、`pypdf`、`requests`）。该隔离环境不含凭据，也不代表授权运行上游下载 CLI。项目 `AGENTS.md` 禁用其付费 TDM、登录浏览器、cookie/SSO、Cloudflare 重试和默认批量 CLI；只允许事先核实为合法公开的 OA 入口和用户合法提供的文件。
- 当前未配置 `UNPAYWALL_EMAIL`、商业检索 API key 或出版社 token。Unpaywall 调用需用户自己的有效联系邮箱；未配置时跳过。`literature-search` 只有 `SKILL.md`，其文档示例所指 `scripts/search/*` 不在上游该 Skill 目录内，不能按示例直接运行；使用 Codex 可用的公开检索工具或官方 API 完成 Collect。
- `TASK.md` 对应 `literature-search` + `paper-fulltext-harvest`（Collect / Source Layer）；`Crosswind_Learning_Knowledge_Graph_Task.md` 对应 `paper-reading` + `crosswind-knowledge-base`（Learn / Knowledge Layer）。从 `learning/state.json` 和现有 nodes/edges 继续，避免重建图谱。

## 历史第三方学术 Skill 评估（2026-09-25）

本轮没有安装或运行第三方 Skill，未向其提供凭据。实际 DOI 核验使用 Crossref REST；OA 入口筛查使用 OpenAlex；本地 PDF 校验使用 Codex 自带 `pdf` skill 和本机 pypdf。GitHub 访问只读。

| Skill | 来源与检查时 main SHA | 用途 / 已读范围 | 访问域名与脚本审查结论 | 状态 |
|---|---|---|---|---|
| academic-search v1.4.0 | https://github.com/ustc-ai4science/academic-search ; `b9b692ed1334c858eb42d1f2710ccfcae1a43eb8` | 已读公开 SKILL.md；元数据核验、OA PDF 工作流与批量记录 | SKILL.md 提及 Crossref、OpenAlex、Unpaywall、Semantic Scholar、PMC、机构仓储及本机独立 Chrome profile；脚本 `oa-pdf-download.mjs` 尚未逐行审计，故未安装/运行。说明文档明确禁止 Sci-Hub、LibGen 和挑战绕过。 | evaluated_only |
| pdf-paper-ingestion v1.5.0 | https://github.com/hideshi/scholarly-agent-skills ; `3ef50b4c6a12240a768e7a70ef5b57f2906f10a1` | 已读公开 SKILL.md；PDF 下载后转 Markdown/抽取图 | SKILL.md 提及 OpenAlex、Semantic Scholar、出版者和作者来源；`download_literature_pdf.py` 尚未逐行审计，故未安装/运行。其建议将下载 PDF 版本控制，与本库许可不明确则只存本机的规则冲突；后者优先。挑战页需停下交由用户处理。 | evaluated_only |

如将来安装，必须先审查对应 SHA 的全部可执行脚本、依赖与网络目标，禁用任何绕过访问控制方案；不得输入 GitHub token、企业账号或 cookie。本轮用官方 API 的轻量只读核验即可完成 DOI 总账初版，不需要运行第三方代码。

## 2026-09-26 本轮工具审计

最新 TASK 提及 jxtse/scientific-research-skills 的 literature-search/paper-fulltext-harvest；本轮没有安装、下载或运行其代码，未完成可执行代码和域名审计，不标为已启用。使用内置 web、Python 标准库官方 API 和已有校验器完成有界访问审计。内置 PDF skill 已读；无新 PDF 取得，无全文重读。Unpaywall 因未配置联系邮箱跳过，不伪造邮箱。SAE/ASME/HathiTrust/HAL/OATAO/Google Books 的失败均记录，未绕过访问限制。

## 2026-09-27 Learn skills

Read and used installed C:/Users/17984/.agents/skills/paper-reading/SKILL.md plus repository .agents/skills/crosswind-knowledge-base/SKILL.md. Instruction-only local reading workflow; no third-party executable, network service or credentials used. Built-in PDF skill supports read-only equation/figure inspection. New audit_hucho_1973.py is local standard-library mathematical checking code, not a harvest CLI. No install performed.

## 2026-09-28 Learn usage

Reused reviewed instruction-only paper-reading and project crosswind-knowledge-base; read-only built-in PDF rendering for Beauvais p2220/2222-2225. No skill installation, upstream executable, third-party credentials or network harvesting. Offline first-party audit_beauvais_1967.py only computes labelled source arithmetic.
