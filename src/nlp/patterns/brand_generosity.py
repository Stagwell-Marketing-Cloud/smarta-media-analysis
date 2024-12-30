from enum import Enum

class BrandGenerosityPattern(Enum):
    GENEROSITY = "generosity"
    APPRECIATION = "appreciation"

BRAND_GENEROSITY_PATTERNS = {
    BrandGenerosityPattern.GENEROSITY: [
        "the brand was so generous", "they were kind enough to", 
        "the brand went above and beyond", "their generosity made this possible", 
        "such a generous offer", "an incredible gesture from the brand",
        "thanks to their generosity", "they made this possible for us",
        "this amazing brand gave us", "a special gift from the brand"
    ],
    BrandGenerosityPattern.APPRECIATION: [
        "we’re so thankful to", "I’m grateful to the brand", 
        "thanks to the brand", "a big thank you to", 
        "we owe this deal to", "I appreciate what they’ve done", 
        "a huge shoutout to the brand", "this wouldn’t have happened without them"
    ]
}

ALL_BRAND_GENEROSITY_PHRASES = set().union(*BRAND_GENEROSITY_PATTERNS.values())
