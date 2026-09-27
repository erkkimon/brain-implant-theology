---
type: todo
title: Open work
description: "The live work queue for the theology implant — what is decided, unstarted, and waiting."
timestamp: 2026-09-27T14:00:00Z
---

# Open

Plan behind this list: [../plans/mvp-then-iteration.md](../plans/mvp-then-iteration.md).
Phases 1–3 are machine time. Phase 4 is the MVP gate; nothing that burns
translation tokens starts before it. The apologetics implant holds the mirror
of this structure for its own half.

## Phase 1 — Finish the interrupted spine work (machine time)

Done 2026-09-26 — see [the archive](archive/2026-09-26.md).

## Phase 2 — Bind the spine to apologetics (machine time)

- [ ] Keep apocrypha outside the spine: ordinary articles that link to canon, never a rung of it (standing rule; closes when the first apocryphal article lands and obeys it)

## Phase 3 — Fill the spine with texts (machine time)

- [ ] Ingest Biblia Hebraica (WLC) through a versification map: WLC numbers verses the Hebrew way, and 138 of its 929 chapters differ in verse count from the KJV numbering the tokens use (Gen 31–32, Exod 7–8, Mal 3–4 …). A naive ingest would put the wrong Hebrew under a token. Source: `scrollmapper/bible_databases` `formats/json/WLC.json` (MIT compilation, public-domain text)
- [ ] Ingest Westcott–Hort (not in `scrollmapper/bible_databases`; find a cleared source first)

## Phase 4 — The MVP gate

- [ ] `henxels check --all` green, implant compiled, served with `brainpick init`
- [ ] Tom uses it for a real question and calls it lovable — no translation tokens spent before this

## Phase 5+ — Daily iteration (token work, one batch per cooldown burst)

- [ ] Draft the theologian article template and ingest the first figure across two traditions to prove the neutrality rule holds in practice
- [ ] Doctrine pages, one tradition-comparison at a time, each grounded in the verse tokens it cites
- [ ] Port the Bayesian appraisal tool via the federated common implant, shared with the apologetics and stem implants
- [ ] Establish the shared common implant (brain-implant-common) holding the appraisal tool + its governing convention
