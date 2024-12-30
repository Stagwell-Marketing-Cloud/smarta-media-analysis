import re

import pandas as pd

def contains_pattern(text: str, pattern_words: list) -> int: 
    return 1 if any([word in text for word in pattern_words]) else 0 


def contains_words(text: str, word_list: list[str]) -> bool:
    text = text.lower()
    patterns = [r'\b' + re.escape(word.lower()) + r'\b' for word in word_list]
    return any(re.search(pattern, text) for pattern in patterns)

def detect_patterns(df, patterns, column="text"):
    """Vectorized pattern detection using combined regex patterns."""
    def create_combined_pattern(word_list):
        escaped_words = [re.escape(word.lower()) for word in word_list]
        return r'\b(?:' + '|'.join(escaped_words) + r')\b'
    
    for pattern_type, word_list in patterns.items():
        pattern = create_combined_pattern(word_list)
        df[pattern_type.name] = df[column].str.lower().str.contains(pattern, regex=True)
    
    return df

def detect_pattern(text: str, all_words_in_pattern: set):
    """
    Detect if the text matches phrases from the new pattern.
    """
    for phrase in all_words_in_pattern:
        if re.search(r'\b' + re.escape(phrase) + r'\b', text, re.IGNORECASE):
            return True
    return False

def find_substring_index_in_string(text: str, substring: str): 
    return text.split().index(substring)

## Use this to match anything that has a sponsor
def detect_pattern_with_keyword(keyword: str , text: str , all_words_in_pattern: set) -> bool:
    pattern = r'\b(?:' + '|'.join(re.escape(word) for word in all_words_in_pattern) + r')\b'
    if keyword in text.lower():
        matches = re.findall(pattern, text, re.IGNORECASE)
        return 1 if matches else 0
    return 0


### Heuristic on when is it mentioned the sponsor relative to the total length of the caption
def find_username_position(row):
    words = row["text"].split()
    username = row["sponsor_username"]
    for i, word in enumerate(words, start=1):
        if pd.notna(username) and username in word:
            return i + 1
    return 0 

def ellipsis(text):
    return 1 if re.search(r"\.{3}", text) else 0