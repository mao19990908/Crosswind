# 引文关系图

仅显示当前已核验或明确标为候选的关系：

```text
sae-960674
  └─ method_extends (verified) → sae-970135

sae-980392
  └─ facility_inherits (verified) → sae-2000-01-0874

iso-12021-2010
  └─ standardizes test target (verified) → sae-2017-01-1515

jcp-2016-tunay
  └─ possible coupling lineage (unverified) → sae-2017-01-1525
```

图不等同于完整 cited-by 网络。下一轮优先用 OpenAlex／Semantic Scholar 建立 DOI cited-by 候选，再回原始论文核验方法关系。


## 2026-09-24 增量

```text
pimeche-2001-passmore --references (verified, publisher ref.4)--> sae-960674
pimeche-2001-passmore --references (verified, publisher ref.6)--> sae-980392
```

上图方向为引用者 → 被引者，对应两篇核心论文的 cited-by 进度。Semantic Scholar 返回 `sae-960674` 的 30 条候选，保存于 `search/cited_by_candidates_2026-09-24.csv`；仅筛题，未把聚合器条目批量升级为 verified 边。OpenAlex W1518832512 的 cited_by_count 同为 30，但这不是完备性证明；未拉取其分页结果。

## 2026-09-25 增量

`jweia-2014-volpe` → `jfe-2013-volpe`：Crossref 2014 参考文献 bib40 对应 2013 题名、作者、期刊和年份，`references=true`。2013 摘要称沿 Ryan–Dominy 双风洞思路，但未确认具体引用哪条既有 SAE 记录，不制造直接引用边。

`jfe-2013-volpe` → `sae-2000-01-0874`：`method_inherits=true`，限双风洞横向阵风**方法概念**。2013 作者摘要 + [2018 Springer 原始研究](https://link.springer.com/article/10.1007/s00348-018-2586-0)明确指向 2000 SAE DOI；原文引用与硬件细节仍未知。

2013 ASME 文的 [Crossref 参考文献元数据](https://api.crossref.org/works/10.1115%2F1.4023194) B22、B14 还分别指向 `sae-960674`（题名/年份匹配）和 `pimeche-2001-passmore`（题名/年份/DOI 匹配），新增 2 条 verified `references`。这份 28 条元数据中未见 `sae-2000-01-0874` 的直接条目；不把方法概念继承误记为直接引用。元数据可能不完备，原刊全文仍待核对。
