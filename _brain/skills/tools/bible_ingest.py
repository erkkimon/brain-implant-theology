#!/usr/bin/env python3
"""Turn a Bible translation into chapter documents with atomic verse tokens.

One document per chapter (1,189 for a Protestant canon), each carrying every
verse of that chapter as a heading with its atomic reference token, and the
full token list in frontmatter. Translations are CLUSTERED on the chapter: a
second translation merges into the existing chapter file as another section
rather than creating a parallel tree, so reading a passage shows how the
renderings differ.

Deterministic and idempotent — no model calls. Rerunning with the same input
produces byte-identical output, so a re-ingest shows an empty diff.

Why tokens at all: brainpick's BM25 tokenizer splits on punctuation, so
`John 14:6` indexes as john/14/6 — the same term set as `John 6:14`, which it
then cannot tell apart. `jhn14v6` survives as one term. Never hand-write a
token; that is this tool's whole job. See conventions/addressing-scripture.md.

Usage:
    python3 bible_ingest.py --source KJV.json --name "King James Version" \
        --abbrev KJV --out ../../knowledge/scripture [--limit-books John]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from bookcodes import CANON_ORDER, CODE_TO_NAME, code_for, human_ref, verse_token  # noqa: E402

SECTION_RE = re.compile(r"^## (.+?) — (.+)$", re.M)


def load_source(path: Path) -> dict:
    """Read a bible_databases-style JSON: {translation, books:[{name,chapters:[{chapter,verses:[{verse,text}]}]}]}."""
    data = json.loads(path.read_text(encoding="utf-8"))
    if "books" not in data:
        raise SystemExit(f"{path}: expected a top-level 'books' key")
    return data


def chapter_body(code: str, chapter: int, verses: list[dict], abbrev: str) -> str:
    """One translation's rendering of one chapter, as a markdown section."""
    lines = [f"## {abbrev} — {human_ref(code, chapter)}", ""]
    for v in verses:
        num, text = int(v["verse"]), " ".join(str(v["text"]).split())
        token = verse_token(code, chapter, num)
        # The verse heading carries the token AND the human reference: the
        # token is the retrieval key, the reference is what a person reads.
        # brain_read's `sections` can fetch one verse without the chapter.
        lines.append(f"### {human_ref(code, chapter, num)} `{token}`")
        lines.append("")
        lines.append(text)
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def render_chapter(code: str, chapter: int, verses: list[dict], name: str,
                   abbrev: str, existing: str | None) -> str:
    """Build (or extend) a chapter document. Clusters translations on one file."""
    tokens = [verse_token(code, chapter, int(v["verse"])) for v in verses]
    ref = human_ref(code, chapter)
    body = chapter_body(code, chapter, verses, abbrev)

    if existing:
        # Merge: keep existing sections, replace this translation's own, append
        # if new. Frontmatter is rebuilt so `verses:` is the union of tokens.
        # Split off the WHOLE frontmatter block: it opens with --- and closes
        # with ---, so partitioning on the first delimiter alone would leave a
        # fragment in the body and make the output differ run to run.
        if existing.startswith("---\n"):
            old_fm, _, rest = existing[4:].partition("\n---\n")
        else:
            old_fm, rest = "", existing
        old_tokens = []
        m = re.search(r"^verses:\s*\[(.*?)\]", old_fm, re.S | re.M)
        if m:
            old_tokens = [t.strip() for t in m.group(1).split(",") if t.strip()]
        tokens = sorted(set(old_tokens) | set(tokens),
                        key=lambda t: (int(re.search(r"v(\d+)$", t).group(1))))
        sections = {}
        for hm in SECTION_RE.finditer(rest):
            start = hm.start()
            nxt = SECTION_RE.search(rest, hm.end())
            sections[hm.group(1)] = rest[start:nxt.start() if nxt else len(rest)].rstrip() + "\n"
        sections[abbrev] = body
        intro = rest[:SECTION_RE.search(rest).start()] if SECTION_RE.search(rest) else ""
        merged = intro.rstrip() + "\n\n" + "\n\n".join(
            sections[k] for k in sorted(sections)) + "\n"
        rest = merged

    else:
        rest = (
            f"# {ref}\n\n"
            f"Verses are addressed by atomic reference token — "
            f"`{verse_token(code, chapter, 1)}` is {human_ref(code, chapter, 1)} — "
            f"because the search tokenizer splits `{ref}:1` into separate terms "
            f"and cannot then tell it from `{CODE_TO_NAME[code]} 1:{chapter}`. "
            f"See [addressing scripture](../../conventions/addressing-scripture.md).\n\n"
            + body
        )

    # Frontmatter is rebuilt from the document's actual content every time —
    # one code path for the first write and for a later merge — so run 1 and
    # run 2 produce byte-identical files and a re-ingest diffs empty.
    present = sorted(set(re.findall(r"^## (\S+) — ", rest, re.M))) or [abbrev]
    fm = (
        "---\n"
        "type: article\n"
        "about: scripture\n"
        f"title: {ref}\n"
        f'description: "{ref} — the full chapter, every verse individually '
        f'addressable by atomic reference token, with each stored translation '
        f'rendered as its own section so the passage can be compared across '
        f'translations in one read."\n'
        f"book: {code}\n"
        f"chapter: {chapter}\n"
        f"verses: [{', '.join(tokens)}]\n"
        f"translations: [{', '.join(present)}]\n"
        f"tags: [scripture, {code}]\n"
        "timestamp: 2026-09-24T20:00:00Z\n"
        "half_life: 0\n"
        "---\n\n"
    )
    # Normalise the ending so the fresh path and the merge path agree exactly:
    # one trailing newline, always. Without this the two differ by a blank line
    # and every re-ingest rewrites every file for no reason.
    return fm + rest.strip("\n") + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--source", required=True, type=Path, help="translation JSON")
    ap.add_argument("--name", required=True, help='full name, e.g. "King James Version"')
    ap.add_argument("--abbrev", required=True, help="short code used as the section heading, e.g. KJV")
    ap.add_argument("--out", required=True, type=Path, help="knowledge/scripture directory")
    ap.add_argument("--limit-books", nargs="*", default=None,
                    help="only these book names (for a smoke test)")
    args = ap.parse_args()

    data = load_source(args.source)
    args.out.mkdir(parents=True, exist_ok=True)

    written = skipped = 0
    for book in data["books"]:
        if args.limit_books and book["name"] not in args.limit_books:
            continue
        code = code_for(book["name"])
        for ch in book["chapters"]:
            n = int(ch["chapter"])
            path = args.out / f"{code}{n:03d}.md"
            existing = path.read_text(encoding="utf-8") if path.exists() else None
            doc = render_chapter(code, n, ch["verses"], args.name, args.abbrev, existing)
            if existing == doc:
                skipped += 1
                continue
            path.write_text(doc, encoding="utf-8")
            written += 1

    print(f"{args.abbrev}: {written} chapter documents written, {skipped} unchanged", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
