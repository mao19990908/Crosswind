"""One-time v5 bibliography, dedup and manual-retrieval migration.

The source index remains authoritative. Crossref is used only for DOI-matched
metadata; publisher abstracts are copied only where a redistribution licence
has already been verified for the corresponding source.
"""

from __future__ import annotations

import csv
import difflib
import html
import json
import re
import urllib.parse
import urllib.request
from collections import defaultdict
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TODAY = date.today().isoformat()
INDEX = ROOT / "sources/index.csv"
REGISTRY = ROOT / "sources/doi_registry.csv"
BIB_DIR = ROOT / "sources/bibliography"
BIB_DIR.mkdir(exist_ok=True)


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


def write_csv(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def norm(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", text.casefold())


def crossref(doi: str) -> dict:
    url = "https://api.crossref.org/works/" + urllib.parse.quote(doi, safe="")
    request = urllib.request.Request(url, headers={"User-Agent": "Crosswind-research/1.0 (bibliography metadata)"})
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            message = json.load(response)["message"]
        if message.get("DOI", "").casefold() != doi.casefold():
            raise ValueError("Crossref DOI response mismatch")
        return message
    except (OSError, ValueError, KeyError) as error:
        print(f"Crossref unavailable for {doi}: {error}")
        return {}


def bib_escape(value: str) -> str:
    return (value.replace("\\", "\\textbackslash ")
            .replace("{", "\\{").replace("}", "\\}")
            .replace("%", "\\%").replace("_", "\\_").replace("&", "\\&"))


def bib_author(row: dict, metadata: dict) -> str:
    names = []
    for author in metadata.get("author", []):
        family = author.get("family", "").strip()
        given = author.get("given", "").strip()
        if family:
            names.append(f"{family}, {given}" if given else family)
    if names:
        return " and ".join(names)
    if row["authors"] == "ISO":
        return "{International Organization for Standardization}"
    authors = row["authors"].replace("; et al.", "; others")
    return " and ".join(name.strip() for name in authors.split(";") if name.strip())


def journal_fields(row: dict, metadata: dict) -> dict[str, str]:
    item = {}
    containers = metadata.get("container-title") or []
    if containers and row["source_type"] != "sae_technical_paper":
        item["journal"] = containers[0]
    elif row["id"] == "trid-116341":
        item["journal"] = "Automobile Engineer"
    for source_name, target_name in (("volume", "volume"), ("issue", "number"), ("page", "pages")):
        value = metadata.get(source_name)
        if value:
            item[target_name] = str(value).replace("-", "--") if source_name == "page" else str(value)
    if row["id"] == "trid-116341":
        item.update(volume="58", pages="352--355")
    return item


def source_reason(row: dict) -> str:
    source_id = row["id"]
    reasons = {
        "sae-530255": "核对1953道路阵风原试验的风场、传感器和参考文献；解决自动引文日期冲突。",
        "trid-116341": "核对1968准稳态/车辆响应原文及 DOI；TRID 摘要不足以确认模型。",
        "sae-710287": "核对非线性轮胎负荷和阵风输入的原始方程与验证。",
        "sae-730232": "核对气动导数理论的公式、坐标和风梯度假设。",
        "dot-hs-805-078": "核对早期全尺寸有限侧风区试验、评价指标及 Volume II 对应关系。",
        "dot-hs-805-079": "核对188页技术报告中的风场、车辆/驾驶员工况与原始结果。",
        "sae-800848": "核对与1979 DOT 报告是否复用数据及整车响应指标。",
        "sae-960674": "核对静态偏航与动态阵风比较的工况、时程和误差。",
        "sae-970135": "核对剪切/湍流动态试验如何扩展1996方法。",
        "sae-970404": "核对早期瞬态 CFD 的网格、时间步和过车/侧风条件。",
        "sae-980392": "核对有限长度阵风实验的风场、载荷峰值和相位。",
        "sae-2000-01-0874": "核对 Durham 尾流测量方法与1998试验的关系；仓储文件返回403。",
        "sae-2000-01-0876": "核对简化车体表面压力的瞬态峰值和空间分布。",
        "iso-12021-2010": "核对现行风发生器开环标准的原文程序和合格条件。",
        "jfe-2013-volpe": "核对双风洞阵风设施的实际风场和验证；HAL 文档返回机器人验证页。",
        "jweia-2014-volpe": "核对突发横风载荷/流结构的实验参数与2013设施论文的差别。",
        "jcp-2016-tunay": "核对非定常 CFD—车辆—驾驶员耦合的数值方案和适用范围。",
        "sae-2017-01-1515": "核对单向 CFD/多体耦合与整车试验的 Level A/B/C 验证。",
        "sae-2017-01-1525": "核对6DoF+驾驶员耦合方法与其他2017工作的独立性。",
        "sae-06-14-01-0001": "核对全尺寸车辆非定常风洞工况和载荷统计。",
    }
    return reasons.get(source_id, "核对原文的阵风定义、方法参数和结论适用范围；当前证据限于摘要。")


PRIORITY = {
    "sae-530255": "P0", "dot-hs-805-079": "P0", "sae-730232": "P0",
    "sae-960674": "P0", "sae-980392": "P0", "iso-12021-2010": "P0",
    "jcp-2016-tunay": "P0", "sae-2017-01-1515": "P0", "jfe-2013-volpe": "P0",
    "sae-2000-01-0874": "P0", "dot-hs-805-078": "P0",
}

OFFICIAL_TITLE_CORRECTIONS = {
    "sae-970135": "Assessing the Effects of Shear and Turbulence During the Dynamic Testing of the Crosswind Sensitivity of Road Vehicles",
    "sae-2000-01-0876": "Transient Aerodynamic Characteristics of Simple Vehicle Shapes by the Measurement of Surface Pressures",
    "sae-15-18-01-0005": "Evaluation of an Unsteady Yaw, Gust, and Broadband Turbulence Generation System for Closed-Loop Automotive Wind Tunnels",
}


def attempted(row: dict) -> str:
    checks = []
    if row["doi_status"] == "verified":
        checks += ["Crossref DOI metadata", "publisher/DOI landing", "OpenAlex exact DOI"]
    else:
        checks += ["official/TRID catalog", "Crossref/DataCite title check"]
    if row["id"] == "sae-2000-01-0874":
        checks.append("Durham author repository (HTTP 403)")
    if row["id"] == "jfe-2013-volpe":
        checks.append("HAL open deposit (document bot challenge)")
    if row["id"] == "jcp-2016-tunay":
        checks.append("KTH DiVA author record (document anti-bot)")
    return "; ".join(checks)


def main() -> None:
    rows = read_csv(INDEX)
    registry = {row["id"]: row for row in read_csv(REGISTRY)}
    if len(rows) != 23 or len(registry) != len(rows):
        raise ValueError("Unexpected migration baseline; review sources before rerunning")
    ids = {row["id"] for row in rows}
    if len(ids) != len(rows):
        raise ValueError("Duplicate source ID")
    for row in rows:
        if row["id"] == "trid-116341" and row["doi_status"] == "missing_to_search":
            # 2026-09-25: TRID's authoritative serial entry has no DOI;
            # Crossref bibliographic and DataCite exact-title searches found none.
            # This remains reversible if the publisher later registers one.
            row["doi_status"] = "no_doi_confirmed"
            row["doi_verified_date"] = TODAY
            row["doi_source"] = "https://trid.trb.org/View/116341; Crossref bibliographic and DataCite exact-title search 2026-09-25"
            registry[row["id"]]["doi_status"] = row["doi_status"]
            registry[row["id"]]["doi_verified_date"] = TODAY
            registry[row["id"]]["doi_source"] = row["doi_source"]
            registry[row["id"]]["notes"] = "No DOI in TRID catalog or exact-title Crossref/DataCite search; reversible if publisher registration is found."
        corrected = OFFICIAL_TITLE_CORRECTIONS.get(row["id"])
        if corrected and row["title"] != corrected:
            old_title = row["title"]
            row["title"] = corrected
            registry[row["id"]]["title"] = corrected
            record_path = ROOT / "sources/records" / (row["id"] + ".md")
            record_path.write_text(record_path.read_text(encoding="utf-8").replace(old_title, corrected), encoding="utf-8")

    doi_groups: dict[str, list[str]] = defaultdict(list)
    number_groups: dict[tuple[str, str], list[str]] = defaultdict(list)
    title_groups: dict[tuple[str, str], list[str]] = defaultdict(list)
    for row in rows:
        if row["doi"]:
            doi_groups[row["doi"].casefold()].append(row["id"])
        if row["report_or_standard_number"] != "not_applicable":
            number_groups[(row["source_type"], norm(row["report_or_standard_number"]))].append(row["id"])
        title_groups[(norm(row["title"]), row["year"])].append(row["id"])
    for groups in (doi_groups, number_groups, title_groups):
        collisions = [ids for ids in groups.values() if len(ids) > 1]
        if collisions:
            raise ValueError(f"Possible exact duplicates need manual review: {collisions}")

    # The three retained pairs have distinct publication identifiers and content.
    candidate_pairs = [
        ("dot-hs-805-079", "dot-hs-805-078", "companion_report; separate technical and executive volumes", "kept_as_version"),
        ("sae-970135", "sae-960674", "method_extends; same authors, shear/turbulence added", "kept_as_version"),
        ("sae-2000-01-0874", "sae-980392", "facility_inherits; distinct wake survey and force paper", "kept_as_version"),
        ("sae-800848", "dot-hs-805-078", "same investigators/program; SAE analysis and DOT executive report differ", "kept_distinct"),
        ("jweia-2014-volpe", "jfe-2013-volpe", "references; vehicle forces and facility validation differ", "kept_distinct"),
    ]
    dedup = []
    for candidate, canonical, reason, action in candidate_pairs:
        a = next(row for row in rows if row["id"] == candidate)
        b = next(row for row in rows if row["id"] == canonical)
        dedup.append({
            "candidate_id": candidate, "canonical_id": canonical, "match_reason": reason,
            "doi_match": str(bool(a["doi"] and a["doi"].casefold() == b["doi"].casefold())).lower(),
            "title_match": str(norm(a["title"]) == norm(b["title"])).lower(),
            "author_year_match": str(norm(a["authors"]) == norm(b["authors"]) and a["year"] == b["year"]).lower(),
            "action": action, "review_status": "reviewed_metadata_and_existing_edges",
            "notes": "No record deleted; distinct identifier/content. " + reason,
        })
    write_csv(ROOT / "sources/dedup_report.csv", list(dedup[0]), dedup)
    write_csv(ROOT / "sources/aliases.csv", ["old_id", "canonical_id", "reason", "merged_date"], [])

    crossref_data = {}
    for row in rows:
        if row["doi_status"] == "verified":
            crossref_data[row["id"]] = crossref(row["doi"])

    bib_entries = []
    bib_sources = []
    queue = []
    for row in rows:
        source_id = row["id"]
        meta = crossref_data.get(source_id, {})
        registry_row = registry[source_id]
        source_url = ("https://api.crossref.org/works/" + urllib.parse.quote(row["doi"], safe="")) if meta else (row["doi_source"] or row["url"])
        source_name = "Crossref exact DOI + source index/record" if meta else "Source index/record + official catalog"
        meta_title = (meta.get("title") or [""])[0]
        title_similarity = difflib.SequenceMatcher(None, norm(meta_title), norm(row["title"])).ratio() if meta_title else None
        quality = "verified_doi_metadata" if meta and title_similarity is not None and title_similarity >= 0.75 else ("title_variant_review" if meta else "catalog_or_record_metadata")

        source_type = row["source_type"]
        entry_type = {
            "journal_article": "article", "review_article": "article", "sae_technical_paper": "techreport",
            "government_report": "techreport", "institutional_report": "techreport",
            "doctoral_thesis": "phdthesis", "master_thesis": "mastersthesis",
            "conference_paper": "inproceedings", "standard": "standard", "standard_draft": "standard",
        }.get(source_type, "misc")
        fields = {"author": bib_author(row, meta), "title": row["title"], "year": row["year"]}
        if entry_type == "article":
            fields.update(journal_fields(row, meta))
            if source_id == "jfe-2013-volpe":
                fields["eid"] = "011106"
                fields["pages"] = "011106/1--011106/9"
        elif entry_type == "techreport":
            fields["institution"] = row["publisher_or_institution"]
            fields["number"] = row["report_or_standard_number"]
            if source_type == "sae_technical_paper":
                fields["type"] = "SAE Technical Paper"
        elif entry_type in ("phdthesis", "mastersthesis"):
            fields["school"] = row["publisher_or_institution"]
            if source_id == "brandt-2023-thesis":
                fields["isbn"] = "978-91-7905-805-0"
                fields["number"] = "Chalmers New Series No. 5271"
        elif entry_type == "standard":
            fields["institution"] = row["publisher_or_institution"]
            fields["number"] = row["report_or_standard_number"]
        if meta.get("publisher"):
            fields["publisher"] = meta["publisher"]
        if row["doi_status"] == "verified":
            fields["doi"] = row["doi"]
        fields["url"] = row["url"]
        if row["tags"]:
            fields["keywords"] = ", ".join(tag.strip() for tag in row["tags"].split(";") if tag.strip())
        fields["note"] = "Crosswind keywords are curator tags, not necessarily author keywords."

        # SAE 2025 publisher PDF explicitly licenses the complete article CC BY 4.0.
        abstract_status = "available_not_copied"
        abstract_source = "Crossref deposited publisher abstract" if meta.get("abstract") else "Official source or catalog abstract noted in source record"
        abstract_url = source_url if meta.get("abstract") else row["url"]
        if source_id == "sae-15-18-01-0005":
            raw = meta.get("abstract", "")
            cleaned = html.unescape(raw)
            cleaned = re.sub(r"<[^>]+>", " ", cleaned)
            cleaned = re.sub(r"\s+", " ", cleaned).strip()
            if cleaned:
                fields["abstract"] = cleaned
                abstract_status = "full_abstract_saved"
                abstract_source = "SAE/Crossref publisher abstract; publisher full text CC BY 4.0"
                abstract_url = row["url"]
        elif source_id == "pimeche-2001-passmore":
            abstract_status = "full_text_supersedes_abstract"
            abstract_source = "Publisher abstract; author manuscript full text checked"
        elif source_id == "dot-hs-805-079":
            abstract_status = "available_not_copied"
            abstract_source = "TRID/NTIS catalog abstract; research claims remain metadata-level"

        lines = [f"@{entry_type}{{{source_id},"]
        for key, value in fields.items():
            rendered = str(value) if key == "author" and source_id == "iso-12021-2010" else bib_escape(str(value))
            lines.append(f"  {key} = {{{rendered}}},")
        lines.append("}")
        bib_entries.append("\n".join(lines))
        bib_sources.append({
            "id": source_id, "citation_key": source_id, "bib_source": source_name,
            "bib_source_url": source_url, "bib_checked_date": TODAY,
            "abstract_status": abstract_status, "abstract_source": abstract_source,
            "abstract_source_url": abstract_url, "abstract_checked_date": TODAY,
            "metadata_quality": quality,
            "notes": (
                "PDF summary lacks constituent papers A-E; no thesis-wide full-text promotion" if source_id == "brandt-2023-thesis"
                else "Original report absent; catalog abstract only" if source_id == "dot-hs-805-079"
                else "Article pages 011106/1-011106/9 from ISAE-SUPAERO faculty publication listing: https://pagespro.isae-supaero.fr/valerie-ferrand/flux-publications-open-science-isae-supaero.html" if source_id == "jfe-2013-volpe"
                else ""
            ),
        })
        row["bib_key"] = source_id
        row["abstract_status"] = abstract_status
        registry_row["bib_key"] = source_id
        registry_row["verification_status"] = row["verification_status"]

        if row["pdf_status"] not in ("oa_downloaded", "user_provided", "institutional_access"):
            attempted_text = attempted(row)
            queue.append({
                "id": source_id, "title": row["title"], "authors": row["authors"],
                "year": row["year"], "source_type": source_type, "doi": row["doi"],
                "official_url": row["url"], "pdf_status": row["pdf_status"],
                "repository_url": registry_row["pdf_source"] if row["pdf_status"] == "open_repository_available" else "",
                "reason_missing": source_reason(row), "sources_attempted": attempted_text,
                "priority": PRIORITY.get(source_id, "P1"), "requested_date": TODAY,
                "last_checked": TODAY, "manual_status": "needs_user_search",
                "user_supplied_path": "", "notes": "Additional legal OA/library searches remain possible; current status is not proof no OA exists.",
            })

    (BIB_DIR / "references.bib").write_text("% Crosswind canonical bibliography. Keys equal stable source IDs.\n% Abstracts copied only when an explicit redistribution licence was verified.\n\n" + "\n\n".join(bib_entries) + "\n", encoding="utf-8")
    write_csv(BIB_DIR / "bib_sources.csv", list(bib_sources[0]), bib_sources)
    write_csv(INDEX, list(rows[0]), rows)
    write_csv(REGISTRY, list(next(iter(registry.values()))), [registry[row["id"]] for row in rows])

    for row, provenance in zip(rows, bib_sources):
        record_path = ROOT / "sources/records" / (row["id"] + ".md")
        record = record_path.read_text(encoding="utf-8")
        heading = f"## Bibliography and abstract provenance ({TODAY})"
        if heading in record:
            continue
        if row["verification_status"] == "full_text_verified":
            scope = "Complete source PDF was previously read and remains `full_text_verified`."
        elif row["id"] == "brandt-2023-thesis":
            scope = "The 92-page PDF provides the extended thesis summary only; Paper A-E appendices are absent. Keep the source-wide status `abstract_verified`."
        elif row["id"] == "dot-hs-805-079":
            scope = "TRID catalog abstract exists, but the original report remains unavailable; retain `metadata_verified`."
        else:
            scope = "No full text has been validated; do not promote claims beyond the current evidence level."
        addition = (
            f"\n{heading}\n\n"
            f"- Canonical Bib key: `{row['id']}` in `sources/bibliography/references.bib`.\n"
            f"- abstract_status: `{provenance['abstract_status']}`; abstract_source: {provenance['abstract_source']}; "
            f"abstract_source_url: {provenance['abstract_source_url']}.\n"
            f"- Full-text check: {scope}\n"
        )
        record_path.write_text(record.rstrip() + "\n" + addition, encoding="utf-8")
    queue.sort(key=lambda item: (item["priority"], int(item["year"]), item["id"]))
    write_csv(ROOT / "sources/manual_retrieval_queue.csv", list(queue[0]), queue)

    md = [
        "# 需要用户手动查找的资料",
        "",
        f"截至 {TODAY}：新增 {len(queue)} 条，当前未解决 {len(queue)} 条。优先使用官方入口或机构图书馆的合法权限获取；取得后放入 `sources/pdfs/`，下轮将校验题名/DOI、PDF 格式和 SHA-256。",
        "",
        "这些条目已检查所列渠道，但 Unpaywall 需要可用联系邮箱、Semantic Scholar 曾返回 429，部分机构仓储限制自动访问。仍可能存在其他合法 OA 版本；清单不是永久付费判断。",
        "",
        "| 优先级 | 题名；作者；年份 | DOI | 官方入口 | 需要全文的原因 | 已尝试渠道 |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for item in queue:
        title = item["title"].replace("|", "\\|")
        authors = item["authors"].replace("|", "\\|")
        entrance = f"[官方/权威入口]({item['official_url']})"
        if item["repository_url"]:
            entrance += f"；[机构仓储]({item['repository_url']})"
        md.append(f"| {item['priority']} | {title}；{authors}；{item['year']} | {item['doi'] or '未确认'} | {entrance} | {item['reason_missing']} | {item['sources_attempted']} |")
    md += ["", "收到文件后不默认拥有再分发权。只有明确允许再分发的 PDF 才会纳入 GitHub；其余仅本机保存。", ""]
    (ROOT / "sources/manual_retrieval_queue.md").write_text("\n".join(md), encoding="utf-8")
    print(f"Migration: {len(rows)} sources, {len(bib_entries)} Bib entries, {len(queue)} manual requests, 0 exact duplicates, 3 retained related pairs")
    print("Crossref metadata responses:", len([item for item in crossref_data.values() if item]))


if __name__ == "__main__":
    main()
