from enum import Enum

class ProductScarcityPattern(Enum):
    LIMITED_AVAILABILITY = "limited_availability"
    EXCLUSIVITY = "exclusivity"
    TIME_SENSITIVE = "time_sensitive"

PRODUCT_SCARCITY_PATTERNS = {
    ProductScarcityPattern.LIMITED_AVAILABILITY: [
        "limited edition", "only a few left", "while supplies last",
        "exclusive release", "one-time offer", "limited stock",
        "rare find", "scarce availability", "running out fast",
        "almost gone", "few remaining", "selling out quickly"
    ],
    ProductScarcityPattern.EXCLUSIVITY: [
        "exclusive deal", "available to a select few", "members-only",
        "private access", "special release", "only available here",
        "invite-only", "exclusive rights", "VIP only"
    ],
    ProductScarcityPattern.TIME_SENSITIVE: [
        "act now", "hurry up", "offer ends soon", "last chance",
        "today only", "limited time offer", "don’t miss out",
        "expires soon", "closing soon", "just for now"
    ],
}

ALL_PRODUCT_SCARCITY_PHRASES = set().union(*PRODUCT_SCARCITY_PATTERNS.values())