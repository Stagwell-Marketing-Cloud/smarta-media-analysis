from enum import Enum

class DiscountScarcityPattern(Enum):
    LIMITED_TIME = "limited_time"
    EXCLUSIVE_DISCOUNT = "exclusive_discount"
    URGENCY_PROMOTION = "urgency_promotion"

DISCOUNT_SCARCITY_PATTERNS = {
    DiscountScarcityPattern.LIMITED_TIME: [
        "limited time discount", "offer ends soon", "today only",
        "discount expires", "last day for discount", "limited time only",
        "discount available for a short time", "flash sale"
    ],
    DiscountScarcityPattern.EXCLUSIVE_DISCOUNT: [
        "members-only discount", "exclusive offer", "only available here",
        "special deal", "VIP discount", "unique discount",
        "private sale", "restricted access offer"
    ],
    DiscountScarcityPattern.URGENCY_PROMOTION: [
        "act now to save", "hurry, limited discount", "don’t miss out on savings",
        "grab this deal", "discount running out", "save now before it’s gone",
        "discount won’t last", "secure your discount now"
    ],
}

ALL_DISCOUNT_SCARCITY_PHRASES = set().union(*DISCOUNT_SCARCITY_PATTERNS.values())