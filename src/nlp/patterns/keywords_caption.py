from enum import Enum

class KeywordsCaptionPattern(Enum):
    KEYWORDS_CAPTION = "secret"

KEYWORDS_CAPTION_PATTERNS = {
    KeywordsCaptionPattern.KEYWORDS_CAPTION: 
    ["peach of mind", "happy baby", "easy to use", "baby safe", "leak proof",
    "super absorbent", "reliable", "soft", "gentle", "natural", "breathable"
    ]
}

ALL_KEYWORDS_CAPTION_PHRASES = set().union(*KEYWORDS_CAPTION_PATTERNS.values())
