"""Cross-check the v5 bibliography, DOI, aliases and active source references."""

from __future__ import annotations

import csv
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def table(relative: str) -> list[dict[str, str]]:
    with (ROOT / relative).open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


def unique(rows: list[dict[str, str]], field: str, label: str) -> dict[str, dict[str, str]]:
    keys = [row[field] for row in rows]
    if len(keys) != len(set(keys)):
        raise AssertionError(f"Duplicate {label} key")
    return {row[field]: row for row in rows}


def main() -> None:
    index = unique(table("sources/index.csv"), "id", "index")
    registry = unique(table("sources/doi_registry.csv"), "id", "registry")
    provenance = unique(table("sources/bibliography/bib_sources.csv"), "id", "bibliography provenance")
    queue = unique(table("sources/manual_retrieval_queue.csv"), "id", "manual retrieval")
    aliases = unique(table("sources/aliases.csv"), "old_id", "alias")
    dedup = table("sources/dedup_report.csv")
    bib_text = (ROOT / "sources/bibliography/references.bib").read_text(encoding="utf-8")
    entries = re.findall(r"@\w+\{([^,]+),\s*\n(.*?)\n\}", bib_text, flags=re.S)
    bib = unique([{"key": key, "body": body} for key, body in entries], "key", "Bib")
    ids = set(index)
    if ids != set(registry) or ids != set(provenance) or ids != set(bib):
        raise AssertionError("Index / DOI registry / Bib / Bib source ID sets differ")
    if set(queue) - ids:
        raise AssertionError("Manual queue has unknown source IDs")
    normalized = lambda value: re.sub(r"[^a-z0-9]+", "", value.casefold())
    for label, keys in [
        ("DOI", [row["doi"].casefold() for row in index.values() if row["doi_status"] == "verified"]),
        ("report/standard number", [(row["source_type"], normalized(row["report_or_standard_number"])) for row in index.values() if row["report_or_standard_number"] != "not_applicable"]),
        ("title/year", [(normalized(row["title"]), row["year"]) for row in index.values()]),
    ]:
        duplicates = [key for key, count in Counter(keys).items() if count > 1]
        if duplicates:
            raise AssertionError(f"Duplicate {label}: {duplicates}")
    for source_id, row in index.items():
        if row["bib_key"] != source_id or provenance[source_id]["citation_key"] != source_id:
            raise AssertionError(f"Bib key mismatch for {source_id}")
        if row["abstract_status"] != provenance[source_id]["abstract_status"]:
            raise AssertionError(f"Abstract status mismatch for {source_id}")
        body = bib[source_id]["body"]
        doi_match = re.search(r"(?m)^\s*doi\s*=\s*\{([^}]+)\}", body)
        bib_doi = doi_match.group(1) if doi_match else ""
        if bib_doi.casefold() != row["doi"].casefold() or row["doi"].casefold() != registry[source_id]["doi"].casefold():
            raise AssertionError(f"Bib / index / registry DOI mismatch for {source_id}")
        abstract_in_bib = bool(re.search(r"(?m)^\s*abstract\s*=", body))
        if abstract_in_bib != (row["abstract_status"] == "full_abstract_saved"):
            raise AssertionError(f"Bib abstract status mismatch for {source_id}")
        if row["pdf_status"] != registry[source_id]["pdf_status"] or row["pdf_path"] != registry[source_id]["pdf_path"]:
            raise AssertionError(f"PDF status mismatch for {source_id}")
        if row["verification_status"] == "full_text_verified" and not row["pdf_path"]:
            raise AssertionError(f"Full-text verified without PDF for {source_id}")
        record = (ROOT / "sources/records" / f"{source_id}.md").read_text(encoding="utf-8")
        if f"Canonical Bib key: `{source_id}`" not in record:
            raise AssertionError(f"Missing Bib provenance in record {source_id}")
    for old_id, alias in aliases.items():
        if old_id in ids or alias["canonical_id"] not in ids:
            raise AssertionError(f"Invalid alias {old_id}")
    for row in dedup:
        if row["action"] == "merged_and_deleted":
            if aliases.get(row["candidate_id"], {}).get("canonical_id") != row["canonical_id"]:
                raise AssertionError("Deleted duplicate lacks alias")
        elif row["candidate_id"] not in ids or row["canonical_id"] not in ids:
            raise AssertionError("Dedup report references unknown live ID")
    for relative, fields in [
        ("citations/citation_edges.csv", ("source_id", "target_id")),
        ("learning/graph/edges.csv", ("source_id",)),
        ("synthesis/validation_matrix.csv", ("source_id",)),
        ("synthesis/simulation_matrix.csv", ("source_id",)),
        ("synthesis/experiment_matrix.csv", ("source_id",)),
        ("synthesis/gust_parameter_matrix.csv", ("source_id",)),
        ("synthesis/coupled_methods_matrix.csv", ("source_id",)),
    ]:
        for row in table(relative):
            for field in fields:
                value = row.get(field, "")
                if value and value not in ids:
                    raise AssertionError(f"Dangling ID {value} in {relative}")
    for source_id, row in queue.items():
        if row["manual_status"] == "needs_user_search" and index[source_id]["verification_status"] == "full_text_verified":
            raise AssertionError(f"Full-text verified source still requests user search: {source_id}")
    print(f"Bib/dedup validation OK: {len(ids)} sources, {len(bib)} Bib entries, {len(queue)} manual requests, {len(aliases)} aliases, {len(dedup)} reviewed pairs.")


if __name__ == "__main__":
    main()
