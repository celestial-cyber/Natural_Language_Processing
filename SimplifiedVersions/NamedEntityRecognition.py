from sklearn.feature_extraction.text import CountVectorizer
import string
import pandas as pd

print("Enter multiple sentences (type 'STOP' to end input):")

documents = []
while True:
    text = input()
    if text.strip().upper() == "STOP":
        break
    documents.append(text)

def preprocess(text):
    return text.lower().translate(str.maketrans("", "", string.punctuation))

processed_docs = [preprocess(doc) for doc in documents]

vectorizer = CountVectorizer(stop_words="english")
X = vectorizer.fit_transform(processed_docs)

print("\nVocabulary (Feature Names):")
print(vectorizer.get_feature_names_out())

print("\nBag of Words Vectors:")
for i, vec in enumerate(X.toarray(), 1):
    print(f"Sentence {i}: {vec}")

df = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out())
print("\nBag of Words Table:")
print(df)

# Output:
# Enter multiple sentences (type 'STOP' to end input):
# I love Python programming.
# Python is great for AI!
# I love AI.
# stop
#
# Vocabulary (Feature Names):
# ['ai' 'great' 'love' 'programming' 'python']
#
# Bag of Words Vectors:
# Sentence 1: [0 0 1 1 1]
# Sentence 2: [1 1 0 0 1]
# Sentence 3: [1 0 1 0 0]
#
# Bag of Words Table:
#    ai  great  love  programming  python
# 0   0      0     1            1       1
# 1   1      1     0            0       1
# 2   1      0     1            0       0
