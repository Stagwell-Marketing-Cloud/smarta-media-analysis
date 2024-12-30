from enum import Enum

class PersonalOpinionPattern(Enum):
    PERSONAL_PRONOUNS = "personal_pronouns"
    OPINION_INDICATORS = "opinion_indicators"
    EMOTION_WORDS = "emotion_words"
    JUDGMENT_ADJECTIVES = "judgment_adjectives"
    QUALIFIERS_HEDGING = "qualifiers_hedging"
    COMMON_PHRASES = "common_phrases"
    OPINION_PHRASES = "opinion_phrases"

PERSONAL_OPINION_PATTERNS = {
    PersonalOpinionPattern.PERSONAL_PRONOUNS: [
        "I", "me", "my", "mine", "we", "us", "our", "ours"
    ],
    PersonalOpinionPattern.OPINION_INDICATORS: [
        "think", "feel", "believe", "suppose", "assume", 
        "guess", "imagine", "reckon", "suspect"
    ],
    PersonalOpinionPattern.EMOTION_WORDS: [
        "love", "hate", "enjoy", "prefer", "like", "dislike", 
        "wish", "hope", "fear", "concerned"
    ],
    PersonalOpinionPattern.JUDGMENT_ADJECTIVES: [
        "good", "bad", "better", "worse", "amazing", "terrible", 
        "excellent", "awful", "interesting", "boring"
    ],
    PersonalOpinionPattern.QUALIFIERS_HEDGING: [
        "in my opinion", "personally", "to me", "for me", 
        "as far as I’m concerned", "from my perspective", 
        "if you ask me"
    ],
    PersonalOpinionPattern.COMMON_PHRASES: [
        "I think", "I believe", "it seems to me", 
        "my view is", "my perspective is", 
        "what I think is"
    ],
    PersonalOpinionPattern.OPINION_PHRASES: [ 
        "I think", "for me", "to me", "in my opinion", 
        "as far as I’m concerned", "personally", 
        "it seems to me", "I feel that", "from my perspective", 
        "if you ask me", "I reckon", "I suppose"
    ]
}

ALL_PERSONAL_OPINION_PHRASES = set().union(*PERSONAL_OPINION_PATTERNS.values())