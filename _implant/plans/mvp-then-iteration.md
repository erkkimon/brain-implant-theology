---
type: plan
title: "MVP first, then daily iteration"
description: "The decided plan for both brain implants: a definition of the minimum lovable product for apologetics and theology, the quickest route to it, and the ordered iteration that follows. Born from Tom's 2026-09-25 instruction to get both brains usable before spending tokens on translation."
tags: [plan, mvp, roadmap]
timestamp: 2026-10-01T19:10:17Z
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

An implant is lovable when Tom can **query it and get useful answers back**, not
when every page is finished. Semantic search is multilingual once a
multilingual embedding model is in place, so Finnish content is already
useful to an English-speaking user, and an imperfect page with working links
beats an empty folder of perfect intentions. Therefore:

1. Land **algorithmic** work first — conversion, link parsing, spine
   generation. It costs machine time, not tokens, and it makes the implant
   navigable immediately.
2. Then land **mechanical LLM** work in cooldown-sized batches — translation
   and page improvement, one batch per burst.
3. Polish (theology-original pages, appraisal integration) comes last, because
   the implant is already earning its keep by then.

## MVP defined

### Apologetics implant — MVP

*Every ApoWiki article is a searchable Finnish markdown page in `knowledge/`,
with its wiki-links rewritten to implant links that resolve.* Concretely:

- ~470 substantive articles converted from the wikitext exported to
  `_implant/raw/apowiki-export/` in the apologetics implant repository
  (845 of 848 files carry wiki links, 6 798 of them in total — the
  interlinking comes nearly free from parsing, not from an LLM)
- redirects resolved, not imported
- `[[...]]` rewritten to implant links; unresolvable targets kept as visible
  red links so gaps are greppable
- book articles for the `Luokka:Kirjat` corpus, each book bound to an article
  about its biblical book (the shared spine — see below)
- a multilingual embedding model (`bge-m3`) compiled in, so English queries
  find Finnish pages
- contract green, implant compiled, Tom using it

Explicitly **not** in MVP: English translations, template/`<ref>` fidelity,
original theology-flavoured pages.

### Theology implant — MVP

*The spine is whole and the implant is multilingual-searchable.* Concretely:

- KJV chapters (already ingested) hanging on book articles, and book articles
  hanging on testament articles — 66 books, 1 189 chapters, the testament
  roots
- book articles cross-bound to the apologetics implant (`brain://`) so
  a book page reaches the apologetic literature about it
- Finnish spine: PR-1933/38 chapters ingested (1992 is licence-blocked) — done 2026-09-27
- source-language texts ingested (WLC, Textus Receptus, Westcott-Hort) so a
  chapter page carries Hebrew/Greek alongside translations
- `bge-m3` compiled in (this implant already holds English, will hold Finnish,
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
is a spine in both implants; the apologetics implant mounts it through
brainpick's federation.

Binding between the implants is an **autolink**,
`<brain://<alias>-<bundle id>/<path>>`, as described in the
[federation spec](https://github.com/benquemax/brainpick/blob/main/docs/federation.md).
A markdown link to `brain://` would be reported dead by the contract's link
check, so the autolink form is required. The bundle id is the 21-character id
in each repository's `brainpick.toml`: theology `kay4zyljsuy909krumpau`,
apologetics `3hm51e1pxik7zz5la3bve`. brainpick matches exactly 21 characters,
so a longer id never resolves
([journal](../journals/archive/2026/09/2026-09-26.md)). The implants find each
other through the machine's brainpick registry
(`brainpick register <repo>/_implant --implant --alias <name>`), not through
anything committed here.

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
5. **Multilingual embeddings in both implants** — `bge-m3` is free and is the
   unlock; without it the English-to-Finnish use case that makes the MVP
   lovable does not exist.
6. **Compile, contract, serve, use.** That is the MVP gate: Tom queries,
   gets answers, and the daily iteration begins.

Then the daily loop, one batch per cooldown burst: translate one themed slice
to English → improve it (fix red links it reveals, ground claims, enrich
links) → commit. Themed slices, not alphabetical runs, so each batch leaves a
coherent sub-domain finished.

## Status and how to resume

Read this first when coming back after a break. The live checklist is
[../todo/open.md](../todo/open.md), and the latest journal says what happened
last.

- **Done (2026-09-26):** Phase 1, the spine. There are 66 book pages and 2
  testament pages, and all 1 189 KJV chapters hang on them. Each book page
  has a `## In the apologetics implant` autolink to its Finnish rung. `bge-m3`
  vectors are built, and semantic search finds passages by meaning.
- **Done (2026-09-27):** the bundle root is `_implant/` (formerly `_brain/`).
  This repository is an implant; the cortex is the agent's own brain
  ([journal](../journals/archive/2026/09/2026-09-27.md)).
- **Done (2026-09-27):** the live annotation check passed. `brain_read` on a
  theology book page lists the apologetics rung, and the reverse works too.
  Raamattu 1933/38 (`PR1938`, 1 189 chapters) and the Textus Receptus
  (`TR`, 260 NT chapters) now sit beside the KJV in every chapter file.
- **Done (2026-10-01):** the Hebrew text. WLC (929 chapters) is the `WLC`
  section of every Old Testament chapter, re-numbered to the KJV tokens
  through the standard `eng` versification map
  ([journal](../journals/archive/2026/10/2026-10-01.md)).
- **Done (2026-10-01):** Westcott–Hort (`WH`, 260 NT chapters), from
  Robinson's public-domain electronic text, converted by
  `skills/tools/wh_convert.py`. All planned source-language texts are in.
- **Then:** the Phase 4 gate. Tom uses both implants on a real question.
  No translation tokens are spent before he calls it lovable.

To resume on any machine:

1. `git pull --ff-only`, then `brainpick compile --root .` from the repository
   root. Vectors (T2) are machine-local and take a while; run
   `brainpick compile --root . --only t2` in the background, and check it with
   `brainpick doctor --root .`. Embeddings need a `bge-m3` endpoint in the
   gitignored `brainpick.local.toml`.
2. Register both implants if they are not registered yet:
   `brainpick register <repo>/_implant --implant --alias theology` (and
   `apologetics`).
3. Work down `todo/open.md` in phase order. Journal in today's file, archive
   yesterday's, and commit and push each finished step.

## Where this came from

Tom's instruction of 2026-09-25 (MVP first, algorithmic conversion and
interlinking, Finnish first because multilingual semantic search makes it
usable immediately, cooldown-batched translation afterwards, everything on a
visible to-do list), and the decision to found the spine this way recorded in
this implant's journal on 2026-09-25. The 6 798-link figure above was measured
directly from the raw export on 2026-09-25.
