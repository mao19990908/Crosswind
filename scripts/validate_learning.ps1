$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $PSScriptRoot
$state = Get-Content (Join-Path $root 'learning\state.json') -Raw -Encoding utf8 | ConvertFrom-Json
$index = @(Import-Csv (Join-Path $root 'sources\index.csv') -Encoding utf8)
$known = @{}
foreach ($row in $index) { $known[$row.id] = $true }
$pending = @($state.learning_backlog)
$completed = @($state.learning_completed)
if ($state.sources_total -ne $index.Count -or $state.sources_pending_learning -ne $pending.Count) { throw 'Learning state counts do not match index/backlog' }
if (($pending.Count + $completed.Count) -ne $index.Count) { throw 'Learning queue does not partition source index' }
foreach ($id in @($pending) + @($completed)) { if (-not $known.ContainsKey($id)) { throw "Unknown source in learning state: $id" } }
if (@(@($pending) + @($completed) | Select-Object -Unique).Count -ne $index.Count) { throw 'Duplicate source in learning queue' }
$pass = @(Import-Csv (Join-Path $root 'learning\paper_notes\pass_status.csv') -Encoding utf8)
if ($pass.Count -ne $index.Count) { throw 'Pass status count differs from source index' }
foreach ($row in $pass) { if (-not $known.ContainsKey($row.source_id)) { throw "Unknown pass status source: $($row.source_id)" } }
foreach ($id in $completed) {
    $entry = @($pass | Where-Object source_id -eq $id)
    if ($entry.Count -ne 1 -or $entry[0].current_status -notlike 'completed_*') { throw "Completed source lacks matching Pass status: $id" }
}
$nodes = @{}
foreach ($file in @('concepts.csv','methods.csv','variables.csv','equations.csv')) {
    foreach ($row in @(Import-Csv (Join-Path $root "learning\nodes\$file") -Encoding utf8)) { $nodes[$row.id] = $true }
}
foreach ($row in @(Import-Csv (Join-Path $root 'learning\nodes\evidence.csv') -Encoding utf8)) {
    if (-not $known.ContainsKey($row.source_id)) { throw "Unknown evidence source: $($row.source_id)" }
    $nodes[$row.claim_id] = $true
}
foreach ($row in $index) { $nodes[$row.id] = $true }
$edges = @(Import-Csv (Join-Path $root 'learning\graph\edges.csv') -Encoding utf8)
foreach ($edge in $edges) {
    if (-not $nodes.ContainsKey($edge.from_id) -or -not $nodes.ContainsKey($edge.to_id)) { throw "Unknown edge endpoint: $($edge.from_id) -> $($edge.to_id)" }
    if (-not $known.ContainsKey($edge.source_id)) { throw "Unknown edge source: $($edge.source_id)" }
}
Write-Output "Learning validation OK: $($index.Count) sources, $($completed.Count) completed, $($pending.Count) pending, $($edges.Count) graph edges."
