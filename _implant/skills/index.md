# Skills

Procedural memory: procedures an agent follows, with the deterministic tools
they drive. Read the matching skill before improvising.

## Skills

* [Add a Bible translation](add-bible-translation.md) — clear the licence,
  store the source with its terms, then run the deterministic ingest tool.

## Tools

* `tools/bible_ingest.py` — turn a translation into chapter documents with
  atomic verse tokens. Idempotent; clusters translations on the chapter.
* `tools/bookcodes.py` — the canonical book codes the tokens are built from.
  These are permanent: changing one invalidates every token already written.
