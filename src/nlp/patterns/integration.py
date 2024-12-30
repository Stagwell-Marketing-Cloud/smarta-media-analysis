from enum import Enum

class IntegrationPattern(Enum):
    INTEGRATION_BRAND = "P&G"
    INTEGRATION_GENERAL = "More on that later"
    INTEGRATION_END = "back to our content"


INTEGRATION_PATTERNS = {
    IntegrationPattern.INTEGRATION_BRAND: [
        "P&G", "P & G", "Procter and Gamble", "P and G",
        "Coterie", "healthy baby", "healthybaby", "The Honest Company", "Thehonestcompany", "honest company",
        "Huggies", "Kudostobaby", "kudos", "luvs", "milliemoon", "millie moon",
        "pampersus", "rascal babies", "Rascals", "ninjamas"
    ],
    IntegrationPattern.INTEGRATION_GENERAL: [
        "more on that later", "click the link", "today's sponsor"
    ],
    IntegrationPattern.INTEGRATION_END: [
    "back to our", "thanks again to", "for sponsoring the video", "click the link in the description",
    "big thanks to our sponsor", "huge shoutout to", "appreciate the support from", "brought to you by",
    "partnered with us for this video", "continuing with our content", "don’t forget to visit", "find out more details",
    "thanks for listening to our sponsor", "So now we're ready for", "Good night", "now available", "bye", "available at"
    ]
}

ALL_INTETGRATION_PHRASES = set().union(*INTEGRATION_PATTERNS.values())
