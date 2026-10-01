# Westminster Leningrad Codex (Biblia Hebraica) — licence

**Status: public domain text. Free to redistribute.**

## The text

The Hebrew Bible as preserved in the Leningrad Codex (written 1008/9 CE), in
the Westminster Leningrad Codex electronic edition. The manuscript is a
thousand years old. The Open Scriptures Hebrew Bible project, which maintains
the edition, states that "the text of the WLC remains in the Public Domain"
and licenses only its own lemma and morphology data (CC BY 4.0), which this
implant does not use (https://github.com/openscriptures/morphhb).
raamattu.uskonkirjat.net lists it as *vapaassa käytössä*, in free use
(`../licence-audit.md`). Vowel points and cantillation marks are kept; no
Unicode normalisation is applied, as the OSHB manual advises.

## This digital edition

Obtained from `scrollmapper/bible_databases`
(https://github.com/scrollmapper/bible_databases), `formats/json/WLC.json`,
labelled "WLC: Westminster Leningrad Codex", under the compilation's **MIT
Licence**. Retrieved 2026-10-01 and stored unmodified as `wlc.json`: 39 books,
929 chapters, in **Hebrew versification**.

## The versification map

`versification-eng.json` is the standard `eng` mapping of the Copenhagen
Alliance versification specification
(https://github.com/Copenhagen-Alliance/versification-specification,
`versification-mappings/standard-mappings/eng.json`, from the Paratext
standard mappings by Reinier de Blois and Neil Rees), retrieved 2026-10-01
and stored unmodified. Its data is licensed **CC BY-SA 4.0**; this is the
attribution. It is a table of verse numbers, used only to decide which Hebrew
verse sits under which KJV-numbered token. The Hebrew text itself is not
derived from it, so the ShareAlike term attaches to the table and not to the
chapters. That is a judgement, recorded so it can be revisited.

## How it enters the chapters

`skills/tools/versification_remap.py` re-numbers `wlc.json` into the KJV
numbering the verse tokens use, then `bible_ingest.py` writes the `WLC`
sections. The remap refuses to finish unless every Hebrew verse is used once
and the chapter and verse counts match the KJV file. Where the Hebrew has no
verse of its own for an English token (Isa 64:1, Ps 13:6, Neh 7:68, each half
of a Hebrew verse), that token has no Hebrew rendering instead of a guessed
split. Where a Hebrew verse is unclaimed by the map, it is joined to the next
verse's token.

## Verification

`Genesis 1:1` in this edition reads:

> בְּרֵאשִׁ֖ית בָּרָ֣א אֱלֹהִ֑ים אֵ֥ת הַשָּׁמַ֖יִם וְאֵ֥ת הָאָֽרֶץ׃

and `Joel 3:1` (Hebrew 4:1) reads "For, behold, in those days…" in the KJV
and begins כִּי הִנֵּה בַּיָּמִים הָהֵמָּה in the Hebrew, as the map requires.
