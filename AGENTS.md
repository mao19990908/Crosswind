# Crosswind 工作边界

- `TASK.md` 是 Collect / Source Layer：使用 `literature-search` 与 `paper-fulltext-harvest` 发现、核验并登记来源及合法全文，将新资料交给 learning backlog；不做深读、atomic claims 或知识图谱更新。
- `Crosswind_Learning_Knowledge_Graph_Task.md` 是 Learn / Knowledge Layer：使用 `paper-reading` 与项目 Skill `crosswind-knowledge-base` 阅读、记录证据并更新已有知识体系；缺资料时写 `learning/needs_collection.csv`，不重复大规模检索。
- 从 `learning/state.json`、现有 paper notes、nodes 和 edges 继续；不要因为新版任务书而重建已完成的图谱。
- 对本项目，上游 `paper-fulltext-harvest` 的 TDM、付费、登录浏览器、cookie、SSO、Cloudflare 重试及外部 `auto-paper-harvester` 路径均禁用。只用公开 OA 出版社、Unpaywall、OpenAlex、Crossref、机构仓储、作者合法公开版本和用户合法提供的全文。不得绕过 paywall、登录、验证码、Cloudflare 或其他访问控制，不得使用 Sci-Hub 等非授权来源。
- 不运行上游 `paper-fulltext-harvest` 的批量 CLI：其默认路由不是 OA-only。只在审查具体 URL 与许可后使用公开 API/页面；遇访问控制即停止并记录。不得把 GitHub token、企业账号、浏览器 cookie 或密码写入项目或交给第三方脚本。
- 本仓库中的 `.agents/skills/crosswind-knowledge-base/SKILL.md` 规定论文如何进入知识体系。当前阶段不自动转入 research gap、proposal、SCI 写作、润色或审稿回复。
