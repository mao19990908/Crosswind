# Crosswind TASK v5 — Bib 文献库、人工补档清单与去重规则

> 本文件为 `TASK.md` 的增量规则。Codex 首次执行本文件时，应将以下规则合并进仓库根目录 `TASK.md`，之后以合并后的 `TASK.md` 为长期唯一主任务书。本文件保留为版本记录。

## 1. 建立统一 Bib / BibLaTeX 文献库

知识库不能只保留 `index.csv` 和结构化 Markdown 记录。所有适合进入参考文献管理体系的来源，应尽可能建立统一 BibTeX/BibLaTeX 元数据记录。

新增目录：

```text
sources/bibliography/
├─ references.bib
├─ bib_sources.csv
└─ raw/                  # 可选：保存合法取得的原始导出，不强制
```

### 1.1 `references.bib`

`references.bib` 是整个 Crosswind 项目的规范化参考文献总库。每条资料原则上对应一个稳定 citation key，并与 `sources/index.csv` 的 `id` 一一对应或可明确映射。

尽可能保存：

```text
author
title
year
journal / booktitle / institution
volume
number
pages
publisher
doi
url
abstract
keywords
note
```

其中：

- `doi` 必须与 `sources/doi_registry.csv` 的 verified DOI 一致；
- `url` 优先指向 DOI、出版社、机构仓库或官方来源；
- `abstract` 仅在来源实际提供摘要且允许保存的情况下写入；
- 不允许根据题目或二手描述自行生成“伪摘要”写入 `abstract`；
- 若原始 BibTeX/BibLaTeX 没有 `abstract`，但出版社、SAE、Crossref/OpenAlex/Semantic Scholar 或机构仓库明确提供摘要，可补入规范化 Bib 记录，同时必须记录摘要来源；
- 若摘要版权或再利用状态不清晰，可不整段保存原文，只记录 `abstract_status=available_not_copied`，并在 record 中保存结构化摘要笔记。

### 1.2 `bib_sources.csv`

新增：

```text
sources/bibliography/bib_sources.csv
```

字段至少包括：

```text
id
citation_key
bib_source
bib_source_url
bib_checked_date
abstract_status
abstract_source
abstract_source_url
abstract_checked_date
metadata_quality
notes
```

`abstract_status` 推荐使用：

```text
full_abstract_saved
available_not_copied
abstract_not_available
abstract_not_checked
full_text_supersedes_abstract
```

这样必须能区分：

1. 仅有 metadata；
2. 已核验 abstract；
3. 已保存 abstract；
4. 已有 full text，不再依赖 abstract；
5. 摘要来源和全文来源是否相同。

### 1.3 record 与 Bib 的职责分离

- `references.bib`：机器可读的规范文献元数据与可保存摘要；
- `sources/index.csv`：检索、筛选和统计总表；
- `sources/records/*.md`：研究问题、方法、参数、结果、验证、局限、证据级别和对课题的价值；
- `sources/doi_registry.csv`：DOI/PDF 状态总账。

不得把 Bib 当作全文分析的替代品。

## 2. 找不到全文的资料必须进入“人工补档清单”

自动检索完成后，凡属于本课题的重要资料，但在合法公开来源、OA 仓库、官方机构或允许访问的渠道中仍未取得全文，不能静默结束，也不能只写 `paywalled` / `not_found` 后不管。

新增：

```text
sources/manual_retrieval_queue.csv
sources/manual_retrieval_queue.md
```

### 2.1 CSV 字段

至少包含：

```text
id
title
authors
year
source_type
doi
official_url
pdf_status
reason_missing
sources_attempted
priority
requested_date
last_checked
manual_status
user_supplied_path
notes
```

`manual_status` 使用：

```text
needs_user_search
user_searching
user_supplied
resolved_elsewhere
not_needed
```

### 2.2 进入人工清单的条件

至少满足以下任一条件：

- `pdf_status = paywalled` 且没有合法 OA 版本；
- `pdf_status = not_found` 且已经完成规定的 OA/机构仓库检索；
- 早期 SAE / 政府报告 / 学位论文 / 标准等对方法谱系重要，但自动检索仍没有全文；
- 摘要不足以确认关键 CFD、实验或车辆动力学参数；
- 研究结论被频繁引用，但只有二手来源，必须补原文。

### 2.3 人工清单必须给用户可操作信息

`manual_retrieval_queue.md` 必须生成人可读表格，至少给出：

- 题名；
- 作者；
- 年份；
- DOI；
- 官方入口；
- 为什么需要全文；
- 已经尝试过哪些来源；
- 优先级。

每次日任务结束时，如果还有 `needs_user_search`，最终汇报中必须单独列出：

> **需要用户手动查找的资料**

并给出新增项与当前未解决总数。不得让用户自己去数据库里猜哪些文件缺失。

用户手动找到 PDF 后，Codex 应在下一次运行中：

1. 校验 PDF 与目标资料是否一致；
2. 计算 SHA-256；
3. 更新 `pdf_status`；
4. 更新 `manual_status=user_supplied`；
5. 解析全文并把 `verification_status` 从 abstract/metadata 升级为 `full_text_verified`；
6. 更新相关 learning / synthesis 内容中依赖该资料的结论。

## 3. 去重：删除真正重复资料，但保留不同版本和方法演化关系

每次批量新增资料后执行去重；本次首次执行应对整个现有仓库进行一次全量去重。

新增：

```text
sources/dedup_report.csv
sources/aliases.csv
```

### 3.1 重复判断顺序

优先级：

1. 相同 verified DOI；
2. 相同标准号 / SAE paper number / government report number；
3. 规范化题名完全一致 + 年份一致；
4. 规范化题名高度一致 + 作者、年份、venue 一致；
5. 同一资料被不同数据库导入形成的别名记录。

### 3.2 不得误删以下情况

以下属于“相关版本”，不是简单重复，原则上保留两条并建立关系：

- conference paper → journal extension；
- doctoral thesis → journal article；
- preprint → final published version；
- ISO 原版 → BS/GB/T 等国家采用版本；
- report Volume I → Volume II；
- standard draft → final standard；
- 同一项目中方法明显不同的系列论文；
- 原始实验论文 → 后续 CFD/ROM 复用论文。

使用：

```text
version_of
derived_from
extended_by
national_adoption_of
companion_report
```

等关系显式连接。

### 3.3 真重复资料的处理

确认 `exact_duplicate` 后：

1. 选择 metadata 最完整、验证级别最高的记录作为 canonical record；
2. 合并 DOI、URL、abstract source、PDF 状态、tags、notes 和验证信息；
3. 将被删除记录的旧 ID 写入 `sources/aliases.csv`：

```text
old_id,canonical_id,reason,merged_date
```

4. 更新所有活跃文件对旧 ID 的引用，包括：
   - `sources/index.csv`
   - `sources/doi_registry.csv`
   - `sources/bibliography/references.bib`
   - `citations/citation_edges.csv`
   - `synthesis/*matrix.csv`
   - `history/timeline.md`（如引用 ID）
   - `learning/` 和 `synthesis/` 中的机器引用（必要时）
5. 合并后删除真正冗余的 `sources/records/<old_id>.md`；
6. 不重写历史 `logs/`，日志作为历史审计保留；
7. 运行仓库校验脚本，确认没有 dangling ID。

### 3.4 `dedup_report.csv`

至少包含：

```text
candidate_id
canonical_id
match_reason
doi_match
title_match
author_year_match
action
review_status
notes
```

`action`：

```text
merged_and_deleted
kept_as_version
kept_distinct
needs_manual_review
```

不确定时禁止自动删除，必须标为 `needs_manual_review`。

## 4. 每日执行新增步骤

在现有 TASK 流程中增加：

1. 新资料入库后立即查重；
2. 建立/更新规范化 Bib 记录；
3. 尽可能补 DOI；
4. 获取并核验 abstract；
5. 查找合法全文 PDF；
6. 找不到的重要全文进入 `manual_retrieval_queue`；
7. 找到全文则升级 record 的验证级别；
8. 更新 DOI/PDF/Bib/人工补档统计；
9. 运行 dedup 与 repository validation；
10. 日终把“需要用户手动查找的资料”单独汇报。

## 5. 每日日报新增统计

```text
Bibliography
- total_bib_entries
- entries_with_abstract
- entries_abstract_available_not_copied
- metadata_only_entries

Manual retrieval
- needs_user_search_total
- new_needs_user_search_today
- user_supplied_resolved_today

Dedup
- duplicate_candidates
- merged_and_deleted
- kept_as_version
- needs_manual_review
```

## 6. 一次性迁移任务

首次执行本 v5 时必须完成：

1. 从现有 `sources/index.csv`、`sources/records/*.md`、`sources/doi_registry.csv` 构建 `sources/bibliography/references.bib`；
2. 对现有 abstract-verified 记录补 `abstract_status` 和 `abstract_source`；
3. 对现有全部资料执行一次全量去重；
4. 将所有真正重复记录合并并删除冗余记录，同时建立 `aliases.csv`；
5. 对现有 `paywalled` / `not_found` 重要资料建立 `manual_retrieval_queue.csv/.md`；
6. 对已有本地 PDF 的记录重新核验并升级全文状态；
7. 将本文件规则合并进根目录 `TASK.md`；
8. 更新 README，说明 Bib 库、人工补档队列和去重机制；
9. commit + push；
10. 最终报告必须给用户一份明确的“请手动帮我找这些资料”清单。

## 7. 核心原则

- 资料必须能从 `id` 追到 Bib、record、DOI、PDF 和证据级别；
- “只有摘要”必须显式标记摘要来源；
- 有摘要不等于有全文；
- 找不到全文不能静默丢失，要进入人工补档队列；
- 去重的目标是消除真正重复，而不是抹掉学术版本演化；
- 不确定是否重复时宁可保留并人工复核，也不要误删；
- 所有删除都必须通过 Git 历史和 `aliases.csv` 可追溯。
