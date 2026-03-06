import matplotlib.pyplot as plt 
from wordcloud import WordCloud, STOPWORDS 
import nltk 
import string 
from nltk.corpus import stopwords 
from collections import Counter 
import numpy as np 
from PIL import Image 
 
 
nltk.download('stopwords') 
 
def preprocess_text(text): 
    text = text.lower() 
    text = text.translate(str.maketrans('', '', string.punctuation)) 
    stop_words = set(stopwords.words('english')) 
    words = text.split() 
    filtered_words = [word for word in words if word not in stop_words] 
    return filtered_words 
 
def show_top_keywords(words, n=10): 
    counter = Counter(words) 
    most_common = counter.most_common(n) 
 
    print("\nTop Keywords:") 
    for word, freq in most_common: 
        print(f"{word} : {freq}") 
 
def generate_wordcloud(text): 
    wordcloud = WordCloud( 
        width=800, 
        height=400, 
        background_color='white', 
        colormap='viridis' 
    ).generate(text) 
 
    plt.figure(figsize=(10,5)) 
    plt.imshow(wordcloud, interpolation='bilinear') 
    plt.axis('off') 
    plt.title("Standard Word Cloud") 
    plt.show() 
 
def generate_shaped_wordcloud(text): 
    # Create circular mask 
    x, y = np.ogrid[:500, :500] 
    mask = (x - 250) ** 2 + (y - 250) ** 2 > 240**2 
    mask = 255 * mask.astype(int) 
 
    wordcloud = WordCloud( 
        width=500, 
        height=500, 
        background_color='black', 
        mask=mask, 
 

        colormap='plasma' 
    ).generate(text) 
 
    plt.figure(figsize=(6,6)) 
    plt.imshow(wordcloud, interpolation='bilinear') 
    plt.axis('off') 
    plt.title("Styled Word Cloud (Circle Shape)") 
    plt.show() 
 
def main(): 
    print("=== Word Cloud Generator ===") 
    user_text = input("Enter your text:\n") 
 
    words = preprocess_text(user_text) 
    cleaned_text = " ".join(words) 
 
    show_top_keywords(words) 
    generate_wordcloud(cleaned_text) 
    generate_shaped_wordcloud(cleaned_text) 
 
if __name__ == "__main__": 
    main()