import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download required resource (run once)
nltk.download('vader_lexicon')

def get_sentiment_label(compound, pos_th=0.05, neg_th=-0.05):
    if compound >= pos_th:
        return "Positive"
    elif compound <= neg_th:
        return "Negative"
    return "Neutral"

def analyze_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    scores = sia.polarity_scores(text)
    label = get_sentiment_label(scores["compound"])

    print("Input text:")
    print(text)
    print("\nVADER scores:", scores)
    print("Overall Sentiment:", label)

    return label, scores

if __name__ == "__main__":
    user_text = input("Enter a sentence, comment, or review: ")
    analyze_sentiment(user_text)

# Output:
# Enter a sentence, comment, or review: The ambiance here is always inviting and comfortable
#
# Input text:
# The ambiance here is always inviting and comfortable
#
# VADER scores: {'neg': 0.0, 'neu': 0.517, 'pos': 0.483, 'compound': 0.6808}
# Overall Sentiment: Positive
