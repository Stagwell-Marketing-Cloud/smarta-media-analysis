from enum import Enum

class ProductSalesVelocityPattern(Enum):
    SELLING_FAST = "selling_fast"

PRODUCT_SALES_VELOCITY_PATTERNS = {
    ProductSalesVelocityPattern.SELLING_FAST: [
        "selling fast", "flying off the shelves", "going fast", 
        "selling out quickly", "almost gone", "running out of stock", 
        "hard to keep in stock", "demand is high", "limited stock remaining", 
        "selling like hotcakes", "popular demand", "can’t keep up with demand"
    ]
}

ALL_PRODUCT_SALES_VELOCITY_PHRASES = set().union(*PRODUCT_SALES_VELOCITY_PATTERNS.values())
