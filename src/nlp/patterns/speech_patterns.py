from enum import Enum

class SpeechPattern(Enum):
   BASIC_SOUNDS = "basic_sounds"
   HESITATION_WORDS = "hesitation_words"
   VERBAL_CRUTCHES = "verbal_crutches"
   REPETITIVE_STARTS = "repetitive_starts"
   FILLED_PAUSES = "filled_pauses"
   DISCOURSE_MARKERS = "discourse_markers"

SPEECH_PATTERNS = {
   SpeechPattern.BASIC_SOUNDS: [
       "um", "uh", "er", "ah", "ar", "hmm", "huh", 
       "eh", "mm", "mhm", "mmm", "oh", "uh-huh"
   ],
   
   SpeechPattern.HESITATION_WORDS: [
       "like", "well", "so", "just", "kind of", 
       "sort of", "basically", "literally", "totally"
   ],
   
   SpeechPattern.VERBAL_CRUTCHES: [
       "you know", "I mean", "actually", "basically",
       "right", "okay", "alright", "anyway", 
       "supposedly", "essentially", "fundamentally",
       "pretty much", "you see", "you know what I mean",
       "know what I'm saying", "like I said", "got it"
   ],
   
   SpeechPattern.REPETITIVE_STARTS: [
       "and then", "but then", "so then"
   ],
   
   SpeechPattern.FILLED_PAUSES: [
       "um", "uh", "er", "ah", "hmm", "mm", "mmm", "eh",
       "oh", "uh-huh"
   ],
   
   SpeechPattern.DISCOURSE_MARKERS: [
       "well", "like", "you know", "I mean", "so", 
       "right", "okay", "actually", "yeah"
   ],
}

ALL_FILLER_WORDS = set().union(*SPEECH_PATTERNS.values())