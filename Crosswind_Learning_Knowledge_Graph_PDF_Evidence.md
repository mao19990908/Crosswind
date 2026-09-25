# 车辆瞬态侧风知识图谱：PDF 全文证据层与结构化学习规则

> 适用仓库：`mao19990908/Crosswind`  
> 本地目录：`D:\GEELY\Crosswind`  
> 本文件是 `Crosswind_Learning_Knowledge_Graph_Task.md` 的全文证据扩展规则。  
> 目标：建立 **本地 PDF 原始证据层 → 单篇全文结构化 MD → learning / citations / history / synthesis / knowledge graph** 的稳定更新链路。

---

# 1. 总体原则

GitHub 不作为 PDF 的主要存储位置。

所有合法获得的论文、报告、学位论文 PDF 优先保存在本机：

```text
D:\GEELY\Crosswind\sources\pdfs\
```

PDF 是原始证据层；GitHub 主要保存由全文提取后的结构化 Markdown、BibTeX、CSV、知识图谱与综合分析。

整体链路：

```text
PDF（本地原始证据）
        ↓
Codex 通读全文
        ↓
sources/records/<stable_id>.md
        ↓
atomic claims / evidence
        ↓
learning/
        ↓
citations/ + history/
        ↓
synthesis/
        ↓
knowledge graph
```

最终职责：

```text
PDF = 原始证据
record MD = 单篇全文知识
learning = 系统教材
citations/history = 文献、方法与知识演化
synthesis = 研究现状、争议、空白、研究假设
knowledge graph = 概念—方法—证据—工程应用关系网络
```

---

# 2. PDF 与 GitHub MD 的职责分离

## 2.1 PDF

PDF 用于保存和重新核验：

- 原文；
- 页码；
- 图表；
- 公式；
- 实验参数；
- CFD 设置；
- 原作者结论；
- 限制条件；
- 定量数据。

PDF 默认仅保存在本机，不要求上传 GitHub。

## 2.2 Record MD

GitHub 中的：

```text
sources/records/<stable_id>.md
```

是知识图谱直接使用的单篇全文知识记录。

它不是简单摘要，而是全文结构化提取结果。

每个 PDF、Bib、index、record MD 必须通过同一 `stable_id` 对应。

---

# 3. 全文验证等级

统一使用：

```text
metadata_verified
abstract_verified
full_text_verified
```

含义：

## 3.1 metadata_verified

只确认：

- title；
- authors；
- year；
- DOI / report number；
- publication / institution。

不得据此写技术结论。

## 3.2 abstract_verified

允许整理：

- 研究目的；
- 摘要明确公开的方法；
- 摘要明确公开的主要结论。

摘要中未报告的网格、时间步、试验参数、误差等必须写：

```text
not reported in abstract
```

不得推断。

## 3.3 full_text_verified

仅当 Codex 实际打开并通读全文后才允许设置。

全文核验后，可进入：

- CFD 参数矩阵；
- 实验参数矩阵；
- 定量结论；
- 公式库；
- 图表证据；
- 详细方法谱系；
- 高可信知识图谱；
- research gap / research hypothesis 的关键证据。

---

# 4. PDF 全文读取流程

对每一个已获得 PDF 的来源：

1. 打开并实际通读 PDF；
2. 不得只读取摘要、首页或元数据；
3. 核对：
   - title；
   - authors；
   - year；
   - DOI；
   - publication / institution；
   - source_type；
4. 匹配或建立唯一 `stable_id`；
5. 计算 SHA-256；
6. 更新 `sources/index.csv` 与 `sources/doi_registry.csv`；
7. 建立或升级 `sources/records/<stable_id>.md`；
8. 再将新的全文知识传播到 learning、citations、history、synthesis 与知识图谱。

禁止同一篇资料因为 PDF、DOI、题名入口不同而生成多个 record。

---

# 5. 每篇全文 Record MD 的最低结构

每篇全文记录至少整理：

```markdown
# <stable_id> — <title>

## Bibliographic information

## Access / verification

## Research question

## Physical problem

## Gust / crosswind definition

## Coordinate system and normalization

## Vehicle / model geometry

## Experimental setup

## CFD setup

## Vehicle-dynamics model

## Coupling method

## Important equations

## Important parameters

## Main quantitative results

## Flow / aerodynamic mechanisms

## Validation method

## Main conclusions

## Limitations

## Relation to previous work

## Relation to subsequent work

## Relevance to 车辆侧风模拟及实验验证

## Follow-up questions

## Evidence map
```

不适用的栏目写 `not applicable`，全文未报告的写：

```text
not reported in full text
```

不得自行补数值。

---

# 6. Evidence Map：全文证据定位

所有重要技术结论尽量记录证据位置。

至少支持：

```text
PDF filename
page number
section
subsection
equation number
figure number
table number
appendix
```

示例：

```markdown
### Yawing moment overshoot

车辆进入给定横风区后，偏航力矩出现瞬态峰值。

Evidence:
- PDF: `sae-980392__ryan__1998.pdf`
- Page: 6
- Figure: Fig. 7
- Evidence level: full_text
```

实验参数示例：

```markdown
## Experimental setup

- Vehicle/model scale: ...
- Crosswind incidence: ...
- Sampling frequency: ...
- Gust-zone length: ...

Evidence:
- PDF: ...
- Pages: 3–5
- Table: Table 1
```

知识图谱中的重要节点应能够反向追溯：

```text
Knowledge node
    ↓
Atomic claim
    ↓
source record MD
    ↓
page / figure / table / equation
    ↓
local PDF
```

---

# 7. 摘要记录升级为全文记录

当原资料状态为：

```text
abstract_verified
```

且后续获得 PDF 时：

1. 重新读取全文；
2. 重新检查所有原有 abstract-derived notes；
3. 摘要阶段过于宽泛的描述必须收窄；
4. 摘要与全文不一致时，以全文为准；
5. 不能删除原来的访问历史，但要更新当前知识结论；
6. 状态升级为：

```text
full_text_verified
```

7. 写入：

```text
full_text_verified_date
local_pdf_path
pdf_sha256
```

---

# 8. 知识图谱证据优先级

同一知识节点存在多个证据层时：

```text
full-text PDF evidence
        >
full_text_verified record MD
        >
abstract_verified record
        >
metadata_verified
```

注意：

- 知识图谱日常构建优先读取结构化 MD；
- PDF 是最终原始证据，不要求每天重复解析；
- record MD 必须准确反映 PDF，而不能替代 PDF 的原始证据地位。

以下情况必须回到 PDF 重新核验：

- 出现结论冲突；
- 需要精确数值；
- 需要公式；
- 需要实验参数；
- 需要 CFD 参数；
- 需要图表；
- 需要页码引用；
- record 信息不足；
- 构建 research gap；
- 构建 research hypothesis；
- 不同来源看似互相矛盾。

---

# 9. Atomic Claim 与 PDF Evidence 的绑定

每个重要 atomic claim 除现有字段外，增加：

```text
source_id
verification_status
pdf_filename
page
section
equation
figure
table
evidence_excerpt_or_note
evidence_type
```

不要求保存大段版权原文。

`evidence_excerpt_or_note` 优先使用自己的结构化转述；仅在确有必要时保留短引用。

例如：

```text
Claim
某一给定有限阵风条件下，瞬态 yaw moment peak 高于对应 steady baseline。

Condition
specific geometry + gust profile + velocity

Evidence
p. 8, Fig. 6

Verification
full_text_verified
```

知识图谱不得把一个特定工况下的 atomic claim 扩大为普适结论。

---

# 10. 全文学习后必须传播到哪些层

完成一篇全文整理后，不能停止在 `sources/records/`。

必须判断是否需要更新：

```text
learning/
history/timeline.md
citations/citation_edges.csv
citations/citation_graph.md
citations/method_lineages.md
synthesis/state_of_the_art.md
synthesis/research_gaps.md
synthesis/research_hypotheses.md
synthesis/disputed_findings.md
synthesis/gust_parameter_matrix.csv
synthesis/experiment_matrix.csv
synthesis/simulation_matrix.csv
synthesis/validation_matrix.csv
synthesis/coupled_methods_matrix.csv
learning/nodes/
learning/graph/edges.csv
learning/graph/knowledge_graph.md
learning/graph/knowledge_graph.mmd
```

执行时先问：

```text
这篇全文改变了什么知识？
```

如果没有改变已有知识，只增加支持证据：

```text
Concept
    └── evidence +1
```

即可，不需要制造重复节点。

---

# 11. PDF 与知识图谱的增量更新机制

日常不允许每次从头解析全部 PDF。

流程应为：

```text
检测 sources/pdfs/
        ↓
发现新增 / hash 变化的 PDF
        ↓
匹配 stable_id
        ↓
全文解析
        ↓
更新 record MD
        ↓
生成/更新 atomic claims
        ↓
判断知识节点是否变化
        ↓
增量更新 learning / graph / synthesis
```

已处理 PDF 使用 SHA-256 作为变化检测依据之一。

同一 PDF hash 未变化且 record 已 `full_text_verified` 时，不应每天重复全文解析。

---

# 12. 用户手动提供 PDF 后的处理

如果用户把新 PDF 放入：

```text
D:\GEELY\Crosswind\sources\pdfs\
```

下一次执行必须：

1. 自动发现新增文件；
2. 根据 DOI、题名、作者、年份匹配 stable_id；
3. 无法自动确定时标记 `manual_match_required`，不得错配；
4. 计算 SHA-256；
5. 通读全文；
6. 将对应记录从 metadata/abstract 层升级为全文层；
7. 更新知识图谱；
8. 从 `manual_retrieval_queue` 中移除或标记已解决。

---

# 13. 找不到全文时的图谱处理

重要资料没有全文时，不得假装已经深读。

必须：

```text
verification_status = metadata_verified / abstract_verified
```

并根据情况标记：

```text
NEEDS_FULLTEXT
```

关键知识节点若依赖该资料但证据不足：

```text
Evidence gap
    ↓
manual retrieval queue
```

同时维护：

```text
sources/manual_retrieval_queue.csv
sources/manual_retrieval_queue.md
```

每轮结束向用户汇报需要人工寻找的资料。

---

# 14. BibTeX / BibLaTeX 与全文知识的关系

统一维护：

```text
sources/bibliography/references.bib
sources/bibliography/bib_sources.csv
```

Bib 层负责规范文献元数据，尽可能保存：

```text
author
title
year
journal / booktitle / institution
volume
issue
pages
doi
url
abstract
keywords
publisher
```

规则：

- 原始 Bib/BibLaTeX 带 `abstract` 时保留；
- 原始 Bib 没有 abstract，但官方来源明确提供摘要时，可以补充；
- 必须记录 `abstract_source`；
- 不得生成 AI 摘要后写入 `abstract` 字段冒充原始摘要；
- Bib 中的 abstract 与 record 中的全文分析不是同一层。

关系：

```text
references.bib
    = bibliographic metadata + original abstract when available

sources/records/*.md
    = analytical / structured knowledge from abstract or full text
```

---

# 15. 知识图谱中的 Evidence Node

知识图谱需要把证据本身作为显式对象管理。

至少区分：

```text
Metadata Evidence
Abstract Evidence
Full-text Text Evidence
Equation Evidence
Figure Evidence
Table Evidence
Experimental Evidence
CFD Evidence
Road-test Evidence
Standard Evidence
```

示例：

```text
Aerodynamic Overshoot
        ↓ supported_by
Claim-001
        ↓ evidence_from
Fig. 7 / p.6 / Source-X
        ↓ contained_in
Local PDF-X
```

不要把“source node”和“evidence node”完全等同。

同一 source 可以包含多个互相独立的 evidence nodes。

---

# 16. 知识图谱学习策略

知识图谱更新优先使用：

```text
full_text_verified records
        ↓
abstract_verified records
        ↓
metadata-only records
```

其中 metadata-only 只用于：

- 历史存在性；
- bibliographic relation；
- citation relation；
- 发现候选方法节点。

不得用 metadata-only 直接支持物理机制、CFD 参数、实验数据或定量结论。

---

# 17. Research Gap 的证据要求

任何重要 research gap 都必须检查：

1. 是否只因为我们没找到全文；
2. 是否只是数据库覆盖不足；
3. 是否由多个 full-text verified sources 支持；
4. 是否存在反例；
5. 是否需要回到原始 PDF 检查作者真正的 limitation；
6. 是否属于分析者推断。

如果证据不足：

```text
POTENTIAL_GAP
```

而不是直接写成确定研究空白。

---

# 18. Research Hypothesis 的证据要求

每个 hypothesis 至少记录：

```text
hypothesis
supporting_fulltext_sources
contradicting_sources
conditions
known_mechanism
missing_validation
proposed_experiment_or_CFD
```

如果核心支持资料仅是 abstract：

```text
HYPOTHESIS_PENDING_FULLTEXT
```

---

# 19. 每日 / 周期更新统计

每轮知识图谱学习增加统计：

```text
new_pdfs_detected
pdfs_fulltext_read
records_upgraded_to_full_text
atomic_claims_added
atomic_claims_revised
knowledge_nodes_added
knowledge_nodes_revised
graph_edges_added
graph_edges_removed
abstract_claims_corrected_by_fulltext
new_evidence_gaps
manual_retrieval_items_added
manual_retrieval_items_resolved
```

特别记录：

```text
Changed understanding
```

即全文阅读后是否改变了过去仅根据摘要形成的理解。

---

# 20. 质量检查

每次全文处理后检查：

## 20.1 PDF identity integrity

PDF 是否与 stable_id、DOI、题名完全匹配？

## 20.2 Evidence integrity

是否把 abstract information 错写成 full-text evidence？

## 20.3 Page integrity

页码、图号、表号、公式号是否真实存在？

## 20.4 Condition integrity

是否保留具体工况？

## 20.5 Claim integrity

record MD 是否准确反映原文，而不是分析者想当然的总结？

## 20.6 Graph integrity

新知识节点和边是否能追溯到具体证据？

## 20.7 Upgrade integrity

从 abstract 升级到 full text 后，旧的低证据结论是否重新检查？

---

# 21. 禁止事项

禁止：

1. PDF 未实际打开就标记 `full_text_verified`；
2. 只读摘要后填写全文参数；
3. 使用 AI 常识补论文没有报告的数值；
4. 把摘要宽泛结论当成全文精确结论；
5. 没有页码/图表证据却伪造 Evidence Map；
6. 每天无变化地重复解析同一 PDF；
7. 因为 GitHub 没有 PDF 就认为资料不存在；
8. 因为本地有 PDF 就默认可上传 GitHub；
9. 把付费全文重新分发到 GitHub；
10. 将一篇论文建立多个 stable_id；
11. 删除摘要阶段记录而不保留升级轨迹；
12. 为了补全知识图谱而制造未经证据支持的节点或 edge。

---

# 22. 首次执行本扩展规则

第一次执行时：

## Step 1

扫描：

```text
D:\GEELY\Crosswind\sources\pdfs\
```

建立当前本地 PDF 清单。

## Step 2

与以下内容交叉匹配：

```text
sources/index.csv
sources/doi_registry.csv
sources/bibliography/references.bib
sources/records/
```

## Step 3

对尚未 full-text verified 的本地 PDF 按优先级全文读取：

1. 历史源头；
2. 方法转折点；
3. 标准关联关键论文；
4. 关键实验论文；
5. 关键 transient CFD；
6. CFD–vehicle dynamics coupling；
7. validation；
8. 当前 research gap / hypothesis 直接依赖的资料。

## Step 4

生成 / 升级 record MD，并建立 Evidence Map。

## Step 5

重新运行现有知识图谱学习流程：

```text
record MD
    ↓
atomic claims
    ↓
concept / method / variable / equation / evidence nodes
    ↓
graph edges
    ↓
learning chapters
    ↓
research frontier
```

## Step 6

更新所有受影响的 synthesis matrices。

## Step 7

输出：

```text
full_text_verified sources
abstract_verified sources
metadata_only sources
manual_retrieval_queue
changed understanding
new / revised knowledge nodes
```

---

# 23. 最终原则

长期维护始终遵循：

> **PDF 保存原始证据，MD 保存结构化理解，知识图谱保存跨资料关系。**

以及：

> **知识图谱不应该每天重新阅读所有 PDF，但任何重要结论都应该能够最终回到 PDF 证据。**

最终实现：

```text
Local PDF
    ↓
Full-text Record
    ↓
Atomic Evidence
    ↓
Knowledge Node
    ↓
Learning Chapter
    ↓
Method Evolution / Research Gap / Research Hypothesis
```

使仓库既能长期扩展，又能保持科学可追溯性。