from sklearn.feature_extraction.text import CountVectorizer
print("Bag of words")

print("Enter multiple sentences type done when finished")

documents=[]
while True:
    text=input("Enter a sentence")
    if text.lower()=="done":
        break
    if text.strip():
        documents.append(text)
if not documents:
    print("No input provided existing")
    exit()

vectorizer=CountVectorizer()
bar_matrix = vectorizer.fit_transform(documents)
print("Vocabulary")

print("Bag of Words Matrix")
print(bar_matrix.toarrays())

print("Each Row corresponds to a senetence you haev enetered")
print("Each column corresponds to a word in a vocabulary")
