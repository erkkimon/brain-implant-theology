# Scripture

The Bible at **chapter granularity**: one document per chapter, verses
addressable individually. A chapter is the unit theologians actually argue
about — verse-level documents would shatter the graph into fragments too small
to carry meaning, and book-level ones would be too coarse to link a commentary
to.

Translations are **clustered on the chapter**, not split into parallel trees,
so reading a passage shows how the renderings differ without having to know in
advance which translation to open.

Every chapter declares its verses as atomic reference tokens in frontmatter —
`verses: [jhn14v1, jhn14v2, …]` — because the search tokenizer splits
`John 14:6` into `john`/`14`/`6` and cannot then distinguish it from
`John 6:14`. The tokens are what makes finding content *by verse* work at all.
See `../../conventions/addressing-scripture.md`; they are written by the
ingest tooling, never by hand.

## Status: no scripture ingested yet

This folder holds **no chapters at the moment** — only this index. The
structure and the addressing scheme are settled; the text is not in, and that
is deliberate rather than an oversight.

Two things gate the first ingest, in order:

1. **Licence clearance.** Which translations may be redistributed at all, and
   which may only be cited by reference. The contract enforces this
   mechanically: a translation folder without a `LICENCE.md` blocks the
   commit. Public-domain editions (KJV, Textus Receptus, the Septuagint,
   the Masoretic text) are the safe first targets; modern Finnish and English
   translations are where copyright usually bites.
2. **The ingest tool.** A deterministic script that turns a source text into
   chapter documents carrying verse tokens in frontmatter and verse headings.
   It is written once and generates everything, because hand-written tokens
   are a bug waiting to happen — a wrong one fails silently.

Ingesting a public-domain translation end to end is the reference
implementation that proves the shape before it is applied at scale. Roughly
1,189 chapters per translation, so getting the shape right first matters more
than starting early. Tracked in `../../todo/open.md`.
