import re
import spacy

def lower_case_text(text:str) -> str: 
    return text.lower()

def count_single_word(text: str, word: str) -> int: 
    """Counts a single word in a string and doesn't match exact"""
    return lower_case_text(text).count(word)

def count_exact_single_word(text: str, exact_word: str) -> int: 
    """counts exact matches of a specific word"""
    lower_text_split = lower_case_text(text).split(" ")
    return sum(1 for word in lower_text_split if word == exact_word)

def count_two_words(text: str, word1: str, word2: str) -> tuple[int,int]: 
    """Counts two specific words in a string"""
    return count_exact_single_word(text, word1), count_exact_single_word(text, word2)


def create_combined_cta_column(df):
    """
    Combines '_transcription' and '_caption' columns into a new '_trans_capt' column for each CTA type.

    Args:
        df (pd.DataFrame): The dataframe to modify.

    Returns:
        pd.DataFrame: The dataframe with new '_trans_capt' columns added.
    """
    cta_columns = [col for col in df.columns if '_transcription' in col or '_caption' in col]
    cta_bases = set(col.rsplit('_', 1)[0] for col in cta_columns)  

    for base in cta_bases:
        transcription_col = f"{base}_transcription"
        caption_col = f"{base}_caption"
        trans_capt_col = f"{base}_trans_capt"

        if transcription_col in df.columns and caption_col in df.columns:

            df[trans_capt_col] = (df[transcription_col].astype(bool) & df[caption_col].astype(bool))
        else:
            print(f"Columns for base '{base}' are incomplete, skipping.")

    return df



### Talking in second person

def second_person(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    return 1 if any("2" in token.morph.get("Person") for token in doc) else 0


### Asking the audience questions

def question_mark_counter(text):
    return len(re.findall(r"\?", text))


# Asking questions directly
def asking_questions_directly(text):
    sec_pers = bool(second_person(text))
    quest_mark = question_mark_counter(text) > 0
    return int(sec_pers and quest_mark)
