from enum import Enum

class TipsPattern(Enum):
    SHORTCUTS = "shortcut"
    CLEAN = "clean"
    FOOD_PREPARATION = "meal preparation"

TIPS_PATTERNS = {
    TipsPattern.SHORTCUTS: [
        "shorcut", "make everyday task easier"
    ],
    TipsPattern.TIDY_UP: [
        "clean", "tidy up"
    ],
    TipsPattern.FOOD_PREPARATION: [
        "meal preparation", "food storage"
    ],
    TipsPattern.GROOMING: [
        "grooming", "personal care"
    ],
    TipsPattern.GADGETS: [
        "improve gadgets"
    ]
}

ALL_TIPS_PHRASES = set().union(*TIPS_PATTERNS.values())
