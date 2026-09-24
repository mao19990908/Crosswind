# 车辆瞬态侧风知识学习与知识图谱构建：Codex 长期任务书

> 适用仓库：`mao19990908/Crosswind`  
> 本地目录：`D:\GEELY\Crosswind`  
> 本任务与现有 `TASK.md` 分工不同：  
> - `TASK.md` 负责 **找资料、核验资料、追踪历史与引用链**；  
> - 本任务负责 **把已经进入知识库的资料真正学懂、组织成可学习的知识体系，并持续构建“概念—方法—证据—工程应用”知识图谱**。  
>
> 核心目标不是再做一份文献列表，而是逐步形成一本可追溯的“车辆瞬态侧风教材 + 研究知识图谱”。

---

# 1. 任务定位

对仓库中已经收集、已经核验或正在核验的资料进行持续学习和知识重构，从最基础概念开始，逐层建立：

> **基础物理 → 阵风输入 → 非定常气动 → 车辆动力学 → 实验方法 → CFD → 气动/车辆耦合 → 验证评价 → 标准 → 工程应用 → 研究空白**

最终使一个刚进入“车辆瞬态侧风”领域的研究人员，可以只沿 `learning/` 目录阅读，就逐步建立完整知识体系；同时又能从任一知识点反向追溯到原始论文、标准、报告或数据来源。

这不是普通综述。

最终产物应同时具备：

1. **教材属性**：从基础开始讲清楚；
2. **知识图谱属性**：每个概念与上下游关系可追踪；
3. **证据属性**：结论知道来自哪篇资料、证据等级如何；
4. **研究属性**：能看到方法演化、争议、缺口和可研究问题；
5. **工程属性**：能够直接服务“车辆侧风模拟及实验验证”博士后课题。

---

# 2. 可借鉴的社区 Skill 思路

本任务可借鉴社区中以下三类成熟思路，但必须适配本仓库，不能机械照搬。

## 2.1 Literature Survey：Intent → Triage → Deepen → Synthesize

借鉴点：

- 先建立领域地图，再决定哪些资料需要深读；
- 对关键论文采用分层阅读：
  - Pass 1：知道论文解决什么；
  - Pass 2：理解方法、结论、证据和限制；
  - Pass 3：能够重新推导、复现、质疑并迁移；
- 不按“论文 A、论文 B、论文 C”顺序写综述，而要按问题和知识结构重组。

本项目对应为：

> **Map → Learn → Connect → Synthesize → Apply**

---

## 2.2 Literature Review + Knowledge Graph

借鉴点：

- backward citation；
- forward citation；
- full-text reading；
- method lineage；
- knowledge graph；
- 可追溯的研究日志。

本仓库已经在 `citations/` 中做引用关系，因此本任务不能重复只画“谁引用谁”。

本任务要进一步生成：

> **Concept Graph / Method Graph / Evidence Graph / Validation Graph**

也就是：

> 文献之间有关系，知识之间也必须有关系。

---

## 2.3 Research Synthesis

借鉴点：

每次读资料时，不只保存摘要，而提取最小知识单元：

- Claim：论文声称什么；
- Evidence：用什么证据支持；
- Condition：在什么条件下成立；
- Limitation：哪里不能外推；
- Relation：和已有知识是支持、补充、限制还是冲突。

因此本任务禁止：

> 一篇论文一个摘要，然后把摘要堆在一起。

必须转换为：

> 多篇资料共同支撑一个知识节点。

---

# 3. 与现有仓库的关系

开始执行前必须读取：

```text
README.md
TASK.md
taxonomy.md
history/timeline.md
sources/index.csv
sources/records/
citations/
search/
synthesis/
logs/
```

其中：

- `sources/`：事实来源；
- `citations/`：文献关系；
- `history/`：历史演化；
- `synthesis/`：已有跨文献综合；
- `learning/`：本任务新建的“学习层”。

原则：

> **learning 层不得成为新的事实源。**

如果 learning 中出现某个技术结论，必须能够追溯到：

```text
learning
    ↓
knowledge node
    ↓
source record
    ↓
original source / verified metadata
```

如果某个知识点无法找到足够依据：

```text
UNKNOWN
OPEN_QUESTION
NEEDS_FULLTEXT
ANALYST_INFERENCE
```

必须明确标记，不能自行补齐。

---

# 4. 新建目录结构

在仓库根目录新增：

```text
learning/
├── README.md
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

如目录已经存在，不删除已有内容，只增量更新。

---

# 5. 学习主线：必须从基础开始

`learning_path.md` 必须定义明确的阅读顺序。

不得直接从 CFD 或某篇论文开始。

建议主线如下。

---

## Level 0：问题是什么

首先回答：

### 0.1 什么叫车辆侧风

区分：

- steady crosswind；
- transient crosswind；
- crosswind gust；
- natural gust；
- finite wind zone；
- vehicle entering a crosswind；
- passing manoeuvre；
- bridge / tunnel exit disturbance。

### 0.2 为什么固定偏航角不等于阵风

从最直观角度说明：

```text
稳态偏航：
来流方向不随时间变化
        ↓
车辆周围流场可趋向稳定状态

阵风：
来流方向/速度随时间和空间变化
        ↓
分离、涡结构、压力场具有建立与衰减过程
        ↓
气动力存在超调、滞后、记忆效应
```

此处只能用已有证据支持，不提前给出未经验证的普适结论。

### 0.3 研究链条

必须建立整个知识库最重要的一条主链：

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
Driver / Controller Response
        ↓
Trajectory / Stability
```

之后所有知识节点都应该能够挂到这条链上。

---

# 6. Level 1：基础变量与坐标系

建立最基础变量表。

至少覆盖：

## 6.1 来流变量

例如：

- vehicle speed；
- crosswind velocity；
- resultant relative velocity；
- instantaneous yaw angle；
- gust rise time；
- gust duration；
- gust length；
- turbulence intensity；
- shear；
- gust frequency；
- reduced frequency。

禁止假定所有论文中的定义一致。

若不同论文采用不同 reduced frequency 定义，必须写成：

```text
Definition A
Definition B
Definition C
```

并分别标注来源。

---

## 6.2 气动力

至少建立：

- drag；
- side force；
- lift；
- roll moment；
- pitch moment；
- yaw moment。

并记录：

- 坐标轴；
- 正负号；
- reference area；
- reference length；
- moment reference point；
- coefficient normalization。

不得在不同来源定义不一致时直接横向比较系数。

---

## 6.3 车辆动力学响应

至少覆盖：

- lateral acceleration；
- yaw rate；
- roll rate；
- roll angle；
- vehicle sideslip angle；
- path deviation；
- steering-wheel angle；
- steering correction；
- tyre lateral force。

明确区分：

```text
aerodynamic yaw angle
vehicle heading angle
vehicle sideslip angle
```

---

# 7. Level 2：阵风输入

将所有阵风形式建立为独立知识节点。

至少包括：

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

每种阵风节点必须回答：

1. 数学或物理定义；
2. 如何生成；
3. 时间尺度；
4. 空间尺度；
5. 典型参数；
6. 可模拟什么实际问题；
7. 不能模拟什么；
8. 哪些论文使用过；
9. 哪些实验设施可以生成；
10. CFD 中如何实现。

最终建立：

```text
Gust Type
   ├── Experiment
   ├── CFD Boundary Condition
   ├── Typical Metrics
   ├── Applicable Scenario
   └── Source
```

---

# 8. Level 3：非定常气动

按照物理问题，而不是论文顺序学习。

至少形成以下知识节点：

## 8.1 Quasi-steady assumption

回答：

- 什么是准稳态；
- 为什么会想到使用稳态偏航数据预测阵风；
- 数学上如何理解；
- 哪些情况下可能成立；
- 哪些实验发现其不足；
- 不足体现在哪些载荷分量；
- 是否存在频率、阵风长度、偏航角等适用边界。

不要人为总结一个“统一阈值”，除非原始证据足够。

---

## 8.2 Overshoot / Undershoot

建立：

```text
gust entry
    ↓
flow-field transient
    ↓
surface-pressure transient
    ↓
force / moment overshoot
```

分别记录：

- side force；
- lift；
- yaw moment；
- roll moment。

不得假设所有分量行为相同。

---

## 8.3 Phase lag

建立：

```text
gust input
    ↓ Δt / phase
aerodynamic response
```

区分：

- 风场自身传播滞后；
- 压力响应滞后；
- 整体气动力滞后；
- 车辆运动滞后。

---

## 8.4 Flow structures

逐渐建立：

- separation；
- A-pillar / C-pillar flow；
- leeward vortex；
- wake；
- base pressure；
- rear geometry effect。

仅在现有资料有充分证据时展开。

---

# 9. Level 4：气动系统响应模型

重点建立：

```text
Input:
gust / yaw history

System:
vehicle aerodynamics

Output:
force / moment history
```

学习：

- aerodynamic derivatives；
- transfer function；
- frequency response；
- aerodynamic admittance；
- weighting function；
- convolution；
- reduced-order model；
- state-space representation（若已有资料涉及）。

每个模型必须回答：

1. 输入是什么；
2. 输出是什么；
3. 是线性还是非线性；
4. 是否考虑记忆；
5. 是否区分不同载荷分量；
6. 参数从哪里得到；
7. 能否直接接入车辆动力学；
8. 验证方式；
9. 适用范围；
10. 当前证据等级。

---

# 10. Level 5：车辆动力学

从最简单模型开始。

建议顺序：

```text
kinematic intuition
    ↓
2-DOF bicycle model
    ↓
nonlinear tyre
    ↓
roll dynamics
    ↓
multi-body vehicle
    ↓
6-DOF vehicle motion
    ↓
driver/controller closed loop
```

每一级说明：

- 新增加了什么自由度；
- 解决什么问题；
- 输入需要什么气动力；
- 输出什么车辆响应；
- 相比上一层多了什么；
- 哪些侧风问题必须用这一层；
- 哪些问题用简单模型已经足够。

---

# 11. Level 6：实验方法

不要按实验室分类，而按“输入—测量—输出”组织。

建立：

## 11.1 静态风洞

说明：

- fixed yaw；
- steady baseline；
- 为什么仍然重要；
- 为什么不能直接等价于 gust。

---

## 11.2 Moving model

建立：

```text
model motion
      +
stationary / prescribed wind field
      ↓
relative transient yaw
```

重点整理：

- 模型速度；
- 风区长度；
- blockage；
- measurement synchronization；
- repeated runs；
- dynamic force measurement。

---

## 11.3 Dynamic wind tunnel / gust generator

包括：

- lateral jet；
- oscillating aerofoil；
- active grid；
- multi-fan array；
- transient yaw system。

逐个建立设施节点。

---

## 11.4 Full-scale vehicle test

包括：

- roadside wind generator；
- finite wind zone；
- natural crosswind；
- instrumented vehicle。

记录：

- driver locked / free；
- open-loop / closed-loop；
- vehicle states；
- steering input；
- repeatability；
- environmental uncertainty。

---

# 12. Level 7：瞬态 CFD

按照“如何重现物理阵风”组织，而不是按软件名称。

至少覆盖：

```text
Transient inlet
Moving vehicle
Moving gust field
Sliding / overset mesh
ALE
URANS
DES / DDES
LES
```

每种方法建立统一比较表：

| 项目 | 内容 |
|---|---|
| gust implementation | |
| vehicle motion | |
| mesh motion | |
| turbulence model | |
| temporal resolution | |
| spatial resolution | |
| computational cost | |
| validation level | |
| known limitations | |
| supporting sources | |

尤其强调：

> 高保真湍流模型 ≠ 自动完成有效验证。

---

# 13. Level 8：气动—车辆动力学耦合

建立清晰等级体系。

例如：

```text
Level 0
steady coefficients

Level 1
quasi-steady lookup

Level 2
precomputed transient aerodynamic loads
        ↓
vehicle dynamics

Level 3
ROM / transfer function
        ↔
vehicle dynamics

Level 4
online one-way CFD → vehicle dynamics

Level 5
fully coupled CFD ↔ vehicle motion
```

如果仓库现有文献中的等级定义不同，以资料实际定义为准，并解释差异。

必须区分：

- one-way；
- two-way；
- loose coupling；
- strong coupling；
- open-loop；
- closed-loop driver；
- closed-loop controller。

---

# 14. Level 9：验证体系

建立三级验证框架：

```text
Level A：Gust field validation
        ↓
风场是否正确

Level B：Aerodynamic load validation
        ↓
气动力是否正确

Level C：Vehicle response validation
        ↓
车辆运动是否正确
```

并进一步加入：

- uncertainty；
- repeatability；
- phase error；
- peak error；
- RMS；
- response timing；
- trajectory error。

每篇 CFD 论文都要标出：

```text
Validation:
A = yes/no
B = yes/no
C = yes/no
```

不得只因为论文写了“validated”就直接认为 Level C 已验证。

---

# 15. Level 10：标准与规范

建立标准发展线：

```text
historical methods
      ↓
ISO 12021-1:1996
      ↓
ISO 12021:2010
      ↓
later verification / related methods
```

每个标准节点回答：

- 研究对象；
- 输入形式；
- 试验速度；
- 风发生器；
- open/closed loop；
- 评价量；
- 适用范围；
- 明确不代表什么；
- 与真实道路阵风的差异。

不得复制受版权保护标准全文。

只允许：

- 官方公开信息；
- 合法获取后的研究性摘要；
- 参数的必要引用；
- 本项目自己的结构化解释。

---

# 16. Level 11：工程应用

当基础知识成熟后，再建立工程应用。

包括但不限于：

```text
body shape
rear geometry
underbody
ride height
active aero
steering control
ESC / chassis control
crosswind compensation
robust aerodynamic design
```

每个工程应用必须回答：

```text
改变了什么物理量？
        ↓
改变了什么气动力？
        ↓
改变了什么车辆响应？
        ↓
在什么 gust condition 下有效？
```

不要只写：

> “某方案提高了侧风稳定性。”

必须写清楚因果链。

---

# 17. Knowledge Graph 节点体系

知识图谱至少包含以下节点类型。

## 17.1 Concept

例如：

```text
Transient Crosswind
Quasi-steady Assumption
Aerodynamic Overshoot
Phase Lag
Aerodynamic Admittance
```

---

## 17.2 Variable

例如：

```text
Crosswind Velocity
Yaw Angle
Side Force Coefficient
Yaw Moment Coefficient
Yaw Rate
Lateral Acceleration
```

---

## 17.3 Equation / Model

例如：

```text
Relative-wind relation
Bicycle model
Transfer function
Weighting function
ROM
```

---

## 17.4 Gust

例如：

```text
Step Gust
Finite Wind Zone
Sinusoidal Gust
Turbulent Gust
Natural Gust
```

---

## 17.5 Method

例如：

```text
Static Wind Tunnel
Moving Model
Dynamic Wind Tunnel
Road Test
Transient CFD
DES
Overset Mesh
```

---

## 17.6 Facility

例如：

```text
DOT full-scale disturbance facility
Cranfield moving-model facility
Durham transient crosswind facility
BMW crosswind facility
```

仅在来源足够明确时建节点。

---

## 17.7 Standard

例如：

```text
ISO 12021-1:1996
ISO 12021:2010
```

---

## 17.8 Source

直接关联：

```text
sources/records/<id>.md
```

---

## 17.9 Research Question

例如：

```text
When does quasi-steady prediction fail?
How should gust spectra be transferred to vehicle dynamics?
How representative is ISO wind-generator input of natural road gusts?
```

---

# 18. Edge 关系类型

`learning/graph/edges.csv` 至少支持：

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
improves
extends
refines
contradicts
supports
standardized_by
implemented_in
used_by
derived_from
cited_by
evidence_from
open_question_for
```

不要无限新增同义关系。

新增 edge type 时必须在 `knowledge_graph.md` 中解释。

---

# 19. 每个知识节点的标准卡片

每个重要知识节点都应具备统一结构。

示例：

```markdown
# Aerodynamic Overshoot

## 一句话解释
车辆进入阵风时，瞬态气动力峰值可能高于对应稳态条件。

## 前置知识
- Relative wind
- Separation
- Finite gust

## 定义
...

## 物理机制
...

## 数学描述
...

## 影响变量
...

## 实验观察
...

## CFD 观察
...

## 对车辆动力学的影响
...

## 适用边界
...

## 争议 / 未确定问题
...

## Evidence
- source A
- source B

## Evidence Level
abstract_verified / full_text_verified / ...

## Related Nodes
- Quasi-steady
- Phase lag
- Side force
- Yaw moment
```

---

# 20. Atomic Claim：最小知识单元

对每篇值得学习的资料，不直接生成长摘要。

先抽取 atomic claims。

统一格式：

```text
claim_id
source_id
claim
evidence
conditions
variables
method
confidence
verification_status
related_nodes
```

例如逻辑上：

```text
Claim:
某有限阵风条件下，瞬态侧向力峰值高于对应稳态值。

Condition:
特定车型、阵风装置、偏航角、速度。

Evidence:
动态风洞测量。

Limitation:
不能直接推广到所有车辆与所有阵风。
```

同一个知识结论如果有多个来源支持：

```text
Concept
 ├─ Evidence A
 ├─ Evidence B
 └─ Evidence C
```

而不是复制三遍结论。

---

# 21. 证据等级

必须继承仓库现有 verification status，并额外建立“学习可信度”。

建议：

```text
E0 = metadata only
E1 = abstract verified
E2 = full text verified
E3 = independently supported by multiple primary sources
E4 = experimentally / numerically cross-validated across methods
```

注意：

- E3/E4 是本任务综合评级；
- 不能覆盖或修改 `sources/index.csv` 中原始 verification_status；
- 必须记录评级依据。

---

# 22. 矛盾不能被消除

当不同资料结论不同：

禁止：

> “综合来看，应该是……”

除非证据充分。

必须建立：

```text
Tension Node
```

例如：

```text
Finite gust result
        ↘
         disagreement
        ↗
Sinusoidal gust result
```

并分析可能原因：

- gust type；
- reduced frequency；
- vehicle geometry；
- Reynolds number；
- measurement method；
- force component；
- normalization；
- open/closed loop；
- steady baseline definition。

输出到：

```text
learning/open_questions.md
synthesis/disputed_findings.md
```

---

# 23. 方法演化图

`learning/method_evolution.md` 不能只是时间线。

需要同时表达：

```text
Historical road test
        ↓
Controlled full-scale gust
        ↓
Static-vs-dynamic comparison
        ↓
Moving model
        ↓
Dynamic gust generator
        ↓
Transient CFD
        ↓
Transient aerodynamic ROM
        ↓
CFD–vehicle dynamics coupling
        ↓
Closed-loop driver / controller
```

每一次方法升级都回答：

```text
旧方法解决了什么？
旧方法缺什么？
新方法增加了什么？
新方法代价是什么？
是否真正被验证？
```

---

# 24. 图谱输出

`knowledge_graph.md` 中使用 Mermaid 维护可读图谱。

不要一开始生成几百个节点的大图。

按层次拆分：

## Graph A：总体物理链

```mermaid
flowchart LR
A[Gust] --> B[Relative Wind]
B --> C[Transient Flow]
C --> D[Aerodynamic Loads]
D --> E[Vehicle Dynamics]
E --> F[Driver / Controller]
F --> G[Trajectory]
```

## Graph B：Gust taxonomy

## Graph C：Unsteady aerodynamics

## Graph D：Experimental methods

## Graph E：CFD methods

## Graph F：Aero–vehicle coupling

## Graph G：Validation

## Graph H：Method evolution

同时维护机器可读：

```text
nodes/*.csv
graph/edges.csv
```

Mermaid 图必须由节点/边数据生成或至少与其保持一致。

---

# 25. 论文学习深度

每篇资料划分：

## Pass 1：定位

回答：

```text
这篇资料在整个知识图谱中属于哪里？
解决了什么问题？
为什么值得保留？
```

---

## Pass 2：理解

回答：

```text
输入是什么？
方法是什么？
输出是什么？
关键结论是什么？
证据是什么？
限制是什么？
```

---

## Pass 3：研究级理解

仅对核心资料执行。

回答：

```text
如果重新做一次，实验/仿真该如何搭建？
最关键假设是什么？
最容易出错的地方是什么？
哪些结果可以迁移到当前博士后课题？
哪些不能？
它真正改变了领域中的什么？
```

---

# 26. 核心文献优先级

优先 Pass 3：

1. 历史源头；
2. 方法转折点；
3. 标准；
4. 被大量后续工作继承的方法；
5. 直接连接：
   - gust；
   - transient aerodynamic load；
   - vehicle dynamics；
   - validation；
6. 当前博士后课题可能直接采用的方法。

普通背景资料保持 Pass 1 或 Pass 2 即可。

---

# 27. 学习输出的写法

所有章节必须遵循：

## 第一层：直觉

先用工程语言解释：

> “它到底是什么？”

---

## 第二层：定义

写严谨术语和符号。

---

## 第三层：机制

解释：

> “为什么会这样？”

---

## 第四层：数学 / 方法

写方程、模型、测试方法。

所有公式必须确认定义和来源。

---

## 第五层：证据

列出：

> 哪些资料支持？

---

## 第六层：边界

回答：

> 什么时候不成立？

---

## 第七层：工程意义

回答：

> 对车辆气动开发有什么用？

---

## 第八层：研究意义

回答：

> 对“车辆侧风模拟及实验验证”下一步有什么启发？

---

# 28. equations.md

统一维护公式，避免不同章节重复产生不一致公式。

每条公式：

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

特别检查：

- yaw angle；
- relative wind；
- aerodynamic coefficients；
- reduced frequency；
- aerodynamic admittance；
- vehicle lateral dynamics。

如果资料中的公式尚未核验全文：

```text
FORMULA_PENDING_FULLTEXT
```

不得仅凭记忆补写。

---

# 29. glossary.md

建立中英术语表：

```text
英文
中文
缩写
定义
易混淆概念
source
```

重点避免：

```text
crosswind
gust
yaw
sideslip
side force
lateral force
yaw moment
aerodynamic derivative
admittance
transient
unsteady
quasi-steady
```

在不同领域含义混用。

---

# 30. open_questions.md

开放问题不是简单列“未来研究”。

必须从图谱中的断边产生。

例如：

```text
Natural road gust
        ?
        ↓
Wind-tunnel reproducibility
```

或者：

```text
Transient CFD
        ?
        ↓
Validated ROM
        ?
        ↓
Vehicle dynamics
```

每个 open question 记录：

```text
question
why_it_matters
known_evidence
missing_evidence
possible_method
related_sources
related_nodes
```

---

# 31. 与博士后课题的映射

在 `learning/12_research_frontier.md` 中持续建立：

```text
已有知识
    ↓
已验证方法
    ↓
尚未解决问题
    ↓
可形成博士后研究问题
```

重点服务：

> **车辆侧风模拟及实验验证**

但禁止为了迎合课题预设“研究空白”。

必须先由证据图谱暴露断点，再形成研究问题。

优先关注：

- realistic gust definition；
- natural gust → wind tunnel reconstruction；
- gust → transient aerodynamic response；
- steady vs transient validity boundary；
- CFD gust implementation；
- load phase / overshoot；
- CFD ↔ experiment validation；
- aerodynamic ROM；
- CFD → vehicle dynamics interface；
- crosswind robustness；
- geometry sensitivity under transient gust。

不研究气动噪声。

---

# 32. 每日执行逻辑

本任务建议作为现有资料采集任务之后的第二阶段执行。

顺序：

```text
06:00
TASK.md
资料搜索 / 核验 / 入库

        ↓

资料库发生变化

        ↓

LEARNING TASK
学习新增资料
更新知识节点
更新图谱
更新章节
更新开放问题
```

不要每天重写整个 learning 目录。

只做增量。

---

# 33. 每日学习日志

在：

```text
logs/YYYY-MM-DD.md
```

现有日志中追加：

```markdown
## Learning update

### New concepts
- ...

### Updated concepts
- ...

### New edges
- ...

### Deep-read sources
- ...

### Changed understanding
- ...

### New contradiction
- ...

### New open question
- ...

### Impact on research topic
- ...
```

---

# 34. 质量检查

每次更新必须检查：

## 34.1 Source integrity

所有技术结论是否有来源？

---

## 34.2 Definition integrity

同一术语是否出现多个不一致定义？

---

## 34.3 Coordinate integrity

力、力矩、角度是否混用坐标系？

---

## 34.4 Condition integrity

是否把特定工况结论写成普适结论？

---

## 34.5 Loop integrity

是否混淆：

```text
open-loop
closed-loop driver
closed-loop controller
```

---

## 34.6 Steady / transient integrity

是否把 steady yaw 结论误写成 transient gust 结论？

---

## 34.7 Evidence integrity

abstract evidence 是否被写成 full-text verified？

---

## 34.8 Graph integrity

每条边是否能解释：

> “为什么 A 和 B 有这条关系？”

---

# 35. 禁止事项

禁止：

1. 把文献摘要机械拼接成教材；
2. 按作者逐篇流水账；
3. 把引用次数当成科学正确性；
4. 自动把后发表论文视为更正确；
5. 未核验公式就写进 `equations.md`；
6. 未核验全文就填具体试验参数；
7. 把稳态偏航和瞬态阵风混为一谈；
8. 把 CFD 高保真模型等同于高可信度；
9. 忽略实验条件差异直接比较数字；
10. 为了让图谱完整而制造不存在的 edge；
11. 删除“不确定”“争议”“未知”；
12. 把分析者推断写成论文结论；
13. 保存无授权的版权全文；
14. 为了博士后课题刻意制造研究空白。

---

# 36. 第一阶段执行任务

第一次执行本任务时，不再做大规模外部搜索。

优先只学习仓库已有资料。

按以下顺序执行。

## Step 1

读取完整：

```text
sources/index.csv
sources/records/
history/timeline.md
citations/
synthesis/
```

---

## Step 2

根据已有资料生成：

```text
learning/learning_path.md
learning/glossary.md
learning/concept_map.md
```

先搭知识骨架。

---

## Step 3

优先完成：

```text
01_foundations.md
02_gust_and_environment.md
03_unsteady_aerodynamics.md
```

这是整个知识库的基础。

---

## Step 4

从已有 1953 → 当前时间线中识别：

```text
foundational papers
method-turning papers
validation papers
coupling papers
standard
```

并给出 Pass 1 / Pass 2 / Pass 3 优先级。

---

## Step 5

构建第一版：

```text
nodes/concepts.csv
nodes/methods.csv
nodes/variables.csv
graph/edges.csv
graph/knowledge_graph.md
```

---

## Step 6

对当前最重要的核心资料进行 Pass 2。

只有证据足够的少数核心资料进入 Pass 3。

---

## Step 7

更新：

```text
learning/method_evolution.md
learning/open_questions.md
learning/12_research_frontier.md
```

---

# 37. 第二阶段以后

当 learning 基础稳定后，再逐步：

```text
补公式
补设施
补 CFD 方法细节
补车辆动力学模型
补验证矩阵
补工程应用
```

每次新资料进入 `sources/`：

先问：

```text
它改变了什么知识？
```

而不是：

```text
它应该放在哪个文件夹？
```

如果新资料没有改变现有知识，只增加支持证据：

```text
Concept
   └── evidence +1
```

即可，不必新增重复章节。

---

# 38. 最终目标

随着长期维护，仓库应逐步形成四层结构：

```text
Layer 1
SOURCE
原始论文 / 标准 / 报告 / 数据

        ↓

Layer 2
EVIDENCE
atomic claims / experiment / simulation evidence

        ↓

Layer 3
KNOWLEDGE
concepts / equations / methods / relationships

        ↓

Layer 4
UNDERSTANDING
physical mechanism / method evolution / gaps / research questions
```

最终用户应该能够从一个问题出发：

> “为什么车辆进入阵风时横摆力矩不能总用稳态偏航结果预测？”

沿知识图谱看到：

```text
Quasi-steady assumption
        ↓
Finite gust
        ↓
Transient separation
        ↓
Pressure redistribution
        ↓
Yaw moment response
        ↓
Overshoot / phase lag
        ↓
Dynamic experiment
        ↓
CFD
        ↓
Vehicle dynamics
        ↓
Validation
        ↓
Relevant papers
```

也应该能反方向从某篇论文出发看到：

```text
Paper
   ↓
Method
   ↓
Claim
   ↓
Evidence
   ↓
Concept
   ↓
Related concepts
   ↓
Research question
```

这才是本任务所定义的“知识图谱”。

---

# 39. 执行原则总结

始终遵循：

> **先理解，再连接；先证据，再总结；先基础，再前沿。**

以及：

> **Synthesis is not summary.**

本项目的 learning 层不追求“资料最多”，而追求：

```text
概念清楚
关系清楚
证据清楚
条件清楚
未知也清楚
```

当资料数量继续增加时，优先让知识图谱变得更准确，而不是让文字变得更长。
