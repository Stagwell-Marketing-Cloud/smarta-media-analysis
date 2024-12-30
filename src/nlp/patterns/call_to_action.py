from enum import Enum

class CTAPattern(Enum):
    CTA_BUY = "buy"
    CTA_GIFT = "gift"
    CTA_READ = "read"
    CTA_SIGN_UP = "sign up"
    CTA_FIND_OUT = "find out"
    CTA_LEARN = "learn"
    CTA_SUBSCRIBE = "subscribe"
    CTA_SHARE = "share"
    CTA_DOWNLOAD = "download"
    CTA_VISIT = "visit"
    CTA_CONTACT = "contact"
    CTA_PARTICIPATE = "participate"

CTA_PATTERNS = {
    CTAPattern.CTA_BUY: [
        "buy", "shop now", "order today", "add to cart", "get yours",
    ],
    CTAPattern.CTA_GIFT: [
        "gift", "send a gift", "gift it", "perfect present", "surprise someone",
    ],
    CTAPattern.CTA_READ: [
        "read", "check this out", "discover", "explore", "read more", "dive in"
    ],
    CTAPattern.CTA_SIGN_UP: [
        "sign up", "join us", "get started", "register now", "sign up today", "reserve your spot"
    ],
    CTAPattern.CTA_FIND_OUT: [
        "find out", "see why", "uncover", "check this out"
    ],
    CTAPattern.CTA_LEARN: [
        "learn", "how to", "improve",
    ],
    CTAPattern.CTA_SUBSCRIBE: [
        "subscribe", "follow us", "subscribe now", "stay updated", "don’t miss out", "get notified"
    ],
    CTAPattern.CTA_SHARE: [
        "share this", "tell a friend", "spread the word", "retweet", "repost", "tag someone"
    ],
    CTAPattern.CTA_DOWNLOAD: [
        "download now", "save this", "access now", "install today"
    ],
    CTAPattern.CTA_VISIT: [
        "visit us", "check out our site", "find us here", "go to", "see more here"
    ],
    CTAPattern.CTA_CONTACT: [
        "contact us", "DM us", "reach out", "ask us", "get in touch"
    ],
    CTAPattern.CTA_PARTICIPATE: [
        "join the challenge", "enter now", "participate", "be part of this", "vote now"
    ]
}

ALL_CTA_PHRASES = set().union(*CTA_PATTERNS.values())
