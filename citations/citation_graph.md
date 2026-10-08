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

## v5 去重后的保留关系（2026-09-25）

- `dot-hs-805-079` → `dot-hs-805-078`：`companion_report`，同一项目的技术卷与执行摘要卷，报告号不同，均保留。
- `sae-970135` → `sae-960674`：现有 `method_extends`；剪切/湍流动态试验扩展1996比较方法，均保留。
- `sae-2000-01-0874` → `sae-980392`：现有 `facility_inherits`；尾流调查与1998载荷论文不同，均保留。
- `jweia-2014-volpe` → `jfe-2013-volpe`：现有 `references`；2013设施验证与2014车体流动/载荷研究不同，均保留，不把普通引用升级成硬件继承。


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

## 2026-09-25：Ryan/Dominy 1998 全文参考文献

- `sae-980392` → `sae-670608`：PDF p. 11 reference 2 明确引 Beauvais SAE 670608。
- `sae-980392` → `sae-960674`：PDF p. 11 reference 13 明确引 Macklin/Garry/Howell SAE 960674；p. 10 对两设施的 30° 横摆力矩结果作条件化讨论。两边均为已核 `references`，不自动表示同一阵风边界、硬件继承或直接 `contradicts`。

## 2026-09-25：Benner 1958 原文引文

`bams-1958-benner` → `sae-530255`：`references=true`，Benner 1958 publisher PDF p.425 reference 5 明确列 Lay/Lett 1953；pp.424–425 描述其道路车装置。这是 1953 核心论文的一条已核 cited-by，不证明新的独立试验或后续方法继承。
## 2026-09-25 全文核验补充

- `sae-970135` article p.34 reference 1 → `sae-960674`：直接引用；1997 的廓线/湍流研究沿用 1996 Cranfield 移动车模方法，但粗糙板造成剪切与湍流混杂。
- `sae-2000-01-0874` article p.9 reference 1 → `sae-960674`：直接引用，不表示硬件继承。reference 2 指向未入库的 1999 改进风洞论文。
- `sae-2000-01-0874` ↔ `sae-980392`：保留同组 Durham 方法谱系，缩窄为 `facility_lineage`；2000 挡板、5 m、22° 与 1998 移动开口、1.5 m、30° 的条件不同，不将载荷与尾流数字混同。

## 2026-10-09 全文增量

jcp-2016-tunay → sae-980392 / jfe-2013-volpe / sae-2000-01-0876，references=true，PDF35–36 refs6/7/8。仅引用，非装置或代码继承。
