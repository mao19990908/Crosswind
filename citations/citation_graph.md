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
