# Translation licence audit — raamattu.uskonkirjat.net

Audited 2026-09-24 from https://raamattu.uskonkirjat.net/help/copyright.html
(the site's own copyright page). Verbatim terms preserved below; the verdict
column is this repository's reading of them for **redistribution inside a
public git repository**, which is a stricter test than personal study use.

"Vapaassa käytössä" = "in free use" is the site's phrase for texts it treats
as unrestricted. Nearly all of these are old enough to be public domain by
age; the phrase is recorded as the site's assertion, not as a licence grant
by us.

## Verdict summary

| Translation | Site's terms | May we redistribute? |
| --- | --- | --- |
| **Raamattu 1992** | Kirkon keskusrahasto; "kopioiminen ja edelleen levittäminen on **ehdottomasti kielletty**" | **NO — forbidden outright** |
| Raamattu 1933/38 | Vapaassa käytössä | YES |
| Biblia 1776 | Vapaassa käytössä | YES |
| STLK 2017 | CC BY-NC-ND 4.0 | NO for this repo — ND forbids derivatives, and chapter-splitting with added tokens is a derivative; NC also conflicts with unrestricted public reuse |
| Folkbibeln 2015 | © Stiftelsen Svenska Folkbibeln | NO |
| Svenska Bibeln 1917 | Vapaassa käytössä | YES |
| Danske Bibel 1931 | Vapaassa käytössä | YES |
| Norsk Bibelen 1930 | Vapaassa käytössä | YES |
| **King James** | Vapaassa käytössä | **YES — the reference implementation target** |
| New English Translation (NET) | "Ei-kaupallinen käyttö sallittu" (non-commercial only) | NO — NC restriction |
| Young's Literal | Vapaassa käytössä | YES |
| Darby Bible | Vapaassa käytössä | YES |
| American Standard Version | Vapaassa käytössä | YES |
| International Standard Version | "distributed freely in its current form, **without changes**" | NO — we restructure into chapters |
| Green's Literal (LITV) | © 1993 Jay P. Green Sr.; non-commercial, granted for The SWORD Project | NO |
| JPS Tanakh 1917 | © 1998 Larry Nelson, All Rights Reserved | NO — the 1917 text is PD by age, but this *electronic edition* is claimed |
| Louis Segond | Vapaassa käytössä | YES |
| Luther 1545 | Vapaassa käytössä | YES |
| Statenvertaling 1637 | Vapaassa käytössä | YES |
| Riveduta Bibbia | Vapaassa käytössä | YES |
| Reina-Valera | Vapaassa käytössä | YES |
| Russkaja Biblija | Vapaassa käytössä | YES |
| Septuaginta | Vapaassa käytössä | YES |
| Syrian Peshitta (Eng. tr.) | Vapaassa käytössä | YES |
| Latin Vulgata | Vapaassa käytössä | YES |
| Biblia Hebraica (Westminster Leningrad Codex) | Vapaassa käytössä | YES |
| SBLGNT | © 2010 SBL & Logos; free to distribute, **may not be sold on its own** | LIKELY YES — needs the upstream licence read directly before ingest |
| Westcott-Hort | Vapaassa käytössä | YES |
| **Textus Receptus** | Vapaassa käytössä | YES |
| Bysantin tekstilaitos | Vapaassa käytössä | YES |

## The finding that matters most

**Raamattu 1992 — the standard modern Finnish translation, and the one most
Finnish readers would expect — cannot be used.** Its terms forbid copying and
redistribution outright; only personal retrieval for study is allowed. It is
owned by Kirkon keskusrahasto (the Church Central Fund), and any other use
requires their separate written permission.

That is not a grey area to be argued around. The Finnish-language spine of
this implant must therefore be **Raamattu 1933/38** (the older church
translation, in free use) and **Biblia 1776**, with 1992 cited by reference
only — quoting a verse in an article is ordinary right of quotation; storing
the text is not.

If Raamattu 1992 is wanted later, the route is a written licence request to
Kirkon keskusrahasto, Satamakatu 11 A, 00160 Helsinki. Nothing else.

## A note on "vapaassa käytössä"

The site asserting free use is evidence, not title. For anything we ingest,
the real ground is that the work is old enough to be public domain in Finland
and the source country: life of author plus 70 years, and these translations
are 17th–20th century. The KJV (1611) is additionally subject to a perpetual
Crown copyright *in the United Kingdom only*, administered by Cambridge
University Press; it is public domain everywhere else, and Finland is
everywhere else. Recorded here so the reasoning is auditable rather than
assumed.

## Consequence for ingest order

1. **King James (1611)** — the reference implementation. Unambiguous, English,
   widely known, easy to verify against other copies.
2. **Raamattu 1933/38** — the Finnish spine.
3. **Textus Receptus** and **Westcott-Hort** — Greek source texts.
4. **Biblia Hebraica (WLC)** — Hebrew source text.
5. **Septuaginta**, **Vulgata** — the ancient translations.

Everything in the NO column is cited by reference and never stored.
