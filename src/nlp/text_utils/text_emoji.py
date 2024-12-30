from emot.emo_unicode import UNICODE_EMOJI

def text_has_emoji(text):
    for character in text:
        if character in UNICODE_EMOJI:
            return True
    return False