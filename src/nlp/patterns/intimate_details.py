from enum import Enum

class IntimateDetailsPattern(Enum):
    SELF_DISCLOSURES = "self_disclosures"
    HEALTH = "health"
    FINANCES = "finances"
    RELATIONSHIPS = "relationships"
    FAMILY = "family"

INTIMATE_DETAILS_PATTERNS = {
    IntimateDetailsPattern.SELF_DISCLOSURES: [
        "I feel", "I went through", "I experienced", 
        "my past", "my struggle", "I’m dealing with", 
        "I’m struggling with", "my secret", "I admit"
    ],
    IntimateDetailsPattern.HEALTH: [
        "mental health", "depression", "anxiety", "illness", 
        "therapy", "disease", "sick", "doctor", "hospital", 
        "diagnosis", "pain", "injury", "recovery", "medication", 
        "surgery", "treatment"
    ],
    IntimateDetailsPattern.FINANCES: [
        "debt", "loan", "bankrupt", "financial problems", 
        "credit card", "mortgage", "savings", "retirement", 
        "salary", "income", "paycheck", "bills", "budget", 
        "expenses", "cost", "money problems"
    ],
    IntimateDetailsPattern.RELATIONSHIPS: [
        "breakup", "divorce", "dating", "partner", 
        "boyfriend", "girlfriend", "spouse", "marriage", 
        "relationship problems", "cheating", "love life", 
        "ex-boyfriend", "ex-girlfriend", "arguments", "fighting"
    ],
    IntimateDetailsPattern.FAMILY: [
        "my child", "my kids", "my children", "my son", "my daughter", 
        "my parents", "my mom", "my dad", "my brother", "my sister", 
        "grandparents", "uncle", "aunt", "cousin", "family problems", 
        "family issues", "family drama"
    ],
}


ALL_INTIMATE_DETAILS_PHRASES = set().union(*INTIMATE_DETAILS_PATTERNS.values())
