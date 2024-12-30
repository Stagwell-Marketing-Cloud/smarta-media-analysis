from enum import Enum

class GRWMPattern(Enum):
    GRWM = "get_ready_with_me"


GRWM_PATTERNS = {
    GRWMPattern.GRWM: [
        "grwm", "get ready with me", "getreadywithme"
    ]
}

ALL_GRWM_PHRASES = set().union(*GRWM_PATTERNS.values())
