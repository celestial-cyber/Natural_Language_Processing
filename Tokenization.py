import re 
# 1. Whitespace Tokenization 
def whitespace_tokenize(text): 
    return text.split() 
# 2. Simple Regex Tokenization (removes punctuation) 
def regex_simple_tokenize(text): 
    return re.findall(r"\b\w+\b", text) 
 
# 3. Advanced Regex Tokenization (keeps contractions & numbers) 
def regex_advanced_tokenize(text): 
    pattern = r"[A-Za-z]+(?:'[A-Za-z]+)?|\d+(?:\.\d+)?" 
    return re.findall(pattern, text) 
# 4. NLTK Tokenization 
def nltk_tokenize(text): 
    try: 
        import nltk 
        from nltk.tokenize import word_tokenize 
        nltk.download("punkt", quiet=True) 
        nltk.download("punkt_tab", quiet=True) 
        return word_tokenize(text) 
    except Exception as e: 
        return ["NLTK not available:", str(e)] 
 
# 5. SpaCy Tokenization 
def spacy_tokenize(text): 
    try: 
        import spacy 
        try: 
            nlp = spacy.load("en_core_web_sm") 
        except: 
            import os 
            os.system("python -m spacy download en_core_web_sm") 
            nlp = spacy.load("en_core_web_sm") 
        doc = nlp(text) 
        return [token.text for token in doc] 
    except Exception as e: 
        return ["SpaCy not available:", str(e)] 
 
# ---------------- MAIN PROGRAM ---------------- 
text = input("Enter text for tokenization: ") 
print("\n--- TOKENIZATION RESULTS ---") 
print("\n1. Whitespace Tokenization:") 
print(whitespace_tokenize(text)) 
print("\n2. Simple Regex Tokenization:") 
print(regex_simple_tokenize(text)) 
print("\n3. Advanced Regex Tokenization:") 
print(regex_advanced_tokenize(text)) 
print("\n4. NLTK Tokenization:") 
print(nltk_tokenize(text)) 
print("\n5. SpaCy Tokenization:") 
print(spacy_tokenize(text))

# Enter text for tokenization: The world is not enough !
# --- TOKENIZATION RESULTS ---
#
# 1. Whitespace Tokenization:
# ['The', 'world', 'is', 'not', 'enough', '!']
#
# 2. Simple Regex Tokenization:
# ['The', 'world', 'is', 'not', 'enough']
#
# 3. Advanced Regex Tokenization:
# ['The', 'world', 'is', 'not', 'enough']
#
# 4. NLTK Tokenization:
# ['The', 'world', 'is', 'not', 'enough', '!']
#
# 5. SpaCy Tokenization:
# ['The', 'world', 'is', 'not', 'enough', '!']
