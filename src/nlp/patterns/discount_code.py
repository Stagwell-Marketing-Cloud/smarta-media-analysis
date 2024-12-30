from enum import Enum

class DiscountCodePattern(Enum):
    UNIQUE_CODE = "unique_code"
    SHARING_CODE = "sharing_code"

DISCOUNT_CODE_PATTERNS = {
    DiscountCodePattern.UNIQUE_CODE: [
        "use my code", "my discount code", "this special code", 
        "use the code", "enter code", "apply my code", 
        "get your discount with code", "redeem using code", 
        "exclusive code", "personal discount code", 
        "this unique code"
    ],
    DiscountCodePattern.SHARING_CODE: [
        "I’m sharing this code", "I’ve got a code for you", 
        "here’s my code", "you can use my code", 
        "let me share this code with you", "sharing this discount code", 
        "giving you this code", "passing this code along"
    ]
}

ALL_DISCOUNT_CODE_PHRASES = set().union(*DISCOUNT_CODE_PATTERNS.values())
