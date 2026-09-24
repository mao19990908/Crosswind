# CFD：先核对阵风实现

`sae-970404` 摘要包含一厢车进入侧风区及会车场景、滑移网格、ALE 和 k–ε 模型；其试验比较的量和网格/时步收敛细节仍需全文。`jcp-2016-tunay` 摘要包含 DES、overset 与车辆运动耦合。两者的物理输入和车辆反馈不同，不能仅按湍流模型复杂度排序。

| 项目 | `sae-970404` | `jcp-2016-tunay` |
|---|---|---|
| gust implementation | 车辆进入侧风区，具体边界待核 | transient crosswind，具体时空输入待核 |
| vehicle motion | ALE/滑移网格，运动自由度待核 | 单轨车辆侧向/横摆反馈 |
| turbulence model | k–ε | DES |
| mesh/time resolution | NEEDS_FULLTEXT | NEEDS_FULLTEXT |
| validation A/B/C | 摘要称与试验气动特性比较，等级待核 | 摘要未报告独立验证 |

每篇 CFD 后续按风场 A、气动 B、车辆运动 C 分开登记；“与试验一致”不足以自动得到 Level C。
