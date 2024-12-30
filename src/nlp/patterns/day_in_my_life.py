from enum import Enum

class DayInMyLifePattern(Enum):
    DAY_IN_MY_LIFE_PATTERNS = "DITL"


DAY_IN_MY_LIFE_PATTERNS = {
    DayInMyLifePattern.DAY_IN_MY_LIFE_PATTERNS: [
        "Day in My Life", "Day in the Life", "Daily Routine",
        "24 Hours with Me", "Spend the Day with Me", "Follow Me Around",
        "A Typical Day", "Daily Vlog", "DayInMyLife", "DITL"
    ]
}

ALL_DAY_IN_MY_LIFE_PHRASES = set().union(*DAY_IN_MY_LIFE_PATTERNS.values())
