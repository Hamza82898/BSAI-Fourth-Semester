import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

sia = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    scores = sia.polarity_scores(text)
    compound = scores['compound']

    if compound > 0.05:
        sentiment, emoji = 'Positive', '😊'
    elif compound < -0.05:
        sentiment, emoji = 'Negative', '😢'
    else:
        sentiment, emoji = 'Neutral', '😐'


    confidence = abs(compound)
    return sentiment, emoji, f"{confidence:.2f}"
