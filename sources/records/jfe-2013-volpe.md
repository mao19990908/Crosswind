# jfe-2013-volpe — Experimental and Numerical Validation of a Wind Gust Facility

## Bibliographic information

Raffaele Volpe; Arthur da Silva; Valérie Ferrand; Luis Le Moyne. 2013, Journal of Fluids Engineering135(1),011106/1–011106/9. DOI [10.1115/1.4023194](https://doi.org/10.1115/1.4023194). Canonical Bib key: `jfe-2013-volpe`. GB/T7714: VOLPE R, DA SILVA A, FERRAND V, et al. Experimental and numerical validation of a wind gust facility[J]. Journal of Fluids Engineering,2013,135(1):011106.

## Access / verification

Current2026-10-21: `full_text_verified`; `oa_downloaded`; author-deposited manuscript from [HAL public file](https://hal.science/hal-01920549/file/Ferrand_8416.pdf), discovered through public HAL API `files_s`. Local `sources\pdfs\jfe-2013-volpe__volpe__2013.pdf`; 3,240,703bytes;30pages; SHA256 `b6fb24a6c19f6624b4c868740ed07e4abbf45053b0128fac6b3d42c41da15eee`; readable and unencrypted. Pages1/2 are HAL/OATAO covers; **PDF page = manuscript page+2**. Journal's nine-page layout must not be used to locate this28page manuscript. Title/authors/DOI match both covers and manuscript. Rights: repository public access, no explicit redistribution license in API/file; `github_pdf=false`. Historical /document challenge/ASME403/OATAO timeout remain history, not today's result. [Access proof](../access_check_2026-10-21.json).

## Research question

顺序挡板双风洞能否在预定区域生成移动侧向阵风？3D URANS能否重现空场速度演化？本文提供风场Level A的对照证据，车辆测力在文中仍是后续计划，没有车辆载荷或运动结果。

## Physical problem

主风洞纵向气流与辅助风洞斜向射流相互穿透。顺序开启双挡板使射流前沿沿主流移动，互补出口用于限制通道流量随开启数量的变化。两风洞的30°夹角是硬件方向，不能直接代替局部来流角。

## Gust / crosswind definition

§2.1–2.2，稿件6–9/PDF8–11：20通道；主流9m/s；辅助流9/cos30°=10.39m/s，目标横向分量5.20m/s。参考长度0.28m，Re=1.68e5；名义阵风10L/U=0.311s。参考长度为未来车模设定，不是本次车辆响应测量。Fig4给出0.045m通道间距和名义顺序间隔0.005s；不能混同单挡板开启/关闭动作时间或采样间隔。

## Coordinate system and normalization

Fig6/§4，稿件10/16（PDF12/18）：设施固定坐标，原点在主风洞起始处、下半截面中心；x为下游、y为横向、z为竖向。长度除以Lref、速度除以Uref=9m/s，t+=tUref/Lref。零时刻为首个挡板开启，不是局部阵风到达。报告正向u工况下β=atan(v+/u+)为气流方向角，不是车辆航向或侧偏角。建立区间、建立延迟、名义10长度持续时间分别记录。

Table1/PDF21：A(3.75,0.35)、B(3.25,0)、C(3.75,0)、D(4.25,0)、E(3.75,-0.35)，依次距辅助出口D_y+=1.15/0.8/0.8/0.8/0.45。坐标均为原文无量纲值，不是车体CG坐标。

## Vehicle / model geometry

本次空场，没有车模。未来参考车长0.28m，计划抬高地板；主试验段0.45×0.21m，辅助末端0.90×0.15m，竖向居中。PDF26建议未来迎风侧沿B/C/D，几何中心(x+,y+)=(3.43,0.33)。不能与2014 Windsor车模0.25m或约21°实测输入混用。

## Experimental setup

PDF11–12：实际TR-PIV为500Hz，首挡板触发，15次事件相位平均；水平面位于主截面半高（未来车模3/4高），分为9个134×105mm测窗。最终相关窗64pixel、50%重叠，空间分辨率3.5mm；用信噪比/空间速度波动筛查向量。粒子St=0.002。相机最大1kHz和激光最大10kHz均为设备能力，不是实际采样率。分窗和重复事件不能证明单事件全场同时测量；该稿没有提供完整原始场或总置信区间。

## CFD setup

§3，PDF12–18：ICEM11/Fluent6.3；不可压3D URANS，SA与SST k–ω；140万结构单元，域尺寸7.05×5.7×1.34（参考长度归一化）。数值主风洞宽度为实物两倍，以远离出口边界。入口湍强2%来自热线估计；计算后检查y+=51–89。挡板以固定平面壁面条件切换代替动作，忽略转轴与真实泄漏。

空间二阶中心、时间一阶隐式，恒定2ms步长；以全关闭稳态初始化。未取得原始网格/求解器文件，文中没有量化目标输出随网格和时间步变化的序列；单元质量不能替代瞬态输出收敛证据。

## Vehicle-dynamics model

not applicable；没有轮胎、驾驶员或车辆运动求解。

## Coupling method

not applicable；PIV与CFD比较设施流场，不是气动—车辆运动耦合。

## Important equations

稿件Eqs1–4为无量纲URANS/SA/SST方程，Eqs5–6为入口湍流参数构造（PDF13–15）。用于解释结果的是源内t+=tUref/Lref和β=atan(v+/u+)（PDF18/23）。Fig4的顺序触发间隔、名义持续时间与有限实物动作时间分开。复杂输运式不依据有损文本提取重新转录。

## Important parameters

主流9m/s，辅助流10.39m/s，参考长度0.28m，名义阵风10参考长度；TR-PIV实际500Hz、15次重复、3.5mm空间分辨率；20组双挡板；CFD140万单元、2ms；真实开启12ms、关闭30ms。局部建立风角A点23°至E点27°。均为作者报告，非本轮新测量。

## Main quantitative results

PDF19：建立延迟δt+从E点0.8到A点1.5，作者换算24.9–46.7ms；实际建立区间短于名义10长度阵风。PDF24–26：E点来流风角在t+=4.7的峰比其自身建立值高约30%，这是设施输入，不是车辆横摆力矩峰。CFD偏早到达，横向速度/风角未充分稳定；两种湍流模型行为相似不等于无误差。PDF22报告C点模拟TI为2.1%（t+=7.97），去掉挡板模拟2.5%；不是普适抑湍规律或独立实测结论。

## Flow / aerodynamic mechanisms

Fig10中作者解释：主流绕行横向射流前沿而局部加速，关闭阶段排出剩余射流而减速。辅助流压力损失随挡板状态变化是横向峰值的候选解释；装置没有Ryan使用的下游蜂窝，峰值仍存在。瞬时数值开关与真实12/30ms动作的区别是作者对数值到达/建立失配的解释，未形成独立控制的因果误差分解。

## Validation method

Fig9五个探针的u/v历史、Fig11/12风角场与历史比较15次重复PIV均值和SA/SST。只支持风场Level A；不含车辆载荷B或运动C。局部缺示踪导致PIV遮罩，空间输入也不均匀。原文没有提供本轮可重放的原始数据或输出网格/时间收敛序列。Fig11最后快照时刻，PDF23正文写t+=13.82，而PDF24图标/图注写13.5；保留冲突，不自行订正。

## Main conclusions

该设施产生移动侧向射流，实际输入风角随位置变化。接近挡板可增加局部风角、缩短建立延迟，也会增加寄生峰。应先核对模型位置的输入，再解释车辆非定常载荷；3D URANS定性吻合不能消除边界切换理想化的限制。

## Limitations

本文为空场；所展示工况的主流速度和名义持续时间单一；15次均值不提供逐次离散度或总置信区间。原始图像、挡板动作历史和求解器文件未随该稿提供，也未给出量化输出收敛研究。压力降平滑模型只是结论中的后续初步工作。2014年的0.25m车模、约21°来流和测力结果分别来自其自身原文，不能回填本篇。全文Pass 2已完成；2026-10-22完成Pass 3定义/时序/几何与复现条件审计，原图重放仍待NC-2013-GUST-REPLAY，不称全部Pass 3完成。

## Relation to previous work

§1.3/2.1/3.2和PDF29的ref16明确为Ryan2000 Durham博士论文，而非SAE2000-01-0874。既有指向SAE文章的方法概念边仍只依据外部2018原始研究，不改成本文直接引用。PDF28 ref4引用SAE670608，PDF29 ref14引用Passmore2001，PDF30 ref22引用Macklin1996。未新增博士论文source或声称读过该论文。

## Relation to subsequent work

既有Volpe2014原文引用并延伸2013设施研究；后者的车体载荷、风角和几何参数保持独立。

## Relevance to 车辆侧风模拟及实验验证

在模型位置核对真实输入及其峰、相位和空间变化；区分装置夹角、局部来流角和车辆横摆；区分有限挡板动作与瞬时数值开关；分别核对风场、载荷及车辆运动的验证对象。

## Follow-up questions

时序/坐标定义审计已经完成，见[2026-10-22审计](../../learning/audits/volpe_2013_shutter_timing.md)。只等待NC-2013-GUST-REPLAY所列实际PIV/挡板/求解器输入，不再次通读/下载同哈希、重复名义换算或虚构原图重放。

## Evidence map

Allitemsuse`jfe-2013-volpe__volpe__2013.pdf`;printednumbersrefermanuscript,notjournalpagination.

|Claim|PDF / manuscript|Section / figure|Boundary|
|---|---|---|---|
|E-2013-01updated|8–12;26–27 /6–10;24–25|2;5|EmptyfieldA;vehiclefuture|
|E-2013-02|10–12 /8–10|2.2;Figs4–6|500Hz15eventmeans;9windows|
|E-2013-03|19;21;24–26 /17;19;22–24|4;Figs9/12;Table1|Localβ/delay,notvehicleload|
|E-2013-04|15–18 /13–16|3.2;Figs7/8|Reportedresolution,notconvergence|
|E-2013-05|17;20;25;27 /15;18;23;25|3.2;4;5|Authoractuationhypothesis|
|E-2013-06|7–8;16;28–30 /5–6;14;26–28|1.3;2.1;3.2;refs4/14/16/22|RyanthesisidentitydistinctfromSAE|

## 2026-10-22 Pass 3 timing / reproduction checkpoint

本机原文PDF9–12/16–21/23–26靶向核对，9整页视检；未新收集或重新通读全稿。新增E-2013-07（顺序双挡板/5ms间隔）与08（未来迎风侧/几何中心规划），全部旧89claims保持。复杂代码/原图输出没有恢复。名义时序与探针坐标的源内数值及分析者派生见[时序CSV](../../learning/audits/volpe_2013_timing.csv)和[坐标CSV](../../learning/audits/volpe_2013_probes.csv)。

ANALYST_INFERENCE：5ms/2ms=2.5，只说明若固定网格节点执行全部事件则无法精确表达全部相邻命令，原文实际事件处理算法未知；不据此认定CFD误差或伪造2/3步切换。Fig4的绝对dt起点可平移至§4首触发零点。理想矩形命令条件下20门相邻触发跨度95ms、全开命令交集216.111ms、任意门并集406.111ms，均不代替单门名义持续311.111ms或实测局部平台/速度历史。原动作12/30ms、15事件/9测窗的实际同步、原CFD事件日志等缺口统一写入NC-2013-GUST-REPLAY（未检索或联络）。

|新claim|PDF / 稿件|定位|边界|
|---|---|---|---|
|E-2013-07|9–10 /7–8|§2.1;Figs3/4|装置顺序命令与互补出口，非真实叶片轨迹|
|E-2013-08|21;25–26 /19;23–24|Table1;Figs9/12;§4/5|计划的几何中心，非CG或已测车辆|

## Historical access / abstract record (superseded by current full text)

以下保留2026-10-21以前的访问历史和摘要阶段临时结论；以本节之前的现行全文结论为准。

# jfe-2013-volpe — Experimental and Numerical Validation of a Wind Gust Facility

## Bibliographic
- ID: `jfe-2013-volpe`; Authors: Raffaele Volpe; Arthur da Silva; Valérie Ferrand; Luis Le Moyne
- Year / venue: 2013, *Journal of Fluids Engineering* 135(1), 011106/1–011106/9
- DOI / URL: [10.1115/1.4023194](https://doi.org/10.1115/1.4023194)
- GB/T 7714: VOLPE R, DA SILVA A, FERRAND V, et al. Experimental and numerical validation of a wind gust facility[J]. Journal of Fluids Engineering, 2013, 135(1): 011106.

## Access / verification
- access_status: abstract; access_level: abstract; verification_status: abstract_verified
- source_type: journal_article
- publisher_or_institution: ASME; ISAE-SUPAERO
- report_or_standard_number: 011106
- evidence_type: dynamic_wind_tunnel; validation_level: compared_with_CFD
- DOI/title/authors/volume verified via [Crossref](https://api.crossref.org/works/10.1115%2F1.4023194); abstract and open-access deposit metadata verified via [HAL](https://hal.science/hal-01920549v1).

## Classification and method
- Primary category F; secondary categories B,H,J. Stationary ground-vehicle model, lateral moving gust, double wind tunnel, time-resolved PIV, three-dimensional URANS.
- The primary abstract explicitly describes the Ryan–Dominy proposed facility as its starting point. It does not identify which Ryan–Dominy publication or provide enough detail to assert exact hardware inheritance.
- A [2018 Springer primary methods article](https://link.springer.com/article/10.1007/s00348-018-2586-0) explicitly identifies Ryan–Dominy (2000, DOI 10.4271/2000-01-0874) as the predecessor adapted by Volpe et al. (2013). This corroborates the **conceptual** method link to `sae-2000-01-0874`; the 2013 article's own reference number and hardware details still require full text.
- Compared the two wind-tunnel streams' interpenetration and simulated/observed gust development. Gust amplitude, spatial gradient, Reynolds number, mesh, timestep, uncertainty, detailed vehicle loads and results: **not reported in accessible abstract**.
- Level A gust-field/facility validation only in the accessible abstract. Do not infer Level B vehicle forces or Level C vehicle motion/driver response.

## DOI / legal PDF status (2026-09-25)
- doi_status: `verified`; doi_verified_date: 2026-09-25; doi_source: https://api.crossref.org/works/10.1115%2F1.4023194.
- pdf_status: `open_repository_available`; pdf_source: https://hal.science/hal-01920549/document; pdf_path: `none`; pdf_sha256: `not applicable`; pdf_bytes: not applicable; pdf_license: `repository_open_access_redistribution_unclear`; github_pdf: false.
- HAL API lists `openAccess_bool=true` and a document URL. The document request returned an HTML bot challenge, **not a PDF**. No challenge bypass was attempted, no file was retained, and no full-text claims are made. ASME's Crossref PDF resource has no open license in the checked metadata.

## Method lineage / follow-up
- The 2014 Volpe et al. paper's Crossref reference list cites this 2013 article by title/author/year. This is a verified reference edge, not proof that every apparatus detail was reused.
- The 2013 article's Crossref-deposited references B22 and B14 match `sae-960674` and `pimeche-2001-passmore`; the 28 deposited references do not include `sae-2000-01-0874`. This does not negate the independently corroborated conceptual facility lineage, but no direct 2013→2000 citation is asserted.
- Obtain the official HAL PDF through ordinary authorized access, verify file identity and reuse license, then perform Pass 2/3 on calibration, PIV–URANS comparison, and its relationship to the 1998/2000 Ryan–Dominy studies.

## Bibliography and abstract provenance (2026-09-25)

- Canonical Bib key: `jfe-2013-volpe` in `sources/bibliography/references.bib`.
- abstract_status: `available_not_copied`; abstract_source: Crossref deposited publisher abstract; abstract_source_url: https://api.crossref.org/works/10.1115%2F1.4023194.
- Full-text check: No full text has been validated; do not promote claims beyond the current evidence level.

## 2026-09-26 DOI/PDF access checkpoint

Crossref exact DOI reconfirmed. ASME PDF HTTP 403; OpenAlex and Semantic Scholar both identify http://oatao.univ-toulouse.fr/8416/1/Ferrand_8416.pdf (other-oa). HTTPS handshake and original HTTP URL timed out. HAL prior bot challenge retained; no bypass. No PDF acquired; other-oa is not a redistribution grant.

- Current pdf_status: `open_repository_available`; local file not acquired; `github_pdf=false`. No full-text verification upgrade or new technical claim. Unpaywall not called: no configured research contact email available; no invented email or credentials supplied.

## 2026-10-13 bounded access checkpoint

2026-10-13: Crossref title/authors/2013 reconfirmed; DOI web-open internal error. OpenAlex/Semantic Scholar still point to OATAO Ferrand_8416.pdf as green/other-oa; one ordinary HTTP repository request timed out at15s. No HAL challenge or prior ASME403 retry; no PDF acquired. other-oa is not a redistribution grant.

DOI remains verified; abstract verification unchanged; no new source or technical claim. Evidence: [public API metadata](../access_check_2026-10-13.json). Unpaywall deferred because no configured research contact was available in prior checkpoint; no invented email/credential. Previously protected routes not retried. Current PDF status retained, github_pdf=false.

## 2026-10-23 原始输入请求的限定检索

为昨日新建NC-2013-GUST-REPLAY首次检查补充数据入口：Crossref关系字段为空；DataCite精确relatedIdentifier DOI查询返回0；HAL所请求文件/链接字段仍为已取得作者稿和旧OATAO链接，未给出本轮可核实的原始PIV、挡板或CFD文件。两条题名/DOI+data/code检索未取得可验证数据；检索到的后续引用论文不替代原实验文件。仅该查询范围未找到，不断言数据永远不存在。

没有再下载论文、重试HAL挑战/ASME403/旧超时入口或向作者联络；现有全文等级、科学主张及DOI/PDF证明日期保持。请求仍open，下一需新线索/实际文件，不重复相同查询。见[原始API查询记录](../access_check_2026-10-23.json)。
