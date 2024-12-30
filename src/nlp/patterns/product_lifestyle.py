from enum import Enum 

class ProductLifestylePattern(Enum):
    NATURAL_FIT = "natural_fit"
    LIFESTYLE_IMPROVEMENT = "lifestyle_improvement"

PRODUCT_LIFESTYLE_PATTERNS = {
    ProductLifestylePattern.NATURAL_FIT: [
        "fits perfectly into your life", "easy to use daily", 
        "a natural fit for your routine", "blends seamlessly into your lifestyle", 
        "works perfectly with your day-to-day", "makes your life easier", 
        "designed for everyday use", "perfect for your daily routine"
    ],
    ProductLifestylePattern.LIFESTYLE_IMPROVEMENT: [
        "makes your life better", "improves your daily routine", 
        "helps you stay on track", "enhances your lifestyle", 
        "perfect addition to your life", "helps simplify your day", 
        "makes things more convenient", "helps you achieve your goals"
    ]
}

ALL_PRODUCT_LIFESTYLE_PHRASES = set().union(*PRODUCT_LIFESTYLE_PATTERNS.values())
