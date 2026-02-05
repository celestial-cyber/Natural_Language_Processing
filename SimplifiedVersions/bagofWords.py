from sklearn.feature_extraction.text import CountVectorizer

print("=== Bag of Words Encoder ===")
print("Enter multiple sentences. Type 'done' when finished.\n")

documents = []
while (text := input("Enter a sentence: ").strip().lower()) != "done":
    if text:
        documents.append(text)

if not documents:
    print("No input provided. Exiting.")
    exit()

vectorizer = CountVectorizer()
bow_matrix = vectorizer.fit_transform(documents)

print("\n=== Vocabulary ===")
print(vectorizer.vocabulary_)

print("\n=== Bag of Words Matrix ===")
print(bow_matrix.toarray())

print("\nEach row corresponds to one sentence you entered.")
print("Each column corresponds to a word in the vocabulary.")

# Output:
# === Bag of Words Encoder ===
# Enter multiple sentences. Type 'done' when finished.
# Enter a sentence: cats are cute
# Enter a sentence: dogs are loyal
# Enter a sentence: i love dogs
# Enter a sentence: done
#
# === Vocabulary ===
# {'cats': 1, 'are': 0, 'cute': 2, 'dogs': 3, 'loyal': 5, 'love': 4}
#
# === Bag of Words Matrix ===
# [[1 1 1 0 0 0]
#  [1 0 0 1 0 1]
#  [0 0 0 1 1 0]]
#
# Each row corresponds to one sentence you entered.
# Each column corresponds to a word in the vocabulary.
