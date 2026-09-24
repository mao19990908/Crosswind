# 图谱断边与开放问题

| question | why_it_matters | known_evidence | missing_evidence | possible_method | related_sources | related_nodes |
|---|---|---|---|---|---|---|
| 自然道路阵风能否由标准风发生器等效重建？ | 决定实验外推性 | ISO 官方声明不代表真实驾驶；1953 道路事件 | 同车道路风谱、空间相干、发生器风场与运动 | 同车道路与风洞 Level A/B/C 对照 | `sae-530255`;`iso-12021-2010` | `G-NATURAL`;`G-FINITE`;`C-VALIDATION` |
| 不同载荷分量的准稳态失效边界是什么？ | 决定气动模型所需复杂度 | 移动模型、有限射流、正弦输入条件性差异 | 同几何同输入的幅相/峰值与坐标 | 多频/多梯度扫描并分量建模 | `sae-960674`;`sae-980392`;`pimeche-2001-passmore` | `C-QS`;`C-DYNLOAD`;`C-PHASE` |
| 动态气动响应模型如何可靠接入车辆动力学？ | 连接 Level B 与 Level C | 2001 载荷频率响应；2017 Level 2 整车对照 | 经核验的传递函数/ROM及独立运动数据 | 同车 Level 2/3 对比试验 | `pimeche-2001-passmore`;`sae-2017-01-1515` | `C-DYNLOAD`;`C-VEHMOTION` |

这些是目前仓库的缺证关系，`OPEN_QUESTION` 不等于已经证实学界无人研究。若原始全文或新来源补边，再更新本表与 `synthesis/research_gaps.md`。
