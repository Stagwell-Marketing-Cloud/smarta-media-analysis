from enum import Enum

class ProductJourneyPattern(Enum):
    CONTINUATION = "continuation"
    GOALS = "goals"

PRODUCT_JOURNEY_PATTERNS = {
    ProductJourneyPattern.CONTINUATION: [
        "the next step in your journey", "the natural progression", 
        "a continuation of your efforts", "builds on what you've started", 
        "helps you take the next step", "moves you closer to your goal",
        "takes your progress further", "advances your journey", 
        "fits perfectly into your path", "a logical next step"
    ],
    ProductJourneyPattern.GOALS: [
        "aligns with your goals", "helps you achieve your dreams", 
        "keeps you on track", "takes you closer to your aspirations", 
        "supports your mission", "makes your goals achievable", 
        "helps you continue your work", "follows your vision"
    ]
}

ALL_PRODUCT_JOURNEY_PHRASES = set().union(*PRODUCT_JOURNEY_PATTERNS.values())
