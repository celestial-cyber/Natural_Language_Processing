import nltk 
import string 
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
from gensim import corpora 
from gensim.models import LdaModel 
 
# Download required NLTK data 
nltk.download('punkt') 
nltk.download('punkt_tab') 
nltk.download('stopwords') 
 
def preprocess_text(text): 
    text = text.lower() 
    words = word_tokenize(text) 
    stop_words = set(stopwords.words('english')) 
     
    words = [ 
        word for word in words 
        if word.isalpha() and word not in stop_words 
    ] 
     
    return words 
 
def main(): 
    print("=== Topic Modelling using LDA ===") 
     
    n = int(input("Enter number of documents: ")) 
    documents = [] 
     
    for i in range(n): 
        text = input(f"\nEnter document {i+1}:\n") 
        documents.append(preprocess_text(text)) 
     
    # Create Dictionary 
    dictionary = corpora.Dictionary(documents) 
     
    # Create Document-Term Matrix 
    corpus = [dictionary.doc2bow(doc) for doc in documents] 
     
    # Train LDA Model 
    lda_model = LdaModel( 
        corpus=corpus, 
        id2word=dictionary, 
        num_topics=2, 
        random_state=42, 
        passes=10 
 
Page | 29  
 
    ) 
     
    print("\nGenerated Topics:\n") 
     
    topics = lda_model.print_topics(num_words=5) 
    for topic in topics: 
        print(topic) 
 
if __name__ == "__main__": 
    main()