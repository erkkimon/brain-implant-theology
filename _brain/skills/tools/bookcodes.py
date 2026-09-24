"""Canonical book codes for atomic verse reference tokens.

The code is the first component of a verse token (`jhn14v6`), so it must be
lowercase alphanumeric and stable forever: changing one invalidates every
token already written. These follow the OSIS abbreviations, lowercased, with
numbered books keeping their digit prefix (`1co`, `2ti`, `3jn`).

See conventions/addressing-scripture.md for why tokens carry no punctuation.
"""

# OSIS code -> canonical English name. Order is canonical (Protestant),
# which is also the order chapters sort in.
CANON = [
    ("gen", "Genesis"), ("exo", "Exodus"), ("lev", "Leviticus"),
    ("num", "Numbers"), ("deu", "Deuteronomy"), ("jos", "Joshua"),
    ("jdg", "Judges"), ("rut", "Ruth"), ("1sa", "1 Samuel"),
    ("2sa", "2 Samuel"), ("1ki", "1 Kings"), ("2ki", "2 Kings"),
    ("1ch", "1 Chronicles"), ("2ch", "2 Chronicles"), ("ezr", "Ezra"),
    ("neh", "Nehemiah"), ("est", "Esther"), ("job", "Job"),
    ("psa", "Psalms"), ("pro", "Proverbs"), ("ecc", "Ecclesiastes"),
    ("sng", "Song of Solomon"), ("isa", "Isaiah"), ("jer", "Jeremiah"),
    ("lam", "Lamentations"), ("ezk", "Ezekiel"), ("dan", "Daniel"),
    ("hos", "Hosea"), ("jol", "Joel"), ("amo", "Amos"),
    ("oba", "Obadiah"), ("jon", "Jonah"), ("mic", "Micah"),
    ("nam", "Nahum"), ("hab", "Habakkuk"), ("zep", "Zephaniah"),
    ("hag", "Haggai"), ("zec", "Zechariah"), ("mal", "Malachi"),
    ("mat", "Matthew"), ("mrk", "Mark"), ("luk", "Luke"),
    ("jhn", "John"), ("act", "Acts"), ("rom", "Romans"),
    ("1co", "1 Corinthians"), ("2co", "2 Corinthians"), ("gal", "Galatians"),
    ("eph", "Ephesians"), ("php", "Philippians"), ("col", "Colossians"),
    ("1th", "1 Thessalonians"), ("2th", "2 Thessalonians"),
    ("1ti", "1 Timothy"), ("2ti", "2 Timothy"), ("tit", "Titus"),
    ("phm", "Philemon"), ("heb", "Hebrews"), ("jas", "James"),
    ("1pe", "1 Peter"), ("2pe", "2 Peter"), ("1jn", "1 John"),
    ("2jn", "2 John"), ("3jn", "3 John"), ("jud", "Jude"),
    ("rev", "Revelation"),
]

CODE_TO_NAME = dict(CANON)
CANON_ORDER = {code: i for i, (code, _) in enumerate(CANON)}

# Source-data spellings seen in the wild -> our code. Roman-numeral prefixes
# ("I Samuel"), "Revelation of John", "Canticles" and friends all land here so
# a new source needs a mapping entry, never a change to the codes themselves.
_ALIASES = {
    "i samuel": "1sa", "ii samuel": "2sa", "i kings": "1ki", "ii kings": "2ki",
    "i chronicles": "1ch", "ii chronicles": "2ch",
    "i corinthians": "1co", "ii corinthians": "2co",
    "i thessalonians": "1th", "ii thessalonians": "2th",
    "i timothy": "1ti", "ii timothy": "2ti",
    "i peter": "1pe", "ii peter": "2pe",
    "i john": "1jn", "ii john": "2jn", "iii john": "3jn",
    "revelation of john": "rev", "the revelation": "rev",
    "song of songs": "sng", "canticles": "sng",
    "psalm": "psa", "ecclesiastes or the preacher": "ecc",
}


def code_for(name: str) -> str:
    """Map a source's book name to our canonical code, or raise.

    Raising is deliberate: a silently skipped or mis-mapped book would produce
    tokens that look right and point nowhere, and a wrong token fails quietly —
    exactly the failure the addressing convention exists to prevent.
    """
    key = " ".join(str(name).strip().lower().split())
    if key in _ALIASES:
        return _ALIASES[key]
    for code, canonical in CANON:
        if key == canonical.lower():
            return code
    # "1 Samuel" / "1Samuel" / "1st Samuel" style
    compact = key.replace(".", "").replace("st ", " ").replace("nd ", " ")
    for code, canonical in CANON:
        if " ".join(compact.split()) == canonical.lower():
            return code
    raise KeyError(
        f"unknown book name {name!r} — add it to _ALIASES in bookcodes.py "
        "rather than inventing a code; codes are permanent once tokens ship"
    )


def verse_token(code: str, chapter: int, verse: int) -> str:
    """The atomic reference token: no punctuation, so BM25 cannot split it."""
    return f"{code}{int(chapter)}v{int(verse)}"


def human_ref(code: str, chapter: int, verse: int | None = None) -> str:
    """The form a person reads. Always written beside the token, never alone."""
    name = CODE_TO_NAME[code]
    return f"{name} {chapter}" + (f":{verse}" if verse is not None else "")
