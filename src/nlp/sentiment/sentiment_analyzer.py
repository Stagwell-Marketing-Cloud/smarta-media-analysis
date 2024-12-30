## sentiment analysis 
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def get_polarity_score(text: str): 
    analyzer = SentimentIntensityAnalyzer()
    return analyzer.polarity_scores(text)

def process_sentiment_score(sentiment_output) -> str: 
    """we get the max from the keys: 'neg', 'neu', 'pos'"""
    max_sent = max(sentiment_output, key=sentiment_output.get)
    if max_sent == 'neg': 
        return 'negative'
    elif max_sent == 'neu':
        return 'neutral'
    else:
        return 'positive'

def get_sentiment(text) -> str:
    return process_sentiment_score(get_polarity_score(text))