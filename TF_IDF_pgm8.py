#!/usr/bin/env python3
"""
AIM:
This program implements TF-IDF (Term Frequency-Inverse Document Frequency) algorithm 
to measure word importance across multiple documents. It helps identify how relevant 
a specific word is within one document compared to the entire collection.

THEORY:
TF-IDF is a numerical statistic used in information retrieval and text mining. 
TF (Term Frequency) measures how frequently a word appears in a document. 
IDF (Inverse Document Frequency) reduces the weight of commonly occurring words 
and increases the weight of rare words across documents. The TF-IDF score = TF × IDF.
Higher scores indicate words that are both frequent in a specific document AND rare 
in the overall collection - making them more distinctive/important.

ALGORITHM:
1. Preprocess text: lowercase, remove punctuation, split into words
2. Compute TF(word, doc) = (word count in doc) / (total words in doc)
3. Compute IDF(word, docs) = log(total_docs / docs_containing_word)
4. Compute TF-IDF = TF × IDF for target word in target document
5. User inputs documents, target word, and document index for calculation
"""

import math
import string

def preprocess(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text.split()

def compute_tf(word, document):
    words = preprocess(document)
    return words.count(word.lower()) / len(words) if len(words) > 0 else 0

def compute_idf(word, documents):
    num_docs = len(documents)
    docs_with_word = 0
   
    for doc in documents:
        words = preprocess(doc)
        if word.lower() in words:
            docs_with_word += 1
   
    if docs_with_word == 0:
        return 0
   
    return math.log(num_docs / docs_with_word)

def compute_tfidf(word, document, documents):
    tf = compute_tf(word, document)
    idf = compute_idf(word, documents)
    return tf * idf

# ----------- USER INPUT SECTION -----------

n = int(input("Enter number of documents: "))
documents = []

for i in range(n):
    doc = input(f"Enter document {i+1}: ")
    documents.append(doc)

word = input("Enter word to compute TF-IDF: ")
doc_index = int(input(f"Enter document number (1 to {n}): ")) - 1

# ----------- CALCULATION -----------

tfidf_score = compute_tfidf(word, documents[doc_index], documents)

# ----------- OUTPUT -----------

print("\nResults:")
print("TF-IDF score of '{}' in document {} is: {:.6f}".format(
    word, doc_index + 1, tfidf_score))

"""
EXPECTED OUTPUT:
Enter number of documents: 3
Enter document 1: Data science is amazing
Enter document 2: Machine learning is part of data science
Enter document 3: Artificial intelligence and machine learning
Enter word to compute TF-IDF: learning
Enter document number (1 to 3): 2

Results:
TF-IDF score of 'learning' in document 2 is: 0.057924

CALCULATION BREAKDOWN:
Document 2: "Machine learning is part of data science" → 8 words total
TF("learning") = 1/8 = 0.125
IDF("learning") = log(3/2) = log(1.5) ≈ 0.405465
TF-IDF = 0.125 × 0.405465 ≈ 0.057924 ✓
"""
