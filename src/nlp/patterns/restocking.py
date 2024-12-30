from enum import Enum

class RestockingPattern(Enum):
    RESTOCKING = "restock"


RESTOCKING_PATTERNS = {
    RestockingPattern.RESTOCKING: [
        "restock", "restocking", "filling up", "replenishing", "stocking up"
    ]
}

ALL_RESTOCKING_PHRASES = set().union(*RESTOCKING_PATTERNS.values())
