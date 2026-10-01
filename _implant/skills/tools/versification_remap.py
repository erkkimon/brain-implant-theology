#!/usr/bin/env python3
"""Re-number a Hebrew-versified Bible source into the KJV numbering the tokens use.

The verse tokens (`gen32v1`) follow the KJV/English numbering. The Westminster
Leningrad Codex numbers the Hebrew way, and 138 of its 929 chapters differ in
verse count from the KJV (Gen 31-32, Exod 7-8, Psalms with their titles
counted as verses, Joel 2-4, Malachi 3-4 ...). Ingesting it as-is would put the
wrong Hebrew under a token and nothing would complain. This adapter sits
between the raw source and `bible_ingest.py`:

    source.json  +  eng.json (standard mapping)  +  kjv.json (the shape to hit)
        ->  source in KJV numbering  (same JSON shape, ready for bible_ingest)

The mapping is the Copenhagen Alliance / Paratext `eng` standard
(`mappedVerses`: English reference -> original-language reference).

Rules, all checked rather than assumed:
  * an English verse with a mapping rule takes the Hebrew verse(s) it names;
    one without takes the Hebrew verse with the same number;
  * English verse 0 (a psalm title counted separately) is folded into English
    verse 1, the way the KJV file already carries titles inside verse 1;
  * a Hebrew verse no rule claims (Ps 51:1, 52:1, 54:1, 60:1 - the first line
    of a two-verse title; Num 25:19, which opens KJV Num 26:1) is folded into
    the verse that owns the next Hebrew verse, and reported;
  * the result must reproduce the KJV chapter and verse counts exactly, every
    Hebrew verse must be used exactly once, and any exception stops the run.

Deterministic, no model calls.

Usage:
    python3 versification_remap.py --source WLC.json --mapping eng.json \
        --shape kjv.json --out WLC-kjv-numbering.json
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from bookcodes import CODE_TO_NAME, code_for  # noqa: E402

REF = re.compile(r"^(\w{3}) (\d+):(\d+)(?:-(\d+))?$")


def expand(ref: str) -> tuple[str, list[tuple[int, int]]]:
    """'PSA 3:0-8' -> ('psa', [(3,0),(3,1),...,(3,8)]). Single-chapter only."""
    m = REF.match(ref)
    if not m:
        raise SystemExit(f"mapping reference not understood (cross-chapter range?): {ref!r}")
    book, ch, a, b = m.group(1).lower(), int(m.group(2)), int(m.group(3)), m.group(4)
    return book, [(ch, v) for v in range(a, int(b or a) + 1)]


def load_rules(mapping: Path) -> dict[str, dict[tuple[int, int], list[tuple[int, int]]]]:
    """book code -> {(eng_ch, eng_v): [(heb_ch, heb_v), ...]} for canonical books."""
    rules: dict[str, dict] = {}
    for eng, heb in json.loads(mapping.read_text(encoding="utf-8"))["mappedVerses"].items():
        if eng[:3].lower() not in CODE_TO_NAME:
            continue  # apocrypha and other books outside the 66-book spine
        ebook, elist = expand(eng)
        hbook, hlist = expand(heb)
        if ebook != hbook or len(elist) != len(hlist):
            raise SystemExit(f"mapping rule is not one-to-one: {eng} -> {heb}")
        for e, h in zip(elist, hlist):
            rules.setdefault(ebook, {}).setdefault(e, []).append(h)
    return rules


def remap_book(code: str, heb: dict[tuple[int, int], str], shape: dict[int, int],
               rules: dict, notes: list[str]) -> dict[int, dict[int, str]]:
    name = CODE_TO_NAME[code]
    owner: dict[tuple[int, int], tuple[int, int]] = {}   # hebrew ref -> english ref
    gaps: list[tuple[int, int]] = []
    sources: dict[tuple[int, int], list[tuple[int, int]]] = {}
    chapters_with_rules = {c for (c, _v) in rules}

    # English verses to produce: every shape verse, plus verse 0 where a rule names one.
    wanted = [(c, v) for c, n in shape.items() for v in range(1, n + 1)]
    wanted += [e for e in rules if e[1] == 0]
    # Explicit rules claim first, so a same-numbered default can never steal a
    # Hebrew verse a rule assigns elsewhere (Isa 64:1 vs the rule for 64:2).
    wanted.sort(key=lambda e: e not in rules)
    for e in wanted:
        src = rules.get(e) or [e]            # no rule: same number
        if e not in rules and src[0] in owner:
            # The same-numbered Hebrew verse already belongs to another English
            # verse: this English verse is half of a Hebrew verse (Isa 64:1 is
            # the tail of Hebrew 63:19). The Hebrew is not split by guesswork;
            # this token simply has no Hebrew section, and the run says so.
            gaps.append(e)
            notes.append(f"{name} English {e[0]}:{e[1]} has no Hebrew verse of its own "
                         f"(shares Hebrew {owner[src[0]][0]}:{owner[src[0]][1]}); left without a Hebrew rendering")
            continue
        for h in src:
            if h not in heb:
                raise SystemExit(f"{name}: English {e[0]}:{e[1]} needs Hebrew {h[0]}:{h[1]}, which the source lacks")
            if h in owner:
                raise SystemExit(f"{name}: Hebrew {h[0]}:{h[1]} claimed twice ({owner[h]} and {e})")
            owner[h] = e
        sources[e] = list(src)

    # Hebrew verses nobody claimed: attach to the owner of the next Hebrew verse
    # (which may sit in the next chapter: Num 25:19 opens KJV Num 26:1).
    for h in sorted(set(heb) - set(owner)):
        later = [x for x in sorted(owner) if x > h and x in heb]
        if not later:
            raise SystemExit(f"{name}: Hebrew {h[0]}:{h[1]} is unclaimed and has no later verse to join")
        target = owner[later[0]]
        owner[h] = target
        sources[target].append(h)
        notes.append(f"{name} Hebrew {h[0]}:{h[1]} (no mapping rule) folded into English {target[0]}:{target[1]}")

    out: dict[int, dict[int, str]] = {}
    for (c, v), src in sorted(sources.items()):
        text = " ".join(heb[h] for h in sorted(src))
        out.setdefault(c, {})[v] = text
    # Verse 0 (a title counted apart) belongs to verse 1, as in the KJV file.
    for c, verses in out.items():
        if 0 in verses:
            verses[1] = verses.pop(0) + " " + verses[1]
    for c, n in shape.items():
        got = sorted(out.get(c, {}) | {g[1]: "" for g in gaps if g[0] == c})
        if got != list(range(1, n + 1)):
            raise SystemExit(f"{name} {c}: produced verses {got[:3]}..{got[-3:]}, KJV has 1..{n}")
    extra = set(out) - set(shape)
    if extra:
        raise SystemExit(f"{name}: produced chapters {sorted(extra)} the KJV shape does not have")
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--source", required=True, type=Path)
    ap.add_argument("--mapping", required=True, type=Path)
    ap.add_argument("--shape", required=True, type=Path, help="KJV json: the chapter/verse counts to reproduce")
    ap.add_argument("--out", required=True, type=Path)
    args = ap.parse_args()

    src = json.loads(args.source.read_text(encoding="utf-8"))
    shape = json.loads(args.shape.read_text(encoding="utf-8"))
    rules = load_rules(args.mapping)
    shapes = {code_for(b["name"]): {int(c["chapter"]): len(c["verses"]) for c in b["chapters"]}
              for b in shape["books"]}

    notes: list[str] = []
    books = []
    changed = 0
    for b in src["books"]:
        code = code_for(b["name"])
        heb = {(int(c["chapter"]), int(v["verse"])): str(v["text"])
               for c in b["chapters"] for v in c["verses"] if str(v["text"]).strip()}
        out = remap_book(code, heb, shapes[code], rules.get(code, {}), notes)
        if any(len(c["verses"]) != shapes[code].get(int(c["chapter"])) for c in b["chapters"]):
            changed += 1
        books.append({"name": b["name"], "chapters": [
            {"chapter": c, "verses": [{"verse": v, "text": t} for v, t in sorted(vs.items())]}
            for c, vs in sorted(out.items())]})

    # Everything must have been used exactly once.
    n_in = sum(1 for b in src["books"] for c in b["chapters"] for v in c["verses"] if str(v["text"]).strip())
    words_in = sum(len(str(v["text"]).split()) for b in src["books"] for c in b["chapters"] for v in c["verses"])
    words_out = sum(len(v["text"].split()) for b in books for c in b["chapters"] for v in c["verses"])
    if words_in != words_out:
        raise SystemExit(f"word count changed in remap: {words_in} in, {words_out} out")

    args.out.write_text(json.dumps({"translation": src.get("translation", ""), "books": books},
                                   ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    for n in notes:
        print("note:", n)
    print(f"remapped {len(books)} books, {n_in} source verses, {words_in} words intact; "
          f"{changed} books had chapters renumbered -> {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
