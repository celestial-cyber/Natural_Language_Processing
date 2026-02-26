#!/usr/bin/env python3
"""
Program 7: Term Frequency – Inverse Document Frequency

AIM:
To write a Python program to calculate Term Frequency – Inverse Document Frequency 
(TF-IDF) for a set of documents given by the user and determine the importance of 
each word in the documents.

ALGORITHM:
1. Start the program.
2. Input the number of documents from the user.
3. Accept each document as input.
4. Split each document into words.
5. Count total words in each document.
6. Calculate Term Frequency (TF) for each word in each document:
   TF = (Number of occurrences of word in document) / (Total words in document)
7. Calculate Inverse Document Frequency (IDF) for each word:
   IDF = log(Total number of documents / Number of documents containing the word)
8. Display TF-IDF values for each word in every document.
9. Stop the program.
"""

import math
from collections import Counter

# Function to calculate TF
def calculate_tf(word_counts, total_words):
    tf_dict = {}
    for word, count in word_counts.items():
        tf_dict[word] = count / total_words
    return tf_dict

# Function to calculate IDF
def calculate_idf(documents):
    N = len(documents)
    idf_dict = {}
    all_words = set()
    for doc in documents:
        all_words.update(doc)
    for word in all_words:
        containing_docs = sum(1 for doc in documents if word in doc)
        idf_dict[word] = math.log(N / (1 + containing_docs)) + 1
    return idf_dict

# Function to calculate TF-IDF
def calculate_tfidf(tf, idf):
    tfidf = {}
    for word, val in tf.items():
        tfidf[word] = val * idf.get(word, 0)
    return tfidf

# --- User Input ---
num_docs = int(input("Enter number of documents: "))
documents = []
for i in range(num_docs):
    text = input(f"Enter document {i+1}: ").lower()
    words = text.split()
    documents.append(words)

# --- Processing ---
word_counts_list = []
tf_list = []
for doc in documents:
    word_count = Counter(doc)
    word_counts_list.append(word_count)
    tf = calculate_tf(word_count, len(doc))
    tf_list.append(tf)

idf = calculate_idf(documents)

# --- Output ---
for i, tf in enumerate(tf_list):
    tfidf = calculate_tfidf(tf, idf)
    print(f"\nTF-IDF for Document {i+1}:")
    for word, score in tfidf.items():
        print(f"{word}: {score:.4f}")

"""
EXPECTED OUTPUT:
Enter number of documents: 2
Enter document 1: NLP is fun
Enter document 2: NLP is powerful

TF-IDF for Document 1:
nlp: 0.1982
is: 0.1982
fun: 0.3333

TF-IDF for Document 2:
nlp: 0.1982
is: 0.1982
powerful: 0.3333

CALCULATION BREAKDOWN:
N = 2 documents
IDF("nlp") = log(2/(1+2)) + 1 = log(2/3) + 1 ≈ 0.1982
IDF("fun") = log(2/(1+1)) + 1 = log(1) + 1 = 1.0
TF("fun" in doc1) = 1/3 ≈ 0.3333
TF-IDF("fun") = 0.3333 × 1.0 = 0.3333 ✓
"""
