# 公式账本

仅录入原文核验过的定义。`pimeche-2001-passmore` 页码为期刊页，PDF页=期刊页−777。

| equation_id | name / formula | symbols and units | assumptions / source | alternative definitions / limits |
|---|---|---|---|---|
| EQ-RELWIND | FORMULA_PENDING_FULLTEXT | 车速、横风、相对风角 | 来源论文待核；TASK.md仅提示 | 不跨坐标系代入 |
| EQ-RED-FREQ | \(k_m=\pi f l/U\) | f Hz；l 模型全长 m；U 风洞自由流 m/s；k_m 无量纲 | Passmore pp.779–780，E2 | 不等同 2πfl/U；不能用车速无条件替换U |
| EQ-MAGNIFICATION | \(\chi_a=A_{\mathrm{transient}}/A_{\mathrm{QS}}\) | 同一载荷分量的正弦幅值；无量纲 | Passmore p.785，E2；同频、同一归一化和明确QS基线 | 幅值比不含复数相位；压力和天平基线不混换 |
| EQ-ADMIT | \(\text{power admittance}=\chi_a^2\) | 论文定义的功率比；无量纲 | Passmore p.785，E2；同频正弦简化 | 不是任意宽带输入下的通用导纳公式 |
| EQ-YAW | c_N=N/(q_inf Ay l) | N关于xs；Ay侧面积；l车长 | Hucho p.896 Eqs15-16，E2 | 仅此来源；Passmore归一化仍未齐全，不能跨来源直接比较 |

## 正弦准稳态预测（Passmore p.785，E2）

\[
C_y(t)=\frac{dC_y}{d\beta} A_g A_0\sin(\omega t).
\]

原文 p.781 定义 \(A_g=v/[(u+U)A_0]\)：v 为横向分量，u 为纵向脉动，U 为自由流，A0 为翼角最大值（rad）。这里的 β 是风洞偏航角，不是车辆航向或质心侧偏角；ω 为正弦角频率。导数来自稳态压力数据；Table 1 未写角度单位，Fig.4 以度绘制，故本库不直接将表内数值代入弧度公式。

逐测点版本在正弦相位中加 ψ_n，取决于测点纵向位置和来流传播。原文未写可直接抄用的 ψ_n 正负号公式；保留作者定义并要求复现时记录参考时刻。Fig.9 已去除阵风传播相位，不能重复扣除。

## Hucho 1973：侧面积、参考点与车底积分（2026-09-27）

原文p.896 Eqs14-16：c_s=S/(q_inf Ay)、c_N=N/(q_inf Ay l)、N=integral(x-xs)dS。这里Ay是侧投影面积；不能替换为前投影面积或忽略参考点。原文单位kp/mkp，beta与psi按命名表分别为气动偏航与车辆横摆。

新增EQ-HUCHO-CLEARANCE：Eq19的积分比在Eq8第一压力分量与Eq8梯度/Eq11时间分量下不同。a=zB/z1时，分析者推得phi_s=1-2 asin(a)/pi、phi_i=1-2[asin(a)+a sqrt(1-a^2)]/pi；仅限0<=a<=1的原平板近似，未验证实际车底流动。详见[公式审计](audits/hucho_1973_equations.md)与可运行数值检查。
