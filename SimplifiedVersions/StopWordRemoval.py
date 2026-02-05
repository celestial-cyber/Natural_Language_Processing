import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter

# Download required resources (run once)
for pkg in ["punkt", "stopwords"]:
    nltk.download(pkg)

text = input("Enter your text:\n")

tokens = word_tokenize(text)
print("\nOriginal Tokens:")
print(tokens)

print("\n" + "-" * 50 + "\n")

stop_words = set(stopwords.words("english"))

filtered_tokens = [
    w for w in tokens if w.isalpha() and w.lower() not in stop_words
]

print("Tokens after Stop Words Removal:")
print(filtered_tokens)

print("\n" + "-" * 50 + "\n")

word_freq = Counter(filtered_tokens)
print("Word Frequency:")
for word, freq in word_freq.items():
    print(f"{word}: {freq}")

# Output:
# Enter your text:
# A friend should bear his friend's infirmities
#
# Original Tokens:
# ['A', 'friend', 'should', 'bear', 'his', 'friend', "'s", 'infirmities']
#
# --------------------------------------------------
#
# Tokens after Stop Words Removal:
# ['friend', 'bear', 'friend', 'infirmities']
#
# --------------------------------------------------
#
# Word Frequency:
# friend: 2
# bear: 1
# infirmities: 1
