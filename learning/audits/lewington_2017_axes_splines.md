# Lewington2017 Pass3：参考点、样条与偏移指标（2026-10-11）

Source `sae-2017-01-1515`，已于9月25日完成全文P2；本次针对PDF3–8/12–15文字与7/8/13整页图像重核，不重复整篇通读。既有15页用户PDF SHA `1623c0555f0449164870c98225e4abeb53e296ca7411a108582299abebe255c5` 未变；6659712 bytes，本机专存，github_pdf=false。PDF页与本文引用的article页一致。

## 1. 已确定的是准稳态参考系，不能自动等同于样条接口

PDF7 Fig9/正文明确：准稳态六分量按SAE J1594命名，参考点位于车辆中心线、地面、轴距中点。Eqs1–2为 `Fi=0.5 rho ci A v²` 和 `Mi=0.5 WB rho ci A v²`，A为横截面积（末页定义为前面积），WB为轴距，v为相对车体的合风速。不能用车长L替换WB，也不能当CG力矩直接施加。

这段明确描述quasi-steady lookup分支。PDF8的直接导入仅给 `Fi=F(t)i`，未明确公布导出/导入marker原点、轴顺序、正负号、参考系随车旋转与否或参考点平移实现。ADAMS采用global coordinate formulation不意味着所有force元素都以惯性坐标定义；PDF6指出force方向依赖参考frame。因此CFD→ADAMS的完整轴/力矩变换仍UNKNOWN，不能借Fig9推定所有转换已完成。

ANALYST_INFERENCE：若源/目标轴旋转矩阵Q已知且同一物理时刻，载荷变换可写 `F_new=Q F_old`、`M_new=Q[M_old−(r_new−r_old)×F_old]`，括号中的r与F须在同一旧坐标系。这里只列必要条件，未将假设Q、CG坐标或合成力矩写成论文数据。

## 2. “未滤波载荷”不等于原始数组直接回放

PDF5–8：CFD沿规定路径推进，没有gust-induced姿态/横向偏移反馈；六分量时程以action-only time-history splines驱动车身。作者要求平滑lead-in/lead-out及线性外推来避免端部伪效应。未报告样条阶数、节点、边界导数、平滑窗口、输出采样率和导入后的时移。不能因摘要说unfiltered就省掉这些接口处理，也不能声称现有曲线可唯一重建输入。

CFD步长2.5e−4s，MBD使用变阶变步BDF，测量50Hz即名义0.02s间隔；计算所得80倍是两个名义间隔之比，不证明CFD输出率、MBD固定步长或重采样策略。原文CFD总时长约2s含0.5s初始化；约0.75s开始接触风场（PDF6）与阻力上升约0.9s（PDF8）是不同语境，不能未经原始时程对齐强定相位偏差。

## 3. 车体侧偏与气动入流偏角用了同一个β符号

PDF7 Fig10和PDF8开头用β作相对来流angle of attack；PDF8 Eq5/文字又以β作车辆sideslip。Eq4/6中的α是积分横摆角，亦不能与前面yaw polar中的α直接合并。保留原符号的局部上下文，数据库说明用beta_aero、beta_vehicle、alpha_heading区分，不能以同字母认定同变量。

PDF8 Eqs4–6视觉确认：

`alpha = integral(r dt)`

`beta_vehicle = integral((a_y/v_x − r) dt)`

`gamma = integral(v_x*(alpha+beta_vehicle) dt)`。

r为横摆角速度，a_y为文中侧向加速度，gamma为横向偏移。作者说采用简单梯形积分并援引ISO12021:2010；本次核的是论文公式，未获得/认证ISO全文内容。初值、精确积分窗口、传感器frame和重力/侧倾补偿实现并未完整给出。

**ANALYST_INFERENCE**：在这些小角形式下，使用同一时刻/同一r信号，`d(alpha+beta_vehicle)/dt=a_y/v_x`。若v_x恒定且初值一致，则gamma退化为a_y的二次积分加初值项；因此相同a_y却不同r时，此指标可能相同。变速时 `gamma''=a_y+v_x_dot*(alpha+beta_vehicle)`，不能继续简单等同加速度二次积分。不同滤波/重采样或初值会破坏离散抵消。

离线脚本用两条不同**合成**yaw序列、同一合成a_y、同网格/零初值/恒速验证梯形离散抵消；这不是任何一辆试验车的真实响应。假设恒定加速度偏置0.01m/s²持续2s时偏移漂移0.02m仅展示积分敏感性，不认定该测量系统有此偏差。

## 4. SD范围、置信区间与时程准确性是不同判断

PDF4：光学触发在入风前1s，总记录3s，每车至少6次；有anti-alias滤波、offset校准、后处理moving average和无风对照。未给完整滤波器参数、每车精确n和逐次数据。作者提95%confidence interval的采样目标，Table2却报告均值和**标准差**；不能把±1SD换名为95%CI，或自行按n=6计算置信区间/显著性。PDF12–13的Figs21–23横轴延伸至4s，也不能据图轴推断原记录长度或统一触发偏移。

PDF13 Table2复核；用已发表约数计算 `(预测−均值)/SD`：

| Vehicle | One-way | Quasi-steady | 范围解释 |
|---|---:|---:|---|
| Everest | 0 | −1.000 | 准稳态恰在下侧一SD边界（约数） |
| Escort | +0.609 | +0.174 | 准稳态更靠近均值 |
| B-Max | +0.048 | +0.143 | 单向更靠近均值 |

这里是描述性SD距离，不是z检验或统计显著性结论。两方法落在一SD范围内，既不表示等效，也不推翻其他时程差异；尤其gamma在上述恒速条件下不能独立验证yaw-rate通道。保留原文对yaw/roll/a_y时程的条件化比较，不提升为各指标普适优越。

## 5. 审计边界与下个断点

已核参考点、WB/合速度规范化、局部符号、样条端部要求和积分结构。原始六分量、markers/frames、样条/滤波/触发设置、逐次50Hz数据/精确n及MBD模型尚缺，登记NC-2017-1515-REPLAY；不请求重复PDF。P3保持partial，不宣称实测时程回放或原结果复现。

`scripts/audit_lewington_2017.py` 生成16行算术/合成检查CSV，只有Table2发表约数和显式标记的合成验证。下一可执行来源 `sae-2017-01-1525` Pass3；仍有backlog，继续Learn而不扩库。
