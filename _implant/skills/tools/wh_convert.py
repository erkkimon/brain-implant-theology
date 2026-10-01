#!/usr/bin/env python3
"""Convert Robinson's Westcott-Hort text files into the JSON `bible_ingest.py` reads.

The source (byztxt/greektext-westcott-hort, `textonly/*.WH`, stored lower-cased as `*.txt`) is Greek in Latin
letters, one file per book, verses opening a line as `     1:1 text` and running
over following lines. This tool:

  * transliterates it to unaccented lower-case Greek, the form the `TR`
    section already uses (final sigma is written `v` in the source, so there
    is no guessing about it);
  * keeps the square brackets W-H print around doubtful words, and writes
    its double brackets (later additions) as ⟦ ⟧ so markdown cannot read
    them as wiki-links;
  * leaves out verses the source carries with no text (W-H omits them: Matt
    12:47, Mark 9:44 ... the ingest skips an empty verse, so the token simply
    has no `WH` section);
  * folds the one verse the numbering disagrees on (3 John 1:15 into 14,
    because the tokens follow KJV numbering);
  * strips Robinson's in-text `[c:v]` versification markers (reported);
  * resolves Robinson's `|` marker for alternative readings by an explicit,
    reported override, never silently.

It refuses to finish unless every KJV chapter is present and every verse
number it produced exists in the KJV file (so no text lands under a token that
does not exist), and unless the source uses only the letters mapped here.
Deterministic, no model calls.

Usage:
    python3 wh_convert.py --source-dir raw/translations/wh/source \
        --shape raw/translations/kjv/kjv.json --out _temp/wh.json
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from bookcodes import CANON, code_for  # noqa: E402

# Source file stem for each NT book code, in canon order.
FILES = {
    "mat": "MT", "mrk": "MR", "luk": "LU", "jhn": "JOH", "act": "AC",
    "rom": "RO", "1co": "1CO", "2co": "2CO", "gal": "GA", "eph": "EPH",
    "php": "PHP", "col": "COL", "1th": "1TH", "2th": "2TH", "1ti": "1TI",
    "2ti": "2TI", "tit": "TIT", "phm": "PHM", "heb": "HEB", "jas": "JAS",
    "1pe": "1PE", "2pe": "2PE", "1jn": "1JO", "2jn": "2JO", "3jn": "3JO",
    "jud": "JUDE", "rev": "RE",
}

# Robinson's transliteration (Online Bible / CCAT-style, with y=theta,
# q=psi, c=chi, v=final sigma). Anything else is an error, not a guess.
LETTERS = {
    "a": "α", "b": "β", "g": "γ", "d": "δ", "e": "ε", "z": "ζ", "h": "η",
    "y": "θ", "i": "ι", "k": "κ", "l": "λ", "m": "μ", "n": "ν", "x": "ξ",
    "o": "ο", "p": "π", "r": "ρ", "s": "σ", "v": "ς", "t": "τ", "u": "υ",
    "f": "φ", "c": "χ", "q": "ψ", "w": "ω",
}

# Verses the source gives in a different numbering than the KJV: (code, ch, verse)
# -> the KJV verse its text belongs to. 3 John has 15 verses in W-H, 14 in KJV.
FOLD = {("3jn", 1, 15): 14}

# `|` marks alternative readings in Robinson's files. Mark 1:45 reads
# `eiselyein | alla | all | exw ...`: alternatives `alla` and `all`
# (elided alla, as in W-H's printed text and the TR section). Take `all`.
PIPE_OVERRIDES = {("mrk", 1, 45): ("| alla | all |", "all")}

# Robinson also prints `[2:7]` inside the text where another edition's verse
# break falls. That is versification apparatus, not text: stripped and
# reported. (Doubtful-word brackets like `[ihsou]` never contain a colon.)
MARKER_RE = re.compile(r"\s*\[\d+:\d+\]\s*")

VERSE_RE = re.compile(r"^\s+(\d+):(\d+)(?:\s+(.*))?$")


def to_greek(text: str, where: str) -> str:
    # W-H's `[[ ... ]]` marks passages the editors judge later additions
    # (Luke 22:19b-20, 22:43-44, John 7:53-8:11 ...), often spanning verses.
    # Markdown reads `[[x]]` as a wiki-link, so they are written as the
    # mathematical white brackets, which keep the two grades distinct from
    # the single `[doubtful]` brackets.
    text = text.replace("[[", "\u27e6").replace("]]", "\u27e7")
    out = []
    for ch in text:
        if ch in LETTERS:
            out.append(LETTERS[ch])
        elif ch in " []\u27e6\u27e7":
            out.append(ch)
        else:
            raise SystemExit(f"{where}: character {ch!r} has no mapping — extend LETTERS or handle it")
    return " ".join("".join(out).split())


def parse_book(path: Path, code: str) -> dict[tuple[int, int], str]:
    verses: dict[tuple[int, int], list[str]] = {}
    cur = None
    for raw in path.read_text(encoding="ascii").replace("\r", "").split("\n"):
        m = VERSE_RE.match(raw)
        if m:
            cur = (int(m.group(1)), int(m.group(2)))
            if cur in verses:
                raise SystemExit(f"{path.name}: verse {cur[0]}:{cur[1]} appears twice")
            verses[cur] = [m.group(3) or ""]
        elif raw.strip():
            if cur is None:
                raise SystemExit(f"{path.name}: text before the first verse: {raw!r}")
            verses[cur].append(raw.strip())
    return {k: " ".join(" ".join(v).split()) for k, v in verses.items()}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--source-dir", required=True, type=Path)
    ap.add_argument("--shape", required=True, type=Path, help="KJV json: the chapters/verses that exist")
    ap.add_argument("--out", required=True, type=Path)
    args = ap.parse_args()

    kjv = json.loads(args.shape.read_text(encoding="utf-8"))
    shape = {code_for(b["name"]): {int(c["chapter"]): len(c["verses"]) for c in b["chapters"]}
             for b in kjv["books"]}
    names = {code_for(b["name"]): b["name"] for b in kjv["books"]}

    notes: list[str] = []
    books = []
    n_verses = n_empty = 0
    for code, _name in CANON:
        if code not in FILES:
            continue
        raw = parse_book(args.source_dir / f"{FILES[code].lower()}.txt", code)
        chapters: dict[int, dict[int, str]] = {}
        for (c, v), text in sorted(raw.items()):
            if (code, c, v) in FOLD:
                tv = FOLD[(code, c, v)]
                text = to_greek(text, f"{code} {c}:{v}")
                chapters[c][tv] = (chapters[c][tv] + " " + text).strip()
                notes.append(f"{names[code]} {c}:{v} folded into {c}:{tv} (KJV numbering)")
                continue
            if (code, c, v) in PIPE_OVERRIDES:
                marker, keep = PIPE_OVERRIDES[(code, c, v)]
                if marker not in text:
                    raise SystemExit(f"{code} {c}:{v}: expected {marker!r} in the source, not found")
                text = text.replace(marker, keep)
                notes.append(f"{names[code]} {c}:{v}: alternative readings {marker!r} resolved to {keep!r}")
            found = MARKER_RE.findall(text)
            if found:
                text = MARKER_RE.sub(" ", text).strip()
                notes.append(f"{names[code]} {c}:{v}: stripped versification marker(s) "
                             f"{[f.strip() for f in found]}")
            if "|" in text:
                raise SystemExit(f"{code} {c}:{v}: unhandled `|` alternative-reading marker")
            if v not in range(1, shape[code].get(c, 0) + 1):
                raise SystemExit(f"{code} {c}:{v}: no such verse in the KJV numbering")
            if not text.strip():
                n_empty += 1
                notes.append(f"{names[code]} {c}:{v}: empty in the source (omitted by W-H) — no WH section")
                continue
            chapters.setdefault(c, {})[v] = to_greek(text, f"{code} {c}:{v}")
            n_verses += 1
        missing = set(shape[code]) - set(chapters)
        if missing:
            raise SystemExit(f"{names[code]}: chapters missing from the source: {sorted(missing)}")
        books.append({"name": names[code], "chapters": [
            {"chapter": c, "verses": [{"verse": v, "text": t} for v, t in sorted(vs.items())]}
            for c, vs in sorted(chapters.items())]})

    args.out.write_text(json.dumps({"translation": "Westcott-Hort Greek New Testament (1881)",
                                    "books": books}, ensure_ascii=False, indent=1) + "\n",
                        encoding="utf-8")
    for n in notes:
        print("note:", n)
    print(f"converted {len(books)} books, {n_verses} verses with text, {n_empty} empty -> {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
