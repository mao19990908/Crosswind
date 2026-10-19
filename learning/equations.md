# 公式账本

仅录入原文核验过的定义。`pimeche-2001-passmore` 页码为期刊页，PDF页=期刊页−777。

| equation_id | name / formula | symbols and units | assumptions / source | alternative definitions / limits |
|---|---|---|---|---|
| EQ-RELWIND | psi=atan(Vv/Vu); V=sqrt(Vu²+Vv²) | Vu轨道车速、Vv垂直横流，ft/s；psi为相对来流角 | Beauvais p.2222 Eqs2–3，E2；Vu>0，无纵向环境风 | psi不是Hucho车辆航向；不跨坐标系代入 |
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

## Beauvais1967：支撑反力与图示归一化（2026-09-28）

EQ-BEAUVAIS-BALANCE：C_Fi=Fi/(qA)，C_Y=C_F1+C_F2，C_N=(C_F1-C_F2)d/x。q按总相对V；d为半支撑距，x为全长1.646ft，力矩中心车头后0.513x。A保留原文“最大投影横截面积”，不能替换Hucho侧面积。图8–10处理链用3L动态平台作分母，与独立静态曲线不同。原文/推断/缺项见[复现审计](audits/beauvais_1967_reproduction.md)。

## Macklin1996系数（2026-10-07）

EQ-MACKLIN-COEFF：CF=F/(0.5rho U²A)，CM=M/(0.5rho U²Al)，U=sqrt(UF²+UW²)。PDF3中A为前投影面积、l为轴距；不能换成车身全长。地面参考点和镜像MIRA轴约定见PDF5；75mm是天平距底板高度。详见[信号与坐标审计](audits/macklin_1996_signal_axes.md)。

## Ryan1998轴速归一化（2026-10-08）

EQ-RYAN-COEFF：CY=Y/(0.5rhoAv²)，Cmz=Mz/(0.5rhoAv²l)，Czu=Zu/(0.5rhoAv²)。PDF11/印刷9：v是轴向等效前进速度，A为零偏航前面积，l为模型长度；PDF6力矩参考侧面积形心。与Macklin总速U/轴距不同。仅相同载荷、面积、长度、参考点且垂直横流条件下，换总速归一化的cos²因子为ANALYST_INFERENCE，非跨论文实测修正；见[审计](audits/ryan_1998_pressure_reference.md)。

## Winkler2016跨尺度定义（2026-10-09）

EQ-WINKLER-SCALE：PDF11–12 Eqs1–3，Cs=Fya/(0.5 rho u_inf² A)，Cyaw=Mza/(0.5 rho u_inf² A L)，St=L/(u_inf t)。原文A前面积、L车长、u_inf自由流速、t时间；St不是直接沿用Passmore的pi*f*l/U。P3将核对模型/整车时间映射、重心力矩平移以及控制器Eq8–14误差符号，不先给未经核验的可执行控制律。

## Winkler2016控制符号与尺度审计（2026-10-10）

EQ-WINKLER-PREVIEW保留Eq11负曲率与Eq12正轮角的印刷差别；由圆心几何得到负号，但Δ误差/执行器方向未交代，不能直接生成闭环律。线性无气动稳态方程推得Kus=m/(f+b)*(b/Cf-f/Cr)，增益幅值按rad输出为0.021553/0.538836，仅把输出换成deg时与表1.2/30.9相容；不是作者代码单位声明。EQ-WINKLER-SCALE的St不变给时间比29.312、全尺度步长0.00175872s，均标ANALYST_INFERENCE。脚本检查稳态力矩/力平衡、四个有符号圆几何点及尺度不变性；见[审计](audits/winkler_2016_controller_scaling.md)。

## Lewington2017：载荷与偏移公式（2026-10-11）

EQ-LEWINGTON-LOAD保留PDF7–8准稳态Fi=0.5rho ci A v²、Mi=0.5WB rho ci A v²和直接样条Fi=F(t)i。地面轴距中点参考明确属于QS描述；不自动证明CFD接口已旋转/平移到CG。

EQ-LEWINGTON-PATH按Eq4–6记录alpha=int(r)、beta_vehicle=int(a_y/v_x-r)、gamma=int(v_x*(alpha+beta_vehicle))。恒速/一致初值及网格时，yaw项相消，gamma为加速度二次积分加初值项；变速须保留v_x_dot项。此为ANALYST_INFERENCE和合成梯形检查，不是原道路时程复现。beta在Fig10另指气动偏角，不能混用。

## Nakasato前视误差（2026-10-12）

EQ-NAKASATO-PREVIEW：p667 Fig15 e_g=A+B，单位m，A为朝向的前视横向投影，B为车辆横向位移。源内Yaw是车身朝向，不是气动偏角。Fig14支路缩放/符号和增益未给，不能按图直接将m与m/s²相加实现控制器；50/33.3约1.50s也不是纯时延。详见[audit](audits/nakasato_2017_driver_frames.md)。

## 源间载荷重新表达（2026-10-15）

EQ-LOAD-REEXPRESSION为ANALYST_INFERENCE：先以各自qA/qAL还原物理力和力矩，再按Ft=R Fs、Mt=R Ms-d×Ft变换，d是新原点减旧原点、用目标轴表示，最后用目标qA/qAL归一化。R限右手正交旋转；缺载荷分量/单位/原点时不计算。16个显式合成检查通过，不代表恢复作者接口。见[推导与对照](audits/load_reexpression.md)。

## 空间遇风时间与幅值非唯一性（2026-10-16）

EQ-SPATIAL-ENCOUNTER为条件运动学：静止空间风场、指定参考点及恒速V时，s=V(t-t0)、tr=sm/V；不是全车暴露/载荷建立时间。EQ-MAGNITUDE-NONUNIQUENESS以稳定H0=1/(1+Ts)和增加非负时延的Hd说明幅值/功率相同仍有不同相位/时域响应。两条均标ANALYST_INFERENCE，无作者新测量或原始输出复现。

## 压力减缩与固定时刻协方差（2026-10-17）

EQ-PRESSURE-OPERATOR为ANALYST_INFERENCE：以外法向、Δp和面片权重写F=−ΣΔp n A、M=−Σ(r−rO)×(Δp n A)，即已测表面固定几何的L=Kp。复压力先有符号积分再取幅值；不恢复未测底面/剪切。共同线性滤波只在固定K、共同时间参考/边界等条件下可交换。

EQ-LINEAR-LOAD-COV为ANALYST_INFERENCE：已知固定K、固定时刻有Σ_L=KΣ_pKᵀ；双反力差的力矩方差含−2cov(F1,F2)。这是线性代数恒等式与来源缺项的联系，不是作者报告的不确定度模型，也不覆盖选峰置信区间或未知几何/标定误差。13个合成检查及符号条件见[测量链审计](audits/measurement_chain.md)。

## 显式平面相对来流（2026-10-19）

EQ-RELWIND-PLANAR为ANALYST_INFERENCE：R(ψ)把x前/y左车体系转至右手地面系；同一参考点的车辆地速u_b=Rᵀv_g，空气地面流向速度w_g，则车辆穿空气速度a_b=u_b−Rᵀw_g。α_a=atan2(a_y,a_x)、β_v=atan2(u_y,u_x)与姿态ψ分别定义，非零地速下χ=wrap(ψ+β_v)。零地速不赋侧偏/航迹角，零穿空气速度不赋α_a；不覆盖三维局部旋转速度或自动映射作者角度/规范化。源内EQ-RELWIND仍保留Beauvais原定义。见[推导、输入及可复算例子](audits/relative_wind_kinematics.md)。

## 零横摆率配平与中性侧向力作用位置（2026-10-20）

EQ-NSP-TRIM为ANALYST_INFERENCE：CG为原点、x前/y左、a/b为前后轴正距离、Cf/Cr为整轴刚度；固定U、δ=0、小角线性轮胎、r=0且横向速度不变时，Fy−(Cf+Cr)β=0、Mz+(bCr−aCf)β=0，故β=Fy/(Cf+Cr)、Mz=x_n Fy、x_n=(aCf−bCr)/(Cf+Cr)。它不保证零侧向漂移、稳定性或瞬态轨迹，亦不是Nakasato原6DoF模型NSP算法。Winkler标准表参数的−0.092857m仅为派生值；见[条件与平衡核对](audits/neutral_steer_point.md)。
