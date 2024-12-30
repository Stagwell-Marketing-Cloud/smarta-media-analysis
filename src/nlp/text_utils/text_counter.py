import re

import pandas as pd

def findall_counter(text: str, all_words_in_pattern: set) -> int:
    """
    Count how many times any of the words in the pattern appear in the text.
    
    Parameters:
        text (str): The input text to search within.
        all_words_in_pattern (set): A set of words/phrases to search for.
    
    Returns:
        int: Total count of matches.
    """
    # Combine words into a single regex pattern
    pattern = r'\b(?:' + '|'.join(re.escape(word) for word in all_words_in_pattern) + r')\b'
    
    # Find all matches
    matches = re.findall(pattern, text, re.IGNORECASE)
    
    # Return the total count of matches
    return len(matches)

def count_words_from_list(text: str, all_words_in_pattern: set) -> int:
    """
    Count how many times any of the words in the pattern appear in the text.
    
    Parameters:
        text (str): The input text to search within.
        all_words_in_pattern (set): A set of words/phrases to search for.
    
    Returns:
        int: Total count of matches.
    """
    # Combine words into a single regex pattern
    pattern = r'\b(?:' + '|'.join(re.escape(word) for word in all_words_in_pattern) + r')\b'
    
    # Find all matches
    matches = re.findall(pattern, text, re.IGNORECASE)
    
    # Return the total count of matches
    return len(matches)


## move this one to a general text utility 
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

def get_text_length(text: str) -> int: 
    """returns the number of words delimited by a single blank space"""
    return len(text.split())

# Paid Partnership
def paid_partnership(row):
    return 1 if pd.notna(row["sponsor_username"]) and row["standalone_ad_count"] == 0 and \
    row["hashtag_ad_count"] == 0 else 0
