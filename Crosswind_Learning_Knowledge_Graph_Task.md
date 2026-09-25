# 车辆瞬态侧风知识学习与知识图谱构建：Codex 长期任务书

> 适用仓库：`mao19990908/Crosswind`  
> 本地目录：`D:\GEELY\Crosswind`  
> 本任务负责 **阅读、理解、提取证据、构建概念体系与知识图谱**。  
> `TASK.md` 只负责 **找资料、核验资料、获取合法全文、source 入库**。  
> 当前阶段只做一件核心事情：**把已有资料逐步转化成自己的车辆瞬态侧风知识体系。**

---

# 1. 当前阶段定位

当前不是论文写作阶段、proposal 阶段，也不是“找 research gap”阶段。

当前目标是先把领域基础打牢，形成一个能够持续扩展的知识系统：

```text
SOURCE
原始论文 / 标准 / 报告 / 数据
        ↓
EVIDENCE
atomic claims / equations / observations / conditions
        ↓
KNOWLEDGE
concepts / methods / variables / relationships
        ↓
UNDERSTANDING
physical mechanism / method evolution / limitations
```

当前阶段最重要的问题不是：

> “还有多少论文没搜？”

而是：

> “现有资料已经能让我理解哪些知识？这些知识之间如何连接？还有哪些关键节点证据不足？”

---

# 2. 当前只启用的分析 Skills

## 2.1 `paper-reading`

来源：`jxtse/scientific-research-skills`

用途：

```text
P1 skim
P2 structured reading
P3 deep analysis
```

它只负责“把论文读懂”，不能替代本仓库自己的知识组织规则。

## 2.2 `crosswind-knowledge-base`

这是本项目自己的 project-level Skill，放在：

```text
D:\GEELY\Crosswind\.agents\skills\crosswind-knowledge-base\
```

它不是外部通用 Skill，而是本仓库的“知识入库规范”。

它必须要求 Codex：

1. 每篇资料先定位到知识体系；
2. 提取 atomic claims；
3. 记录条件、证据、限制；
4. 更新已有概念，不轻易制造重复概念；
5. 建立 Concept / Method / Variable / Equation / Evidence 关系；
6. 任何技术结论都能反向追溯到 source；
7. 不足证据写入 `learning/needs_collection.csv`；
8. 不直接开展论文写作、proposal、审稿回复。

## 2.3 当前不启用

当前 learning 阶段不主动调用：

```text
literature-search
paper-fulltext-harvest
related-work-survey
nature-reader
nature-polishing
nature-response
nature-figure
proposal writer
academic-research-suite
```

如果阅读过程中缺资料，只创建 collection request，不在分析任务里重新大规模搜索。

这样避免收集与分析重复。

---

# 3. 与 source 层的关系

执行前读取：

```text
README.md
TASK.md
taxonomy.md
history/timeline.md
sources/index.csv
sources/records/
sources/bibliography/
citations/
learning/backlog.csv
logs/
```

其中：

```text
sources/     = 原始事实来源
citations/   = 文献之间的关系
history/     = 历史演化
learning/    = 用户自己的知识体系
```

原则：

> **learning 不是新的事实源。**

所有 learning 结论必须能追溯：

```text
learning statement
      ↓
knowledge node / atomic claim
      ↓
source_id
      ↓
sources/records/<id>.md
      ↓
original source
```

证据不足时使用：

```text
UNKNOWN
OPEN_QUESTION
NEEDS_FULLTEXT
NEEDS_MORE_EVIDENCE
ANALYST_INFERENCE
```

不得把分析者推断伪装成论文原结论。

---

# 4. 当前阶段目录结构

维护：

```text
learning/
├── README.md
├── state.md
├── backlog.csv
├── needs_collection.csv
├── learning_path.md
├── glossary.md
├── equations.md
├── concept_map.md
├── method_evolution.md
├── open_questions.md
│
├── 01_foundations.md
├── 02_gust_and_environment.md
├── 03_unsteady_aerodynamics.md
├── 04_aerodynamic_response_models.md
├── 05_vehicle_dynamics.md
├── 06_experimental_methods.md
├── 07_transient_cfd.md
├── 08_aero_vehicle_coupling.md
├── 09_validation_and_metrics.md
├── 10_standards_and_test_methods.md
│
├── 11_engineering_applications.md
├── 12_research_frontier.md
│
├── nodes/
│   ├── concepts.csv
│   ├── methods.csv
│   ├── variables.csv
│   ├── equations.csv
│   └── evidence.csv
│
├── graph/
│   ├── edges.csv
│   ├── knowledge_graph.md
│   └── knowledge_graph.mmd
│
└── paper_notes/
```

### 当前阶段重点

优先建设：

```text
learning_path.md
glossary.md
equations.md
concept_map.md
01_foundations.md
02_gust_and_environment.md
03_unsteady_aerodynamics.md
04_aerodynamic_response_models.md
05_vehicle_dynamics.md
06_experimental_methods.md
07_transient_cfd.md
08_aero_vehicle_coupling.md
09_validation_and_metrics.md
10_standards_and_test_methods.md
nodes/*
graph/*
```

### 当前阶段暂缓

```text
11_engineering_applications.md
12_research_frontier.md
系统性 research gap
博士后方案论证
SCI 论文写作
```

这些文件可以保留骨架，但基础知识体系没有稳定前，不要为了“完整”强行填充。

---

# 5. 学习主线：从基础开始

知识体系必须按下面顺序逐渐建立：

```text
Level 0  问题定义
Level 1  变量 / 坐标系 / 系数
Level 2  阵风输入
Level 3  非定常气动响应
Level 4  气动系统响应模型
Level 5  车辆动力学
Level 6  实验方法
Level 7  瞬态 CFD
Level 8  气动—车辆动力学耦合
Level 9  验证体系
Level 10 标准与试验方法
```

不得直接从 CFD 或某一篇最新论文开始搭知识体系。

---

# 6. Level 0：问题定义

首先建立最基本概念。

必须区分：

```text
steady crosswind
fixed yaw
transient crosswind
crosswind gust
natural gust
finite wind zone
vehicle entering crosswind
passing disturbance
bridge / tunnel-exit disturbance
```

核心主链：

```text
Atmospheric / Generated Gust
        ↓
Relative Wind
        ↓
Transient Flow Field
        ↓
Aerodynamic Forces & Moments
        ↓
Vehicle Motion
        ↓
Driver / Controller
        ↓
Trajectory / Stability
```

以后所有知识节点尽量挂到这条主链。

固定偏航角只能作为 steady baseline / quasi-steady reference / mechanism comparison，不能自动等价于阵风。

---

# 7. Level 1：变量、坐标系和定义

至少建立以下变量族。

## 来流

```text
vehicle speed
crosswind velocity
resultant velocity
instantaneous yaw angle
gust rise time
gust duration
gust length
turbulence intensity
integral length scale
frequency
reduced frequency
Strouhal number
```

## 气动力

```text
drag
side force
lift
roll moment
pitch moment
yaw moment
```

必须记录：

```text
coordinate system
sign convention
reference area
reference length
moment reference point
normalization
```

## 车辆响应

```text
lateral acceleration
yaw rate
roll rate
roll angle
vehicle sideslip angle
lateral displacement
steering-wheel angle
steering correction
```

严格区分：

```text
aerodynamic yaw angle
vehicle heading angle
vehicle sideslip angle
```

不同来源定义不一致时，不得自动统一。

---

# 8. Level 2：阵风输入体系

至少建立：

```text
step gust
ramp gust
pulse gust
doublet
sinusoidal gust
finite crosswind zone
turbulent gust
natural road gust
transient yaw
```

每个 Gust 节点回答：

```text
定义
数学表达 / physical description
时间尺度
空间尺度
关键参数
实验如何生成
CFD 如何实现
对应真实场景
适用范围
不能代表什么
支持来源
```

---

# 9. Level 3：非定常气动

优先建立以下核心概念：

```text
quasi-steady assumption
non-quasi-steady response
overshoot / undershoot
phase lag
hysteresis
flow establishment / relaxation
wake memory
surface-pressure transient
```

尤其要回答：

```text
输入变化后，流场为什么不能瞬间到达对应稳态？
不同气动力分量是否有不同响应时间？
steady yaw 数据何时可以近似 transient response？
何时不可以？
```

不能人为制造统一阈值，除非原始证据充分。

---

# 10. Level 4：气动系统响应模型

建立输入—系统—输出视角：

```text
Input
  gust / yaw history
        ↓
Vehicle aerodynamic system
        ↓
Output
  force / moment history
```

重点概念：

```text
aerodynamic derivatives
transfer function
frequency response
aerodynamic admittance
weighting function
convolution
impulse response
reduced-order model
state-space representation
```

每个模型节点必须记录：

```text
input
output
assumptions
linear / nonlinear
memory
parameter identification
validation
applicable range
source
```

---

# 11. Level 5：车辆动力学

建议从简单到复杂：

```text
kinematic intuition
        ↓
2-DOF bicycle model
        ↓
nonlinear tyre
        ↓
roll dynamics
        ↓
multibody
        ↓
6-DOF vehicle motion
        ↓
driver / controller closed loop
```

每层回答：

```text
增加了什么自由度？
输入是什么？
输出是什么？
什么侧风问题必须用到这一层？
什么问题不需要这么复杂？
```

---

# 12. Level 6：实验方法

按“输入—测量—输出”组织。

至少建立：

```text
static wind tunnel
moving model
dynamic wind tunnel
gust generator
full-scale wind generator
road test
natural-wind measurement
```

每种方法统一记录：

```text
gust generation
vehicle/model motion
scale
Reynolds number
blockage
ground/wheel treatment
measurement
sampling
synchronization
repeatability
uncertainty
validation role
limitations
```

---

# 13. Level 7：瞬态 CFD

按照“如何重现阵风物理”组织，不按软件品牌组织。

至少覆盖：

```text
transient inlet
spatial gust field
moving vehicle
moving gust region
sliding mesh
overset mesh
ALE
URANS
DES / DDES / IDDES
LES
synthetic turbulence
precursor / mapped turbulence
```

每个方法统一比较：

```text
gust implementation
vehicle motion
mesh motion
turbulence treatment
temporal resolution
spatial resolution
computational cost
validation level
known limitation
supporting source
```

高保真 turbulence model 不等于高可信度。

---

# 14. Level 8：气动—车辆动力学耦合

统一知识框架：

```text
Level 0  steady coefficient table
Level 1  quasi-steady lookup
Level 2  precomputed transient loads → vehicle dynamics
Level 3  ROM / transfer function → vehicle dynamics
Level 4  online one-way CFD → vehicle dynamics
Level 5  fully coupled CFD ↔ vehicle motion
```

同时区分：

```text
one-way
two-way
loose coupling
strong coupling
open-loop
closed-loop driver
closed-loop controller
```

若文献定义不同，保留原定义并解释映射，不强行改写作者术语。

---

# 15. Level 9：验证体系

建立三级验证：

```text
Level A: gust field validation
Level B: aerodynamic load validation
Level C: vehicle response validation
```

同时记录：

```text
uncertainty
repeatability
phase error
peak error
RMS
response timing
trajectory error
```

“CFD 与风洞气动力一致”不能自动写成“车辆侧风稳定性已验证”。

---

# 16. Level 10：标准与试验方法

重点包括：

```text
historical methods
ISO 12021-1:1996
ISO 12021:2010
related later methods
```

每个标准节点至少回答：

```text
研究对象
输入形式
试验速度
wind generator
open / closed loop
评价量
适用范围
与真实道路阵风的差异
明确不代表什么
```

不得复制受版权保护标准全文。

---

# 17. Atomic Claim：知识体系的最小单位

不要直接把每篇论文写成长摘要。

每篇值得学习的 source 先抽取 atomic claims。

建议字段：

```text
claim_id
source_id
claim
evidence
conditions
variables
method
limitation
verification_status
confidence
related_nodes
```

一个 claim 必须同时回答：

```text
作者发现了什么？
依据是什么？
在什么条件下？
不能外推到哪里？
它连接哪些知识节点？
```

同一个知识结论由多个来源支持时：

```text
Concept
 ├─ Evidence A
 ├─ Evidence B
 └─ Evidence C
```

而不是复制三份概念。

---

# 18. 节点类型

至少支持：

```text
Concept
Variable
Equation
Model
Gust
Method
Facility
Standard
Evidence
Source
```

当前阶段 `Research Question` 可以保留，但不作为重点扩展对象。

---

# 19. Edge 类型

`learning/graph/edges.csv` 建议统一使用：

```text
is_a
part_of
defined_by
described_by
measured_by
generated_by
predicted_by
validated_by
input_to
output_of
depends_on
affects
causes
correlates_with
approximated_by
fails_under
extends
refines
contradicts
supports
standardized_by
implemented_in
used_by
derived_from
evidence_from
```

不要无限制造同义 edge。

每条边都必须能回答：

> “为什么 A 和 B 有这条关系？”

---

# 20. 每个知识节点的标准卡片

重要节点使用统一结构：

```markdown
# Node Name

## 一句话解释

## 前置知识

## 严格定义

## 物理直觉

## 数学描述

## 影响变量

## 实验认识

## CFD 认识

## 适用范围

## 不成立 / 不确定的情况

## Evidence
- source_id

## Evidence Level

## Related Nodes
```

不是所有节点都必须有全部章节；没有证据时写未知，不补猜测。

---

# 21. 学习深度：P1 / P2 / P3

## P1：定位

```text
这篇资料解决什么问题？
在知识体系什么位置？
为什么值得保留？
```

## P2：理解

```text
输入是什么？
方法是什么？
输出是什么？
关键结论是什么？
证据是什么？
限制是什么？
```

## P3：研究级理解

仅限核心资料：

```text
关键假设是什么？
如何复现？
最容易出错什么？
哪些结论可以迁移？
哪些不能？
它改变了领域中的什么？
```

优先 P3：

```text
历史源头
方法转折点
核心标准
关键实验方法
关键 transient CFD 方法
关键 validation paper
```

普通资料 P1 / P2 即可。

---

# 22. 证据等级

继承 source verification，并在 learning 层建立：

```text
E0 = metadata only
E1 = abstract verified
E2 = full text verified
E3 = independently supported by multiple primary sources
E4 = cross-validated across methods / experiments
```

E3 / E4 必须给出明确依据。

不能用 learning 评级覆盖 source 层原始 verification status。

---

# 23. 矛盾与不确定性

不同资料结论不一致时，不要自动平均成一句话。

建立 tension / contradiction，并检查：

```text
gust type
reduced frequency
vehicle geometry
Reynolds number
measurement method
force component
normalization
coordinate system
open / closed loop
steady baseline definition
```

把争议保留下来。

---

# 24. 公式管理

所有正式公式集中维护：

```text
learning/equations.md
learning/nodes/equations.csv
```

每条公式记录：

```text
equation_id
name
formula
symbols
units
assumptions
source
alternative_definitions
notes
```

重点检查：

```text
relative wind
yaw angle
aerodynamic coefficients
reduced frequency
Strouhal number
aerodynamic admittance
vehicle lateral dynamics
```

未核全文：

```text
FORMULA_PENDING_FULLTEXT
```

不得凭记忆补公式。

---

# 25. Glossary

`learning/glossary.md` 至少记录：

```text
英文
中文
缩写
定义
易混淆概念
source
```

重点避免混淆：

```text
crosswind
gust
yaw
sideslip
side force
lateral force
yaw moment
transient
unsteady
quasi-steady
admittance
aerodynamic derivative
```

---

# 26. Knowledge Graph 输出

不要一开始生成数百节点大图。

优先维护多个可读子图：

```text
Graph A 总体物理链
Graph B Gust taxonomy
Graph C Unsteady aerodynamics
Graph D Experimental methods
Graph E CFD methods
Graph F Aero–vehicle coupling
Graph G Validation
Graph H Method evolution
```

机器可读数据：

```text
learning/nodes/*.csv
learning/graph/edges.csv
```

人类可读：

```text
learning/graph/knowledge_graph.md
learning/graph/knowledge_graph.mmd
```

Mermaid 图必须与 nodes / edges 基本一致。

---

# 27. 分析任务不得自行扩库

如果阅读发现：

```text
缺关键原始论文
缺标准入口
缺全文
缺定义来源
缺实验验证
缺 CFD validation
```

不要在 learning task 里继续大规模搜索。

写入：

```text
learning/needs_collection.csv
```

字段：

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

下一次由 `TASK.md` 的 collection task 处理。

---

# 28. Backlog 与状态

维护：

```text
learning/backlog.csv
learning/state.md
```

`backlog.csv`：

```text
source_id
added_date
priority
reason
access_level
verification_status
suggested_pass
learning_status
last_processed
notes
```

`learning_status`：

```text
pending
in_progress
done
needs_more_evidence
```

`state.md` 至少记录：

```text
当前学习 Level
当前章节
当前核心 nodes
未完成 backlog 数
P1/P2/P3 完成量
needs_collection 数
本轮断点
下一步
```

这样 Codex 即使第二天继续，也能从断点恢复。

---

# 29. 当前阶段执行节奏

用户要求：收集一天、分析一天；但如果分析 backlog 没清完，则连续分析直到当前 backlog 基本清理完成。

执行逻辑：

```text
Collection Day
    ↓
source 入库
    ↓
backlog 增长
    ↓
Learning Day
```

如果 Learning Day 用完当天额度仍未完成：

```text
第二天继续 Learning
第三天仍未完成则继续 Learning
...
```

如果 Learning Day 提前完成且仍有额度：

```text
剩余额度可执行 TASK.md 的 Collection
```

但新资料只加入 backlog；避免无限循环。

当前阶段优先级：

> **消化已有资料 > 继续扩大资料数量。**

---

# 30. Learning Day 标准流程

```text
01 检查 Git 状态并同步
02 读取 learning/state.md
03 读取 learning/backlog.csv
04 优先处理基础 Level 未完成节点
05 对 backlog source 执行 paper-reading P1/P2/P3
06 提取 atomic claims
07 更新 Evidence nodes
08 更新 Concept / Method / Variable / Equation nodes
09 更新 graph edges
10 更新 learning 章节
11 更新 glossary / equations
12 检查 contradiction / uncertainty
13 缺证据时写 needs_collection.csv
14 更新 knowledge_graph.md / mmd
15 更新 state / backlog
16 写 Learning 日志
17 git commit / push
18 核对 local HEAD 与 remote SHA
```

---

# 31. 当前第一阶段执行顺序

第一次按新版任务书运行时：

## Step 1：盘点现有 source

读取：

```text
sources/index.csv
sources/records/
history/timeline.md
citations/
```

给全部已有 source 至少建立 P1 状态。

## Step 2：搭骨架

建立 / 校正：

```text
learning_path.md
glossary.md
concept_map.md
nodes/concepts.csv
nodes/methods.csv
nodes/variables.csv
graph/edges.csv
```

## Step 3：优先基础三章

```text
01_foundations.md
02_gust_and_environment.md
03_unsteady_aerodynamics.md
```

## Step 4：再扩展方法体系

```text
04_aerodynamic_response_models.md
05_vehicle_dynamics.md
06_experimental_methods.md
07_transient_cfd.md
08_aero_vehicle_coupling.md
09_validation_and_metrics.md
10_standards_and_test_methods.md
```

## Step 5：核心资料 P2 / P3

对历史源头、方法转折、标准、关键验证文献优先深读。

## Step 6：只在基础稳定后再考虑前沿

在用户明确进入下一阶段前，不主动把工作重点转成 research gap / proposal。

---

# 32. 当前阶段完成标准

当以下条件基本满足，可以认为“初始知识体系搭建完成”：

1. `learning_path.md` 有清晰学习顺序；
2. 核心术语在 `glossary.md` 中有定义和来源；
3. 主要变量、坐标、系数定义已整理；
4. Gust taxonomy 已建立；
5. steady vs transient 的边界清楚；
6. quasi-steady / non-quasi-steady / overshoot / lag 等核心概念已形成节点；
7. 实验方法、CFD 方法、车辆动力学、耦合与验证已有基本框架；
8. 重要公式有来源；
9. 所有已有 source 至少完成 P1 定位；
10. 核心 source 完成 P2，少数基础 source 完成 P3；
11. nodes / edges 与 learning 章节能互相对应；
12. 知识图谱可以从一个概念反查 supporting sources；
13. 未解决问题被明确标记为未知或缺证据，而不是被补猜。

完成这些后，再进入：

```text
related-work synthesis
research gaps
博士后开题
实验/仿真方案设计
SCI output
```

---

# 33. 日志

在：

```text
logs/YYYY-MM-DD.md
```

追加：

```markdown
## Learning update

### Processed sources

### P1 / P2 / P3

### New concepts

### Updated concepts

### New atomic claims

### New edges

### Changed understanding

### Contradictions / uncertainty

### Needs collection

### Backlog remaining

### Current learning level

### Next breakpoint
```

---

# 34. 质量检查

每次更新必须检查：

```text
Source integrity
Definition integrity
Coordinate integrity
Condition integrity
Steady/transient integrity
Open/closed-loop integrity
Evidence integrity
Equation integrity
Graph integrity
```

尤其检查：

- abstract evidence 是否被写成 full-text verified；
- 不同坐标系的力矩符号是否混用；
- 不同 reduced frequency 定义是否混用；
- 特定车型 / 特定 gust 工况是否被写成普适结论；
- steady yaw 是否被误写成 transient evidence；
- CFD fidelity 是否被误当作 validation level。

---

# 35. 禁止事项

禁止：

1. 一篇论文一段摘要机械堆叠；
2. 按作者流水账写知识体系；
3. 为了图谱完整制造不存在的 edge；
4. 为了章节完整补猜公式；
5. 未核全文写具体试验 / CFD 参数；
6. 把引用次数当作证据强度；
7. 把新论文自动视为更正确；
8. 把 steady yaw 和 transient gust 混为一谈；
9. 把分析者推断当作者结论；
10. 为博士后课题刻意制造 research gap；
11. learning task 自己重复执行大规模 literature search；
12. 当前阶段主动进入论文写作、proposal、润色、审稿回复。

---

# 36. 当前知识系统的核心闭环

```text
TASK.md
literature-search
        ↓
SOURCE
        ↓
paper-fulltext-harvest
        ↓
learning/backlog.csv
        ↓
paper-reading
        ↓
Atomic Claims
        ↓
crosswind-knowledge-base
        ↓
Concept / Method / Variable / Equation / Evidence
        ↓
Knowledge Graph + Learning Chapters
        ↓
missing evidence
        ↓
learning/needs_collection.csv
        ↓
TASK.md
```

当前阶段始终遵循：

> **先理解，再连接；先证据，再总结；先基础，再前沿。**

以及：

> **Synthesis is not summary.**

最终目标不是“资料最多”，而是：

```text
概念清楚
关系清楚
证据清楚
条件清楚
未知也清楚
```
