---
type: todo
title: Open work
description: "The live work queue for the theology implant — what is decided, unstarted, and waiting."
timestamp: 2026-10-02T07:50:33Z
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

Done 2026-10-01 — see [the archive](archive/2026-10-01.md).


## Phase 4 — The MVP gate (next session, the week of 2026-10-05)

Everything machine-side is ready: the contract is green, the implant is compiled, and the vectors (T2) are fresh and cover the Hebrew and Greek. What remains is Tom's.

- [ ] Tom dogfoods the implant on a real question and reports bugs (suggested first questions: Isaiah 7:14 across `WLC`, `TR`, `WH` and the Finnish; John 1:1 in the Greek sections; the Mary Magdalene page). Calls it lovable, or lists what is not — no translation tokens spent before this
- [ ] Fix what dogfooding finds, then re-run `henxels check --all` and recompile
- [ ] Tom confirms the Westcott–Hort licence (it rests on one README line, see `raw/translations/wh/LICENCE.md`); the WLC mapping table is CC BY-SA 4.0, which this repository judged to attach to the table rather than the Hebrew chapters, and that call is his too

## Phase 5+ — Daily iteration (token work, one batch per cooldown burst)

- [ ] Store the primary sources the [Magdalene page](../knowledge/doctrines/mary-magdalene.md) now quotes at second hand — Gregory's Homily 33, an Orthodox liturgical source (Synaxarion or Prologue), and the Fathers' own passages (Ambrose, Augustine, Chrysostom, Hippolytus) — then replace the second-hand quotations
- [ ] Write the apocryphal Magdalene article (Gospel of Mary, Gospel of Philip, Pistis Sophia) under the spine rule: it links to canon, never the reverse
- [ ] Draft the theologian article template and ingest the first figure across two traditions to prove the neutrality rule holds in practice
- [ ] Doctrine pages, one tradition-comparison at a time, each grounded in the verse tokens it cites
- [ ] Port the Bayesian appraisal tool via the federated common implant, shared with the apologetics and stem implants
- [ ] Establish the shared common implant (brain-implant-common) holding the appraisal tool + its governing convention
