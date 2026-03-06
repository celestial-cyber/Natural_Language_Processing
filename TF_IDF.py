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
 
Page | 18  
 
 
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