from enum import Enum

class DirectQuestionPattern(Enum):
    FIRST_PERSON_QUESTIONS = "first_person_questions"
    GENERAL_AUDIENCE_QUESTIONS = "general_audience_questions"

DIRECT_QUESTION_PATTERNS = {
    DirectQuestionPattern.FIRST_PERSON_QUESTIONS: [
        "I want to know", "I’d love to hear", "I’m curious", 
        "I wonder", "I’d like your opinion", "I’d like to ask", 
        "I need your input", "I have a question for you"
    ],
    DirectQuestionPattern.GENERAL_AUDIENCE_QUESTIONS: [
        "what do you think", "how do you feel", "have you ever tried", 
        "does this resonate with you", "would you try this", 
        "do you agree", "does this interest you", "what’s your opinion"
    ]
}

ALL_DIRECT_QUESTION_PHRASES = set().union(*DIRECT_QUESTION_PATTERNS.values())
