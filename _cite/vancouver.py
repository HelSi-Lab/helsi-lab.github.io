"""
Post-processing step: convert author names to Vancouver style.

Reads _members/*.md to auto-detect the PI (bold) and lab students (underline).
Converts "Given M. Family" → "Family GM" for all authors.
Special tokens like "et al." and "…" are preserved as-is.
"""

import re
import yaml
from pathlib import Path


# tokens that should never be converted
_PASSTHROUGH = {"et al.", "et al", "…", "..."}


def _load_members(members_dir="_members"):
    """
    Read _members/*.md front-matter.
    Returns (pi_names: set, student_names: set) of full natural names.
    """
    pi_names = set()
    student_names = set()
    members_path = Path(members_dir)

    if not members_path.is_dir():
        return pi_names, student_names

    for md_file in members_path.glob("*.md"):
        text = md_file.read_text(encoding="utf-8")
        parts = text.split("---")
        if len(parts) < 3:
            continue
        try:
            meta = yaml.safe_load(parts[1])
        except yaml.YAMLError:
            continue

        name = (meta.get("name") or "").strip()
        if not name:
            continue

        # Also collect any aliases
        aliases = meta.get("aliases") or []
        all_names = [name] + [a.strip() for a in aliases if a and a.strip()]

        if meta.get("is-pi") or meta.get("role") == "pi":
            pi_names.update(all_names)
        else:
            student_names.update(all_names)

    return pi_names, student_names


def _name_to_vancouver(full_name):
    """
    Convert a single natural name to Vancouver abbreviated form.
    "Jeremy D. Goldhaber-Fiebert" → "Goldhaber-Fiebert JD"
    "Serin Lee"                   → "Lee S"
    "Li Tao"                      → "Tao L"
    """
    parts = full_name.split()
    if len(parts) < 2:
        return full_name

    last_name = parts[-1]
    initials = "".join(p.rstrip(".")[0].upper() for p in parts[:-1])
    return f"{last_name} {initials}"


def _strip_markup(name):
    """Remove **bold** and <u>underline</u> markup, return (clean_name, suffix)."""
    s = name.strip()

    # extract suffix like (PI)
    suffix = ""
    m = re.search(r"\s*\(PI\)\s*$", s)
    if m:
        suffix = " (PI)"
        s = s[: m.start()].strip()

    # strip bold
    if s.startswith("**") and s.endswith("**"):
        s = s[2:-2].strip()

    # strip underline
    if s.startswith("<u>") and s.endswith("</u>"):
        s = s[3:-4].strip()

    return s, suffix


def _format_author(name, pi_names, student_names):
    """
    Convert one author string to Vancouver with appropriate markup.
    """
    clean, suffix = _strip_markup(name)

    # passthrough special tokens
    if clean in _PASSTHROUGH:
        return name

    vancouver = _name_to_vancouver(clean)

    # apply markup based on lab membership
    if clean in pi_names:
        return f"**{vancouver}**{suffix}"
    if clean in student_names:
        return f"<u>{vancouver}</u>{suffix}"

    return f"{vancouver}{suffix}"


def format_citations(citations, members_dir="_members"):
    """
    In-place: convert all author names in a list of citation dicts
    to Vancouver style with PI bold and student underline.
    """
    pi_names, student_names = _load_members(members_dir)

    for citation in citations:
        authors = citation.get("authors")
        if not authors or not isinstance(authors, list):
            continue
        citation["authors"] = [
            _format_author(a, pi_names, student_names) for a in authors
        ]

    return citations
