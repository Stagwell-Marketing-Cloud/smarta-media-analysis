from enum import Enum

class HookPattern(Enum):
    GENERAL_HOOK = "secret"
    NEGATIVE_HOOK = "don't"

HOOK_PATTERNS = {
    HookPattern.GENERAL_HOOK: [
        "dangerous", "secret", "illegal", "calling all", "unpopular opinion",
        "fun fact", "how to", "did you know", "here's how", "how i went from",
        "I have a confession to make", "why I don't", "...", "hack", "tip", "trick",
        "dangerous", "secret", "illegal", "calling all…", "unpopular opinion",
        "fun fact", "how to", "did you know", "here's how", "how I went from",
        "I have a confession to make", "why I don't…"
    ],
    HookPattern.NEGATIVE_HOOK: [
        "don't", "stop", "mistake", "things I wish I knew sooner"
    ]
}

ALL_HOOK_PHRASES = set().union(*HOOK_PATTERNS.values())
