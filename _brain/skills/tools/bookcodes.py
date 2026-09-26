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

# Per-book metadata: (testament, division, one-line description, chapter count).
# Division is the traditional grouping (Torah, Former Prophets, etc. for OT;
# Gospels, Pauline epistles, etc. for NT). Chapter count is the Protestant canon.
BOOK_META = {
    "gen": ("ot", "Torah", "Creation, the flood, the patriarchs, and the origin of Israel.", 50),
    "exo": ("ot", "Torah", "The exodus from Egypt, the covenant at Sinai, and the tabernacle.", 40),
    "lev": ("ot", "Torah", "Priestly law: sacrifices, purity, and the holiness code.", 27),
    "num": ("ot", "Torah", "The wilderness wandering and the census of Israel.", 36),
    "deu": ("ot", "Torah", "Moses' final addresses and the renewal of the covenant.", 34),
    "jos": ("ot", "Former Prophets", "The conquest and division of Canaan under Joshua.", 24),
    "jdg": ("ot", "Former Prophets", "Israel's cycle of apostasy and deliverance before the monarchy.", 21),
    "rut": ("ot", "Former Prophets", "A Moabite widow's loyalty and her place in David's lineage.", 4),
    "1sa": ("ot", "Former Prophets", "From the judges to Saul: the rise and fall of Israel's first king.", 31),
    "2sa": ("ot", "Former Prophets", "David's reign: triumph, sin, and its consequences.", 24),
    "1ki": ("ot", "Former Prophets", "Solomon's kingdom, the temple, and the divided monarchy.", 22),
    "2ki": ("ot", "Former Prophets", "The divided kingdoms to the Assyrian and Babylonian exiles.", 25),
    "1ch": ("ot", "Writings", "Genealogies and Saul's death, setting up David's reign.", 29),
    "2ch": ("ot", "Writings", "Solomon's temple to the Babylonian exile, from the priestly view.", 36),
    "ezr": ("ot", "Writings", "The return from exile and the rebuilding of the temple.", 10),
    "neh": ("ot", "Writings", "Rebuilding Jerusalem's walls and covenant renewal under Nehemiah.", 13),
    "est": ("ot", "Writings", "A Jewish queen saves her people in the Persian court.", 10),
    "job": ("ot", "Wisdom", "The suffering of a righteous man and the question of divine justice.", 42),
    "psa": ("ot", "Wisdom", "One hundred and fifty songs of praise, lament, and royal trust.", 150),
    "pro": ("ot", "Wisdom", "Solomonic aphorisms on the way of wisdom and folly.", 31),
    "ecc": ("ot", "Wisdom", "A philosopher's meditation on meaning under the sun.", 12),
    "sng": ("ot", "Wisdom", "A love poem between a shepherd and a king's daughter.", 8),
    "isa": ("ot", "Latter Prophets", "Judgement, comfort, and the servant songs over sixty-six chapters.", 66),
    "jer": ("ot", "Latter Prophets", "A prophet's forty-year warning before Jerusalem falls.", 52),
    "lam": ("ot", "Latter Prophets", "Five laments over the destruction of Jerusalem.", 5),
    "ezk": ("ot", "Latter Prophets", "Exilic visions: judgement, the valley of dry bones, and a new temple.", 48),
    "dan": ("ot", "Latter Prophets", "A courtier's faith under empire and apocalyptic visions.", 12),
    "hos": ("ot", "Minor Prophets", "A prophet's marriage as a parable of God's covenant with Israel.", 14),
    "jol": ("ot", "Minor Prophets", "Locusts, the day of the Lord, and the outpoured Spirit.", 3),
    "amo": ("ot", "Minor Prophets", "A shepherd's indictment of Israel's social injustice.", 9),
    "oba": ("ot", "Minor Prophets", "A single chapter against Edom's pride and cruelty.", 1),
    "jon": ("ot", "Minor Prophets", "A reluctant prophet and God's mercy to Nineveh.", 4),
    "mic": ("ot", "Minor Prophets", "What the Lord requires, and a ruler from Bethlehem.", 7),
    "nam": ("ot", "Minor Prophets", "The fall of Nineveh foretold in poetry.", 3),
    "hab": ("ot", "Minor Prophets", "The just shall live by faith, and judgement on the proud.", 3),
    "zep": ("ot", "Minor Prophets", "The day of the Lord and a remnant saved.", 3),
    "hag": ("ot", "Minor Prophets", "Rebuild the temple: God's house before your own houses.", 2),
    "zec": ("ot", "Minor Prophets", "Night visions, two olive branches, and a coming king.", 14),
    "mal": ("ot", "Minor Prophets", "The last prophet before silence: robbing God, and a messenger to come.", 4),
    "mat": ("nt", "Gospels", "Jesus as the promised king: genealogy, Sermon on the Mount, passion.", 28),
    "mrk": ("nt", "Gospels", "The shortest gospel: Jesus acts with authority and suffers as servant.", 16),
    "luk": ("nt", "Gospels", "A historian's account: Jesus among the lost, the poor, and the marginal.", 24),
    "jhn": ("nt", "Gospels", "Signs and discourses: Jesus as the Word made flesh and the way, truth, life.", 21),
    "act": ("nt", "History", "The Spirit given, the church born, and the gospel reaching Rome.", 28),
    "rom": ("nt", "Pauline Epistles", "Justification by faith, life in the Spirit, and God's plan for Israel.", 16),
    "1co": ("nt", "Pauline Epistles", "A divided church corrected: gifts, the body, love, and the resurrection.", 16),
    "2co": ("nt", "Pauline Epistles", "Paul's defence of his apostleship and the generosity of the new covenant.", 13),
    "gal": ("nt", "Pauline Epistles", "Justification by faith alone; no return to the law.", 6),
    "eph": ("nt", "Pauline Epistles", "The cosmic scope of the church: one body, one Spirit, one new humanity.", 6),
    "php": ("nt", "Pauline Epistles", "Joy in chains: Christ's mind, the gospel's advance, and contentment.", 4),
    "col": ("nt", "Pauline Epistles", "Christ as the image of the invisible God, head of all things.", 4),
    "1th": ("nt", "Pauline Epistles", "Comfort in bereavement and the hope of the Lord's return.", 5),
    "2th": ("nt", "Pauline Epistles", "The man of lawlessness and the stability of the believer.", 3),
    "1ti": ("nt", "Pastoral Epistles", "Church order, elders and deacons, and the good fight of faith.", 6),
    "2ti": ("nt", "Pastoral Epistles", "Paul's last letter: guard the deposit, preach the word, endure.", 4),
    "tit": ("nt", "Pastoral Epistles", "Set in order what was left: elders, sound doctrine, and good works.", 3),
    "phm": ("nt", "Pauline Epistles", "A runaway slave received as a brother: the gospel's social reach.", 1),
    "heb": ("nt", "General Epistles", "Christ greater than angels, Moses, and the old covenant's priesthood.", 13),
    "jas": ("nt", "General Epistles", "Faith without works is dead: practical wisdom for the diaspora.", 5),
    "1pe": ("nt", "General Epistles", "Suffering as a Christian and a holy identity under fire.", 5),
    "2pe": ("nt", "General Epistles", "False teachers, the certainty of Christ's return, and growth in grace.", 3),
    "1jn": ("nt", "General Epistles", "Light, love, and the test of true fellowship with God.", 5),
    "2jn": ("nt", "General Epistles", "Walking in truth and love, and refusing those who deny Christ's flesh.", 1),
    "3jn": ("nt", "General Epistles", "Hospitality commended, and a self-serving leader named.", 1),
    "jud": ("nt", "General Epistles", "Contend for the faith against those who turn grace into licence.", 1),
    "rev": ("nt", "Apocalypse", "Seven churches, a heavenly throne, and the Lamb's victory over the beast.", 22),
}

TESTAMENTS = {
    "ot": ("Old Testament", "The thirty-nine books of the Hebrew Bible, from creation to the "
           "prophets — the scripture Jesus and the apostles read, cite, and fulfil."),
    "nt": ("New Testament", "The twenty-seven books of the apostolic witness: four gospels, "
           "the church's birth, letters to churches and pastors, and the apocalypse."),
}

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
