from enum import Enum

class DupePattern(Enum):
    DUPE = "dupe"


DUPE_PATTERNS = {
    DupePattern.DUPE: [
        "dupe", "duplicate", "Affordable alternative to", "Budget-friendly version", "Substitute to", 
        "Cheap product", "Replica", "Copycat", "LookForLess"

    ]
}

ALL_DUPE_PHRASES = set().union(*DUPE_PATTERNS.values())
