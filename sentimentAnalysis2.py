import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Uncomment this only once to download the lexicon
# nltk.download('vader_lexicon')

def analyze_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    sentiment = sia.polarity_scores(text)

    compound_score = sentiment['compound']
    if compound_score >= 0.5:
        return "positive"
    elif compound_score <= -0.5:
        return "negative"
    else:
        return "neutral"

print("Sentiment Analyzer is ready!")
print("Type 'exit' to stop.\n")

while True:
    user_input = input("Enter text: ")

    if user_input.lower() == "exit":
        print("Program terminated.")
        break

    result = analyze_sentiment(user_input)
    print(f"The sentiment of the text is: {result}\n")
