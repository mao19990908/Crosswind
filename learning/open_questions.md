# 图谱断边与开放问题

| question | why_it_matters | known_evidence | missing_evidence | possible_method | related_sources | related_nodes |
|---|---|---|---|---|---|---|
| 自然道路阵风能否由标准风发生器等效重建？ | 决定实验外推性 | ISO 官方声明不代表真实驾驶；1953 道路事件 | 同车道路风谱、空间相干、发生器风场与运动 | 同车道路与风洞 Level A/B/C 对照 | `sae-530255`;`iso-12021-2010` | `G-NATURAL`;`G-FINITE`;`C-VALIDATION` |
| 不同载荷分量的准稳态失效边界是什么？ | 决定气动模型所需复杂度 | 移动模型、有限射流、正弦输入条件性差异 | 同几何同输入的幅相/峰值与坐标 | 多频/多梯度扫描并分量建模 | `sae-960674`;`sae-980392`;`pimeche-2001-passmore` | `C-QS`;`C-DYNLOAD`;`C-PHASE` |
| 动态气动响应模型如何可靠接入车辆动力学？ | 连接 Level B 与 Level C | 2001 载荷频率响应；2017 Level 2 整车对照 | 经核验的传递函数/ROM及独立运动数据 | 同车 Level 2/3 对比试验 | `pimeche-2001-passmore`;`sae-2017-01-1515` | `C-DYNLOAD`;`C-VEHMOTION` |

这些是目前仓库的缺证关系，`OPEN_QUESTION` 不等于已经证实学界无人研究。若原始全文或新来源补边，再更新本表与 `synthesis/research_gaps.md`。

## 2026-09-25：已读原文后的明确缺项
- question：Passmore正文2–8 Hz为何与Figs.9/11的1 Hz不一致？why_it_matters：频率映射与低频极限判断。known_evidence：pp.784、786–787；missing_evidence：勘误或原始测试日志；possible_method：核查原始数据/勘误后再标准化。related_sources：`pimeche-2001-passmore`；related_nodes：`EQ-RED-FREQ`、`C-VALIDATION`。
- question：有限带宽的气动幅值比怎样成为可验证整车ROM？known_evidence：已核平方关系和传播相位基线，不能再称这两项缺全文；missing_evidence：完整归一化、原始幅相和独立运动证据；possible_method：固定同车坐标及参考点，辨识分量复数频响并用非拟合事件测试；related_nodes：`EQ-ADMIT`、`C-PHASE`、`C-VEHMOTION`。

## 2026-09-27：Hucho输出复现断点

Eq19修正已可推导，不再笼统称其缺失。尚需Fig11原车轮廓/参考点/坐标映射和Fig12车辆模型参数；请求NC-1973-GEOMETRY、NC-1973-VEHICLE见needs_collection.csv。原始数据到达前避免重复输入公式检查。

## 2026-09-28：Beauvais 原始输入缺口

NC-1967-REPRO：正文20–40/20–80ft/s与Fig7/8工况标签不一致；需要原试验台账及A/d、输入廓线、动态天平响应和逐次信号。15°结论仍是特定论文主张，尚无足以核查低角度采样的资料。当前审计不重复全文获取或新增来源。
