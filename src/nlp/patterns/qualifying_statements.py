from enum import Enum

class QualifyingStatementsPattern(Enum):
    HONESTY = "honesty"
    CONTRAST = "contrast"

QUALIFYING_STATEMENTS_PATTERNS = {
    QualifyingStatementsPattern.HONESTY: [
        "I'll be honest", "to be honest", "let me be honest", 
        "truth be told", "honestly speaking", "in all honesty"
    ],
    QualifyingStatementsPattern.CONTRAST: [
        "on the other hand", "that being said", "however", 
        "having said that", "but then again", "even so", 
        "nevertheless", "nonetheless"
    ]
}

ALL_QUALIFYING_STATEMENTS_PHRASES = set().union(*QUALIFYING_STATEMENTS_PATTERNS.values())
