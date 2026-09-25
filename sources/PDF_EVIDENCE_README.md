# 本地 PDF 全文证据层断点

本机 `sources/pdfs/` 的身份、SHA-256、页数和当前阅读状态由 [pdf_evidence_inventory.csv](pdf_evidence_inventory.csv)记录。生成脚本是 `scripts/build_pdf_evidence_inventory.py`；每次运行只匹配已登记的哈希和四处书目台账，不执行全文研究阅读。哈希或书目不唯一时标记 `manual_match_required`。脚本不会新建规范来源。

`review_action=skip_unchanged_verified_pdf` 表示现有文件哈希不变且 source 已 `full_text_verified`；若 record 信息不足、结论冲突或需要新公式/图表/参数，仍按 [全文证据规则](../Crosswind_Learning_Knowledge_Graph_PDF_Evidence.md)回看原文。`full_text_read_pending` 表示需要按 Pass 1/2/3 继续研究阅读，不能把本次扫描算作通读。

2026-09-25 初始化结果：17 文件均按已登记 SHA-256 唯一匹配，4 条对应来源已 `full_text_verified`，13 条尚待全文级处理。其中 Brandt 92 页仅含 extended summary，来源整体仍是 `abstract_verified`；已核读的限定章节不等于附带 Paper A–E 的全文。Beauvais 1967 和 Hucho/Emmelmann 1973 虽标全文已读，学习 Pass 3 的公式、坐标和复现审计仍在 `learning/state.json` 待办中。

先从 `sae-730232` 的 Pass 3 断点继续，再核 `sae-670608`；随后按历史源头、steady/dynamic 对比、moving model、CFD 和耦合验证的顺序处理其它已收 PDF。7 条仍没有本地全文的请求见 [manual_retrieval_queue.md](manual_retrieval_queue.md)。
