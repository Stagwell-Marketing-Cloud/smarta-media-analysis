from enum import Enum

class BTSPattern(Enum):
    BTS = "behind the scenes"


BTS_PATTERNS = {
    BTSPattern.BTS: [
        "behind the scenes"
    ]
}

ALL_BTS_PHRASES = set().union(*BTS_PATTERNS.values())
