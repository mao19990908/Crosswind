"""Validate the local PDF evidence inventory and atomic-claim evidence levels."""

from __future__ import annotations

import csv
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def table(path: str) -> list[dict[str, str]]:
    with (ROOT / path).open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


def main() -> None:
    index = {row["id"]: row for row in table("sources/index.csv")}
    inventory = table("sources/pdf_evidence_inventory.csv")
    files = list((ROOT / "sources/pdfs").glob("*.pdf"))
    assert len(inventory) == len(files), "Inventory/PDF count differs"
    assert len({row["pdf_filename"] for row in inventory}) == len(files), "Duplicate inventory filename"
    for entry in inventory:
        pdf = Path(entry["local_pdf_path"])
        assert pdf.is_file(), f"Missing PDF: {pdf}"
        assert pdf.resolve().is_relative_to((ROOT / "sources/pdfs").resolve()), f"PDF outside local folder: {pdf}"
        sha = hashlib.sha256(pdf.read_bytes()).hexdigest()
        assert sha == entry["pdf_sha256"], f"Inventory hash changed: {pdf}"
        if entry["match_status"] == "matched":
            source = index[entry["stable_id"]]
            assert source["pdf_sha256"] == sha and source["verification_status"] == entry["verification_status"], f"Source mismatch: {pdf}"
            assert entry["index_registry_bib_record_check"] == "pass", f"Metadata mismatch: {pdf}"
        else:
            assert entry["match_status"] == "manual_match_required", f"Invalid match status: {pdf}"
    evidence = table("learning/nodes/evidence.csv")
    required = {"pdf_filename", "page", "section", "equation", "figure", "table", "evidence_type"}
    assert required <= set(evidence[0]), "Atomic-claim evidence schema incomplete"
    for claim in evidence:
        assert claim["source_id"] in index, f"Unknown claim source: {claim['claim_id']}"
        status = claim["verification_status"]
        source = index[claim["source_id"]]
        if status == "full_text_verified":
            assert source["verification_status"] == "full_text_verified" and source["pdf_path"], f"Unbacked full-text claim: {claim['claim_id']}"
            assert claim["confidence"] == "E2", f"Full-text claim with wrong confidence: {claim['claim_id']}"
            assert "abstract" not in claim["evidence"].casefold(), f"Abstract mislabelled full-text: {claim['claim_id']}"
        if status == "abstract_verified":
            assert claim["confidence"] in {"E1", "E0"}, f"Abstract mislabelled high confidence: {claim['claim_id']}"
    print(f"PDF evidence validation OK: {len(inventory)} local PDFs, {len(evidence)} claims; evidence level checks passed.")


if __name__ == "__main__":
    main()
