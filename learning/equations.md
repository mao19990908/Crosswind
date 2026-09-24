# 公式账本

仅录入原文核验过的定义。`pimeche-2001-passmore` 页码为期刊页，PDF页=期刊页−777。

| equation_id | name / formula | symbols and units | assumptions / source | alternative definitions / limits |
|---|---|---|---|---|
| EQ-RELWIND | FORMULA_PENDING_FULLTEXT | 车速、横风、相对风角 | 来源论文待核；TASK.md仅提示 | 不跨坐标系代入 |
| EQ-RED-FREQ | \(k_m=\pi f l/U\) | f Hz；l 模型全长 m；U 风洞自由流 m/s；k_m 无量纲 | Passmore pp.779–780，E2 | 不等同 2πfl/U；不能用车速无条件替换U |
| EQ-MAGNIFICATION | \(\chi_a=A_{\mathrm{transient}}/A_{\mathrm{QS}}\) | 同一载荷分量的正弦幅值；无量纲 | Passmore p.785，E2；同频、同一归一化和明确QS基线 | 幅值比不含复数相位；压力和天平基线不混换 |
| EQ-ADMIT | \(\text{power admittance}=\chi_a^2\) | 论文定义的功率比；无量纲 | Passmore p.785，E2；同频正弦简化 | 不是任意宽带输入下的通用导纳公式 |
| EQ-YAW | FORMULA_PENDING_FULLTEXT | 参考面积、参考长度、正号待核 | Passmore明确力矩关于模型中点，但未给完整归一化 | 不据此跨来源比较系数 |

## 正弦准稳态预测（Passmore p.785，E2）

\[
C_y(t)=\frac{dC_y}{d\beta} A_g A_0\sin(\omega t).
\]

原文 p.781 定义 \(A_g=v/[(u+U)A_0]\)：v 为横向分量，u 为纵向脉动，U 为自由流，A0 为翼角最大值（rad）。这里的 β 是风洞偏航角，不是车辆航向或质心侧偏角；ω 为正弦角频率。导数来自稳态压力数据；Table 1 未写角度单位，Fig.4 以度绘制，故本库不直接将表内数值代入弧度公式。

逐测点版本在正弦相位中加 ψ_n，取决于测点纵向位置和来流传播。原文未写可直接抄用的 ψ_n 正负号公式；保留作者定义并要求复现时记录参考时刻。Fig.9 已去除阵风传播相位，不能重复扣除。
