from enum import Enum

class CuriosityPattern(Enum):
    WHATISNEXT = "next we have"
    OPINION = "what do you think about"

CURIOSITY_PATTERNS = {
    CuriosityPattern.WHATISNEXT: [
        "next we have"
    ],
    CuriosityPattern.OPINION: [
        "what do you think about", "what is your opinion on"
    ]
}

ALL_CURIOSITY_PHRASES = set().union(*CURIOSITY_PATTERNS.values())
