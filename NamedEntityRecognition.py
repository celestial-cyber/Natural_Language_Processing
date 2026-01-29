# Import required libraries 
from sklearn.feature_extraction.text import CountVectorizer 
import string 
 
# Step 1: Take multiple sentences as input from the user 
print("Enter multiple sentences (type 'STOP' to end input):") 
documents = [] 
while True: 
    text = input() 
    if text.strip().upper() == 'STOP': 
        break 
    documents.append(text) 
 
# Step 2: Preprocess the text 
def preprocess(text): 
    # Convert to lowercase 
    text = text.lower() 
    # Remove punctuation 
    text = text.translate(str.maketrans('', '', string.punctuation)) 
    return text 
 
processed_docs = [preprocess(doc) for doc in documents] 
 
# Step 3: Create Bag of Words model with stop words removal 
vectorizer = CountVectorizer(stop_words='english')  # removes common English stop words 
X = vectorizer.fit_transform(processed_docs) 
 
# Step 4: Display vocabulary (feature names) 
print("\nVocabulary (Feature Names):") 
print(vectorizer.get_feature_names_out()) 
 
# Step 5: Display Bag of Words vectors 
print("\nBag of Words Vectors:") 
# Display each vector with corresponding sentence 
for i, vec in enumerate(X.toarray()): 
    print(f"Sentence {i+1}: {vec}") 
 
 
 
# Optional: Display in a table format 
import pandas as pd 
df = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out()) 
print("\nBag of Words Table:") 
print(df)