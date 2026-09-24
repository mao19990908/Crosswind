# 中英术语与定义边界

| English | 中文 | 定义或本库用法 | 易混淆项 | 来源／状态 |
|---|---|---|---|---|
| crosswind | 侧风 | 相对车辆行进方向具有横向分量的风；需说明坐标系 | gust、相对来流 | `TASK.md` §1.2；定义层 |
| transient crosswind / gust | 瞬态侧风／阵风 | 横向来流随时间或车辆位置改变的输入；不能只凭固定偏航推断动态载荷 | steady yaw | `sae-530255`、`sae-960674`，E1 |
| finite wind zone | 有限侧风区 | 车辆经过有限长度风区产生入风和出风事件 | 无限持续 step gust | `dot-hs-805-078`、`sae-960674`，E1 |
| relative-wind yaw angle | 相对来流偏航角 | 车辆坐标中相对风向的角度；必须记录风和车速约定 | 航向角、质心侧偏角 | `TASK.md` §1.2、§5；来源公式待核 |
| vehicle heading | 车辆航向角 | 车体纵轴相对地面参考方向 | 相对风角、质心侧偏角 | `TASK.md` §1.2；概念边界 |
| vehicle sideslip | 车辆质心侧偏角 | 质心速度方向相对车体纵轴 | 相对风角、航向角 | `TASK.md` §1.2；概念边界 |
| side force / lateral force | 侧向气动力／横向力 | 应区分气动力与轮胎／总横向力；正号随作者坐标定义 | 轮胎侧向力 | `sae-730232`、`sae-980392`，E1；符号待核 |
| yaw moment | 横摆力矩 | 气动力矩须指定参考点和正向 | 横摆角速度 | `sae-960674`、`pimeche-2001-passmore`，E1 |
| quasi-steady | 准稳态 | 以瞬时风状态查询稳态气动关系的近似；实际作者公式待核 | 已验证瞬态模型 | `sae-960674`、`pimeche-2001-passmore`，E1 |
| aerodynamic derivative | 气动导数 | 载荷对风角等输入变化的敏感量；具体偏导定义需原文 | 气动导纳 | `sae-730232`，E1 |
| admittance | 气动导纳 | 风输入频率分量与载荷响应的关系；归一化及复数定义待核 | 单一峰值比 | `pimeche-2001-passmore`，E1；公式 NEEDS_FULLTEXT |
| overshoot / undershoot | 超调／欠调 | 只在同一来源明确基线和分量后比较瞬态与稳态 | 所有载荷同向变化 | `sae-980392`、`sae-06-14-01-0001`，E1 |
| open-loop / closed-loop | 开环／闭环 | 必须按转向约束、驾驶员或控制器参与区分 | 风洞回流闭环（风洞类型） | `iso-12021-2010`、`dot-hs-805-078`，E1 |
