"""Custom checks for the implant (ported from stem, with apologetics-specific additions).

Stem checks ported:
  - log_headings_are_dates
  - skill_tools_exist
  - archived_journals_sit_under_year_month
  - done_todos_are_archived

Theology-specific additions:
  - translation_licence_present — every stored translation states its licence
  - verse_tokens_well_formed    — chapter `verses:` tokens are atomic and match the file
"""

import datetime
import re

import yaml

from henxels import statement

_SECTION = re.compile(r"^##\s+(.+?)\s*$")
_DAY = re.compile(r"^(\d{4})-(\d{2})-(\d{2})\.md$")
_CHECKBOX = re.compile(r"^\s*[-*+]\s+\[([ xX])\]\s+(.*?)\s*$")
_DONE = re.compile(r"\(done:\s*(\d{4}-\d{2}-\d{2})\)\s*$")

# An atomic verse reference token: book code, chapter, 'v', verse — no
# punctuation, so brainpick's BM25 tokenizer cannot split it. Ranges allowed
# as jhn14v6to7. See conventions/addressing-scripture.md.
_VERSE_TOKEN = re.compile(r"^[1-3]?[a-z]{2,3}\d{1,3}v\d{1,3}(?:to\d{1,3})?$")


def _folder(param):
    return str(param).strip().removeprefix("./").strip("/")


def _frontmatter(text):
    """The leading ``---`` YAML block as a dict (empty when absent or unparseable)."""
    if not text or not text.startswith("---"):
        return {}
    lines = text.splitlines()
    end = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), None)
    if end is None:
        return {}
    try:
        data = yaml.safe_load("\n".join(lines[1:end]))
    except yaml.YAMLError:
        return {}
    return data if isinstance(data, dict) else {}


@statement("log_headings_are_dates", help="log.md sections are '## YYYY-MM-DD' headings, newest first")
def log_headings_are_dates(file, scope):
    dates, problems = [], []
    for line in (scope.read_text(file) or "").splitlines():
        m = _SECTION.match(line)
        if not m:
            continue
        try:
            dates.append(datetime.date.fromisoformat(m.group(1)))
        except ValueError:
            problems.append(f"section '{m.group(1)}' — head log sections with an ISO date: ## YYYY-MM-DD")
    if dates != sorted(dates, reverse=True):
        problems.append("order the date sections newest first")
    return problems


@statement("skill_tools_exist", help="every path a skill lists under `tools:` exists, relative to the bundle root")
def skill_tools_exist(param, file, scope):
    """brainpick indexes and points at a skill's tools (spec/85); a path that lands
    nowhere is a broken promise. `param` is the bundle root (./_implant)."""
    root = _folder(param)
    tools = _frontmatter(scope.read_text(file)).get("tools") or []
    if not isinstance(tools, list):
        return f"{file} — `tools:` must be a list of bundle-relative paths"
    missing = [t for t in tools if not scope.exists(f"{root}/{str(t).lstrip('/')}")]
    return [f"{file} — tool {t} does not exist under {root}/ (add it or drop it from `tools:`)" for t in missing]


@statement("archived_journals_sit_under_year_month",
           help="archived journal days live at archive/YYYY/MM/YYYY-MM-DD.md, the folders matching the name")
def archived_journals_sit_under_year_month(param, file, scope):
    """`param` is the archive folder (./_implant/journals/archive)."""
    archive = _folder(param)
    rel = file[len(archive) + 1:] if file.startswith(archive + "/") else file
    name = rel.rsplit("/", 1)[-1]
    m = _DAY.match(name)
    if not m:
        return f"{file} — name an archived day YYYY-MM-DD.md"
    want = f"{m.group(1)}/{m.group(2)}/{name}"
    if rel != want:
        return f"{file} — move it to {archive}/{want} (the day roll keeps archive/YYYY/MM/)"
    return None


@statement("done_todos_are_archived",
           help="a [x] item in open.md carries (done: YYYY-MM-DD) and leaves for archive/YYYY-MM-DD.md the next day; "
                "the archive is day files holding only done items")
def done_todos_are_archived(param, file, scope):
    """`param` is the todo folder (./_implant/todo)."""
    todo = _folder(param)
    rel = file[len(todo) + 1:] if file.startswith(todo + "/") else file
    problems = []
    items = [(m.group(1).lower() == "x", m.group(2)) for m in map(_CHECKBOX.match, (scope.read_text(file) or "").splitlines()) if m]
    if rel == "open.md":
        today = datetime.date.today()
        for done, text in items:
            if not done:
                continue
            m = _DONE.search(text)
            if not m:
                problems.append(f"{file} — '{text[:40]}' is ticked but undated: end it with (done: YYYY-MM-DD)")
                continue
            day = m.group(1)
            if datetime.date.fromisoformat(day) < today:
                problems.append(f"{file} — '{text[:40]}' was done {day}: move the line to {todo}/archive/{day}.md")
        return problems
    if rel.startswith("archive/"):
        name = rel.rsplit("/", 1)[-1]
        if "/" in rel[len("archive/"):] or not _DAY.match(name):
            return f"{file} — an archived to-do file is {todo}/archive/YYYY-MM-DD.md, the day its items were closed"
        for done, text in items:
            if not done:
                problems.append(f"{file} — '{text[:40]}' is still open: it belongs in {todo}/open.md, not the archive")
        return problems
    return None


# --- Theology-specific checks -----------------------------------------------

@statement("translation_licence_present",
           help="every translation folder under raw/translations/ holds a LICENCE.md stating its redistribution terms")
def translation_licence_present(param, file, scope):
    """`param` is the translations folder. Scripture text is cleared BEFORE it
    is stored: a translation folder without a stated licence is a licensing
    failure waiting to be published."""
    root = _folder(param)
    rel = file[len(root) + 1:] if file.startswith(root + "/") else file
    parts = rel.split("/")
    if len(parts) < 2:
        return None            # a file directly in translations/, not a translation folder
    if not scope.exists(f"{root}/{parts[0]}/LICENCE.md"):
        return (f"{file} — translation '{parts[0]}' has no LICENCE.md. State its "
                "redistribution terms before storing its text; a translation that "
                "may not be redistributed is cited by reference only.")
    return None


@statement("verse_tokens_well_formed",
           help="a scripture chapter's `verses:` frontmatter lists atomic reference tokens (jhn14v6) that the search tokenizer cannot split")
def verse_tokens_well_formed(param, file, scope):
    """`param` is the scripture folder. The tokens are the retrieval key for
    finding content BY VERSE; a malformed one is invisible rather than loud,
    which is exactly the failure the addressing convention exists to prevent."""
    verses = _frontmatter(scope.read_text(file)).get("verses") or []
    if not isinstance(verses, list):
        return f"{file} — `verses:` must be a list of atomic reference tokens (e.g. [jhn14v1, jhn14v2])"
    problems = []
    for v in verses:
        tok = str(v)
        if not _VERSE_TOKEN.match(tok):
            problems.append(
                f"{file} — '{tok}' is not an atomic verse token. Use <book><chapter>v<verse>, "
                "lowercase alphanumeric only (jhn14v6, 1co13v4, jhn14v6to7) — punctuation "
                "would let the BM25 tokenizer split it apart.")
    return problems
