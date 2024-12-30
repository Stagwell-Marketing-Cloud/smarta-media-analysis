from enum import Enum

class UnboxingPattern(Enum):
    UNBOXING = "unboxing"


UNBOXING_PATTERNS = {
    UnboxingPattern.UNBOXING: [
        "unboxing", "opening", "let's unbox", "unbox"
    ]
}

ALL_UNBOXING_PHRASES = set().union(*UNBOXING_PATTERNS.values())
