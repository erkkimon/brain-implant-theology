---
type: plan
title: "MVP first, then daily iteration"
description: "The decided plan for both brain implants: a definition of the minimum lovable product for apologetics and theology, the quickest route to it, and the ordered iteration that follows. Born from Tom's 2026-09-25 instruction to get both brains usable before spending tokens on translation."
tags: [plan, mvp, roadmap]
timestamp: 2026-09-26T11:50:00Z
---

# MVP first, then daily iteration

Tom's instruction, in his own framing: the whole project will take days of
local-model time and a real share of subscription tokens, so **the minimum
lovable product must ship first** and be usable *before* translation, and the
improvement work then proceeds in daily bursts bounded by cooldown. This page
is the decided plan; the live checklist lives in [../todo/open.md](../todo/open.md).
If those two disagree, the plan is the *why* and the todo is the *now* — fix
the disagreement, don't act on a stale list.

The decision record is
[journals/2026-09-25.md](../journals/archive/2026/09/2026-09-25.md).

## The principle: content before polish

A brain is lovable when Tom can **query it and get useful answers back**, not
when every page is finished. Semantic search is multilingual once a
multilingual embedding model is in place, so Finnish content is already
useful to an English-speaking user, and an imperfect page with working links
beats an empty folder of perfect intentions. Therefore:

1. Land **algorithmic** work first — conversion, link parsing, spine
   generation. It costs machine time, not tokens, and it makes the brain
   navigable immediately.
2. Then land **mechanical LLM** work in cooldown-sized batches — translation
   and page improvement, one batch per burst.
3. Polish (theology-original pages, appraisal integration) comes last, because
   the brain is already earning its keep by then.

## MVP defined

### Apologetics implant — MVP

*Every ApoWiki article is a searchable Finnish markdown page in `knowledge/`,
with its wiki-links rewritten to brain links that resolve.* Concretely:

- ~470 substantive articles converted from the wikitext exported to
  `_brain/raw/apowiki-export/` in the apologetics implant repository
  (845 of 848 files carry wiki links, 6 798 of them in total — the
  interlinking comes nearly free from parsing, not from an LLM)
- redirects resolved, not imported
- `[[...]]` rewritten to brain links; unresolvable targets kept as visible
  red links so gaps are greppable
- book articles for the `Luokka:Kirjat` corpus, each book bound to an article
  about its biblical book (the shared spine — see below)
- a multilingual embedding model (`bge-m3`) compiled in, so English queries
  find Finnish pages
- contract green, brain compiled, Tom using it

Explicitly **not** in MVP: English translations, template/`<ref>` fidelity,
original theology-flavoured pages.

### Theology implant — MVP

*The spine is whole and the brain is multilingual-searchable.* Concretely:

- KJV chapters (already ingested) hanging on book articles, and book articles
  hanging on testament articles — 66 books, 1 189 chapters, the testament
  roots
- book articles cross-bound to the apologetics implant (`brain://`) so
  a book page reaches the apologetic literature about it
- Finnish spine: PR-1933/38 chapters ingested (1992 is licence-blocked)
- source-language texts ingested (WLC, Textus Receptus, Westcott-Hort) so a
  chapter page carries Hebrew/Greek alongside translations
- `bge-m3` compiled in (this brain already holds English, will hold Finnish,
  Greek and Hebrew)
- contract green, compiled, in use

Explicitly **not** in MVP: theologian articles, doctrine pages beyond what
the spine needs, the Bayesian appraisal tool.

## Shared spine (the cross-brain binding)

The decision: **one article per biblical book, chapters joined to it, each
book bound to a testament article (and to apocrypha where applicable)**.
The apocrypha are *outside* the spine — the canon articles stand as the
structure, apocryphal books are ordinary articles that link *to* a canon
book, never load-bearing rungs. This spine lives in the theology implant and
is a spine in both brains; the apologetics implant mounts it through
brainpick's federation.

Binding between the brains uses the documented form from the
[federation spec](https://github.com/benquemax/brainpick/blob/main/docs/federation.md):
`[[target-path|label]]{brain://brain-id}`. The `brainpick.toml` of each implant
declares the other under `[brains]` with stable ids (`apologetics`, `theology`).

## The ordered path

Machine-time work (no tokens, run it while asleep) then token work
(cooldown-batched). The full decomposition with owners and batch sizes is in
the todo; the milestones are:

1. **Finish the interrupted spine work in theology** — the chapter up-links,
   book articles and testament articles exist on disk; the verse-token henxel
   needs narrowing so book indexes are not judged as chapters, and the ghost
   links measured after the path fixes.
2. **Wikitext→markdown converter for apologetics** — a deterministic tool
   under `skills/tools/`. Heading/bold/italic/link mapping is string work;
   templates and tables are a minority and degrade to visible raw markup
   rather than being silently dropped.
3. **Link resolution pass** — targets resolved through the slug map the
   importer already built (the collision fix that appends `-v2` is part of
   that map); misses become red links, never silent text.
4. **Book spine in apologetics** — generated from the same canonical book
   list theology uses (`skills/tools/bookcodes.py`), one article per book,
   chapters joined upward, each book bound to its apologetics articles and
   across to the theology spine.
5. **Multilingual embeddings in both brains** — `bge-m3` is free and is the
   unlock; without it the English-to-Finnish use case that makes the MVP
   lovable does not exist.
6. **Compile, contract, serve, use.** That is the MVP gate: Tom queries,
   gets answers, and the daily iteration begins.

Then the daily loop, one batch per cooldown burst: translate one themed slice
to English → improve it (fix red links it reveals, ground claims, enrich
links) → commit. Themed slices, not alphabetical runs, so each batch leaves a
coherent sub-domain finished.

## Where this came from

Tom's instruction of 2026-09-25 (MVP first, algorithmic conversion and
interlinking, Finnish first because multilingual semantic search makes it
usable immediately, cooldown-batched translation afterwards, everything on a
visible to-do list), and the decision to found the spine this way recorded in
this brain's journal on 2026-09-25. The 6 798-link figure above was measured
directly from the raw export on 2026-09-25.
