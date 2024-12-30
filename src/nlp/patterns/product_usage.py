from enum import Enum

class ProductUsageByOthersPattern(Enum):
    OTHERS = "others"

PRODUCT_USAGE_BY_OTHERS_PATTERNS = {
    ProductUsageByOthersPattern.OTHERS: [
        "others are using", "people are using", "they use this",
        "others recommend", "many are using", "a lot of people are using", 
        "everyone is talking about", "others love this", "people love this", 
        "everyone is buying", "they tried this", "others have tried this"
    ]
}

ALL_PRODUCT_USAGE_BY_OTHERS_PHRASES = set().union(*PRODUCT_USAGE_BY_OTHERS_PATTERNS.values())
