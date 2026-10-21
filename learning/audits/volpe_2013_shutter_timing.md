# Volpe2013 Pass 3：挡板时钟、局部输入和原图复现边界

2026-10-22。沿既有`jfe-2013-volpe`全文P2断点，针对时序/坐标做深读，不重新收集或通读相同PDF。PDF哈希保持b6fb24a6c19f6624b4c868740ed07e4abbf45053b0128fac6b3d42c41da15eee；本机文件`jfe-2013-volpe__volpe__2013.pdf`，PDF页=稿件页+2。靶向读PDF9–12/16–21/23–26；9整页视检。原图与PDF均不上传。

原文记录及证据地图见[record](../../sources/records/jfe-2013-volpe.md)。本页的 **SOURCE_REPORTED** 与 **ANALYST_INFERENCE** 分开；没有原始PIV、执行器日志或求解器文件，因此没有重放Fig9/12。

## 先核对原文的时间定义

|量|原文位置|含义和边界|
|---|---|---|
|20通道双挡板，顺序间隔dt=d_x/U=5ms，d_x=0.045m|PDF9–10，稿件7–8，§2.1/Figs3–4；E-2013-07|相邻门的名义触发间隔；辅助出口与互补出口反向动作，不能解释成全体同时开启|
|t_gust=10L/U，印刷值0.311s|PDF10–11，稿件8–9|Fig4单门名义开启保持区间，不是所有门同时全开的区间，也不是局部实际稳定平台长度|
|真实开启约12ms、关闭约30ms|PDF17，稿件15，§3.2；E-2013-05|动作过程持续时间，区别于5ms相邻触发，也不能凭一个持续时间猜叶片角度轨迹|
|CFD恒步长2ms；挡板瞬时边界切换|PDF16–18，稿件14–16；E-2013-04/05|没有模拟真实叶片连续运动；6/15个步长的换算不证明该动作被实际求解|
|PIV500Hz，首挡板触发，15次均值、9测窗|PDF11–12，稿件9–10；E-2013-02|采样周期2ms不是已知的CFD/PIV共同相位、触发零延迟或系统有效带宽|
|t+=tU/L，t+=0对应首挡板开启触发|PDF18，稿件16，§4|设施时间基准，不是每个探针自己的阵风到达零点|
|δt+为达到建立状态的延迟；E点0.8/A点1.5|PDF19/21，稿件17/19，Fig9/Table1；E-2013-03|不能改称10–90%升时、横向飞行时间或车辆气动力建立时间；不另从低分辨率图中选择阈值|

Fig4从`t=dt`画首门、`t=20dt`画全开状态，§4以首触发为零点。可以用**显式平移时间原点**协调这两种标注，不必制造原文矛盾；实际命令、叶片动作与PIV触发之间的偏差仍须日志/标定。

## 分析者换算：哪些数值能算，哪些不能

[时间CSV](volpe_2013_timing.csv)分13行源内参数与20行派生量；[探针CSV](volpe_2013_probes.csv)逐列区分表1无量纲坐标和乘L得到的米制坐标。它们不包含构造的作者时程；派生量保留的小数用于复算，不增加原参数的测量精度。

以源报U=9m/s、L=0.28m作名义换算，T_ref=L/U=0.0311111111s，名义T_g=10T_ref=0.3111111111s；0.311s为原文舍入值，不应把由舍入引起的末位差异当成模型误差。2ms对应Δt+=0.0642857143，5ms对应0.1607142857。

**事件网格条件**：5ms/2ms=2.5。若所有边界事件只能发生在同一个固定2ms网格的节点上，两个相隔5ms的事件不可能都精确落点：两节点差必须是2ms的整数倍。这是整数格点条件，不是识别出作者的具体算法。原文未说明子步处理、事件回调、取整/插值或实际执行时刻；不猜“交替2/3步”，不指定误差正负，也不把CFD提前到达归因于这项未核实现。PIV与CFD周期同为2ms也不建立两时钟的相位联系。

真实开启12ms等于2.4个相邻触发间隔，关闭30ms等于6个；因此顺序命令可以与多门动作过程重叠，不能按“上一门完全打开后才开下一门”重写装置。它们分别等于6和15个CFD步长，只是单位换算；在原模型中叶片动作已经被瞬时开关替代。延迟0.8/1.5乘T_ref给24.8889/46.6667ms，与源报24.9/46.7ms的舍入一致；相对名义T_g为8%/15%。作者把它们视为测非定常力时足够短，这不是没有频率/误差判据也能迁移到任意车体或输出的结论。

### 条件性命令区间推导（EQ-VOLPE-SHUTTER-CLOCKS）

仅在**理想矩形命令**假设下，令N=20、首门触发归零，相邻间隔d=5ms，每门命令保持T_g，定义第j门区间I_j=[(j−1)d,(j−1)d+T_g)。这只是把Fig4理想时序写清，不是测得的叶片开度、流量或探针风速函数。

- 首门至末门触发跨度为(N−1)d=95ms。Fig4绝对示意的20d=100ms与此不同，原因是第一行从d而非0计时。
- 因T_g>d，任意门开启的命令并集长度为T_g+(N−1)d≈406.111ms。
- 全部门同时处于开启命令的交集长度为max(0,T_g−(N−1)d)≈216.111ms。

两者均不同于单门T_g≈311.111ms；也不能替换Fig9中任一位置的建立区间Δt+。有限叶片动作、互补出口、漏流、压力相互作用和流场传播没有由这些集合长度算出。不是车体完整暴露时间，更没有预测气动峰值或相位。

### 表1坐标及测量位置

表1（PDF21）以设施坐标给A/C/E相同x+=3.75，B/C/D相同y+=0。乘L所得A(1.05,0.098)m、C(1.05,0)m、E(1.05,−0.098)m；B/D的x分别0.91/1.19m。A/E的表内D_y分别0.322/0.126m，BCD为0.224m。

ANALYST_INFERENCE：五行满足D_y+−y+=0.8，等价表内辅助出口横向基准y+=−0.8；这不是欧氏最近壁距、沿射流轨迹长度或测得传播速度。B到D的Δx=L，只在另加“平直前沿以恒定U传播”的理想化下才对应一个T_ref，不能把它当局部实测到达差。t+=0仍是全局触发，不按每点改零。

原文PDF25–26计划未来迎风侧沿B/C/D，推荐车模几何中心(3.43,0.33)，见E-2013-08。它不是测量点C的位置、车辆CG或当时已经存在的车体实验，也不直接给出车体宽度。不得用该建议替代2014的实际车模、位置和21°输入。

## 原图复现需要的输入

新增唯一请求 **NC-2013-GUST-REPLAY**，见[collection requests](../needs_collection.csv)与[交付表](reproduction_inputs.csv)。只针对现有源，未新增source、检索或联络。

|部分|原文已知|仍需实际输入|
|---|---|---|
|PIV与Fig9/12|500Hz、15次均值、9窗、表1位置、局部风角定义|逐次时间戳/触发、坐标标定及窗变换/拼接、有效向量掩膜/筛选参数、原始或可合法再分析的矢量场、事件分组与均值处理；原图输出数值|
|挡板输入|20组、名义5ms间隔、12/30ms动作、互补出口|每组命令和实物角度/有效面积时间戳、触发偏移/抖动、漏流/通道几何与压降、入口历史；不能用猜测线性开度补齐|
|CFD与时序|静态网格、SA/SST、2ms、瞬时边界切换、双倍数值主段宽度|原网格/案例/边界ID、事件回调及实际切换日志、求解迭代/收敛准则、初始化场、记录与插值频率、探针提取方法，若存在则网格/步长对照|
|判定|位置特定的u/v/β对照、输入峰/建立行为|原始同步关系、用于区分到达/建立的定义、源内误差和输出比较设置；无数据不编RMSE、置信带或收敛阶|

交付CSV/JSON命名是策展人建议，非作者报告格式；没有声称数据存在于公共仓储，亦未向任何人发送请求。原文Fig11文字13.82/图注13.5的历史冲突保留。

## 可迁移的知识与停止边界

可迁移的是先核对命令时钟、叶片动作、局部输入、采样/数值网格和输出定义，并分开源内假设。5ms、12/30ms、23°–27°和约30%输入峰均为本设施工况，不提供通用修正。命令事件与时间网格不整除只证明实现细节必须说明，不证明数值结果错误或确定其误差。

本轮完成P3定义/时序/几何和可复现性审计；原始Fig9/12重放仍缺上述输入，保持learning backlog，不把派生算术宣布为原输出复现。没有新输入时不重复本页换算或再次解析同一PDF。

## 复算方法

以下标准库代码从CSV的源内参数重新计算20项派生量并核对米制表。它只检验记录/代数一致性，不验证实际装置或原始CFD。

```python
import csv
from fractions import Fraction as F
from pathlib import Path
base = Path("learning/audits")
rows = list(csv.DictReader((base / "volpe_2013_timing.csv").open(encoding="utf-8")))
p = {r["quantity"]: F(r["value"]) for r in rows if r["provenance"] == "SOURCE_REPORTED_PARAMETER"}
T, d = p["L_ref"] / p["U_ref"], p["d_x"] / p["U_ref"]
h, q, G = p["CFD_step"], 1 / p["PIV_rate"], p["gust_duration_plus"] * T
span = (p["channels"] - 1) * d
v = dict(T_ref=T, command_interval=d, command_interval_plus=d/T,
    gust_duration_nominal=G, PIV_interval=q, CFD_step_plus=h/T, PIV_interval_plus=q/T,
    command_to_CFD_step_ratio=d/h, command_to_PIV_interval_ratio=d/q,
    opening_to_command_ratio=p["opening_duration"]/d, closing_to_command_ratio=p["closing_duration"]/d,
    opening_to_CFD_step_ratio=p["opening_duration"]/h, closing_to_CFD_step_ratio=p["closing_duration"]/h,
    establishment_delay_E=p["establishment_delay_E_plus"]*T,
    establishment_delay_A=p["establishment_delay_A_plus"]*T,
    establishment_E_fraction_of_nominal_gust=p["establishment_delay_E_plus"]/p["gust_duration_plus"],
    establishment_A_fraction_of_nominal_gust=p["establishment_delay_A_plus"]/p["gust_duration_plus"],
    first_to_last_command_span_ideal=span, all_open_command_overlap_ideal=max(F(0),G-span),
    any_open_command_union_ideal=G+span)
for r in rows:
    if r["provenance"].startswith("ANALYST"):
        assert abs(float(v[r["quantity"]])-float(r["value"])) < 1e-10
assert d == p["command_interval_reported"] and d/h == F(5,2)
assert d/q == F(5,2) and span == F(95,1000)
assert v["establishment_E_fraction_of_nominal_gust"] == F(8,100)
assert v["establishment_A_fraction_of_nominal_gust"] == F(15,100)
for r in csv.DictReader((base / "volpe_2013_probes.csv").open(encoding="utf-8")):
    assert F(r["D_y_plus"])-F(r["y_plus"]) == F(8,10)
    for a,b in [("x_plus","x_m"),("y_plus","y_m"),("D_y_plus","D_y_m")]:
        assert abs(float(F(r[a])*p["L_ref"])-float(r[b])) < 1e-10
print("20 timing values and 5 probe coordinate rows consistent; not original-output replay")
```
