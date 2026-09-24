$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $PSScriptRoot
$graphRoot = Join-Path $root 'learning\graph'
$edges = @(Import-Csv (Join-Path $graphRoot 'edges.csv') -Encoding utf8)
$nodes = @{}
foreach ($file in @('concepts.csv', 'methods.csv', 'variables.csv', 'equations.csv')) {
    foreach ($row in @(Import-Csv (Join-Path $root "learning\nodes\$file") -Encoding utf8)) {
        $nodes[$row.id] = $row.id
    }
}
foreach ($row in @(Import-Csv (Join-Path $root 'learning\nodes\evidence.csv') -Encoding utf8)) {
    $nodes[$row.claim_id] = $row.claim_id
}
foreach ($row in @(Import-Csv (Join-Path $root 'sources\index.csv') -Encoding utf8)) {
    $nodes[$row.id] = $row.id
}
$lines = [System.Collections.Generic.List[string]]::new()
$lines.Add('flowchart LR')
foreach ($edge in $edges) {
    if (-not $nodes.ContainsKey($edge.from_id) -or -not $nodes.ContainsKey($edge.to_id)) {
        throw "Unknown graph endpoint: $($edge.from_id) -> $($edge.to_id)"
    }
    $from = 'N_' + ($edge.from_id -replace '[^A-Za-z0-9_]', '_')
    $to = 'N_' + ($edge.to_id -replace '[^A-Za-z0-9_]', '_')
    $lines.Add(('    {0}["{1}"] -->|{2}| {3}["{4}"]' -f $from, $edge.from_id, $edge.relation, $to, $edge.to_id))
}
$mermaid = $lines -join "`n"
Set-Content (Join-Path $graphRoot 'knowledge_graph.mmd') $mermaid -Encoding utf8
$header = @'
# 初版知识图谱

下图由 `graph/edges.csv` 生成，箭头均在该表保留 `source_id`、条件、核验状态和说明。E1 是公开摘要层级，E2 是已核读原文范围；箭头表示有条件的关系，不是跨车型普适定律。图中证据节点 `E-*` 再指向规范来源，构成知识→主张→来源路径。

当前图谱覆盖已建立证据节点的来源；覆盖数量由 nodes/evidence.csv 与 sources/index.csv 核对，学习完成状态以 state.json 为准。图谱尚未包含完整风→车→驾驶员因果链；断边记录于 `open_questions.md`。

```mermaid
'@
$footer = @'
```

`evidence_from` 表示原始来源支撑该 atomic claim；`described_by` 表示概念受到特定条件下主张说明；`generated_by` 表示该输入由文献中的方法实现；`depends_on` 表示当前准稳态比较以稳态基线为参照。`supported_by` 表示方法受到特定原文证据支持，与 supports 的反向阅读对应；不表示独立跨方法验证。这些关系不能自动推成 `causes` 或跨研究 `validated_by`。
'@
Set-Content (Join-Path $graphRoot 'knowledge_graph.md') ($header + "`n" + $mermaid + "`n" + $footer) -Encoding utf8
Write-Output "Graph regenerated: $($edges.Count) edges."
