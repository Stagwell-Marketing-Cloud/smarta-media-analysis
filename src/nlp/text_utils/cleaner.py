import re 
def text_normalizer(text):
    text = re.sub(r"[^A-Za-z0-9\s%.#]+", "", text, re.IGNORECASE)
    text = text.strip().replace('\n', ' ')
    text = re.sub(r"\*", "", text)
    return text