import re
from Levenshtein import ratio

def get_first_sentence(text):
    """
    Extract the first sentence from a given text.

    Args:
    - text (str): The input text.

    Returns:
    - str: The first sentence.
    """
    sentences = re.split(r'(?<=[.!?]) +', text.strip())
    return sentences[0] if sentences else ""

def get_last_sentence(text):
    """
    Extract the last sentence from a given text.

    Args:
    - text (str): The input text.

    Returns:
    - str: The last sentence.
    """
    sentences = re.split(r'(?<=[.!?]) +', text.strip())
    return sentences[-1] if sentences else ""

def compare_sentences(first_sentence, last_sentence, threshold=0.85, return_similarity: bool = False):
    """
    Compare two sentences using Levenshtein similarity ratio.

    Args:
    - first_sentence (str): The first sentence.
    - last_sentence (str): The last sentence.
    - threshold (float): Similarity threshold to consider sentences as "same."

    Returns:
    - bool: True if the sentences are similar enough, False otherwise.
    - float: Similarity score.
    """
    first = first_sentence.strip().lower()
    last = last_sentence.strip().lower()
    ## levenshtein 
    similarity = ratio(first, last)
    if return_similarity: 
        return similarity >= threshold, similarity
    else: 
        return similarity >= threshold

def compare_first_and_last_sentence(text: str, threshold: float) -> bool: 
    first_sentence = get_first_sentence(text)
    last_sentence = get_last_sentence(text)
    return compare_sentences(first_sentence=first_sentence, last_sentence=last_sentence, threshold = threshold)