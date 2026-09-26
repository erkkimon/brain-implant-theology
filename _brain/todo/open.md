---
type: todo
title: Open work
description: "The live work queue for the theology implant — what is decided, unstarted, and waiting."
timestamp: 2026-09-26T11:55:00Z
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
- [ ] Verify through a live `brain_read` that a theology book page shows the apologetics rung as an annotation — the links land by id (136/136 checked by script), but serving the full set compiles every registered brain first

## Phase 3 — Fill the spine with texts (machine time)

- [ ] Ingest Raamattu 1933/38 as the Finnish spine — Raamattu 1992 is licence-blocked and may only be cited by reference
- [ ] Ingest the source-language texts: Biblia Hebraica (WLC), Textus Receptus, Westcott-Hort — so a chapter page carries Hebrew or Greek alongside its translations
- [ ] Build the T2 vectors with `bge-m3` (already pulled and set in `brainpick.local.toml` on the apologetics side) — the detected `nomic-embed-text` is English-only; on a CPU-only backend the build takes hours, so run it as a background job

## Phase 4 — The MVP gate

- [ ] `henxels check --all` green, brain compiled, served with `brainpick init`
- [ ] Tom uses it for a real question and calls it lovable — no translation tokens spent before this

## Phase 5+ — Daily iteration (token work, one batch per cooldown burst)

- [ ] Draft the theologian article template and ingest the first figure across two traditions to prove the neutrality rule holds in practice
- [ ] Doctrine pages, one tradition-comparison at a time, each grounded in the verse tokens it cites
- [ ] Port the Bayesian appraisal tool via the federated common brain, shared with the apologetics and stem implants
- [ ] Establish the shared common brain (brain-implant-common) holding the appraisal tool + its governing convention
