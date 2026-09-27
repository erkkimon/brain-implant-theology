# brain-implant-theology

A **brainpick brain implant**: a knowledge repository written to be read by AI
agents, not just by people. The material here is plain markdown in a git
repository — you can read it with any text editor — but it is also a compiled
knowledge graph with semantic search, typed memory, dependency-linked skills,
and grounding links on every claim. An agent with brainpick attached navigates
this the way a person navigates a reference library they already know by
heart: overview first, then search, then read, then follow the links out.

**Scope: theology.** Articles about subjects that help Christians defend their
Christian views against *other Christian views*. Articles defending the faith
against non-Christian views are apologetics and belong to the sibling implant,
`brain-implant-apologetics`. The boundary is who the opponent is: inside the
faith here, outside the faith there.

**Neutral point of view.** Nothing here asserts that a contested theological
claim is true. It asserts that a named theologian, council or tradition *said*
something — and that is what gets proven, with a citation to the text. Which
of them is right is left to the reader. This is what lets Orthodox, Catholic,
Lutheran, Reformed, Pentecostal, Adventist and Episcopal positions sit in one
repository without it becoming an argument: each is reported, none is
endorsed.

---

## Using this with an agent

### If brainpick is already installed

```bash
git clone <this-repo> && cd brain-implant-theology
brainpick compile --root .          # --root is where brainpick.toml lives
brainpick overview --root .         # start here
```

Then `brainpick search`, `brainpick read`, `brainpick neighbors`. To wire it
into an agent harness as an MCP server:

```bash
brainpick register "$PWD/_implant"    # register once, then harnesses see it
brainpick integrate                 # writes harness config (Claude Code, opencode, …)
```

Or serve the web UI, which renders the graph:

```bash
brainpick serve --root . --open
```

### If brainpick is not installed

brainpick is a Python CLI published on PyPI. Any of these work; `uv` is the
lightest because it needs no virtualenv of your own:

```bash
uv tool install brainpick           # recommended
# or:
pipx install brainpick
# or:
pip install --user brainpick
```

If the `brainpick` command is not found afterwards, it is almost certainly in
`~/.local/bin` — add that to your `PATH`.

You can also run it without installing anything:

```bash
uvx brainpick overview --root .
```

Source, issues and full documentation: <https://github.com/benquemax/brainpick>

### Minimum version

**brainpick >= 0.7.0 is required.** Check with `brainpick --version`.

This is not arbitrary. This brain uses **brain format 3**, introduced in
0.7.0, which made `type: convention` a memory type the engine actually
recognises — compiled into `conventions.json`, listed first in the overview
and in the generated `AGENTS.md` report. On an older brainpick the conventions
in this repository are not *broken*, they are **invisible**: the engine will
not surface them, so an agent reads the material without ever seeing the rules
that govern how it is written and what it may claim. For a repository whose
central rule is "report what was said, never endorse it", that is exactly the
rule you cannot afford to lose silently.

For context on the versions below the floor: federation and implants
(`brainpick register`, one cortex plus implants) arrived in 0.5.0, and
`--root` pointing at a repo root above the bundle arrived in 0.4.5. Neither is
sufficient on its own — 0.7.0 is the floor for this repository.

**Install the `[vectors]` extra**, not plain `brainpick`. Without it the
vector tier is silently off and search degrades to keyword only — no warning
at install time, just worse results:

```bash
uv tool install "brainpick[vectors]"
```

**Use 0.8.1 or later if you will run `brainpick serve`.** Earlier versions
applied `[bundle] root` twice and served a path that does not exist, so the
web UI showed a single generated index and nothing else. 0.7.0 remains the
floor for reading this implant; 0.8.1 is the floor for serving it.

The latest release is otherwise recommended but not required.

---

## How this repository is organised

`_implant/` is the bundle. Its folders are memory types, one job each:

| Folder | Holds |
| --- | --- |
| `knowledge/` | Scripture, theologians, doctrines, councils, traditions |
| `skills/` | Procedures an agent follows, with the tools they drive |
| `conventions/` | Standing rules: scope, neutrality, citation, publication |
| `journals/` | What happened, one file per day |
| `vision/` | Where this implant is going, as a book |
| `plans/` | Decided work |
| `todo/` | The live work queue |
| `raw/` | Undistilled source material, excluded from search results |

Read `conventions/` first — a rule constrains what every other read is for —
then `skills/`, then `knowledge/`.

### Scripture

The Bible is the spine of this implant, held at **chapter granularity**: one
document per chapter, with verse anchors inside it. Verse-level documents
would shatter the graph into tens of thousands of fragments too small to carry
meaning; book-level documents would be too coarse to link a commentary to.
A chapter is the unit a theologian actually argues about.

Translations are **clustered on the chapter**, not siloed into parallel trees:
one chapter document carries its renderings across translations, so an agent
reading a passage sees how it differs between them rather than having to know
in advance which translation to open. Finnish translations and the
best-known English ones are the starting set, alongside the source-language
texts and the historically significant editions where they are free to
redistribute. Apocryphal and deuterocanonical books are included wherever a
translation in the set contains them — which books belong in the canon is
itself a theological dispute this repository reports rather than settles.

**Translation licensing is checked before ingest, not after.** Many modern
translations are under active copyright and cannot be redistributed here; the
public-domain and freely-licensed ones can. Every translation in the set
records its licence, and the ingest skill refuses one that has not been
cleared. A translation we cannot redistribute may still be *cited* by
reference without reproducing its text.

### Theologians and traditions

Articles about the significant figures of church history across sects, with
their central positions linked to the specific chapters and verses they rest
on. The link runs both ways: from a chapter you can reach everyone who argued
from it, and from a theologian you can reach the text they stood on.
Ecumenical concepts — where traditions converge, and the precise point at
which they part — are first-class material, not an afterthought.

## Contract

This repository is governed by a [henxels](https://pypi.org/project/henxels/)
contract — machine-checked rules in `henxels.yaml`, digested for agents into
`AGENTS.md`. It runs on commit. Install it before contributing:

```bash
uv tool install henxels && henxels init
henxels check --all
```

## Contributing

Contributions arrive as pull requests, including from agents. A contribution
that adds a claim adds its citation in the same change; a contribution that
adds a translation records its licence. The contract checks what it can check
mechanically, and a human reviews the rest.

## How the content is produced — and a disclaimer

All information in this repository is **distilled by AI agents** from the
cited sources, under the contract above, and reviewed by humans only to the
extent the maintainers and contributors have had time for. The contract
checks what can be checked mechanically — that links land, that citations are
present, that no contested theological claim is asserted in the implant's own
voice — but it cannot check that a source was read correctly or that a
quotation is accurate. Errors of transcription, attribution and interpretation
are therefore possible on any page, and every receipt is there precisely so
that you can verify the claim yourself before relying on it. Scripture texts
are ingested from their stated editions; the ingest is mechanical, but a
transcription error is still possible, so check the cited edition before
quoting a verse from here.

The content is provided **as is**, without warranty of any kind, express or
implied. Nothing here is professional, pastoral or legal advice, and nothing
here is a statement of the maintainers' own views: the implant reports what
named theologians, councils and traditions have said, and any error in such a
report is an error of the implant, not a claim of the source. If you find one,
open an issue or a pull request.

## Licensing

Tooling and conventions authored here are **MIT**. Scripture texts and quoted
works each carry their own licence, recorded with the text; public-domain
editions are marked as such. See `LICENSE` once the bundle is scaffolded.
