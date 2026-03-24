import nltk 
from nltk.tokenize import sent_tokenize, word_tokenize 
from gensim.models import Word2Vec 
import string 
 
# Download tokenizer data 
nltk.download('punkt') 
 
def preprocess_text(text): 
    text = text.lower() 
    sentences = sent_tokenize(text) 
     
    processed_data = [] 
     
    for sentence in sentences: 
        words = word_tokenize(sentence) 
        words = [word for word in words if word.isalpha()]  # remove punctuation 
 
Page | 26  
 
        processed_data.append(words) 
         
    return processed_data 
 
def main(): 
    print("=== Word Embedding using Word2Vec ===") 
     
    user_text = input("Enter your text:\n") 
     
    # Preprocess text 
    data = preprocess_text(user_text) 
     
    # Train Word2Vec model 
    model = Word2Vec( 
        sentences=data, 
        vector_size=100, 
        window=5, 
        min_count=1, 
        workers=4 
    ) 
     
    print("\nVocabulary Words:") 
    print(list(model.wv.index_to_key)) 
     
    # Ask user for a word 
    word = input("\nEnter a word to find similar words:\n").lower() 
     
    if word in model.wv: 
        print("\nTop 5 Similar Words:") 
        similar_words = model.wv.most_similar(word, topn=5) 
         
        for similar_word, similarity in similar_words: 
            print(f"{similar_word} : {similarity:.4f}") 
    else: 
        print("Word not found in vocabulary.") 
         
if __name__ == "__main__": 
    main()