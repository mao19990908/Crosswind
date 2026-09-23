# 车辆瞬态侧风（阵风）知识库：Codex 长期执行任务书

> 本文交给在用户 Windows 电脑上运行、可以访问 `D:\GEELY\Crosswind` 且已获准访问目标 GitHub 仓库的 Codex 执行。首次执行先建库和系统回溯历史，此后每天按计划增量收集。以下路径与时间均按用户本机解释。

---

## 1. 任务目标与边界

建立可溯源、可检索、可持续更新的**道路车辆瞬态侧风／阵风（transient crosswind / crosswind gust）**知识库，重点研究：

**阵风输入 → 非定常气动载荷 → 车辆横向／横摆／侧倾响应 → 驾驶员或控制器修正**

并直接服务于博士后课题“**车辆侧风模拟及实验验证**”。

研究对象以乘用车为主；商用车、客车、列车等仅在方法具有明显可迁移性或可作为对照时纳入。不以气动噪声为研究主题。

### 1.1 核心问题

1. 阵风的时间结构、空间结构、幅值、持续时间、梯度和湍流特征如何影响瞬态侧向力、横摆力矩、升力及侧倾力矩？
2. 非定常气动力如何进一步影响横摆角速度、质心侧偏角、横向加速度、侧倾、车道偏移和驾驶员修正？
3. 固定偏航角稳态结果在什么条件下可以作为阵风响应的准稳态近似，在什么条件下失效？
4. 风洞、移动模型、整车道路试验和 CFD 对同一阵风事件的结果能否相互验证？
5. 如何构建能够用于整车动力学计算的瞬态气动降阶模型、气动导纳或响应函数？
6. 真实道路阵风与标准风发生器工况之间的差异有多大？
7. 当前车辆侧风模拟与实验验证中尚未解决的关键问题是什么？

### 1.2 必须严格区分的概念

- **瞬态阵风 ≠ 固定偏航角稳态侧风。**
- 区分：
  - 车辆驶入有限长度侧风区；
  - step gust；
  - pulse gust；
  - ramp gust；
  - sinusoidal / periodic gust；
  - stochastic / turbulent gust；
  - 自然道路阵风；
  - 会车、桥梁、隧道出口等特殊瞬态横向扰动。
- 固定偏航角研究仅作为：
  - 气动系数基线；
  - 准稳态模型输入；
  - 瞬态结果对比；
  - 非定常效应识别。
- 不得将固定偏航角结果直接写成阵风结论。
- 严格区分：
  - 瞬时相对来流偏航角；
  - 车辆航向角；
  - 车辆质心侧偏角。
- 每篇资料记录：
  - 坐标系；
  - 正负号约定；
  - 力矩参考点；
  - 气动力／力矩系数归一化方式。
- 区分：
  - **open-loop**：锁定转向或无驾驶员输入；
  - **closed-loop**：驾驶员／控制器参与。
- 不得混合开放环与闭环工况下的车道偏移、横摆响应和驾驶员修正结论。

---

## 2. 总体检索原则：从历史源头沿方法演化一直追到当前

本知识库不能只做关键词随机检索。

必须采用：

**历史回溯 + 引文链追踪 + 方法谱系追踪 + 当前增量更新**

四条路线并行。

### 2.1 历史路线

首次建库时：

1. 从目前可核查的 1970 年代资料开始；
2. 沿参考文献继续向更早资料追溯；
3. 找到更早资料后验证原文；
4. 不预设“第一篇论文”；
5. 每发现更早资料，更新 `history/timeline.md`；
6. 明确记录所覆盖数据库、检索式、检索日期和搜索范围。

### 2.2 向后演化路线

对每篇关键历史文献：

- 查其 references；
- 查 cited-by；
- 查作者后续工作；
- 查采用相同方法、设备、阵风模型或评价指标的后续工作；
- 一直追踪到当前年份。

不能只记录“某篇论文引用了谁”，还要识别：

- 方法继承；
- 方法改进；
- 方法分叉；
- 实验装置继承；
- 数据复用；
- 结论冲突；
- 理论替代；
- 工程标准化。

目标是形成：

> **道路车辆瞬态侧风研究的方法演化树，而不仅是文献列表。**

---

## 3. 已确认的早期时间线切入点

以下为当前已发现的重要历史节点，不宣称为绝对最早工作。

### 1971

Mahig，SAE 710287。

关注车辆受到突发风扰／外部脉冲后的横向稳定性及悬架响应。

<https://doi.org/10.4271/710287>

### 1973

Hucho 与 Emmelmann，SAE 730232。

研究侧风阵风条件下车辆气动导数的理论预测。

<https://doi.org/10.4271/730232>

### 1979

美国 DOT：

*Development of Aerodynamic Disturbance Test Procedures*

重点查：

- DOT-HS-805-078
- DOT-HS-805-079

涉及全尺寸侧风扰动试验设施与测试方法。

<https://trid.trb.org/View/143777>

<https://trid.trb.org/View/144116>

### 1980

Klein 与 Hogue，SAE 800848。

全尺寸阵风试验及分析预测。

<https://doi.org/10.4271/800848>

### 1996

#### ISO 12021-1:1996

`Road vehicles — Sensitivity to lateral wind — Part 1: Open-loop test method using wind generator input`

该版本现已撤销，仅作为标准发展历史保存。

#### Macklin, Garry & Howell，SAE 960674

*Comparing Static and Dynamic Testing Techniques for the Crosswind Sensitivity of Road Vehicles*

<https://doi.org/10.4271/960674>

这是知识库中的重要方法节点：

- 比较 static yaw test；
- 与 moving model 穿越模拟 gust 的 dynamic test；
- 重点关注什么时候稳态偏航测试无法代表瞬态阵风载荷。

该文必须作为：

**steady yaw → dynamic gust**

方法转折点之一进行引文链追踪。

### 1997—1998

重点追踪：

- SAE 970135：阵风中的 shear / turbulence；
- SAE 970404：瞬态侧风数值分析；
- SAE 980392：乘用车瞬态阵风气动力。

<https://doi.org/10.4271/970135>

<https://doi.org/10.4271/970404>

<https://doi.org/10.4271/980392>

### 2010

#### ISO 12021:2010

`Road vehicles — Sensitivity to lateral wind — Open-loop test method using wind generator input`

截至 **2026-09-23**：

- ISO 12021-1:1996：Withdrawn；
- ISO 12021:2010：Current / Published；
- ISO 官方记录显示该版本于 2023 年复审后确认继续有效。

官方页面：

<https://www.iso.org/standard/53602.html>

ISO 同时明确指出：该标准规定的试验条件并不代表真实驾驶条件，而是用于获得车辆对横向风动态响应的评价量。

因此知识库中必须严格区分：

**ISO 标准风发生器测试**

与：

**真实道路自然阵风。**

### 2010 年前后以后

重点追踪方法转折：

- transient CFD；
- URANS；
- DES / DDES；
- LES；
- oscillating / sinusoidal gust；
- step gust；
- moving vehicle / moving model；
- aerodynamic admittance；
- reduced-order aerodynamic models；
- CFD → vehicle dynamics 单向耦合；
- fully coupled CFD–vehicle dynamics；
- 驾驶员模型；
- 主动控制；
- 自然道路阵风测量；
- 高保真整车验证。

不能预先假定具体年份，必须通过文献证据构建完整时间线。

---

## 4. 分类体系

允许随研究发展调整，但修改必须留痕。

| 代码 | 类别 | 主要内容 |
|---|---|---|
| A | 历史与定义 | 概念源流、术语演变、核心论文引文链、阵风与定常偏航边界 |
| B | 阵风输入与环境 | 阵风波形、风区尺度、剪切、湍流、自然风、道路场景 |
| C | 非定常气动理论 | 相对风、气动导数、准稳态／非准稳态、相位滞后、overshoot |
| D | 气动系统响应模型 | aerodynamic admittance、frequency response、weighting function、convolution、ROM |
| E | 车辆动力学理论 | 单轨、多轨、多体、轮胎、悬架、横摆、侧倾、驾驶员和控制器 |
| F | 风洞实验 | 静态模型、移动模型、阵风发生器、主动栅格、风场与压力／PIV 测量 |
| G | 整车／道路实验 | 风机阵列、有限风区、自然阵风、道路测试、整车状态测量 |
| H | 气动 CFD | transient inlet、moving/sliding mesh、URANS、DES、DDES、LES |
| I | 气动—车辆动力学耦合 | CFD→车辆动力学、单向／双向耦合、坐标转换、时间同步 |
| J | 验证与评价 | 风场、载荷、运动三级验证，响应峰值、时滞、车道偏移、不确定度 |
| K | 标准与规范 | ISO、SAE、国家标准、行业方法 |
| L | 数据与开放资源 | 数据集、公开模型、代码、实验数据库 |
| M | 工程应用 | 车身造型、底盘、主动控制、稳健性和工程优化 |

若出现无法合理放入现有类别且反复出现的新方向：

1. 写入 `taxonomy_change_log.md`；
2. 给出至少 3 个代表性来源；
3. 说明为什么现有分类不足；
4. 给出旧分类到新分类的映射；
5. 再修改 taxonomy。

一篇资料可有多个标签，但只能有一个规范化主记录。

---

## 5. 阵风参数标准化

这是知识库的核心要求之一。

凡研究包含阵风输入，应尽可能提取以下量。

### 5.1 基础运动参数

- 车辆速度 \(U_v\)
- 纵向来流速度
- 横向风速 \(U_g\)
- 合成相对风速
- 瞬时相对来流偏航角 \(\beta(t)\)

基本关系需记录作者实际采用的定义。

常见几何关系可整理为：

\[
\beta(t)=\tan^{-1}\left(\frac{U_g(t)}{U_v(t)}\right)
\]

但不能用该公式覆盖作者采用不同坐标系或存在纵向风脉动的情况。

### 5.2 时间参数

- gust rise time \(T_r\)
- gust duration
- gust decay time
- gust period
- gust frequency \(f_g\)
- vehicle residence time in gust
- sampling frequency
- simulation time step

### 5.3 空间参数

- gust-zone length \(L_g\)
- gust-zone width
- vertical extent
- longitudinal gradient
- lateral gradient
- vertical shear
- wind-generator distance
- vehicle length \(L_\mathrm{veh}\)

### 5.4 推荐无量纲量

若资料足够，统一计算或记录：

\[
t^*=\frac{tU_v}{L_\mathrm{veh}}
\]

\[
L_g^*=\frac{L_g}{L_\mathrm{veh}}
\]

以及文献定义的：

- reduced frequency；
- Strouhal number；
- gust frequency parameter；
- gust gradient parameter。

必须保留**原作者定义**，不能因公式名字相同就假定定义一致。

### 5.5 湍流／自然风参数

记录：

- turbulence intensity；
- integral length scale；
- power spectral density；
- coherence；
- vertical wind profile；
- shear；
- gust factor；
- atmospheric stability（若有）；
- measurement height；
- terrain / road environment。

---

## 6. 非定常气动理论必须重点追踪的主线

### 6.1 Quasi-steady model

研究：

- 稳态偏航气动系数是否可以映射到瞬时偏航角；
- 准稳态模型在哪些工况有效；
- 什么时候出现明显偏差。

### 6.2 Non-quasi-steady behaviour

记录：

- force overshoot；
- moment overshoot；
- undershoot；
- phase lag；
- hysteresis；
- transient separation；
- vortex development；
- wake memory effect。

### 6.3 Aerodynamic derivative

追踪：

- aerodynamic derivatives 的历史定义；
- 提取方法；
- 可识别性；
- 对车辆动力学模型的作用。

### 6.4 Aerodynamic admittance

作为独立理论路线收集：

- aerodynamic admittance；
- aerodynamic transfer function；
- frequency response function；
- weighting function；
- convolution model；
- impulse response；
- spectral response。

重点研究：

> 随机／湍流阵风如何通过气动系统响应变成车辆载荷时程。

### 6.5 Reduced-order model

收集：

- transfer-function model；
- state-space model；
- convolution model；
- POD / DMD 类降阶方法；
- surrogate model；
- system identification；
- machine-learning ROM。

必须区分：

**物理可解释模型**

与：

**纯数据拟合模型。**

---

## 7. 车辆动力学主线

重点提取：

### 7.1 模型复杂度

- bicycle model；
- four-wheel model；
- multibody model；
- suspension model；
- roll dynamics；
- tyre model；
- steering system；
- driver model。

### 7.2 输入

- aerodynamic side force；
- yawing moment；
- rolling moment；
- vertical force；
- steering input；
- road disturbance。

### 7.3 输出

优先记录：

- yaw rate；
- lateral acceleration；
- sideslip angle；
- roll angle；
- steering wheel angle；
- steering correction；
- lateral displacement；
- lane deviation；
- trajectory deviation。

### 7.4 开环／闭环

每个结果必须注明：

```text
open_loop
closed_loop_driver
closed_loop_controller
autonomous_control
```

不同类型不得直接合并比较。

---

## 8. 实验资料需要提取的复现信息

### 8.1 风洞实验

记录：

- 风洞类型；
- test-section 尺寸；
- blockage ratio；
- turbulence level；
- boundary layer；
- moving ground；
- wheel rotation；
- 模型比例；
- Reynolds number；
- 模型质量与惯量；
- mounting method；
- balance frequency response；
- sampling rate；
- filtering；
- pressure measurement；
- PIV / flow measurement；
- synchronization；
- uncertainty。

### 8.2 阵风产生设备

重点分类：

- side fan array；
- wind generator；
- active grid；
- shutter；
- moving model through crossflow；
- moving vehicle through fixed wind zone；
- oscillating vane；
- rotating blade；
- transient inlet。

提取：

- 风速空间分布；
- rise length；
- gust edge thickness；
- vertical profile；
- uniformity；
- turbulence intensity；
- repeatability；
- calibration method。

### 8.3 道路／整车试验

记录：

- 场地；
- 风发生器布置；
- 车辆速度控制；
- steering constraint；
- driver participation；
- IMU；
- GPS / RTK；
- wheel-force measurement；
- steering torque；
- wind measurement；
- sampling rate；
- road slope；
- temperature；
- ambient wind；
- repeat runs；
- uncertainty。

---

## 9. CFD 资料需要提取的复现信息

每篇 CFD 工作尽可能记录：

### 9.1 几何与域

- vehicle geometry；
- geometry simplification；
- rotating wheels；
- moving ground；
- domain dimensions；
- blockage；
- reference area；
- moment reference point。

### 9.2 网格

- mesh type；
- cell count；
- prism layers；
- \(y^+\)；
- wake refinement；
- gust-boundary refinement；
- mesh-independence test。

### 9.3 湍流模型

明确区分：

- RANS；
- URANS；
- DES；
- DDES；
- IDDES；
- LES；
- hybrid LES。

### 9.4 时间离散

记录：

- physical time step；
- CFL；
- inner iteration；
- residual criteria；
- number of gust events；
- averaging method；
- time-step independence。

### 9.5 阵风实现方式

重点记录：

- transient inlet；
- spatially varying inlet；
- moving mesh；
- moving vehicle；
- moving gust region；
- source term；
- synthetic turbulence；
- precursor simulation；
- mapped turbulence。

### 9.6 结果

除气动力外必须尽可能提取：

- \(C_Y(t)\)
- \(C_N(t)\)
- \(C_L(t)\)
- rolling moment coefficient
- pressure distribution
- vortex topology
- separation topology
- wake response
- phase lag
- peak value
- rise time
- relaxation time

---

## 10. CFD—车辆动力学耦合分类

单独建立耦合谱系。

### Level 0：稳态映射

稳态偏航角 → 气动力系数表 → Vehicle Dynamics。

### Level 1：准稳态瞬态

瞬时相对风角 → 查稳态气动力数据库 → 车辆动力学。

### Level 2：预计算瞬态气动

Transient CFD → load time series → Vehicle Dynamics。

### Level 3：ROM 耦合

CFD / experiment → transfer function / ROM → Vehicle Dynamics。

### Level 4：在线单向耦合

车辆状态变化实时改变 CFD 输入，但车辆运动不改变 CFD 几何运动或反馈有限。

### Level 5：Fully coupled simulation

CFD 与 vehicle dynamics 双向实时交换：

- vehicle attitude；
- velocity；
- aerodynamic forces；
- moments。

每篇耦合研究注明所属 Level。

---

## 11. 验证体系：必须区分三级验证

### Level A：阵风风场验证

验证：

- \(U_g(t)\)
- spatial profile
- shear
- turbulence
- rise time
- gust-zone length

### Level B：气动力验证

验证：

- side force；
- yaw moment；
- roll moment；
- pressure；
- phase；
- peak；
- transient waveform。

### Level C：整车运动验证

验证：

- yaw rate；
- lateral acceleration；
- sideslip；
- steering correction；
- lateral displacement；
- lane deviation。

知识库必须明确：

> “CFD 与风洞气动力一致”不能自动视为“车辆侧风稳定性已验证”。

---

## 12. 检索数据库与信息源

### 12.1 强制资料类型分类

知识库中的“资料”不得默认等同于论文。所有来源必须赋予明确的 `source_type`，并在 `sources/index.csv`、单篇记录和每日统计中保留。

| source_type | 含义 | 主要价值 |
|---|---|---|
| `journal_article` | 同行评议期刊论文 | 理论、CFD、实验、方法演进与最新研究 |
| `sae_technical_paper` | SAE Technical Paper / SAE 技术论文 | 汽车工程原始方法、整车试验、工程应用；侧风领域重点来源 |
| `conference_paper` | 其他会议论文 | 新方法、阶段性结果、设备与工程案例 |
| `standard` | ISO、GB/T、SAE 等正式标准 | 试验工况、测量量、评价方法、术语与规范 |
| `standard_draft` | 标准草案、征求意见稿 | 理解标准形成过程，仅作辅助证据，不替代正式版本 |
| `government_report` | 政府部门技术报告 | 早期整车试验、设施开发、测试流程、原始工程数据 |
| `institutional_report` | 研究机构／实验室技术报告 | 设施、方法、项目成果和公开技术路线 |
| `project_report` | 公开科研／产业项目报告 | 跨机构成果、工程验证与方法集成 |
| `doctoral_thesis` | 博士论文 | 方法细节、实验装置、CFD 设置、参数研究、文献谱系 |
| `master_thesis` | 硕士论文 | 特定问题的详细实现和补充数据 |
| `book` | 专著 | 历史、理论框架、车辆空气动力学基础 |
| `book_chapter` | 专著章节 | 专题综述或特定理论整理 |
| `review_article` | 综述论文 | 发现文献、识别研究路线，不优先作为原始结论证据 |
| `dataset` | 公开数据集 | CFD／实验验证、重复分析、基准数据 |
| `code_repository` | 公开代码／模型仓库 | 方法复现、模型实现、数据处理 |
| `facility_documentation` | 风洞、侧风发生器、移动模型等设施资料 | 理解设备能力、风场质量和实验约束 |
| `manufacturer_technical_document` | OEM／供应商公开技术资料 | 工程开发流程、设备应用和产品化信息 |
| `patent` | 专利 | 侧风发生装置、控制系统、工程方案线索 |
| `regulatory_document` | 法规、测试程序、监管机构文件 | 法规背景、测试要求和道路安全评价 |
| `web_primary_source` | 官方机构、作者或项目原始网页 | 补充状态、版本、项目说明和下载入口 |
| `secondary_web_source` | 二手网页、聚合页面 | 仅作线索，不作为未经核验的最终证据 |

允许新增类型，但必须在 `taxonomy_change_log.md` 中说明。

### 12.2 资料来源优先原则

对于同一研究问题，不机械规定“论文最高”，而应根据用途优先寻找最接近原始证据的资料：

- **试验方法／工况定义**：正式标准 > 原始技术报告 > 原始论文 > 二手综述；
- **历史设施与整车阵风试验**：政府／研究机构报告、SAE Technical Paper、学位论文优先；
- **理论与模型发展**：原始期刊论文、SAE Technical Paper、博士论文优先；
- **CFD 可复现细节**：原始论文 + 学位论文 + 补充材料优先；
- **最新研究进展**：最新原始期刊／会议论文优先；
- **验证数据**：公开数据集、原始实验报告、正式论文优先；
- **标准状态**：ISO、国家标准平台等官方来源优先；
- **工程应用**：OEM／研究机构公开技术资料用于描述其公开内容，不替代独立验证。

综述、教材和二手网页主要用于发现关键词、作者、历史资料和引用关系；一旦找到原始来源，应回到原始来源核验。

### 12.3 资料类型覆盖要求

长期收集不能只累计 `journal_article`。`database_coverage.md` 和 README 应定期统计各类来源数量，至少包括：

```text
journal_article
sae_technical_paper
conference_paper
standard
government_report
institutional_report
doctoral_thesis
master_thesis
dataset
facility_documentation
```

若某一类别长期为 0，必须判断是：
1. 确实不存在；
2. 数据库覆盖不足；
3. 检索词不合适；
4. 权限受限。

不得在未检索前默认“该类资料没有”。

### 12.4 推荐检索重点

优先级：

### 第一优先级：原始来源

- SAE Mobilus
- ScienceDirect
- Springer
- Wiley
- Taylor & Francis
- ASME
- ISO
- TRID
- NHTSA / DOT
- government reports
- university repositories
- doctoral theses

### 第二优先级：文献发现

- Crossref
- OpenAlex
- Semantic Scholar
- Google Scholar
- Web of Science（若可访问）
- Scopus（若可访问）
- CNKI

### 第三优先级：线索

- ResearchGate
- conference pages
- institutional publication lists
- general web search

第三方聚合页面只能作为线索，不得未经核验写成事实。

需要进行：

- 英文检索；
- 中文检索；
- 必要时德文历史检索；
- 作者名追踪；
- DOI 追踪；
- 参考文献追踪；
- cited-by 追踪。

---

## 13. 起始检索式

按不同数据库语法调整。

```text
(vehicle OR automobile OR passenger car)
AND
(crosswind gust OR transient crosswind OR lateral wind disturbance)
AND
(yaw response OR side force OR yawing moment)
```

```text
(road vehicle)
AND
(gust response OR crosswind sensitivity)
AND
(wind tunnel OR moving model OR full-scale OR CFD OR multibody)
```

```text
(vehicle)
AND
(aerodynamic admittance OR gust response OR aerodynamic derivative)
AND
(crosswind)
```

```text
(vehicle)
AND
(transient aerodynamic OR unsteady aerodynamic)
AND
(crosswind OR gust)
```

```text
车辆
AND
(侧风阵风 OR 瞬态侧风 OR 侧风敏感性)
AND
(试验 OR 仿真 OR 横摆 OR 气动力)
```

```text
汽车
AND
(侧风 OR 阵风)
AND
(横向稳定性 OR 横摆响应 OR 风洞 OR CFD)
```

---

## 14. 引文关系数据库

新增：

```text
citations/
├─ citation_edges.csv
├─ citation_graph.md
└─ method_lineages.md
```

### citation_edges.csv

至少包含：

```text
source_id,target_id,relation,verified,note
```

`relation` 可使用：

```text
references
cited_by
method_inherits
method_extends
facility_inherits
data_reuses
supports
contradicts
standardizes
```

### method_lineages.md

分别维护方法谱系，例如：

```text
Static yaw
  ↓
Moving-model gust test
  ↓
Transient CFD
  ↓
LES / hybrid LES
  ↓
CFD–vehicle dynamics coupling
  ↓
Road-validated transient model
```

实际内容必须依据资料构建，不能预先把上述示例当成最终结论。

---

## 15. 检索覆盖率账本

新增：

```text
search/
├─ search_ledger.csv
├─ query_library.md
└─ database_coverage.md
```

### search_ledger.csv

至少：

```text
date,database,query,year_from,year_to,result_count,screened,included,excluded,notes
```

### database_coverage.md

需要能回答：

- 哪个数据库已经系统搜索？
- 哪个年份段已经覆盖？
- 哪些关键词已经使用？
- 搜索到第几页／第多少条？
- 哪些年代资料少是真的资料少，哪些只是尚未搜索完成？
- 哪些数据库因权限无法访问？

不得把“没搜到”直接写成“没有研究”。

---

## 16. 文献筛选规则

### 纳入

包括：

- gust generation；
- gust measurement；
- transient aerodynamics；
- transient crosswind experiment；
- crosswind vehicle dynamics；
- aerodynamic derivative；
- aerodynamic admittance；
- moving model；
- full-scale gust；
- road test；
- CFD；
- CFD–vehicle dynamics coupling；
- validated reduced-order models。

### 条件纳入

固定偏航角研究仅在：

- 用作 transient baseline；
- 提供 quasi-steady coefficients；
- 用于比较 steady / unsteady；
- 解释 transient flow mechanism；

时纳入。

标签：

```text
steady_baseline
```

### 排除

- 仅做定常阻力优化；
- 与瞬态侧风没有实际关联；
- 以 wind noise 为主要主题；
- 与道路车辆无方法迁移价值的飞行器研究；
- 无法确认出处的网页二手结论。

存疑资料：

```text
candidate
```

不得为了扩大数量强行纳入。

---

## 17. 去重与版本管理

优先 DOI 去重。

其次：

- title；
- authors；
- year；
- publisher。

同一研究若存在：

- conference paper；
- technical report；
- journal paper；
- thesis；
- preprint；

建立：

```text
version_of
```

关系。

原则：

> 一项研究只建立一个主记录，但保留所有合法版本和引用关系。

---

## 18. 每篇文献结构化记录

路径：

```text
sources/records/<stable_id>.md
```

至少包含：

### Bibliographic

- ID
- Title
- Authors
- Year
- Journal / Conference
- DOI
- URL
- GB/T 7714 citation
- BibTeX

### Access

- access_status
- full_text_source
- copyright_status

### Verification

- metadata_only
- abstract_verified
- full_text_verified

### Research classification

- source_type
- primary_category
- secondary_categories
- tags

`source_type` 必须从第 12.1 节的规范类型中选择。若同一研究存在不同发布形态，应分别建记录并建立版本关系。例如：

- SAE 正式 Technical Paper → `sae_technical_paper`
- 博士论文后发表的期刊论文 → 分别建记录，并以 `version_of` / `derived_from` 关联
- ISO 草案 → `standard_draft`
- 正式 ISO → `standard`

### Physical problem

- vehicle type
- scale
- vehicle speed
- wind speed
- gust type
- gust spatial scale
- gust temporal scale
- turbulence
- yaw definition

### Method

- theory
- experiment
- CFD
- vehicle dynamics
- coupled simulation

### Coordinate system

- axes
- force directions
- moment directions
- reference point
- reference area
- normalization

### Results

记录：

- key quantities
- peak
- phase
- overshoot
- response delay
- relaxation
- vehicle response

### Validation

- wind-field validation
- aerodynamic validation
- vehicle-motion validation

### Evidence

- supporting figure
- table
- page
- equation

### Limitations

必须优先使用作者明确写出的 limitation。

模型推断的局限必须标记：

```text
analyst_inference
```

### Relevance

说明：

> 对“车辆侧风模拟及实验验证”课题有什么直接价值？

### Follow-up

记录：

- references to chase
- cited-by to chase
- unresolved questions
- missing full text

---

## 19. 证据等级

不要给论文打主观“好／差”分数。

只记录证据性质。

### access_level

```text
metadata_only
abstract
full_text
```

### evidence_type

```text
theory
steady_wind_tunnel
dynamic_wind_tunnel
moving_model
CFD
coupled_simulation
full_scale_test
road_test
natural_wind_measurement
standard
```

### validation_level

```text
none
internal_consistency
compared_with_CFD
compared_with_wind_tunnel
compared_with_full_scale
road_validated
multi_level_validated
```

### verification_status

```text
unverified
metadata_verified
abstract_verified
full_text_verified
cross_source_verified
```

以后所有综合结论都必须能追溯到相应 evidence_type 和 verification_status。

---

## 20. sources/index.csv

至少包含：

```text
id
title
authors
year
doi
url
source_type
publisher_or_institution
report_or_standard_number
primary_category
secondary_categories
tags
gust_type
method
vehicle_class
access_status
evidence_type
validation_level
verification_status
added_date
last_checked
```

UTF-8 编码。

记录 ID 永久稳定，后续不得因文件整理随意重命名。

---

## 21. 综合研究文件

新增：

```text
synthesis/
├─ state_of_the_art.md
├─ research_gaps.md
├─ disputed_findings.md
├─ gust_parameter_matrix.csv
├─ experiment_matrix.csv
├─ simulation_matrix.csv
├─ validation_matrix.csv
├─ coupled_methods_matrix.csv
└─ research_hypotheses.md
```

### state_of_the_art.md

按方法演化，而不是按论文流水账撰写。

### disputed_findings.md

记录：

- 相互矛盾结论；
- 可能原因；
- 不同试验条件；
- 是否得到后续验证。

### research_gaps.md

研究空白不能只写“很少有人研究”。

每条 gap 必须包括：

1. 现有证据；
2. 已经解决到什么程度；
3. 尚未解决什么；
4. 为什么重要；
5. 如何验证；
6. 对博士后课题的价值。

### research_hypotheses.md

把研究空白进一步写成：

> **可通过 CFD、风洞或道路试验验证的假设。**

---

## 22. 仓库结构

目标 GitHub：

`https://github.com/mao19990908/Crosswind`

本机：

```text
D:\GEELY\Crosswind
```

GitHub 与本机是同一 Git 仓库的远端和工作树。

建议最终结构：

```text
Crosswind/
├─ README.md
├─ TASK.md
├─ history/
│  └─ timeline.md
├─ taxonomy.md
├─ taxonomy_change_log.md
│
├─ search/
│  ├─ search_ledger.csv
│  ├─ query_library.md
│  └─ database_coverage.md
│
├─ citations/
│  ├─ citation_edges.csv
│  ├─ citation_graph.md
│  └─ method_lineages.md
│
├─ sources/
│  ├─ index.csv
│  └─ records/
│
├─ notes/
│  ├─ theory/
│  ├─ experiments/
│  ├─ simulation/
│  ├─ vehicle_dynamics/
│  └─ coupling/
│
├─ standards/
│
├─ datasets/
│
├─ synthesis/
│  ├─ state_of_the_art.md
│  ├─ research_gaps.md
│  ├─ disputed_findings.md
│  ├─ gust_parameter_matrix.csv
│  ├─ experiment_matrix.csv
│  ├─ simulation_matrix.csv
│  ├─ validation_matrix.csv
│  ├─ coupled_methods_matrix.csv
│  └─ research_hypotheses.md
│
├─ logs/
│  └─ YYYY-MM-DD.md
│
└─ .gitignore
```

---

## 23. Git 与双份保存规则

每天：

1. 检查本机仓库；
2. fetch / pull；
3. 检查冲突；
4. 开始资料工作；
5. 保存文件；
6. validate；
7. commit；
8. push；
9. 核对：
   - local `HEAD`
   - remote commit SHA
10. 确认一致后才可记录：

```text
local_synced = true
remote_synced = true
```

若 push 失败：

- 本机提交必须保留；
- 日志记录失败原因；
- 下一次运行优先重试；
- 不得写“已双份保存”。

禁止提交：

- GitHub token；
- cookie；
- password；
- 吉利内部数据；
- 吉利内部模型；
- 未授权内部文档；
- 未授权版权 PDF；
- 大型 CFD 计算文件。

---

## 24. 全文与版权

原则：

- 开放许可全文可以合法保存；
- 用户合法拥有的个人副本可在本地用于研究；
- GitHub 只保存允许公开或允许存储的文件；
- 受限论文不得因 Codex 可以访问就自动上传 GitHub。

对受限全文：

只保存：

- metadata；
- citation；
- DOI；
- abstract 范围内信息；
- 自己整理的研究笔记；
- figure / page reference；
- access status。

不得批量复制受版权保护的正文。

---

## 25. 每日 06:00 自动运行

时间：

**每天 06:00 Asia/Shanghai**

Windows 本机优先。

调度必须能够访问：

```text
D:\GEELY\Crosswind
```

并具有 GitHub push 权限。

如果电脑 06:00 未开机：

启用：

> 错过计划后尽快执行。

同一自然日最多自动执行一次。

---

## 26. 每日额度

目标：

**每天使用可用周额度总量的最多 12%。**

原则：

- 12% 是目标上限；
- 不得超支；
- 不要求强行耗满；
- 一周最多 84%；
- 预留约 16%。

每日开始：

记录：

```text
weekly_quota_before
```

每日结束：

记录：

```text
weekly_quota_after
daily_consumption
weekly_consumption
```

如果平台无法可靠读取周额度：

不得假装可以严格控制 12%。

日报写：

```text
quota_status = unavailable
```

并限制自动扩量，优先进行高价值任务。

---

## 27. 每日任务优先级

每日不是随机搜新论文。

执行顺序：

### Priority 1

补齐历史引文链断点。

### Priority 2

追踪已有核心论文 cited-by。

### Priority 3

补齐理论／实验／CFD 方法谱系。

### Priority 4

搜索最近新发表资料。

### Priority 5

补全文、验证旧记录。

### Priority 6

更新 synthesis。

原则：

> **先提高证据质量，再追求文献数量。**

---

## 28. 每日运行流程

```text
01 检查周额度
02 检查 Git 状态
03 同步远端
04 读取昨日断点
05 检查 timeline 缺口
06 检查 citation graph 缺口
07 执行历史追踪
08 执行 cited-by 追踪
09 执行最新文献检索
10 下载／读取可合法获取资料
11 建立结构化 records
12 更新 index
13 更新 citation_edges
14 更新 search_ledger
15 更新 method_lineages
16 更新 timeline
17 更新 synthesis
18 去重
19 校验 DOI / author / year
20 写日报
21 git commit
22 git push
23 校验本地／远端 SHA
```

---

## 29. 每日日报

路径：

```text
logs/YYYY-MM-DD.md
```

至少包括：

### Search

- databases
- queries
- time range
- candidates
- screened
- included
- excluded

同时按 `source_type` 统计当天新增资料，例如：

```text
journal_article = 4
sae_technical_paper = 2
standard = 1
government_report = 1
doctoral_thesis = 1
dataset = 0
```

如果当天只新增普通论文，也应检查是否仍有未覆盖的标准、技术报告、学位论文、数据集或设施资料，而不是机械扩大论文数量。

### Historical progress

今天向前追到哪里？

今天向后追到哪里？

### Citation progress

新增多少 citation edges？

哪些关键文献还没完成 cited-by？

### Most valuable findings

每天最多重点写 3—5 条。

每条必须附 source ID。

### Contradictions

记录：

- 新出现矛盾；
- 尚未解决的问题。

### Research gaps

是否新增或修改研究空白？

### Quota

```text
before
after
daily
weekly_total
```

### Git

```text
commit_SHA
push_status
remote_SHA
```

### Next breakpoint

下一次从哪里继续。

---

## 30. 阶段目标

### Phase I：历史与知识地图

目标：

- 找到早期源头；
- 建立 timeline；
- citation graph；
- terminology；
- taxonomy；
- method lineages。

不要急着写综述结论。

### Phase II：理论体系

形成：

- quasi-steady；
- non-quasi-steady；
- aerodynamic derivative；
- aerodynamic admittance；
- transient response；
- ROM。

### Phase III：实验体系

系统比较：

- static yaw；
- gust generator；
- moving model；
- full-scale；
- road test；
- natural gust measurement。

### Phase IV：CFD

形成：

- transient boundary methods；
- moving vehicle；
- turbulence model；
- grid；
- time step；
- validation；
- gust construction。

### Phase V：气动—车辆动力学耦合

建立：

- quasi-steady；
- one-way；
- ROM；
- fully coupled；

完整谱系。

### Phase VI：综合

最终输出：

1. 研究现状；
2. 方法演化；
3. 理论体系；
4. 实验体系；
5. CFD 体系；
6. 验证体系；
7. 真实道路与标准试验差异；
8. 研究争议；
9. 研究空白；
10. 可验证研究假设；
11. 对博士后“车辆侧风模拟及实验验证”的具体方案启示。

---

## 31. 最重要的长期执行原则

### 原则 1

**从历史源头一直顺着方法演化追到当前，不允许只做随机关键词搜索。**

### 原则 2

**阵风与固定偏航角必须严格区分。**

### 原则 3

**原始文献优先于综述，综述主要用于发现文献。**

### 原则 4

**任何综合结论都必须能够追溯到 source record。**

### 原则 5

**全文未确认的内容不得写成已确认事实。**

### 原则 6

**未报告的数据写“未报告”，不得推测。**

### 原则 7

**论文数量不是核心 KPI，证据完整度和可复现性才是。**

### 原则 8

**持续建立引用关系和方法谱系，而不是建立 PDF 仓库。**

### 原则 9

**真实道路阵风、标准风发生器、风洞模拟和 CFD 输入必须分别描述其物理含义。**

### 原则 10

**“资料”不等于“论文”。**

标准、SAE Technical Paper、政府／研究机构报告、博士论文、公开数据集和设施资料均属于核心知识来源。Codex 必须持续检查资料类型覆盖率，不能因期刊论文更容易检索而把知识库退化成论文收藏夹。

### 原则 11

最终知识库必须能够回答：

> 从道路车辆侧风研究最早可核查的工作开始，这一领域的理论、实验和数值方法是怎样一步步发展到今天的？

以及：

> 当前“车辆侧风模拟及实验验证”最值得继续解决的科学和工程问题是什么？

---

## 32. 开始执行

首次运行直接：

1. 初始化／检查 Git 仓库；
2. 将本文件保存为 `TASK.md`；
3. 建立目录；
4. 建立 timeline；
5. 建立 search ledger；
6. 建立 citation graph；
7. 从 1970 年代关键文献开始；
8. 同时尝试向 1970 年以前继续回溯；
9. 对所有核心文献做 cited-by 向后追踪；
10. 一直沿方法谱系追到当前；
11. 完成第一次 commit 和 push；
12. 在日报中明确下一次断点。

若遇到：

- 来源缺失；
- 数据库权限；
- 版权限制；
- GitHub 权限；
- 本机路径；
- 周额度不可测；

必须在日志中明确记录。

**不得编造资料，不得伪称已完成自动调度，不得伪称 GitHub 与本地已同步。**
