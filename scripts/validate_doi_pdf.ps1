param([switch]$RequireLocalPdf)
$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $PSScriptRoot
$index = @(Import-Csv (Join-Path $root 'sources\index.csv') -Encoding utf8)
$registry = @(Import-Csv (Join-Path $root 'sources\doi_registry.csv') -Encoding utf8)
$validDoi = @('verified','no_doi_confirmed','missing_to_search','invalid_or_conflict','not_applicable')
$validPdf = @('oa_downloaded','user_provided','institutional_access','open_repository_available','paywalled','not_found','not_pdf','download_failed','license_unclear')
if ($index.Count -ne $registry.Count) { throw 'DOI registry and source index count differ' }
$byId = @{}
foreach ($row in $registry) {
    if ($byId.ContainsKey($row.id)) { throw "Duplicate registry ID $($row.id)" }
    $byId[$row.id] = $row
}
foreach ($row in $index) {
    if (-not $byId.ContainsKey($row.id)) { throw "Missing registry ID $($row.id)" }
    $entry = $byId[$row.id]
    if ($validDoi -notcontains $row.doi_status -or $validPdf -notcontains $row.pdf_status) { throw "Invalid status for $($row.id)" }
    if ($entry.doi_status -ne $row.doi_status -or $entry.pdf_status -ne $row.pdf_status -or $entry.doi -ne $row.doi -or $entry.pdf_path -ne $row.pdf_path -or $entry.pdf_sha256 -ne $row.pdf_sha256 -or $entry.pdf_bytes -ne $row.pdf_bytes -or $entry.bib_key -ne $row.bib_key -or $entry.verification_status -ne $row.verification_status) { throw "Index / registry mismatch for $($row.id)" }
    if ($row.doi_status -eq 'verified' -and [string]::IsNullOrWhiteSpace($row.doi)) { throw "Verified DOI missing for $($row.id)" }
    if (-not [string]::IsNullOrWhiteSpace($row.pdf_path)) {
        $path = Join-Path $root $row.pdf_path
        if (-not (Test-Path -LiteralPath $path -PathType Leaf)) {
            if ($RequireLocalPdf) { throw "Missing local PDF for $($row.id)" }
            continue
        }
        $bytes = [System.IO.File]::ReadAllBytes($path)
        if ($bytes.Length -lt 5 -or [System.Text.Encoding]::ASCII.GetString($bytes,0,5) -ne '%PDF-') { throw "Invalid PDF header for $($row.id)" }
        $hash = (Get-FileHash -LiteralPath $path -Algorithm SHA256).Hash.ToLowerInvariant()
        if ($hash -ne $row.pdf_sha256 -or $bytes.Length -ne [int64]$row.pdf_bytes) { throw "PDF hash or size mismatch for $($row.id)" }
    }
}
Write-Output "DOI/PDF validation OK: $($index.Count) sources, $(@($index | Where-Object doi_status -eq 'verified').Count) verified DOI, $(@($index | Where-Object pdf_status -eq 'oa_downloaded').Count) local PDFs."
