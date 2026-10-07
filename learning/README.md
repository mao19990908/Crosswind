# 学习层

从 [学习路径](learning_path.md)进入，先读相对来流与阵风输入，再读气动载荷、车辆响应和验证。知识结论通过 `nodes/evidence.csv` 连接到 `sources/records/`；`graph/edges.csv` 只保存能解释的关系。`sources/` 仍是事实来源。

当前记录同时包含摘要、章节和全文证据；逐条等级以source与claim为准，E1不等于全文已读。`learning/state.json` 是逐日恢复点。`paper_notes/` 保存逐篇 Pass 进度与尚需核验的关键问题，章节按知识问题组织。

标记：`UNKNOWN` 无足够信息；`NEEDS_FULLTEXT` 需要原文；`ANALYST_INFERENCE` 为研究者推断；`OPEN_QUESTION` 是明确断边。标准和受限论文正文不在本库复制。

全文证据层按 [PDF 规则](../Crosswind_Learning_Knowledge_Graph_PDF_Evidence.md)执行。本地清单见 [PDF evidence inventory](../sources/pdf_evidence_inventory.csv)：它只证明文件与既有台账的身份匹配、哈希和可打开性，不代表已通读。`nodes/evidence.csv` 已预留页、节、公式、图和表的定位列；空列表示尚未按新规则核对，不能自动回填或提升证据等级。
