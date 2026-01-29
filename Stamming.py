## stamming -> strips suffix -> cats running -> cat run
import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize 
nltk.download ('punkt', quiet = True)
user_input = input("Enter the sentence")
tokens = [w for w in word_tokenize(user_input.lower()) if w.isalpha()]

stemmer = PorterStemmer()

stemmed = [stemmer.stem(w) for w in tokens]

print("Original", tokens)
print("Stemmed Sentence".join(stemmed))