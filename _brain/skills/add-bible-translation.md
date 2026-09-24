---
type: skill
about: procedure
title: Add a Bible translation
description: "How to bring a new scripture translation into this brain: clear its licence first and record the reasoning, store the raw source with a LICENCE.md beside it, then run the deterministic ingest tool that emits one chapter document per chapter with atomic verse tokens — never hand-write a token, and never store text whose redistribution terms you have not read."
tags: [skill, scripture, ingest, licensing, translations]
depends_on: [skills/using-the-brain.md]
tools: [skills/tools/bible_ingest.py, skills/tools/bookcodes.py]
timestamp: 2026-09-24T20:00:00Z
half_life: 0
---

# Add a Bible translation

Grounded in [addressing scripture](../conventions/addressing-scripture.md),
which is why the tokens exist at all, and in the licence decisions recorded in
[the founding journal](../journals/2026-09-24.md).

Use when adding scripture text to `knowledge/scripture/`. The order matters:
**licence first, text second.** A translation whose terms you have not read is
not a candidate, however convenient the file is to obtain.

## 1. Clear the licence before touching the text

Read the actual terms from the source, not a summary of them. Record what you
find in `raw/translations/licence-audit.md` (that folder is excluded from
the compiled bundle, so it is named here rather than linked), including
the ones you *reject* and why — a future contributor will otherwise re-propose
them.

The test is **redistribution in a public git repository**, which is stricter
than personal study use. These fail it:

* **"All rights reserved" or explicit no-redistribution** — for example
  Raamattu 1992, whose terms forbid copying outright. Not negotiable; the
  route is a written licence request to the rights holder.
* **Non-commercial (NC)** clauses — this repository is public and places no
  restriction on who reuses it, which an NC term contradicts.
* **No-derivatives (ND)** clauses — splitting a text into chapter documents
  and adding verse tokens *is* a derivative work.
* **"Distribute freely without changes"** — same problem: we restructure.
* **A claimed electronic edition** of an old text. The 1917 JPS Tanakh is
  public domain by age, but a particular digitisation may carry its own claim.

What passes: public domain by age (life of author plus seventy years), or a
permissive licence with no NC/ND restriction. Where the text is PD but the
*database* is licensed — a common and fine arrangement — record both, as
`raw/translations/kjv/LICENCE.md` does.

When the terms are ambiguous, **ask rather than assume**. A wrong call here is
a licensing failure in public, not a bug that can be quietly patched.

## 2. Store the raw source with its licence beside it

```
_brain/raw/translations/<name>/
    <name>.json      the source as obtained, unmodified
    LICENCE.md       terms, provenance, retrieval date, a verification quote
```

The contract enforces the `LICENCE.md`: a translation folder without one
blocks the commit. That is deliberate — it makes "I'll document it later"
impossible.

`LICENCE.md` keeps its conventional uppercase spelling and is exempt from the
kebab-case rule, because a licence nobody spots is a licence nobody honours.

## 3. Run the ingest tool

```bash
python3 _brain/skills/tools/bible_ingest.py \
    --source _brain/raw/translations/kjv/kjv.json \
    --name "King James Version" --abbrev KJV \
    --out _brain/knowledge/scripture
```

It expects `{translation, books:[{name, chapters:[{chapter, verses:[{verse,
text}]}]}]}`. A source in another shape gets a small adapter script, not a
hand-edited output.

What it produces, per chapter:

* `<book><NNN>.md` — for example `jhn014.md` for John 14.
* Frontmatter carrying `book`, `chapter`, `translations`, and `verses:` — the
  full list of atomic tokens.
* One heading per verse: `### John 14:6 \`jhn14v6\`` — the human reference a
  person reads, and the token the search engine needs, together.

It is **idempotent**: re-running produces byte-identical files, so a re-ingest
diffs empty. If it reports every chapter rewritten on a second run, something
is wrong — investigate rather than commit the churn.

## 4. Adding a second translation to existing chapters

Run the tool again with a different `--abbrev`. Translations are **clustered
on the chapter**: the new rendering is merged into the existing file as its
own `## <ABBREV> — <ref>` section, `translations:` is updated, and `verses:`
becomes the union of tokens. Existing sections are left untouched.

This is why reading one chapter shows how the translations differ, instead of
requiring a reader to know which parallel tree to open.

## 5. Verify before committing

```bash
henxels check --all          # the verse-token check runs on every chapter
brainpick compile --root .   # expect ~1,189 new docs for a full canon
```

The contract rejects a malformed token with a message naming the file. Trust
it: a wrong token is invisible in ordinary reading, which is exactly why the
check exists.

Note that compiling a full translation embeds over a thousand documents and
takes minutes, not seconds. Run it as a background job rather than assuming it
has hung.

## Never

* **Never hand-write a verse token.** Generating them is this tool's entire
  job. A hand-typed token that is subtly wrong points nowhere and fails
  silently.
* **Never store text you have not cleared.** Cite it by reference instead —
  quoting a verse in an article is ordinary right of quotation; storing the
  full text is redistribution.
* **Never edit `knowledge/scripture/` by hand.** The files are generated. Fix
  the source or the tool, then re-run.
