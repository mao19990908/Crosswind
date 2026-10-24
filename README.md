# 车辆瞬态侧风（阵风）知识库

本仓库持续整理道路车辆瞬态侧风／阵风的历史、理论、实验、CFD、车辆动力学与耦合验证证据。研究主线是：

> 阵风输入 → 非定常气动载荷 → 横向／横摆／侧倾响应 → 驾驶员或控制器修正

## 当前学习断点（2026-10-25）

两项既有核心全文待办限定查找：Lay1953补记Vol61(1953)公共实体馆藏入口；ISO2010确认ANSI公开预览不完整，本机下载403即停，未存PDF。不把馆藏、预览或零售商free片段当合法完整原文。学习23完成/2待办、9open复现请求、91claims/282edges/32citations保持；25sources/19本地全文PDF、缺全文6。见[入口与边界](sources/access_check_2026-10-25.json)。不重开已验收8篇，不扩库。

### 上轮记录（2026-10-24）

按任务书P3六项理解要求逐篇验收8份已有全文笔记/专项审计，纠正我把“原图重放”当成学习完成硬门槛的额外解释。学习已完成23、待办2（Lay1953/ISO2010仍待核心原文）；这不是8次新读或8项独立复现。原始数据/代码9项请求全部open，未决假设/符号/接口/验证边界保留。91claims/282edges/32citationedges、25sources/19本地PDF、缺全文6及源等级保持。见[规则依据与8行验收矩阵](learning/audits/pass3_acceptance_review_2026-10-24.md)。当前仍Learn，不扩库或推进写作阶段。

### 上轮记录（2026-10-23）

为昨日新增Volpe2013原始输入请求做一次限定补档检索，未找到可验证PIV/挡板/CFD数据；查询范围不代表数据不存在。未重做已完成审计，不新增知识主张/节点/图边。现25sources、19本地PDF、91claims/282edges/32citationedges，学习15完成/10待办、9open原始请求、缺全文6保持。下一验收真实新输入或新核实线索，同查询不每日重试。见[本轮查询与边界](sources/access_check_2026-10-23.json)。

### 上轮记录（2026-10-22）

完成Volpe2013 Pass3的挡板时序、探针坐标与原图复现条件审计：分开5ms顺序命令、12/30ms动作、2ms计算/采样及局部建立延迟；名义命令区间推导标为分析者结论，5ms/2ms非整比不反推原算法。新增2条原文主张、1分析者公式、11图边；89旧claims保持，现91claims/282edges/32citationedges。新增该既有源唯一原始输入请求，9open；25sources、19本地PDF、缺全文6保持。学习15完成/10待办，原Fig9/12未复现，下一仅验收真实输入，不重复本次换算。见[审计与可复算表](learning/audits/volpe_2013_shutter_timing.md)。

### 上轮记录（2026-10-21）

取得并通读长期缺档Volpe2013的HAL作者稿：从摘要升级全文，补明空场风场验证、局部风角23°–27°/设施输入峰及挡板动作理想化；纠正Ryan2000博士论文与同年SAE文章的引用身份。新增5条主张、修订1条，更新6既有节点的来源绑定，新增11图边和1引用边；现89claims/271edges/32citationedges。4个来源矩阵同步。25sources、19本地PDF，缺全文降至6；仅1份PDF具GitHub许可，新增文件保持本机。学习15完成/10待办，下一`jfe-2013-volpe` Pass3时序与复现条件，未宣称原图已重放；8项既有原始请求保持。见[全文记录与证据地图](sources/records/jfe-2013-volpe.md)。

### 上轮记录（2026-10-20）

补原文证据解释“气动矩近零仍会横摆”：区分气动力作用位置、CG与NSP，以及气动矩/轮胎矩。新增3条E2claims、1变量/1分析者公式、9图边；现84claims/260edges/31citationedges。用Winkler标准参数核对零横摆率配平系数，未重放9.7°时程或识别NakasatoNSP；扩充1项既有请求。25sources、学习15完成/10待办、8open请求保持。见[NSP与横摆](learning/audits/neutral_steer_point.md)。

### 上轮记录（2026-10-19）

补齐基础章的航向/车辆侧偏/相对来流接口：明确右手平面坐标、空气流向及速度参考点，给出分析者向量推导和8个可复算例子（含象限、零速退化和共同旋转核对）。新增1分析者公式、更新4既有节点、4图边；81claims保持，现251edges/31citationedges。原始速度/轴映射仍需数据，未重放作者曲线。25sources、学习15完成/10待办、8open请求保持。见[相对来流运动学](learning/audits/relative_wind_kinematics.md)。

### 上轮记录（2026-10-18）

完成四篇既有CFD原文数值方法页复核：新增7条E2主张，修订1条风角冲突表述；分开空间/时间格式、网格伪差、数值收敛、实际运动反馈及交换时序。新增2方法＋2分析框架节点，更新5节点，新增24图边；现81claims/247edges/31citationedges。07/08章重写，概念地图/阅读路径同步修正；原始模型未重放。25sources、学习15完成/10待办、8open请求保持。见[CFD与耦合证据](learning/audits/cfd_coupling_evidence.md)。

### 上轮记录（2026-10-17）

完成七来源实验处理链综合，区分测点/通道、标定/动态频响、共同/相对延迟、平均曲线峰/逐次峰均值以及固定时刻/选峰不确定度。13项显式合成检查通过；新增2方法＋2分析者公式、10图边，更新1方法；74claims保持，现223edges/31citationedges。实验方法及验证章节已接入已有全文证据。25sources、学习15完成/10待办、8项原始请求均保留。见[测量链与反例](learning/audits/measurement_chain.md)。

### 上轮记录（2026-10-16）

完成十来源阵风/响应指标比较，区分峰/均值、峰/稳态、正弦幅值、功率导纳和车辆指标；构造同幅异相的合成反例，7频率检查及341行时程/独立图已核。新增2变量＋2分析者公式、13图边，更新9概念；74claims保持，总213edges/31citationedges。更新输入/非定常/响应模型/验证章节。sources25、学习15完成/10待办，原始输出仍等待新数据。 见[比较与反例](learning/audits/gust_response_comparability.md)。

### 上轮记录（2026-10-15）

完成六源规范化/坐标/原点知识综合，交付载荷重新表达工具和8项原始数据交付表；16个合成检查通过，真实作者曲线仍待数据。新增2方法＋1分析者公式、12图边/修订1边；74claims逐字段保持，现200edges/31citationedges。修正车辆动力学、验证表、方法演化、术语及Winkler笔记的过时摘要描述。Bell/Milner原文与既有rawdata定向查找未取得新文件。sources25、学习15完成/10待办、缺全文7。 见[综合与工具](learning/audits/load_reexpression.md)。

### 上轮记录（2026-10-14）

今日复核既有ISO/DOT缺档目录，DOT技术卷补充检索标识PB80-118383；未取得原文。学习15完成/10待办、74claims/188edges、8项原始数据请求保持。现25sources/18localPDF，缺全文7。见[访问记录](sources/access_check_2026-10-14.json)；等待已有缺档或新数据，不重复审计。

### 上轮记录（2026-10-13）

当前25sources、15学习完成/10待办；74claims/188edges。今日为已有Lay/Lett1953和Volpe2013复核DOI/OA入口，未取得新PDF，无新增知识主张。现18份本地PDF/1份可推送，缺全文7；8项原始数据请求保留。下一先处理已有缺档和新输入，不重复已完成审计。见[访问记录](sources/access_check_2026-10-13.json)。

### 上轮学习记录（2026-10-12）

Nakasato2017 Pass3纠正Fig26初始A9%/出风反向B17%；识别试验辅助定参及纯时延，CG/步长定义已核，原始接口/模型/时程仍待补。新增2claims、1公式/1方法、8图边，现74claims/188edges；学习15完成/10待办，8个open requests。下一先检查已有缺档/请求的新输入，sae-530255合法全文优先，不重复已完成定义审计。无新source/PDF。 见[审计](learning/audits/nakasato_2017_driver_frames.md)。

### 上轮学习记录（2026-10-11）

Lewington2017 Pass3核实QS地面轴距中点参考和偏移积分；恒速等条件下yaw项可抵消，SD不能冒充95%CI。新增2claims、2公式、8图边，现72claims/180edges；原始样条/坐标和逐次试验数据待NC-2017-1515-REPLAY。学习15完成/10待办，下一sae-2017-01-1525 Pass3。见[审计](learning/audits/lewington_2017_axes_splines.md)。无新source/PDF。

### 上轮学习记录（2026-10-10）

Winkler2016 P3核得时间尺度29.312与条件性增益单位匹配；Eq11/12转向符号仍需原始代码。新增1证据/1公式/3图边，现70claims/172edges；学习15完成/10待办。既有NC-2016-VALIDATION已扩充，无新source/PDF。下一sae-2017-01-1515 Pass3。见[公式与尺度审计](learning/audits/winkler_2016_controller_scaling.md)。

### 上轮学习记录（2026-10-09）

Winkler2016既有PDF完成全文P2，证据由摘要升级全文；澄清无驾驶员＋两套增益及路径偏差7.3/6.3/3.9%的条件，参数趋势不当实测验证。新增3claims、1方法/1公式和12图边；现69claims/169edges/31引文边，全文17条。学习15完成/10待办；下一同源P3控制器符号、尺度与参考点审计。见[全文审计](learning/audits/winkler_2016_fulltext.md)。无新source/PDF。

### 上轮学习记录（2026-10-08）

Ryan1998 Pass3核实侧面积形心参考点和轴向速度归一化；明确与Macklin总速/轴距定义不同。新增2claims、1公式节点、7图边，现66claims/157edges。原始积分仍缺数值权重/时程，登记NC-1998-INTEGRATION；学习15完成/10待办。下一jcp-2016-tunay先做全文P2，再续P3。见[审计](learning/audits/ryan_1998_pressure_reference.md)。无新source/PDF。

### 上轮学习记录（2026-10-07）

续接Macklin1996 Pass3，核对力矩统计窗口、Hamming滤波信息及地面参考点；75mm距底板不可当总平移高度，力矩系数长度为轴距。新增2claims、1公式节点和7条边；现64claims/150edges。原始输出复现缺输入，已登记NC-1996-SIGNAL-AXES。学习仍15完成/10待办，下一sae-980392 Pass3。见[审计](learning/audits/macklin_1996_signal_axes.md)。

### 上轮学习记录（2026-09-28）

Beauvais1967 Pass3已核对相对风、天平组合及归一化：图中分母是3车长处动态平台，速度图注与正文范围仍有矛盾。新增2条claim、1个公式节点，补全既有EQ-RELWIND，新增8条图边；现62条claims/143边。原始数据不足，已登记NC-1967-REPRO，学习仍15完成/10待办；下次sae-960674 Pass3。见[复现审计](learning/audits/beauvais_1967_reproduction.md)。无新资料或PDF。

### 上轮学习记录（2026-09-27）

续接Hucho1973 Pass3，核对参考面积/点/角定义，并由原积分推导两类车底修正，数值积分检查通过。Fig11/12因原始输入缺失仍未复现，已登记两条collection请求。新增2条claim、2个公式节点和8条边；图谱现135边。学习仍15完成/10待办，下一来源为sae-670608 Pass3。详情见[方程审计](learning/audits/hucho_1973_equations.md)和[学习断点](learning/state.md)。最新heartbeat以学习backlog优先；没有新资料或PDF。

## DOI/PDF审核快照（2026-09-26）

全量审核 25 条：DOI verified 20、no_doi_confirmed 5，其余状态 0；本机 PDF 18、GitHub 1、仅本机 17。全文已核 16 条，学习已完成 15、backlog 10，当前 `sae-730232` Pass 3。下文带日期的进度段为历史快照。

本轮没有新资料或 PDF。DOT 两卷新找到 HathiTrust Full view 馆藏及 Google Books 免费入口，但读者端 403/API 429；Volpe 2013 新找到 OATAO 作者仓储，连接超时。开放入口候选共 3 项，仍缺全文 7 项；[补档队列](sources/manual_retrieval_queue.md)保留可操作链接。Durham 2000 已有用户 PDF，不再属于缺档。DOI/PDF 断点继续，暂不扩大来源库。详见[全量审核](sources/doi_pdf_audit_2026-09-26.csv)。

## 证据边界

- 瞬态阵风与固定偏航角稳态侧风分开记录；稳态结果仅作为基线或准稳态输入。
- open-loop、closed-loop driver、closed-loop controller 与 autonomous control 分开比较。
- `metadata_only`、`abstract_verified` 与 `full_text_verified` 不混用。
- 未报告参数写“未报告”；分析者推断显式标为 `analyst_inference`。
- GitHub 不保存无再分发授权的受版权保护全文、内部数据或大型计算文件；用户提供的合法研究副本可在本机 `sources/pdfs/` 登记并由 `.gitignore` 排除。
- 每条资料同时记录研究主题类别 A–M 与规范发布类型 `source_type`；资料不只限于论文。

## 资料类型覆盖

来源总数和各 `source_type` 数量以 `sources/index.csv` 为准。v3 强制检查的类型包括：

`journal_article`、`sae_technical_paper`、`conference_paper`、`standard`、`government_report`、`institutional_report`、`doctoral_thesis`、`master_thesis`、`dataset`、`facility_documentation`。

当前索引共 25 条；分类型覆盖与尚未检索的类别判断见 [database_coverage.md](search/database_coverage.md)。

## 导航

- [任务书](TASK.md)
- [全文证据层规则](Crosswind_Learning_Knowledge_Graph_PDF_Evidence.md)
- [历史时间线](history/timeline.md)
- [分类体系](taxonomy.md)
- [检索覆盖率](search/database_coverage.md)
- [来源索引](sources/index.csv)
- [规范 Bib 文献库](sources/bibliography/references.bib)与[元数据、摘要来源台账](sources/bibliography/bib_sources.csv)
- [需要用户手动查找的全文](sources/manual_retrieval_queue.md)
- [全库去重复核](sources/dedup_report.csv)与[旧 ID 映射](sources/aliases.csv)
- [方法谱系](citations/method_lineages.md)
- [研究现状](synthesis/state_of_the_art.md)
- [研究空白](synthesis/research_gaps.md)
- [当日日志](logs/2026-10-11.md)

当前处于 Phase I：先建立可追溯的历史与方法地图，不把初步线索包装成成熟综述结论。

## v5 书目、去重和补档（2026-09-25）

v5 迁移时的 23 条资料及随后新增的 1967 Beauvais SAE、1958 Benner 期刊来源，目前共 25 条，均有稳定 ID 对应的 Bib 条目；[Bib 来源台账](sources/bibliography/bib_sources.csv)逐条给出元数据和摘要来源。仅有明确 CC BY 4.0 再利用依据的 SAE 2025 摘要复制进 Bib；其他官方/仓储摘要仅标明可得来源，未整段复制。`abstract_status` 与 `verification_status` 分开：有摘要不代表已核读全文。

首次全量检查 DOI、SAE/标准/报告号、规范化题名和近似题名后，没有确认的真重复项，因此没有删除旧记录，[aliases.csv](sources/aliases.csv)目前只有表头。3 对相关版本/设施延续来源保留为不同资料，判定理由见[去重报告](sources/dedup_report.csv)；报告 Volume I/II 新增 `companion_report` 边。现有 3 份本机 PDF 重新核对文件头、可读页数、题名和 SHA-256；Passmore、SAE 2025 两条为 `full_text_verified`，Brandt 92 页学位论文 PDF 只有扩展摘要与文献目录、不含 Paper A–E 原篇，保持保守的 `abstract_verified`。

[人工补档清单](sources/manual_retrieval_queue.md)原有 21 条待补全文，其中 14 条已于 2026-09-25 从用户提供目录收件并校验 PDF，仍有 7 条待人工查找。CSV 保留全部 21 条的处理轨迹，Markdown 只列当前未解决项。PDF 收件不等于研究级通读；新文件进入 learning backlog，原有摘要级结论需按全文重新检查。

## 本地全文 PDF

合法取得的 PDF 登记在 `D:\GEELY\Crosswind\sources\pdfs\`。旧 `local_fulltext\` 副本保留。两目录默认被 `.gitignore` 排除；只有明确允许再分发的 PDF 才逐个 `git add -f` 纳入 GitHub。

Passmore 作者存档与 Brandt Chalmers 学位论文仅本机留存；前者已核读全文，后者已核读仓储 PDF 的扩展摘要页段（其 Paper A–E 附录原篇不在该 92 页文件内）。SAE 2025 出版者 PDF 首页明确 CC BY 4.0，已核验并纳入 GitHub。用户提供的 14 份 PDF 已核对题名/编号、可读页数、大小和 SHA-256，保存为本机研究副本；其 SAE 版权标记或 Elsevier 许可情况没有提供公开再分发依据，故不推送文件本体。当前 **本机 PDF 18 份、GitHub PDF 1 份、仅本机 17 份**。

其中 Beauvais 1967、Hucho/Emmelmann 1973 和 Benner 1958 已进入 `full_text_verified` 并完成 Pass 1–2；其余 12 份新收件全文等待逐篇研究级复核。当前全库 `full_text_verified` 5 条，学习 backlog 17 条（含因新证据重开的条目）。

2026-09-25 后续进度：又完成 Macklin 1996、Ryan 1998、Macklin 1997 与 Ryan/Dominy 2000 四份用户 PDF 的逐页核读。现 `full_text_verified` 为 9 条，尚有 9 份本机 PDF 待研究级核读；学习目标已完成 10 条、backlog 15 条（另有 Hucho 1973 Pass 3 部分公式核验）。1997 年垂向廓线实验的剪切与湍流混杂、2000 年 Durham 新挡板装置与 1998 年条件差异，均已在原始记录及图谱中标明。PDF 本机 18、GitHub 1、仅本机 17 的版权分流不变。

后续又核读 Mahig 1971、Klein/Hogue 1980、Chadwick 2000、Nakasato 2017、Volpe 2014：全库 `full_text_verified` 14 条，本机 PDF 研究级待核 4 份；learning 已完成 14 条、backlog 11 条。新增的原始引文显示 1980 SAE 文部分取自 DOT 技术报告 Volume II；2014 Volpe 双风洞适配自 Ryan/Dominy 2000，但 30° 风洞夹角对应模型处约 21° 实际偏航。Nakasato 的定量车辆响应验证是固定转向，驾驶员闭环应用的验证证据另计。

再核读 Lewington 2017 与 Okumura 1997 后，全库 `full_text_verified` 16 条，待研究级核读的本机 PDF 2 份，learning 已完成 15 条、backlog 10 条。Lewington 的单向 CFD 优势依赖响应指标；两方法的横向偏移都落在测试一标准差内。Okumura 文中速度与报告的合成偏航角算术不一致，作为待核矛盾保存。

## DOI / 合法全文台账（2026-09-25）

现有 25 条来源全部纳入 [DOI 总账](sources/doi_registry.csv)：20 条 DOI 经 Crossref 精确核验，5 条按当前官方目录及 Crossref/DataCite 题名检索暂列 `no_doi_confirmed`（ISO 原标准、1979 两卷 DOT 报告、Chalmers 学位论文、1968 Milner 期刊条目），`missing_to_search` 为 0。原始题名页或新登记可改变无 DOI 判断；BS ISO 采用版 DOI 不归给原 ISO 记录。**DOI 覆盖率 20/25 = 80.00%**。

公开全文已验证 3 份：Passmore 作者版、Brandt 学位论文、SAE 2025 出版者版。早期 Durham 2000 与 HAL 2013 仓储请求分别返回 403 和 bot challenge；Durham 后已收到用户 PDF，HAL 对应 Volpe 2013 仍缺全文。其余条目的付费或未找到状态只描述已查入口，不能解释为永久无 OA。Passmore 封面与仓储许可版本不一致、Brandt 仅明确可公开访问，两份仅本机保留；SAE 2025 许可 CC BY 4.0，允许署名再分发。来源、大小、SHA-256 和许可边界以 DOI 总账为准。

### 2026-09-25 追加：出版者 CC BY 全文

[SAE 2025 风洞阵风发生系统论文](https://doi.org/10.4271/15-18-01-0005)的出版者 PDF 首页明确标示 CC BY 4.0，已核对题名、DOI、16 页和 SHA-256，并按署名许可纳入 GitHub。其余本机 PDF 仍不推送；实时数量以 DOI 总账为准。

### 2026-09-25 追加：Benner 1958 历史全文

用户提供的 [Benner 1958](https://doi.org/10.1175/1520-0477-39.8.421) 六页期刊论文已存入本机 `sources/pdfs/bams-1958-benner__benner__1958.pdf`，全文 Pass 2 已完成。论文 p.425 reference 5 明确引用 Lay/Lett 1953；其道路仪器说明属于被引研究的历史转述，1955 Ford 的固定风洞例子不计作瞬态阵风试验。该 PDF 再分发许可未核实，所以只同步全文结构化记录、书目、证据节点和引文关系，不推送 PDF 文件。
