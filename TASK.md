# 车辆瞬态侧风知识库：资料收集与证据入库任务书

> 适用仓库：`mao19990908/Crosswind`  
> 本地目录：`D:\GEELY\Crosswind`  
> 本文件只负责 **发现资料、核验资料、获取合法全文、建立可追溯 source 层**。  
> `Crosswind_Learning_Knowledge_Graph_Task.md` 负责 **阅读、分析、概念化、知识图谱与学习体系**。  
> 当前阶段目标是先搭建自己的知识体系，因此必须严格避免“收集任务”和“分析任务”重复工作。

---

# 1. 当前阶段目标

围绕道路车辆**瞬态侧风／阵风（transient crosswind / crosswind gust）**建立高质量 source layer，为后续学习层提供可靠原始材料。

研究主链：

```text
Gust / Crosswind input
        ↓
Relative wind
        ↓
Transient aerodynamic response
        ↓
Vehicle dynamics
        ↓
Driver / controller / trajectory
```

当前阶段的成功标准不是“论文数量多”，而是：

1. 来源可追溯；
2. DOI / 报告号 / 标准号尽可能核验；
3. 合法全文状态清楚；
4. 历史与引用链不断裂；
5. 资料类型覆盖理论、实验、CFD、车辆动力学、标准等主线；
6. 能稳定把新资料交给 learning 层处理。

不以气动噪声为研究主题。

---

# 2. 与分析任务的职责边界

## 本文件负责

```text
发现
→ 筛选
→ 元数据核验
→ DOI/编号核验
→ 合法全文定位与下载
→ 去重/版本关系
→ source record
→ citation relation
→ 交给 learning backlog
```

## 本文件不负责

```text
深度精读
知识节点生成
公式体系重构
概念关系判断
跨论文综合结论
知识图谱主图更新
research gap
proposal
论文写作
润色
审稿回复
科研绘图
```

上述工作统一交给 `Crosswind_Learning_Knowledge_Graph_Task.md`。

收集阶段允许做**最低限度 triage**，只回答：

```text
这是什么资料？
是否与车辆瞬态侧风有关？
大致属于哪一类？
是否值得进入 learning backlog？
```

不得把 triage 写成研究结论。

---

# 3. 当前只启用的外部科研 Skills

当前阶段只需要最小工具集，不安装整套科研写作生态。

## 3.1 `literature-search`

来源：`jxtse/scientific-research-skills`

用途：

- 多源学术检索；
- backward / forward citation discovery；
- 历史资料与最新资料发现；
- DOI、题名、作者、年份交叉定位。

只负责“找”，不负责替代本仓库的分类与证据规则。

## 3.2 `paper-fulltext-harvest`

来源：`jxtse/scientific-research-skills`

用途：

- DOI / metadata → 合法全文；
- OA publisher；
- Unpaywall；
- OpenAlex；
- Crossref；
- institutional repository；
- 作者公开 manuscript；
- 用户本人合法提供的文件。

### 强制限制

不得：

- 绕过 paywall；
- 绕过登录；
- 绕过验证码、Cloudflare 或访问控制；
- 使用 Sci-Hub 等非授权镜像；
- 把无再分发授权的付费 PDF 推送到 GitHub；
- 把企业账号、浏览器 cookie、token、密码交给第三方脚本。

Skill 若提供 browser fallback，只能用于正常公开访问；遇到 access control 必须停止并记录状态。

## 3.3 本任务禁止主动调用

当前收集阶段不主动调用：

```text
paper-reading
related-work-survey
nature-reader
nature-polishing
nature-response
nature-figure
proposal writer
academic research suite
```

其中 `paper-reading` 由分析任务调用。

---

# 4. 研究边界

必须严格区分：

- transient crosswind / gust；
- steady crosswind / fixed yaw；
- vehicle entering finite wind zone；
- step / ramp / pulse / sinusoidal / stochastic gust；
- natural road gust；
- tunnel exit / bridge / overtaking disturbance；
- aerodynamic yaw angle；
- vehicle heading angle；
- vehicle sideslip angle；
- open-loop；
- closed-loop driver；
- closed-loop controller。

固定偏航角资料可以纳入，但必须标记为：

```text
steady_baseline
quasi_steady_reference
mechanism_comparison
```

不能直接当作 transient-gust 证据。

---

# 5. 检索策略：沿历史和方法谱系推进

禁止随机堆论文。

每轮收集同时考虑：

1. **历史回溯**：从已确认资料向更早来源追；
2. **references**：追原始方法、原始实验、原始定义；
3. **cited-by**：追方法如何演化到当前；
4. **method lineage**：追方法继承、改进、分叉；
5. **facility lineage**：追实验设施与数据继承；
6. **current update**：补当前年份的新论文、标准、报告、数据；
7. **missing evidence**：优先响应 learning 层提出的缺失证据请求。

当前重要历史入口包括但不限于：

- SAE 530255；
- SAE 710287；
- SAE 730232；
- DOT-HS-805-078/079；
- SAE 800848；
- SAE 960674；
- SAE 970135 / 970404；
- SAE 980392；
- ISO 12021-1:1996；
- ISO 12021:2010；
- 后续 transient CFD、DES/DDES/LES、aerodynamic admittance、ROM、CFD–vehicle dynamics coupling、road validation。

不得未经充分检索写“第一篇”“首次”“没人做过”。

---

# 6. Source type

每条来源必须有 `source_type`：

```text
journal_article
sae_technical_paper
conference_paper
review_article
standard
standard_draft
government_report
institutional_report
project_report
doctoral_thesis
master_thesis
book
book_chapter
dataset
code_repository
facility_documentation
manufacturer_technical_document
patent
regulatory_document
web_primary_source
secondary_web_source
```

原始资料优先。

二手网页、综述主要用于发现原始资料，不能替代原始证据。

---

# 7. 分类只做 source-level tagging

主类别：

```text
A 历史与定义
B 阵风输入与环境
C 非定常气动理论
D 气动系统响应模型
E 车辆动力学理论
F 风洞／移动模型实验
G 整车／道路实验
H 气动 CFD
I 气动—车辆动力学耦合
J 验证与评价
K 标准与规范
L 数据与开放资源
M 工程应用
```

收集阶段只做“资料属于哪里”的粗粒度分类。

更细的 Concept / Method / Variable / Equation / Evidence 归类由 learning 层负责。

---

# 8. DOI 与唯一标识

所有适用来源检查 DOI。

字段：

```text
doi
doi_status
doi_verified_date
doi_source
```

`doi_status`：

```text
verified
no_doi_confirmed
missing_to_search
invalid_or_conflict
not_applicable
```

DOI 必须通过 Crossref、出版社、SAE 或其他可靠原始入口核验，不得猜测。

没有 DOI 不代表资料无效。标准、政府报告、早期资料、部分学位论文可能本来就无 DOI，应使用标准号、报告号或其他稳定 ID。

维护：

```text
sources/doi_registry.csv
```

---

# 9. 合法全文获取

推荐顺序：

```text
verified DOI / exact metadata
        ↓
publisher / official source
        ↓
Unpaywall
        ↓
OpenAlex
        ↓
Crossref resource link
        ↓
institutional / government / author repository
        ↓
manual retrieval queue
```

无 DOI 时使用：

```text
title + authors + year + venue/report number
```

每条来源记录：

```text
pdf_status
pdf_source
pdf_path
pdf_sha256
pdf_bytes
pdf_license
pdf_checked_date
github_pdf
```

`pdf_status`：

```text
oa_downloaded
user_provided
institutional_access
open_repository_available
paywalled
not_found
not_pdf
download_failed
license_unclear
```

下载后检查：

- PDF 文件头 / MIME；
- 是否可打开；
- 题名、作者、DOI 是否对应；
- 页数与文件大小是否合理；
- SHA-256。

不能把 HTML 错误页当 PDF。

### GitHub 与本地规则

可以提交 GitHub：

- 明确 OA；
- public domain；
- 明确允许再分发。

只能本地保存：

- 机构订阅 PDF；
- 付费 publisher PDF；
- 许可不明确的全文；
- 用户有权阅读但无权公开再分发的材料。

---

# 10. 去重与版本关系

按以下信息检查重复：

```text
verified DOI
SAE paper number
standard number
report number
normalized title + year
near-duplicate title + author + venue
```

真正重复：保留 canonical record，旧 ID 写入 `sources/aliases.csv`。

以下情况通常不是重复，应保留为独立 source 并建立关系：

```text
conference → journal
thesis → paper
preprint → final
standard draft → final
ISO → national adoption
report volume I ↔ volume II
same project, different method paper
```

关系可使用：

```text
version_of
derived_from
extended_by
national_adoption_of
companion_report
```

不确定时标记 `needs_manual_review`。

---

# 11. Source record 最低要求

路径：

```text
sources/records/<stable_id>.md
```

收集阶段只要求能够支撑后续阅读的事实字段：

```text
标准引文
source_type
稳定 ID
DOI / 报告号 / 标准号
官方 URL
作者
年份
venue / institution
abstract status
access level
PDF status
verification status
primary category
secondary categories
steady/transient 标签
大致 method 标签
为什么纳入
后续是否需要 full-text / deep read
```

只有已核验全文时，才允许填具体页码、公式、实验参数和详细结论。

收集阶段不得为了“记录完整”而根据摘要猜方法细节。

---

# 12. 书目库

维护：

```text
sources/bibliography/references.bib
sources/bibliography/bib_sources.csv
```

Bib 用于书目元数据，不替代 research analysis。

`bib_key` 与 `sources/index.csv` 中 source ID 稳定对应。

摘要状态与全文验证状态必须分开。

---

# 13. 引文关系

维护：

```text
citations/citation_edges.csv
citations/citation_graph.md
citations/method_lineages.md
```

`citation_edges.csv` 至少：

```text
source_id,target_id,relation,verified,note
```

relation 可包括：

```text
references
cited_by
method_inherits
method_extends
facility_inherits
data_reuses
standardizes
version_of
derived_from
```

注意：`supports` / `contradicts` 这类需要理解具体论证内容的关系，原则上由 learning 层确认后再写入。

---

# 14. 检索台账

维护：

```text
search/search_ledger.csv
search/query_library.md
search/database_coverage.md
```

`search_ledger.csv` 至少：

```text
date,database,query,year_from,year_to,result_count,screened,included,excluded,notes
```

不得把“没有搜到”写成“没有研究”。

---

# 15. Collection → Learning 交接

任何新进入 sources 的资料都必须进入 learning backlog。

建议维护：

```text
learning/backlog.csv
```

至少包含：

```text
source_id
added_date
priority
reason
access_level
verification_status
suggested_pass
learning_status
```

`suggested_pass`：

```text
P1
P2
P3_candidate
```

仅用于优先级建议，不代表已经完成阅读。

`learning_status`：

```text
pending
in_progress
done
needs_more_evidence
```

收集任务不得把 `pending` 直接改成 `done`。

---

# 16. Learning → Collection 反向请求

分析任务若发现缺少关键证据，写入：

```text
learning/needs_collection.csv
```

至少包含：

```text
request_id
question
needed_source_type
keywords
known_source_ids
priority
status
notes
```

下一次 collection day 优先处理这些请求。

这样形成闭环：

```text
COLLECT
   ↓
sources
   ↓
LEARN
   ↓
knowledge gaps
   ↓
needs_collection
   ↓
COLLECT
```

---

# 17. 人工补档

重要来源合法渠道仍缺全文时，加入：

```text
sources/manual_retrieval_queue.csv
sources/manual_retrieval_queue.md
```

状态：

```text
needs_user_search
user_searching
user_supplied
resolved_elsewhere
not_needed
```

用户提供合法 PDF 后，下一轮重新核验题名、DOI、文件格式、SHA-256，再进入 learning backlog。

---

# 18. 当前阶段执行节奏

用户要求：**收集与分析分阶段运行，不让两个任务在同一天反复重复同一工作。**

默认逻辑：

```text
Collection Day
    ↓
新增 / 补齐 sources
    ↓
形成 learning backlog
    ↓
下一执行日进入 Learning Day
```

如果 Learning Day 在当日额度内没有处理完 backlog：

```text
第二天继续 Learning
第三天仍未清零则继续 Learning
...
直到 backlog 清到当前可接受状态
```

如果 Learning Day 提前完成、当天仍有额度：

```text
使用剩余额度继续 Collection
```

但新收集资料只进入 backlog，不要在同一循环里无限“搜一篇 → 分析一篇 → 再搜一篇”。

### 优先级

只要存在较大的 learning backlog，**知识消化优先于继续扩大资料规模**。

当前阶段目标是建立知识体系，不是最大化论文数量。

---

# 19. 每日 06:00 与额度

计划运行时间：

```text
06:00 Asia/Shanghai
```

机器未开机时允许错过后补跑，同一自然日原则上一次主运行。

每日最多使用可用周额度总量的约 12%，不要求强行耗满。

若无法准确读取额度：

```text
quota_status=unavailable
```

不得伪称已精确控制额度。

---

# 20. Collection Day 流程

```text
01 检查 Git 状态并同步
02 读取上一轮日志 / state
03 读取 learning/needs_collection.csv
04 检查历史链与 citation 缺口
05 literature-search：历史 / references / cited-by / current update
06 筛选并建立 canonical metadata
07 核验 DOI / 报告号 / 标准号
08 paper-fulltext-harvest：只找合法可访问全文
09 验证 PDF
10 更新 index / doi_registry / bibliography
11 去重与版本关系
12 更新 citation edges / search ledger / timeline
13 新资料写入 learning/backlog.csv
14 更新 manual retrieval queue
15 质量检查
16 日志
17 git commit / push
18 核对 local HEAD 与 remote SHA
```

### Collection Day 不执行

```text
paper-reading deep analysis
atomic claim synthesis
knowledge graph restructuring
research gap
proposal / paper writing
```

---

# 21. Collection 日报

`logs/YYYY-MM-DD.md` 中记录：

```text
检索数据库
检索式
候选数
筛选数
纳入数
排除数
新增 source IDs
新增 / 修正 DOI
新增 PDF
manual retrieval 新增
citation edge 新增
learning backlog 新增
quota status
Git SHA
下一轮断点
```

覆盖统计至少保留：

```text
total_sources
verified_doi
no_doi_confirmed
missing_doi
pdf_available
pdf_local_only
pdf_not_found
manual_retrieval_total
learning_backlog_pending
```

---

# 22. 质量原则

1. 原始来源优先；
2. metadata、abstract、full text 三个层级严格区分；
3. 未读全文不推断具体实验/CFD 参数；
4. DOI 不猜；
5. 不绕过访问控制；
6. 不公开上传无再分发权的 PDF；
7. 稳态偏航与瞬态阵风严格区分；
8. 一条 source 只保留一个 canonical record；
9. 版本关系不误删；
10. 收集阶段不抢分析阶段的工作；
11. learning 提出的关键证据缺口优先于盲目扩库；
12. 当前阶段“能形成知识”比“资料更多”更重要。

---

# 23. 当前阶段暂缓事项

以下功能以后进入科研输出阶段再启用：

```text
related-work-survey
academic-research-suite
nature-polishing
nature-response
nature-figure
proposal writer
自动 SCI 写作
自动 research-gap 报告生成
```

除非用户明确切换阶段，否则不要自动安装或调用。

---

# 24. 长期闭环

```text
literature-search
      ↓
source discovery
      ↓
metadata / DOI verification
      ↓
paper-fulltext-harvest
      ↓
canonical source layer
      ↓
learning/backlog.csv
      ↓
Crosswind_Learning_Knowledge_Graph_Task.md
      ↓
knowledge graph / learning chapters
      ↓
learning/needs_collection.csv
      ↓
下一轮 targeted collection
```

当前阶段始终坚持：

> **收集服务于理解，而不是为了囤积。**
