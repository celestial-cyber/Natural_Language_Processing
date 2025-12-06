import nltk 
from nltk.sentiment.vader import SentimentIntensityAnalyzer 

#nltk.download('vader_lexicon')

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

text = "I absolutely love the product! It has changed my life for better"
result = analyze_sentiment(text)
print(f"The Sentiment of the text is:{result}")

text1 = "This is the worst experince I ever had with a product"
result2 = analyze_sentiment(text1)
print(f"The Sentiment of the text is:{result2}")

text3 = "The Product is neither good or bad"
result3 = analyze_sentiment(text3)
print(f"The Sentiment of the text is:{result3}")


        