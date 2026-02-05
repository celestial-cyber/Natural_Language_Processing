import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer

# Download required resources
for pkg in ["wordnet", "omw-1.4", "punkt"]:
    nltk.download(pkg)

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

def normalize_text(sentence):
    words = nltk.word_tokenize(sentence)
    stemmed = [stemmer.stem(w) for w in words]
    lemmatized = [lemmatizer.lemmatize(w) for w in words]
    return words, stemmed, lemmatized

text = input("Enter a sentence: ")

original, stemmed_words, lemmatized_words = normalize_text(text)

print("\nOriginal Words:", original)
print("Stemmed Words:", stemmed_words)
print("Lemmatized Words:", lemmatized_words)

# Output:
# Enter a sentence: The student is studying, and the students are studying hard.
# Original Words: ['The', 'student', 'is', 'studying', ',', 'and', 'the', 'students', 'are', 'studying', 'hard', '.']
# Stemmed Words: ['the', 'student', 'is', 'studi', ',', 'and', 'the', 'student', 'are', 'studi', 'hard', '.']
# Lemmatized Words: ['The', 'student', 'is', 'studying', ',', 'and', 'the', 'student', 'are', 'studying', 'hard', '.']
