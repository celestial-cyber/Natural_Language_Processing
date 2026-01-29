# Lemmatization: turns words into dictionary base forms (lemmas)
# cats ran -> cat run

import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Download required resources
nltk.download('punkt', quiet=True)
nltk.download('wordnet', quiet=True)
nltk.download('omw-1.4', quiet=True)

# User input
user_input = input("Enter the sentence: ")

# Tokenize and clean
tokens = [w for w in word_tokenize(user_input.lower()) if w.isalpha()]

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

# Lemmatize words
lemmatized = [lemmatizer.lemmatize(w) for w in tokens]

# Output
print("Original:", tokens)
print("Lemmatized Sentence:", " ".join(lemmatized))
