from enum import Enum

class BrandMatchingPattern(Enum):
    PG_BRAND = "P&G"
    COTERIE_BRAND = "Coterie"
    HEALTHYBABY_BRAND = "Healthy Baby"
    HONEST_BRAND = "Honest"
    HUGGIES_BRAND = "Huggies"
    KUDOSTOBABY_BRAND = "Kudostobaby"
    LUVS_BRAND = "Luvs"
    MYMILLIEMOON_BRAND = "Mymilliemoon"
    PAMPERSUS_BRAND = "Pampersus"
    RASCALSBABY_BRAND = "Rascalsbaby"
    THENINJAMAS_BRAND = "Theninjamas"




BRAND_PATTERNS = {
    BrandMatchingPattern.PG_BRAND: [
        "P&G", "P & G", "Procter and Gamble", "P and G",
    ],
    BrandMatchingPattern.COTERIE_BRAND: [
        "Coterie"
    ],
    BrandMatchingPattern.HEALTHYBABY_BRAND: [
        "healthy baby", "healthybaby"
    ],
    BrandMatchingPattern.HONEST_BRAND: [
        "The Honest Company", "Thehonestcompany", "honest"
    ],
    BrandMatchingPattern.HUGGIES_BRAND: [
        "Huggies",
    ],
    BrandMatchingPattern.KUDOSTOBABY_BRAND: [
        "Kudostobaby", "kudos"
    ],
    BrandMatchingPattern.LUVS_BRAND: [
        "luvs"
    ],
    BrandMatchingPattern.MYMILLIEMOON_BRAND: [
        "milliemoon", "millie moon", "millie"
    ],
    BrandMatchingPattern.PAMPERSUS_BRAND: [
        "pampersus"
    ],
    BrandMatchingPattern.RASCALSBABY_BRAND: [
        "rascal", "Rascals"
    ],
    BrandMatchingPattern.THENINJAMAS_BRAND: [
        "ninjamas"
    ],
}

ALL_BRAND_MATCHING_PHRASES = set().union(*BRAND_PATTERNS.values())
