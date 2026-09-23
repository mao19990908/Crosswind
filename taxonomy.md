# 分类体系

分类代码 A–M 描述研究主题；`source_type` 描述资料的发布形态，两者是独立维度。一条来源必须同时有且仅有一个规范 `source_type`，可有多个研究类别标签。

## 规范资料类型（source_type）

| source_type | 含义 |
|---|---|
| `journal_article` | 同行评议期刊论文 |
| `sae_technical_paper` | SAE Technical Paper / SAE 技术论文 |
| `conference_paper` | 其他会议论文 |
| `standard` | 正式标准 |
| `standard_draft` | 标准草案 |
| `government_report` | 政府技术报告 |
| `institutional_report` | 研究机构／实验室技术报告 |
| `project_report` | 公开科研／产业项目报告 |
| `doctoral_thesis` | 博士论文 |
| `master_thesis` | 硕士论文 |
| `book` | 专著 |
| `book_chapter` | 专著章节 |
| `review_article` | 综述论文 |
| `dataset` | 公开数据集 |
| `code_repository` | 公开代码／模型仓库 |
| `facility_documentation` | 设施资料 |
| `manufacturer_technical_document` | OEM／供应商公开技术资料 |
| `patent` | 专利 |
| `regulatory_document` | 法规／监管文件 |
| `web_primary_source` | 官方机构、作者或项目原始网页 |
| `secondary_web_source` | 二手网页／聚合页，只作线索 |

新增资料类型必须先记录在 `taxonomy_change_log.md`。检索覆盖率、README 和每日日志需按 `source_type` 统计；长期为 0 的类型要判断是确实不存在、数据库覆盖不足、检索词不合适还是权限受限。

## 研究主题类别

| 代码 | 类别 | 范围 |
|---|---|---|
| A | 历史与定义 | 概念源流、术语、引文链、阵风与稳态边界 |
| B | 阵风输入与环境 | 波形、风区、剪切、湍流、自然风、道路场景 |
| C | 非定常气动理论 | 准稳态／非准稳态、气动导数、相位、超调、记忆 |
| D | 气动系统响应模型 | 导纳、频响、权函数、卷积、ROM |
| E | 车辆动力学理论 | 单轨、多轨、多体、轮胎、悬架、驾驶员／控制器 |
| F | 风洞实验 | 静态、移动模型、阵风发生器、PIV／压力 |
| G | 整车／道路实验 | 风机阵列、自然风、道路试验、整车状态 |
| H | 气动 CFD | 瞬态入口、移动网格、URANS、DES、DDES、LES |
| I | 气动—车辆动力学耦合 | 稳态映射至全双向耦合 |
| J | 验证与评价 | 风场、气动力、整车运动三级验证与不确定度 |
| K | 标准与规范 | ISO、SAE、国家及行业方法 |
| L | 数据与开放资源 | 数据集、模型、代码、数据库 |
| M | 工程应用 | 造型、底盘、主动控制、稳健性优化 |

## 强制标签

- 稳态偏航条件纳入时使用 `steady_baseline`。
- 闭环类型使用 `open_loop`、`closed_loop_driver`、`closed_loop_controller` 或 `autonomous_control`。
- 访问与验证状态使用任务书第 19 节枚举。
