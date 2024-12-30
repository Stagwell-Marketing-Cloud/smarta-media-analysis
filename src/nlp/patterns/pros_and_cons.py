from enum import Enum

class ProsConsPattern(Enum):
    PROS = "pros"
    CONS = "cons"
    CONTRAST = "contrast"

PROS_CONS_PATTERNS = {
    ProsConsPattern.PROS: [
        "the benefits of", "the good thing about", "what I like about", 
        "the advantages of", "one positive is", "one pro is", 
        "one thing I appreciate is", "the best thing about"
    ],
    ProsConsPattern.CONS: [
        "the downside of", "the bad thing about", "what I dislike about", 
        "the disadvantages of", "one negative is", "one con is", 
        "the worst thing about", "the flaws of"
    ],
    ProsConsPattern.CONTRAST: [
        "on the other hand", "that being said", "however", 
        "having said that", "but then again", "even so", 
        "nevertheless", "nonetheless"
    ]
}

ALL_PROS_CONS_PHRASES = set().union(*PROS_CONS_PATTERNS.values())
