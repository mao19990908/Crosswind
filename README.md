# 车辆瞬态侧风（阵风）知识库

本仓库持续整理道路车辆瞬态侧风／阵风的历史、理论、实验、CFD、车辆动力学与耦合验证证据。研究主线是：

> 阵风输入 → 非定常气动载荷 → 横向／横摆／侧倾响应 → 驾驶员或控制器修正

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
- [当日日志](logs/2026-09-25.md)

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

公开全文已验证 3 份：Passmore 作者版、Brandt 学位论文、SAE 2025 出版者版。Durham 2000 与 HAL 2013 有开放仓储页面，但直接文档请求分别返回 403 和 bot challenge，本机未取得 PDF，也未绕过访问控制。其余条目的付费或未找到状态只描述已查入口，不能解释为永久无 OA。Passmore 封面与仓储许可版本不一致、Brandt 仅明确可公开访问，两份仅本机保留；SAE 2025 许可 CC BY 4.0，允许署名再分发。来源、大小、SHA-256 和许可边界以 DOI 总账为准。

### 2026-09-25 追加：出版者 CC BY 全文

[SAE 2025 风洞阵风发生系统论文](https://doi.org/10.4271/15-18-01-0005)的出版者 PDF 首页明确标示 CC BY 4.0，已核对题名、DOI、16 页和 SHA-256，并按署名许可纳入 GitHub。其余本机 PDF 仍不推送；实时数量以 DOI 总账为准。

### 2026-09-25 追加：Benner 1958 历史全文

用户提供的 [Benner 1958](https://doi.org/10.1175/1520-0477-39.8.421) 六页期刊论文已存入本机 `sources/pdfs/bams-1958-benner__benner__1958.pdf`，全文 Pass 2 已完成。论文 p.425 reference 5 明确引用 Lay/Lett 1953；其道路仪器说明属于被引研究的历史转述，1955 Ford 的固定风洞例子不计作瞬态阵风试验。该 PDF 再分发许可未核实，所以只同步全文结构化记录、书目、证据节点和引文关系，不推送 PDF 文件。
