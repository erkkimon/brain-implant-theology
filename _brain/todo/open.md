---
type: todo
title: Open work
description: "The live work queue for the theology implant — what is decided, unstarted, and waiting."
timestamp: 2026-09-24T19:00:00Z
---

# Open

- [ ] Audit `raamattu.uskonkirjat.net` for available translations and their
      licences; record which may be redistributed and which are citation-only
- [ ] Write `skills/add-bible-translation.md` and its ingest tool, emitting
      chapter documents with atomic verse tokens per the addressing convention
- [ ] Ingest a public-domain translation end to end as the reference
      implementation (KJV is the safest first target)
- [ ] Port the Bayesian appraisal tool via the federated common brain, shared
      with the apologetics and stem implants
- [ ] Pull a multilingual embedding model (`ollama pull bge-m3`) and rerun
      `brainpick init` — the detected `nomic-embed-text` is English-only, and
      this brain will hold Finnish, Greek and Hebrew text
- [ ] Draft the theologian article template and ingest the first figure across
      two traditions to prove the neutrality rule holds in practice
