$ErrorActionPreference = 'Stop'
$repoRoot = Split-Path -Parent $PSScriptRoot
$indexPath = Join-Path $repoRoot 'sources\index.csv'
$recordsPath = Join-Path $repoRoot 'sources\records'
$edgePath = Join-Path $repoRoot 'citations\citation_edges.csv'

$expectedHeaders = @('id','title','authors','year','doi','url','source_type','publisher_or_institution','report_or_standard_number','primary_category','secondary_categories','tags','gust_type','method','vehicle_class','access_status','evidence_type','validation_level','verification_status','added_date','last_checked')
$allowedSourceTypes = @('journal_article','sae_technical_paper','conference_paper','standard','standard_draft','government_report','institutional_report','project_report','doctoral_thesis','master_thesis','book','book_chapter','review_article','dataset','code_repository','facility_documentation','manufacturer_technical_document','patent','regulatory_document','web_primary_source','secondary_web_source')
$rows = Import-Csv -LiteralPath $indexPath -Encoding utf8
if (-not $rows) { throw 'sources/index.csv has no records' }

$actualHeaders = $rows[0].PSObject.Properties.Name
if (($expectedHeaders -join ',') -ne ($actualHeaders -join ',')) {
    throw "Unexpected index headers: $($actualHeaders -join ',')"
}

$invalidSourceTypes = $rows | Where-Object { $_.source_type -notin $allowedSourceTypes }
if ($invalidSourceTypes) { throw "Invalid source_type values: $((($invalidSourceTypes | ForEach-Object { $_.id + ':' + $_.source_type }) -join ', '))" }

$duplicateIds = $rows | Group-Object id | Where-Object Count -gt 1
if ($duplicateIds) { throw "Duplicate IDs: $($duplicateIds.Name -join ', ')" }

$duplicateDois = $rows | Where-Object doi | Group-Object { $_.doi.ToLowerInvariant() } | Where-Object Count -gt 1
if ($duplicateDois) { throw "Duplicate DOIs: $($duplicateDois.Name -join ', ')" }

$missingRecords = foreach ($row in $rows) {
    $path = Join-Path $recordsPath ($row.id + '.md')
    if (-not (Test-Path -LiteralPath $path)) { $row.id; continue }
    $recordText = Get-Content -LiteralPath $path -Raw -Encoding utf8
    foreach ($field in @('source_type','publisher_or_institution','report_or_standard_number')) {
        if ($recordText -notmatch "(?m)^- ${field}:") { "$($row.id) missing ${field}" }
    }
    if ($recordText -notmatch "(?m)^- source_type: $([regex]::Escape($row.source_type))\r?$") {
        "$($row.id) source_type differs from index"
    }
}
if ($missingRecords) { throw "Record validation failed: $($missingRecords -join ', ')" }

$knownIds = @{}
foreach ($row in $rows) { $knownIds[$row.id] = $true }
$edges = Import-Csv -LiteralPath $edgePath -Encoding utf8
$badEdges = foreach ($edge in $edges) {
    if (-not $knownIds.ContainsKey($edge.source_id) -or -not $knownIds.ContainsKey($edge.target_id)) {
        "$($edge.source_id)->$($edge.target_id)"
    }
}
if ($badEdges) { throw "Citation edges reference unknown IDs: $($badEdges -join ', ')" }

$required = @('README.md','TASK.md','history\timeline.md','taxonomy.md','search\search_ledger.csv','citations\citation_graph.md','synthesis\state_of_the_art.md')
$missingRequired = foreach ($relative in $required) {
    if (-not (Test-Path -LiteralPath (Join-Path $repoRoot $relative))) { $relative }
}
if ($missingRequired) { throw "Missing required files: $($missingRequired -join ', ')" }

Write-Output "Validation OK: $($rows.Count) source records, $($edges.Count) citation edges."
