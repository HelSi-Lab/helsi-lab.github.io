"""Expand selected entries from a BibTeX library into citation records."""

import re
from pathlib import Path

import bibtexparser


_MONTHS = {
    "jan": 1,
    "january": 1,
    "feb": 2,
    "february": 2,
    "mar": 3,
    "march": 3,
    "apr": 4,
    "april": 4,
    "may": 5,
    "jun": 6,
    "june": 6,
    "jul": 7,
    "july": 7,
    "aug": 8,
    "august": 8,
    "sep": 9,
    "sept": 9,
    "september": 9,
    "oct": 10,
    "october": 10,
    "nov": 11,
    "november": 11,
    "dec": 12,
    "december": 12,
}


def _strip_outer_braces(value):
    value = value.strip()
    while value.startswith("{") and value.endswith("}"):
        depth = 0
        balanced = True
        for index, char in enumerate(value):
            if char == "{":
                depth += 1
            elif char == "}":
                depth -= 1
                if depth == 0 and index != len(value) - 1:
                    balanced = False
                    break
        if not balanced or depth != 0:
            break
        value = value[1:-1].strip()
    return value


def _clean_latex(value):
    """Convert the small subset of LaTeX used by the lab bibliography."""
    if not value:
        return ""
    value = re.sub(r"\\textbf\s*\{([^{}]*)\}", r"\1", str(value))
    value = _strip_outer_braces(value)
    value = value.replace(r"\&", "&")
    value = value.replace("{", "").replace("}", "")
    value = re.sub(r"\s+", " ", value)
    return value.strip()


def _author_to_natural(author):
    author = _clean_latex(author)
    if not author:
        return ""
    if "," in author:
        family, given = [part.strip() for part in author.split(",", 1)]
        return " ".join(part for part in [given, family] if part)
    return author


def _authors(value):
    return [
        name
        for name in (
            _author_to_natural(author)
            for author in re.split(r"\s+and\s+", value or "", flags=re.IGNORECASE)
        )
        if name
    ]


def _doi(value):
    value = _clean_latex(value)
    value = re.sub(r"^https?://(?:dx\.)?doi\.org/", "", value, flags=re.IGNORECASE)
    value = re.sub(r"^doi:\s*", "", value, flags=re.IGNORECASE)
    return value.strip()


def _date(record):
    year = _clean_latex(record.get("year", ""))
    if not re.fullmatch(r"\d{4}", year):
        return ""
    raw_month = _clean_latex(record.get("month", "")).lower()
    try:
        month = int(raw_month)
    except ValueError:
        month = _MONTHS.get(raw_month, 1)
    if month < 1 or month > 12:
        month = 1
    return f"{year}-{month:02d}-01"


def _citation(record, group):
    doi = _doi(record.get("doi", ""))
    journal = _clean_latex(record.get("journal") or record.get("booktitle") or "")
    citation = {
        "id": f"doi:{doi}" if doi else f"bib:{record['ID']}",
        "cite_key": record["ID"],
        "title": _clean_latex(record.get("title", "")),
        "authors": _authors(record.get("author", "")),
        "publisher": journal,
        "journal": journal,
        "year": _clean_latex(record.get("year", "")),
        "volume": _clean_latex(record.get("volume", "")),
        "issue": _clean_latex(record.get("number", "")),
        "pages": _clean_latex(record.get("pages", "")).replace("--", "-"),
        "doi": doi,
        "date": _date(record),
        "group": group,
        "link": f"https://doi.org/{doi}" if doi else "",
        "author_style": "vancouver",
    }
    return {key: value for key, value in citation.items() if value != ""}


def main(entry):
    """Read one configured BibTeX file and return its selected entries."""
    path = Path(entry["path"])
    if not path.is_file():
        raise Exception(f"BibTeX file not found: {path}")

    parser = bibtexparser.bparser.BibTexParser(common_strings=True)
    library = bibtexparser.loads(path.read_text(encoding="utf-8"), parser=parser)
    records = {record["ID"]: record for record in library.entries}
    overrides = entry.get("overrides") or {}
    citations = []

    for group, keys in (entry.get("groups") or {}).items():
        for key in keys:
            if key not in records:
                raise Exception(f"BibTeX entry not found: {key}")
            citation = _citation(records[key], group)
            citation.update(overrides.get(key) or {})
            citation = {
                field: value
                for field, value in citation.items()
                if value is not None and value != ""
            }
            citations.append(citation)

    return citations
