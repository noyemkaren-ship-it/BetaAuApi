import re

PROFANITY_ROOTS = [
    "хуй", "хуя", "хую", "хуе", "хуё", "хуи",
    "пизд", "пизж",
    "бляд", "блят", "блядь",
    "ебал", "ебан", "ебуч", "ебён", "ебен", "ебёт", "ебет", "ебись",
    "ебат", "ебля", "ебло", "ебну",
    "сука", "суки", "суке", "суку", "сукой",
    "мудак", "мудил", "мудень",
    "пидор", "пидар", "пидр", "педик",
    "гандон", "гандо", "гондон",
    "залуп",
    "нахуй", "нахуя",
    "долбо", "долба",
    "шлюх", "шлюш",
    "мразь", "мрази",
    "гнида", "гнид",
    "fuck", "fuk", "fck", "f*ck",
    "shit", "bitch", "asshole", "bastard",
    "cunt", "dick", "pussy", "whore",
    "nigger", "nigga", "faggot", "fag",
    "hitler", "nazi", "swastika",
    "卍", "卐",
]

_PATTERN = re.compile(
    "|".join(re.escape(r) for r in PROFANITY_ROOTS),
    re.IGNORECASE | re.UNICODE,
)


def profanity_checker(text: str) -> bool:
    if not text:
        return False
    cleaned = re.sub(r"[\u200b-\u200f\u2028-\u202f\ufeff]", "", text)
    cleaned = re.sub(r"[\s\.\-_\*\|/\\]+", "", cleaned)
    cleaned = _latin_to_cyrillic(cleaned)
    return bool(_PATTERN.search(cleaned))


_HOMOGLYPHS = str.maketrans({
    "a": "а", "e": "е", "o": "о", "p": "р", "c": "с",
    "x": "х", "y": "у", "k": "к", "m": "м", "t": "т",
    "h": "н", "b": "ь", "n": "п", "u": "и", "и": "и",
    "3": "з", "0": "о", "4": "ч", "6": "б", "9": "д",
    "1": "л", "5": "s",
})

def _latin_to_cyrillic(text: str) -> str:
    return text.translate(_HOMOGLYPHS)