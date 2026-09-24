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
