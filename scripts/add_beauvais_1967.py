"""Register the publisher-verified 1967 Beauvais SAE source after v5 migration.

One-time intake with duplicate guards. Uses exact DOI metadata and the SAE publisher page;
no abstract or paywalled full text is copied.
"""

import csv
import json
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ID = "sae-670608"
TITLE = "Transient Nature of Wind Gust Effects on an Automobile"
DOI = "10.4271/670608"
DOI_URL = "https://doi.org/10.4271/670608"
OFFICIAL_URL = "https://saemobilus.sae.org/papers/transient-nature-wind-gust-effects-automobile-670608"
DOI_SOURCE = "https://api.crossref.org/works/10.4271%2F670608"
TODAY = date.today().isoformat()


def read(path):
    with path.open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


def write(path, rows, headers):
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, headers, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def append_unique(relative, new):
    path = ROOT / relative
    rows = read(path)
    if any(row["id"] == ID for row in rows):
        raise ValueError(f"{ID} already in {relative}")
    headers = list(rows[0])
    if set(new) - set(headers):
        raise ValueError(f"Unexpected fields in {relative}: {set(new)-set(headers)}")
    rows.append({field: new.get(field, "") for field in headers})
    write(path, rows, headers)


def main():
    core = {
        "id": ID, "title": TITLE, "authors": "F. N. Beauvais", "year": "1967",
        "doi": DOI, "url": DOI_URL, "source_type": "sae_technical_paper",
        "publisher_or_institution": "SAE International", "report_or_standard_number": "670608",
        "primary_category": "C", "secondary_categories": "A;F",
        "tags": "transient_gust;quasi_steady_comparison;wind_tunnel",
        "gust_type": "transient_gust", "method": "dynamic_wind_tunnel",
        "vehicle_class": "road_vehicle", "access_status": "restricted",
        "evidence_type": "dynamic_wind_tunnel", "validation_level": "none",
        "verification_status": "abstract_verified", "added_date": TODAY, "last_checked": TODAY,
        "doi_status": "verified", "doi_verified_date": TODAY, "doi_source": DOI_SOURCE,
        "pdf_status": "paywalled", "pdf_source": OFFICIAL_URL, "pdf_path": "",
        "pdf_sha256": "", "pdf_bytes": "", "pdf_license": "publisher-controlled; no OA PDF found in checked sources",
        "pdf_checked_date": TODAY, "github_pdf": "false", "bib_key": ID,
        "abstract_status": "available_not_copied",
    }
    append_unique("sources/index.csv", core)
    append_unique("sources/doi_registry.csv", {
        "id": ID, "title": TITLE, "year": "1967", "source_type": "sae_technical_paper",
        "doi": DOI, "doi_status": "verified", "doi_url": DOI_URL, "doi_source": DOI_SOURCE,
        "doi_verified_date": TODAY, "pdf_status": "paywalled", "pdf_source": OFFICIAL_URL,
        "pdf_path": "", "pdf_sha256": "", "pdf_bytes": "",
        "license": "publisher-controlled; no OA PDF found in checked sources",
        "pdf_checked_date": TODAY, "github_pdf": "false",
        "notes": "SAE publisher abstract and Crossref DOI exact title/author/year; OpenAlex exact DOI closed with no OA full text.",
        "bib_key": ID, "verification_status": "abstract_verified",
    })
    append_unique("sources/bibliography/bib_sources.csv", {
        "id": ID, "citation_key": ID,
        "bib_source": "SAE publisher page + Crossref exact DOI metadata",
        "bib_source_url": DOI_SOURCE, "bib_checked_date": TODAY,
        "abstract_status": "available_not_copied",
        "abstract_source": "SAE/Crossref publisher abstract",
        "abstract_source_url": OFFICIAL_URL, "abstract_checked_date": TODAY,
        "metadata_quality": "verified_doi_metadata",
        "notes": "Abstract is accessible; publisher rights not assumed to permit copying. OpenAlex W2276769015 has no OA location.",
    })
    append_unique("sources/manual_retrieval_queue.csv", {
        "id": ID, "title": TITLE, "authors": "F. N. Beauvais", "year": "1967",
        "source_type": "sae_technical_paper", "doi": DOI,
        "official_url": OFFICIAL_URL, "pdf_status": "paywalled", "repository_url": "",
        "reason_missing": "核对1967年准稳态与瞬态阵风风洞载荷比较的原始风场、标定、波形、峰值与适用范围。",
        "sources_attempted": "Crossref exact DOI; SAE publisher abstract; publisher PDF route redirected to HTML; OpenAlex exact DOI (closed, no OA location)",
        "priority": "P0", "requested_date": TODAY, "last_checked": TODAY,
        "manual_status": "needs_user_search", "user_supplied_path": "",
        "notes": "Legitimate institutional/author copies still possible; no paywall bypass attempted.",
    })
    bib_path = ROOT / "sources/bibliography/references.bib"
    bib = bib_path.read_text(encoding="utf-8")
    if f"@techreport{{{ID}," in bib:
        raise ValueError("Bib entry already exists")
    bib += f"\n@techreport{{{ID},\n  author = {{Beauvais, F. N.}},\n  title = {{{TITLE}}},\n  year = {{1967}},\n  institution = {{SAE International}},\n  number = {{670608}},\n  type = {{SAE Technical Paper}},\n  publisher = {{SAE International}},\n  doi = {{{DOI}}},\n  url = {{{DOI_URL}}},\n  keywords = {{transient\\_gust, quasi\\_steady\\_comparison, wind\\_tunnel}},\n  note = {{Crosswind keywords are curator tags, not necessarily author keywords.}},\n}}\n"
    bib_path.write_text(bib, encoding="utf-8")
    record = f"""# {ID} — {TITLE}

## Bibliographic
- ID: `{ID}`; Author: F. N. Beauvais; Year: 1967; SAE Technical Paper 670608.
- GB/T 7714: BEAUVAIS F N. Transient nature of wind gust effects on an automobile[R]. SAE Technical Paper 670608, 1967. DOI:{DOI}.
- DOI / official URL: [{DOI}]({DOI_URL}); [SAE publisher page]({OFFICIAL_URL}).
- Canonical Bib key: `{ID}` in `sources/bibliography/references.bib`.

## Access / verification
- verification_status: abstract_verified; access_level: abstract; pdf_status: paywalled at checked publisher entrance; no lawful full text acquired.
- abstract_status: available_not_copied; abstract_source: SAE publisher and Crossref deposited publisher abstract ({DOI_SOURCE}).
- Crossref DOI/title/author/1967-02-01 verified on {TODAY}; OpenAlex exact DOI W2276769015 reports closed access and no OA full-text location.

## Classification
- source_type: sae_technical_paper
- publisher_or_institution: SAE International
- report_or_standard_number: 670608
- primary_category: C; secondary_categories: A,F; evidence_type: dynamic_wind_tunnel; validation_level: none.

## Physical problem and method
- Publisher abstract frames a comparison: are quasi-steady wind-tunnel forces and moments representative of the transient interval when a vehicle meets a gust?
- It says the paper describes the experimental facility, airstream calibration, tests and results. Their actual settings, waveforms, axes, load peaks and uncertainty are not available in the abstract.
- Do not infer that a specific overshoot magnitude or vehicle response was measured from this abstract alone.

## Relevance / follow-up
- Historical bridge between the 1953 road study and later dynamic wind-tunnel/derivative work. This is a method-lineage hypothesis, not a verified direct citation edge.
- Seek lawful full text, extract gust definition and quasi-steady comparator, then check its references/cited-by and possible relation to 1973 SAE 730232.
"""
    (ROOT / "sources/records" / f"{ID}.md").write_text(record, encoding="utf-8")
    state_path = ROOT / "learning/state.json"
    state = json.loads(state_path.read_text(encoding="utf-8"))
    state["learning_backlog"].append(ID)
    state["sources_total"] += 1
    state["sources_pending_learning"] += 1
    state["post_v5_collection"] = {
        "date": TODAY, "new_source_ids": [ID], "sources_total": state["sources_total"],
        "manual_retrieval_unresolved": 21, "verified_doi": 19,
        "current_phase": "learning", "current_source_id": state["current_source_id"],
        "current_pass": state["current_pass"],
        "next": "Finish existing Pass 3 backlog before new large-scale collection; newly collected sae-670608 awaits Pass 1-3.",
        "local_remote_sync": "pending_commit_and_push",
    }
    state_path.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    status_path = ROOT / "learning/paper_notes/pass_status.csv"
    status = read(status_path)
    headers = list(status[0])
    status.append({
        "source_id": ID, "source_type": "sae_technical_paper", "role": "C/F",
        "current_pass": "0", "current_status": "not_started",
        "target_pass_current_evidence": "2", "pass3_priority": "high_when_fulltext_available",
        "upgrade_trigger": "obtain_lawful_fulltext_or_author_version",
        "source_verification": "abstract_verified", "last_reviewed": TODAY,
    })
    write(status_path, status, headers)
    (ROOT / "learning/paper_notes" / f"{ID}.md").write_text(
        f"# {ID} — pending learning\n\n- Intake: {TODAY}; Pass 1 not started.\n- Evidence currently limited to SAE/Crossref publisher abstract.\n- Resume from learning state after current higher-priority Pass 3 backlog; obtain lawful full text for Pass 3.\n",
        encoding="utf-8",
    )
    queue = read(ROOT / "sources/manual_retrieval_queue.csv")
    queue.sort(key=lambda item: (item["priority"], int(item["year"]), item["id"]))
    write(ROOT / "sources/manual_retrieval_queue.csv", queue, list(queue[0]))
    md = [
        "# 需要用户手动查找的资料", "",
        f"截至 {TODAY}：v5 迁移新增 20 条，随后新增 1 条；当前未解决 {len(queue)} 条。合法获得的 PDF 请放入 `sources/pdfs/`，下一轮核题名/DOI、格式与 SHA-256。", "",
        "当前已查入口并非穷尽全部合法 OA/机构馆藏；Unpaywall 联系邮箱未配置，Semantic Scholar 前轮返回 429。", "",
        "| 优先级 | 题名；作者；年份 | DOI | 官方入口 | 需要全文的原因 | 已尝试渠道 |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for item in queue:
        entrance = f"[官方/权威入口]({item['official_url']})"
        if item["repository_url"]:
            entrance += f"；[机构仓储]({item['repository_url']})"
        display_title = item["title"].replace("|", "\\|")
        display_authors = item["authors"].replace("|", "\\|")
        md.append(f"| {item['priority']} | {display_title}；{display_authors}；{item['year']} | {item['doi'] or '未确认'} | {entrance} | {item['reason_missing']} | {item['sources_attempted']} |")
    md += ["", "收到文件后不默认拥有再分发权；仅明确允许再分发的 PDF 可纳入 GitHub。", ""]
    (ROOT / "sources/manual_retrieval_queue.md").write_text("\n".join(md), encoding="utf-8")
    print("Added SAE 670608: 24 sources, 19 verified DOI, 24 Bib, 21 manual requests, 9 pending learning")


if __name__ == "__main__":
    main()
