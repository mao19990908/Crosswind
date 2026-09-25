"""Inventory local PDFs without claiming that their full text was read.

Use the registered SHA-256 as the first identity key. Ambiguous/unregistered
files stay manual_match_required; this script never creates source records.
"""

from __future__ import annotations

import csv
import hashlib
import re
from datetime import datetime
from pathlib import Path

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "sources/pdf_evidence_inventory.csv"
FIELDS = [
    "pdf_filename", "local_pdf_path", "pdf_sha256", "pdf_bytes", "pdf_pages",
    "stable_id", "match_status", "match_basis", "index_registry_bib_record_check",
    "verification_status", "review_action", "inventory_date",
]


def table(name: str) -> list[dict[str, str]]:
    with (ROOT / name).open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


def bib_entries() -> dict[str, str]:
    bib = (ROOT / "sources/bibliography/references.bib").read_text(encoding="utf-8-sig")
    return dict(re.findall(r"@\w+\{([^,]+),\s*\n(.*?)\n\}", bib, re.S))


def field(body: str, name: str) -> str:
    found = re.search(rf"(?m)^\s*{name}\s*=\s*\{{([^}}]+)\}}", body)
    return found.group(1).strip() if found else ""


def main() -> None:
    index = {row["id"]: row for row in table("sources/index.csv")}
    registry = {row["id"]: row for row in table("sources/doi_registry.csv")}
    bib = bib_entries()
    by_hash: dict[str, list[str]] = {}
    for source_id, row in index.items():
        if row["pdf_sha256"]:
            by_hash.setdefault(row["pdf_sha256"].lower(), []).append(source_id)
    output = []
    for pdf in sorted((ROOT / "sources/pdfs").glob("*.pdf")):
        raw = pdf.read_bytes()
        sha = hashlib.sha256(raw).hexdigest()
        ids = by_hash.get(sha, [])
        status = "matched" if len(ids) == 1 else "manual_match_required"
        source_id = ids[0] if len(ids) == 1 else ""
        check = "not_checked_ambiguous"
        if source_id:
            row = index[source_id]
            reg = registry.get(source_id, {})
            body = bib.get(source_id, "")
            record = ROOT / "sources/records" / f"{source_id}.md"
            record_text = record.read_text(encoding="utf-8-sig") if record.exists() else ""
            ok = (
                reg.get("pdf_sha256", "").lower() == sha
                and row["pdf_path"].replace("\\", "/") == str(pdf.relative_to(ROOT)).replace("\\", "/")
                and reg.get("doi", "").lower() == row["doi"].lower()
                and field(body, "doi").lower() == row["doi"].lower()
                and field(body, "year") == row["year"]
                and row["title"].casefold() == reg.get("title", "").casefold()
                and row["authors"].split(";")[0].strip().split()[-1].casefold()
                in field(body, "author").casefold()
                and source_id in bib
                and source_id in record_text
            )
            check = "pass" if ok else "manual_metadata_review_required"
            if not ok:
                status = "manual_match_required"
        try:
            if not raw.startswith(b"%PDF-"):
                raise ValueError("missing PDF header")
            pages = len(PdfReader(pdf, strict=False).pages)
            if pages < 1:
                raise ValueError("empty PDF")
        except Exception:
            pages = ""
            status = "manual_match_required"
            check = "pdf_open_failed"
        verified = index[source_id]["verification_status"] if source_id else ""
        output.append({
            "pdf_filename": pdf.name,
            "local_pdf_path": str(pdf),
            "pdf_sha256": sha,
            "pdf_bytes": len(raw),
            "pdf_pages": pages,
            "stable_id": source_id,
            "match_status": status,
            "match_basis": "registered_sha256_and_prior_pdf_identity_receipt" if source_id else "",
            "index_registry_bib_record_check": check,
            "verification_status": verified,
            "review_action": "skip_unchanged_verified_pdf" if verified == "full_text_verified" and status == "matched" else "full_text_read_pending",
            "inventory_date": datetime.now().astimezone().date().isoformat(),
        })
    with OUT.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(output)
    print(f"PDF inventory: {len(output)} files; {sum(r['match_status'] == 'matched' for r in output)} matched; {sum(r['match_status'] == 'manual_match_required' for r in output)} manual matches; {sum(r['review_action'] == 'full_text_read_pending' for r in output)} full-text reads pending.")
    for row in output:
        if row["index_registry_bib_record_check"] != "pass":
            print(row["pdf_filename"], row["index_registry_bib_record_check"])


if __name__ == "__main__":
    main()
