from enum import Enum

class KnowledgeGapPattern(Enum):
    ADMISSION = "admission"
    UNCERTAINTY = "uncertainty"

KNOWLEDGE_GAP_PATTERNS = {
    KnowledgeGapPattern.ADMISSION: [
        "I’m not sure", "I don’t know", "I’m no expert", 
        "I can’t say for certain", "I don’t fully understand", 
        "I’m still learning", "I’m not entirely sure", 
        "I could be wrong", "I don’t have all the answers", 
        "this is just my guess", "I lack the knowledge", 
        "I’m not familiar with", "I’m not well-versed in"
    ],
    KnowledgeGapPattern.UNCERTAINTY: [
        "it might be", "it could be", "I think", "I believe", 
        "possibly", "perhaps", "maybe", "it seems like", 
        "as far as I know", "to the best of my knowledge", 
        "I assume", "I suppose"
    ]
}

ALL_KNOWLEDGE_GAP_PHRASES = set().union(*KNOWLEDGE_GAP_PATTERNS.values())
