from enum import Enum

class ProductUsageDurationPattern(Enum):
    DURATION = "duration"

PRODUCT_USAGE_DURATION_PATTERNS = {
    ProductUsageDurationPattern.DURATION: [
        "I’ve been using this for", "I’ve used this for", 
        "I started using this", "I’ve had this for", 
        "been using this for", "I’ve had it for", 
        "used this product for", "over the last", "over the past", 
        "for the past few weeks", "for the past few months", 
        "for a couple of months", "for years now", 
        "for a long time", "since I started using this", 
        "ever since I got it", "ever since I started using it"
    ]
}

ALL_PRODUCT_USAGE_DURATION_PHRASES = set().union(*PRODUCT_USAGE_DURATION_PATTERNS.values())
