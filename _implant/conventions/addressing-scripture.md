---
type: convention
about: concept
title: Addressing scripture
description: "A verse is addressed by an atomic reference token — jhn14v6 — carried in the chapter document's frontmatter and in the verse's own heading, because brainpick's BM25 tokenizer splits John 14:6 into john/14/6 and cannot then tell it apart from John 6:14; the token is the retrieval key that makes finding content by verse work at all, and it is written by the ingest tool, never by hand."
tags: [convention, scripture, retrieval, addressing, bible, search]
timestamp: 2026-09-27T10:30:00Z
half_life: 0
---

# Addressing scripture

The ordinary question an agent gets is *"what do the traditions say about
John 14:6?"* — finding content **by verse**, not finding a verse by content.
That direction is the one a naive setup fails at, and it fails silently.

## Why the obvious form does not work

brainpick's keyword retrieval is BM25 over a Unicode word tokenizer,
`[^\W_]+` ([keyword.py, spec/50](https://github.com/benquemax/brainpick/blob/main/packages/python/src/brainpick/query/keyword.py)).
Punctuation is a separator, so a human-readable reference shatters:

| Written | Indexed as |
| --- | --- |
| `John 14:6` | `john`, `14`, `6` |
| `John 6:14` | `john`, `6`, `14` |
| `Joh. 14:6` | `joh`, `14`, `6` |
| `Room. 8:28` | `room`, `8`, `28` |

The first two produce **the same set of terms**. BM25 has no notion of word
order, so `John 14:6` and `John 6:14` are not merely similar, they are
*indistinguishable*. Worse, a chapter document naturally contains the verse
numbers 1..n, so every bare digit is a high-frequency term inside it: a query
for any verse matches every chapter of that book roughly equally, and
`Room. 8:28` collides with the English word "room".

This is a formatting problem, and it is fixable entirely at ingest time. It
is not a reason to write a custom search tool.

## The rule

Every verse carries an **atomic reference token**: lowercase, alphanumeric,
no punctuation, so the tokenizer cannot split it.

```
<book><chapter>v<verse>          jhn14v6      rom8v28      1co13v4
```

Book codes are the standard three-letter OSIS-style abbreviations (`gen`,
`jhn`, `rom`, `rev`); a numbered book keeps its digit prefix (`1co`, `2ti`).
A verse range is written as its own token (`jhn14v6to7`), and the individual
verse tokens are also present so a single-verse query still lands.

These tokens do not collide, and the tokenizer's 4-character prefix stem
gives useful chapter-level recall for free:

| Token | Indexed as |
| --- | --- |
| `jhn14v6` | `jhn14v6`, `jhn1` |
| `jhn6v14` | `jhn6v14`, `jhn6` |

Distinct at verse level; `jhn1` gathers the John 1x chapters for a broader
query. That is the behaviour we want from both directions.

## Where the token goes

Three places, all written by the ingest tool:

1. **Chapter frontmatter** — a `verses` field listing every token in the
   chapter, so the whole chapter is reachable by any verse in it.
2. **The verse heading** — each verse is a heading carrying its token, which
   makes it addressable through `brain_read`'s `sections` parameter. brainpick
   returns a document's heading outline and will fetch only the named
   sections, so an agent can read John 14:6 without pulling all of John 14.
3. **Any article that argues from the verse** — a theologian's page cites
   `jhn14v6` in the same line as the human-readable `John 14:6`. This is what
   makes the reverse link work: searching the token finds the chapter *and*
   everyone who argued from it.

The human-readable reference is always written next to the token. The token
is machinery; `John 14:6` is what a person reads. Never show the token alone.

## What this buys, concretely

An agent asked about interpretations of John 14:6 runs one search for
`jhn14v6` and gets: the chapter document containing the verse, and every
theologian, doctrine and tradition page that cites it — ranked together,
because they all carry the same unambiguous term. No special tool, no
verse-lookup index, no custom retrieval path. The convention *is* the
mechanism.

## Consequences for ingest

Because the tokens are mechanical, they are generated, never typed. A
contributor writing an article writes `John 14:6` and the tooling adds the
token; an ingest run that produces a chapter emits the frontmatter list and
the headings. A hand-written token is a bug waiting to happen — a wrong one
is invisible, which is exactly the failure this convention exists to prevent.

Grounded in the tokenizer's actual behaviour, measured against brainpick 0.7.0
on 2026-09-24 ([journal](../journals/archive/2026/09/2026-09-24.md)), and serving the structure
set out in [the theology implant](../vision/the-theology-implant.md), where
scripture is the spine the rest of the implant attaches to.
