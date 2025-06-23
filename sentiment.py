from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk


nltk.download("vader_lexicon")


sia = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
  
    scores = sia.polarity_scores(text)
    compound = scores['compound']

    if compound >= 0.05:
        label = 'positive'
    elif compound <= -0.05:
        label = 'negative'
    else:
        label = 'neutral'

    return label, compound


if __name__ == "__main__":
    examples = [
        "I love McDonald's fries!",
        "Their new menu sucks.",
        "It's okay, just average.",
        "McDonald's is overpriced now.",
        "Best fast food breakfast!"
    ]

    for text in examples:
        label, score = analyze_sentiment(text)
        print(f"Text: {text}\n → Sentiment: {label} (score={score})\n")
