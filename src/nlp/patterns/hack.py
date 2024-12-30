from enum import Enum

class HackPattern(Enum):
    HACK = "hack"
    TUTORIAL = "don't"

HACK_PATTERNS = {
    HackPattern.HACK: [
        "hack"
    ],
    HackPattern.TUTORIAL: [
        "tutorial"
    ]
}

ALL_HACK_PHRASES = set().union(*HACK_PATTERNS.values())
