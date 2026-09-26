---
type: todo
title: Open work
description: "The live work queue for the theology implant — what is decided, unstarted, and waiting."
timestamp: 2026-09-25T00:00:00Z
---

# Open

Plan behind this list: [../plans/mvp-then-iteration.md](../plans/mvp-then-iteration.md).
Phases 1–3 are machine time. Phase 4 is the MVP gate; nothing that burns
translation tokens starts before it. The apologetics implant holds the mirror
of this structure for its own half.

## Phase 1 — Finish the interrupted spine work (machine time)

- [ ] Narrow the verse-token henxel so it applies to chapter files only — it fires today on the book indexes in `knowledge/scripture/<code>/`, which carry no verse tokens by design
- [ ] Re-measure ghosts after the link-path fixes and drive them to zero (`brainpick compile`, then read `t1/graph.json`)
- [ ] Verify traversal both ways: a book article reaches every chapter, and a chapter reaches its book and its testament

## Phase 2 — Bind the spine to apologetics (machine time)

- [ ] Declare the apologetics implant under `[brains]` in `brainpick.toml` with a stable id
- [ ] From each book article, link across the federation boundary (the `{brain://apologetics}` suffix form) to the apologetic literature about that book
- [ ] Keep apocrypha outside the spine: ordinary articles that link to canon, never a rung of it

## Phase 3 — Fill the spine with texts (machine time)

- [ ] Ingest Raamattu 1933/38 as the Finnish spine — Raamattu 1992 is licence-blocked and may only be cited by reference
- [ ] Ingest the source-language texts: Biblia Hebraica (WLC), Textus Receptus, Westcott-Hort — so a chapter page carries Hebrew or Greek alongside its translations
- [ ] Pull a multilingual embedding model (`ollama pull bge-m3`) and rerun `brainpick init` — the detected `nomic-embed-text` is English-only, and this brain will hold English, Finnish, Greek and Hebrew text

## Phase 4 — The MVP gate

- [ ] `henxels check --all` green, brain compiled, served with `brainpick init`
- [ ] Tom uses it for a real question and calls it lovable — no translation tokens spent before this

## Phase 5+ — Daily iteration (token work, one batch per cooldown burst)

- [ ] Draft the theologian article template and ingest the first figure across two traditions to prove the neutrality rule holds in practice
- [ ] Doctrine pages, one tradition-comparison at a time, each grounded in the verse tokens it cites
- [ ] Port the Bayesian appraisal tool via the federated common brain, shared with the apologetics and stem implants
- [ ] Establish the shared common brain (brain-implant-common) holding the appraisal tool + its governing convention
