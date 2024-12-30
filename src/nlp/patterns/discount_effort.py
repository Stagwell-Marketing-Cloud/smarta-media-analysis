from enum import Enum

class DiscountEffortPattern(Enum):
    HARD_WORK = "hard_work"
    EXCLUSIVE_FOR_FOLLOWERS = "exclusive_for_followers"

DISCOUNT_EFFORT_PATTERNS = {
    DiscountEffortPattern.HARD_WORK: [
        "I worked hard to", "I fought to", "I negotiated to", 
        "it took a lot of effort to", "I went the extra mile to", 
        "I secured this for you", "I made this happen for you",
        "I pulled some strings to", "it wasn’t easy to"
    ],
    DiscountEffortPattern.EXCLUSIVE_FOR_FOLLOWERS: [
        "just for my followers", "exclusive for my audience", 
        "special deal for my followers", "made this possible for you",
        "only for my community", "unique deal for my followers",
        "because you support me", "as a thank you to my followers"
    ]
}

ALL_DISCOUNT_EFFORT_PHRASES = set().union(*DISCOUNT_EFFORT_PATTERNS.values())
