# 气动力矩接近零，为什么仍会横摆？（2026-10-20）

本轮只处理这一动力学问题，不重复控制器增益、尺度、坐标换算或数值格式审计。Nakasato的NSP概念与Winkler的轮胎/横摆方程提供原文依据；下面的中性作用位置和配平代数均标 **ANALYST_INFERENCE**，不是作者完整仿真的重放，也不是Nakasato车辆参数辨识。

## 先看两个原文层面的事实

| 来源与新claim | 定位 | 有限结论 |
|---|---|---|
| Nakasato2017，E-2017-1525-07 | PDF3 / p664，Vehicle Model | 该掀背车NSP位于CG后方；作者将气动力作用位置与NSP的关系列为侧风讨论因素，但没有给出可复算的NSP数值和轮胎线性参数 |
| Winkler2016，E-2016-08 | PDF21 / 稿件p20，§3 | 无驾驶员、CG前移至轴距23%时，全浸没气动矩接近零，车辆仍横摆9.7°（标准CG约12.2°）；作者归因于前轮较低侧偏刚度及前后侧偏差异。这是数值参数研究，不是实测真值 |
| Winkler2016，E-2016-09 | PDF12–13、16 / 稿件pp11–12、15，Eqs4–5、Table1 | 两自由度单轨模型分别输入气动侧力和横摆矩，线性轮胎Fi=−Ciαi；Cy12/Cy34是前/后两轮合刚度，不能再把它们乘2 |

这些原页已文本核对并逐整页视检。NSP不等于CG，也不等于侧投影面积形心、天平原点或某一时刻的气动力等效作用位置。

还要分开角加速度、角速度和角度。在这里的平面恒惯量简化下，Jz·dr/dt=M_total、dψ/dt=r。即使某时刻**总矩**也为零，只说明当时横摆角加速度为零；已有横摆率或累计航向偏差不会因此自动清零。原文报告的9.7°是角度，不能把它改读成角速度，或仅凭该数值反推当时的力矩。

## EQ-NSP-TRIM：从轮胎力矩看零横摆率配平

**ANALYST_INFERENCE**。采用明确的平面约定：x向前、y向左、正横摆关于z向上；CG为原点。前轴位置+a、后轴−b，a,b>0；Cf、Cr>0是整轴侧偏刚度，单位N/rad。纵向速度U>0固定，小角线性轮胎、无侧倾/载荷转移/后轮转向，前轮角δ=0，给定外部气动力Fy、CG横摆矩Mz。

只研究**恒定输入下横摆率r=0且横向速度不再变化的配平**，不求瞬态，也不要求横向速度或道路偏移为零。令β=v_y/U，则两轴轮胎力为

\[
F_{yf}=-C_f\beta,\qquad F_{yr}=-C_r\beta.
\]

横向合力与CG总力矩平衡要求

\[
F_y-(C_f+C_r)\beta=0,\qquad
M_z+(bC_r-aC_f)\beta=0.
\]

消去β，得到

\[
\beta=\frac{F_y}{C_f+C_r},\qquad
M_z=x_nF_y,\qquad
x_n=\frac{aC_f-bC_r}{C_f+C_r}.
\]

这里x_n是该线性模型中，允许零横摆率配平的**等效侧向力作用位置**，相对CG计、向前为正。用它解释NSP的作用，不声称这个表达式就是Nakasato非线性6DoF模型中的实际NSP计算方法。

若气动矩关于CG为零，但aCf≠bCr且Fy≠0，横向力平衡所需的β会产生不为零的轮胎合矩。因此“气动矩为零”不等于“CG总力矩为零”，r=0的上述配平一般不成立。此判断不等于证明系统发散、不稳定或必然出现某个横摆峰值。

即使满足Mz=x_nFy而存在零横摆率配平，β和v_y仍可非零；它不保证没有侧向路径漂移，也不证明任意初值/有限阵风都会到达该配平。稳定性、瞬态、气动随姿态变化与驾驶员控制需另外求解。

## 用作者标准参数做一个新的局部核算

Winkler Table1的**标准**模型给a=f=3.7m、b=2.2m、Cf=250000N/rad、Cr=450000N/rad。仅将这些已报告参数代入上面的分析者公式，得到

\[
x_n=\frac{3.7(250000)-2.2(450000)}{700000}
=-0.0928571429\ \mathrm m.
\]

即在这个约定和线性模型下，标准NSP约在CG后9.29cm；这不是论文报告的新测量，也不能当成Nakasato掀背车的NSP。没有擅用43%/23%的圆整数重建作者改变CG后的完整轮胎/惯量模型。

[参数与派生量CSV](neutral_steer_balance.csv)保留输入、原页、单位和REPORT/ANALYST分类。按单位外力的**系数**写横向与力矩平衡，不制造一条阵风力时程：

| 量 | 由标准参数派生的值 | 含义 |
|---|---|---|
| β/Fy | 1.42857143e-6 rad/N | 零横摆率配平所需的侧偏系数 |
| Fyf/Fy | −0.357142857 | 前轮轴分担的抵消力 |
| Fyr/Fy | −0.642857143 | 后轮轴分担的抵消力 |
| 轮胎合矩/Fy | +0.092857143m | 即使气动矩为0也存在的轮胎矩系数 |
| 所需气动矩/Fy | −0.092857143m | 与轮胎矩相消的外矩系数 |

两轴力系数加1为0；两轴力矩系数加x_n为0，分别代回未经消元的两条平衡式核对。这只是局部配平核算，不会给出原文9.7°或12.2°。

核心可复算代码如下；CSV也包含a、b、Cf、Cr输入行。

```python
def trim_coefficients(a, b, cf, cr):
    total = cf + cr
    xn = (a*cf - b*cr) / total
    front_fraction, rear_fraction = -cf/total, -cr/total
    tire_moment_per_force = a*front_fraction - b*rear_fraction
    return {
        "x_n_m": xn,
        "beta_per_force_rad_per_N": 1/total,
        "front_force_fraction": front_fraction,
        "rear_force_fraction": rear_fraction,
        "tire_moment_per_force_m": tire_moment_per_force,
        "required_aero_moment_per_force_m": xn,
        "force_balance_residual": 1+front_fraction+rear_fraction,
        "moment_balance_residual_m": xn+tire_moment_per_force,
    }
```

## 作用位置与力矩原点也不能混用

在只保留同一平面Fy、Mz并将等效力放在车体中心线的表示下，Fy≠0时可定义x_a=Mz/Fy（相对同一CG原点）。这只是这对力/矩的等效作用线截距，不证明真实压力集中在那里；它可以随时间变化，甚至落在车身之外。Fy=0、Mz≠0时无法用有限x_a表示该纯力偶，不能填一个极大的“实测压心”。

于是上述配平条件可写Fy(x_a−x_n)=0。**二者都相对同一CG、轴和符号才有意义**；面积形心只是几何参考，Table1的“Aerodynamic CoG”也不自动是本页的x_a。不同q/A/长度下的CN/CY不能直接变成作用距离，源内单位/原点的还原仍按既有[载荷换算](load_reexpression.md)处理。

## 本轮改变的理解与仍缺的证据

气动矩、轮胎矩和惯性响应在同一个车辆方程中共同作用；减小气动矩是一个输入变化，不等于消除横摆或道路偏离。Winkler的瞬态参数研究和本页静态消元互相说明这个区别，但后者既不证明作者的全部物理解释，也不预测实车稳定性。

现有NC-2016-VALIDATION继续承接原模型/CG/载荷/位姿输入；NC-2017-1525-REPLAY及其最小交付表本轮补明源内NSP定义/数值、匹配CG/轮胎表和工况。这是扩充既有请求，不增另一条重复请求。Nakasato未给的NSP数值不以Winkler参数替代；本轮无原模型重放、无新source/PDF或Pass3完成。
