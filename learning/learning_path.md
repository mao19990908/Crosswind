# 阅读路径

1. [基础与研究链](01_foundations.md)：区分风输入、相对风角、车辆姿态和轨迹；先看 [术语表](glossary.md)。
2. [阵风与环境](02_gust_and_environment.md)：逐个区分自然风、有限风区、脉冲、正弦和风洞输入。
3. [非定常气动](03_unsteady_aerodynamics.md)：读准稳态比较、分量差异、超调和滞后。
4. [气动响应模型](04_aerodynamic_response_models.md)：从气动导数到频率响应；公式定义未核验处见 [公式账本](equations.md)。
5. [车辆动力学](05_vehicle_dynamics.md) → [实验方法](06_experimental_methods.md) → [CFD](07_transient_cfd.md) → [耦合](08_aero_vehicle_coupling.md)。
6. [三级验证](09_validation_and_metrics.md) → [标准](10_standards_and_test_methods.md) → [工程应用](11_engineering_applications.md) → [前沿问题](12_research_frontier.md)。
7. 返回 [概念地图](concept_map.md)、[方法演化](method_evolution.md)、[开放问题](open_questions.md)；沿证据 ID 追溯资料。

当前已有摘要与全文混合证据，逐条等级见source/claim；学习15完成、10项待办，未取得的原文或原始实现数据仍阻断对应Pass3。`paper_notes/pass_status.csv` 给出实际进度，不用文件数量或综合章节完成代替原始输出复现。

读06–09章时，先对照[测量链](audits/measurement_chain.md)，再看[CFD/耦合证据](audits/cfd_coupling_evidence.md)：通道与测点、空间与时间格式、规定运动与反馈、固定转向与驾驶员、积分步与交换时刻分别解释。最后回到各来源的页段和开放请求；图谱关系不能绕过这些条件。
