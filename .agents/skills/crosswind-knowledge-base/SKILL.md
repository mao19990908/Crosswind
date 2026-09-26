---
name: crosswind-knowledge-base
description: 将 Crosswind 仓库中已入库的车辆侧风资料转化为可追溯的 atomic claims、证据、知识节点与图谱关系；用于 Learning / Knowledge Layer，不承担论文检索或全文获取。
---

# Crosswind 知识入库

以仓库根目录的 `Crosswind_Learning_Knowledge_Graph_Task.md` 为主要规范。开始前读取 `learning/README.md`、`learning/state.json`、`learning/nodes/*.csv`、`learning/graph/edges.csv`、已有 `learning/paper_notes/` 和当前 source record。从现有进度继续；不要按任务书的“第一次运行”步骤重建已存在的图谱。

## 职责与入库链

本 Skill 与 `paper-reading` 配合，处理 `TASK.md` 收集并交给 learning backlog 的 source。对每条技术结论执行：

`source → atomic claim → evidence → concept / method / variable / equation → graph edge`

1. 核对 canonical `source_id`、资料版本、可访问内容和 source 层 verification status。P1 定位、P2 理解、P3 深读以实际读到的材料为准。
2. 在 `learning/nodes/evidence.csv` 记录最小、可检验的 atomic claim：`claim_id`、`source_id`、claim、证据位置或摘要来源、conditions、method、variables、limitation、verification_status、related_nodes。当前表若无 `limitation` 列，写入新 claim 前先无损增列；旧行留空表示尚未复核，不补猜限制条件。必要时更新对应的 `learning/paper_notes/<source_id>.md`。
3. 先查已有 `learning/nodes/*.csv`、glossary 和章节；优先补充现有节点的定义、条件及证据。只有概念确实不同才新建节点，保留稳定 ID，避免同义节点和同义 edge。
4. 只为能解释的关系更新 `learning/graph/edges.csv`；每条技术边要有 `source_id`、condition、verification_status 和理由。知识结论必须能经 claim/evidence 反查到 `sources/records/<source_id>.md` 和原始来源。
5. 由 CSV 节点和边更新章节、`learning/graph/knowledge_graph.md` 与 `.mmd`；后两者是同一图谱的可读视图，不是第二套独立知识库。

## 证据与物理边界

- 严格区分 `steady crosswind / fixed yaw` 与 `transient crosswind / gust`。稳态结果可以作为 baseline 或比较，不能冒充瞬态阵风证据。
- 严格区分 aerodynamic yaw angle（相对来流与车体纵轴夹角）、vehicle heading angle（车体指向）和 vehicle sideslip angle（车辆速度与车体纵轴夹角）；记录坐标系、符号、参考速度、工况和开环/闭环条件。保留原文定义及其适用范围。
- 每条 claim 必须记录 condition、evidence、limitation、verification status。`metadata only`、`abstract verified`、`full text verified` 分层；不能把摘要或 PDF 身份/哈希核验写成全文已核读。只有确实读到原文相应页、节、公式、图或表，才用全文级证据。
- 将分析者推断明确标为 `ANALYST_INFERENCE`，不得写成作者结论。缺证据时标记 `UNKNOWN`、`NEEDS_FULLTEXT` 或 `NEEDS_MORE_EVIDENCE`，不补猜公式、参数或因果关系。
- 证据缺口写入 `learning/needs_collection.csv`，交由 `TASK.md` 的 Collect / Source Layer 处理；本 Skill 不自行启动大规模检索或全文获取。
- 当前阶段只建设知识体系；不得自动转入 research gap、proposal、SCI 写作、润色或审稿回复。

结束前核对 source、claim、节点、edge 和图示之间的可追溯性，并按学习任务书维护现有进度状态。
