# Westcott–Hort Greek New Testament (1881) — licence

**Status: public domain. Free to redistribute.**

## The text

*The New Testament in the Original Greek* by Brooke Foss Westcott and Fenton
John Anthony Hort was published in 1881. Both editors died in 1892 and 1896,
so the edition is far beyond any term based on the life of the author plus
seventy years.

## This digital edition

Maurice A. Robinson's electronic Westcott–Hort text, maintained by Ulrik
Sandborg-Petersen at https://github.com/byztxt/greektext-westcott-hort. Its
README (stored beside the source as `source/readme.md`) states, under
*License?*: "Public Domain. Copy freely." Only the `textonly/*.WH` files are
used, not the parsed files with Strong's numbers and morphology. Retrieved
2026-10-01 at commit `91473892d7f36f1227e5c24f8d994d1da40311ad` (2017-05-23)
and stored in `source/` with the contents unmodified and the names made lower-case with a `.txt` extension (`MT.WH` is `mt.txt`), as the raw-folder rules require: 27 books, in a Latin-letter transliteration.

The licence rests on that one README line, not on a separate licence file. It
is a dedication by the electronic edition's author, consistent with the age of
the underlying text. That is recorded here so a later contributor can judge
whether it is enough.

## Rejected alternatives

* CrossWire SWORD module `WHNU` (CC BY-NC-SA 4.0): the NC term fails this
  repository's redistribution test.
* The CCEL copy (`ccel.org/ccel/bible/gntwh`): derived from the Unbound Bible
  data with no clear licence statement, and its text was garbled where
  sampled.

## How it enters the chapters

`skills/tools/wh_convert.py` transliterates the source to unaccented
lower-case Greek, like the `TR` section; the result is ingested by
`bible_ingest.py` as the `WH` section of the 260 New Testament chapters. The
converter stops on any character it has no mapping for and on any verse the
KJV numbering lacks. Reported, not hidden:

* **17 verses are empty** in the source because Westcott–Hort omits them
  (Matt 12:47, 17:21, 18:11, 23:14; Mark 7:16, 9:44, 9:46, 11:26, 15:28;
  Luke 17:36, 23:17; John 5:4; Acts 8:37, 15:34, 24:7, 28:29; Rom 16:24).
  Their tokens have no `WH` section.
* 3 John 1:15 is folded into 1:14 (the tokens follow KJV numbering).
* `[c:v]` versification markers inside the text are stripped (14 places);
  `[word]` brackets, W-H's doubtful readings, are kept.
* `[[ ... ]]`, W-H's double brackets for passages the editors judge later
  additions (Luke 22:19b–20 and 22:43–44, John 7:53–8:11 and others, 15 in
  all), are written `⟦ ... ⟧` in the chapters, because markdown reads `[[x]]`
  as a wiki-link. They stay distinct from the single `[doubtful]` brackets.
* Mark 1:45 carries Robinson's alternative-reading marker
  (`| alla | all |`); the reading `all` is kept.

## Verification

John 14:6 begins, in this edition, `λεγει αυτω ιησους εγω ειμι η οδος`
(no article before Jesus, as the Westcott–Hort edition reads), where the `TR`
section reads `λεγει αυτω ο ιησους`. Across the 7,940 verses with text the
converted words average 94% word-sequence similarity with `TR`.
