import re 
import spacy 
from moviepy import VideoFileClip
from emot.emo_unicode import UNICODE_EMOJI
from sklearn.metrics.pairwise import cosine_similarity


# First person singular
nlp = spacy.load("en_core_web_sm")


def get_text_embedding(text):
    doc = nlp(text)
    return doc.vector


# Apply on the transcription
def regex_matcher(text, lst):
    pattern = r'\b(?:' + '|'.join(re.escape(word) for word in lst) + r')\b'
    return 1 if re.search(pattern, text, re.IGNORECASE) else 0


# Apply on the transcription_translated
def express_personal_opinion(text):
    return 1 if re.search(r'\bI.+(believe|think)\b', text, re.IGNORECASE) else 0


### Family, finance, health
def first_person_singular(text):
    doc = nlp(text)
    first_person = True if any("1" in token.morph.get("Person") for token in doc) else False
    plural = True if any("Sing" in token.morph.get("Number") for token in doc) else False
    return 1 if first_person and plural else 0


def entity_classification(text):
    doc = nlp(text)
    for ent in doc.ents:
        return ent.label_



