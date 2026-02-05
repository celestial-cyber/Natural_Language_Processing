import re

def tokenize_text(text):
    return re.findall(r'\d+|[a-zA-Z]+|[^\w\s]', text)

def classify_token(token):
    return "Word" if token.isalpha() else "Number" if token.isdigit() else "Symbol"

text = """
Tokenization is a key step in NLP!
Python 3 is widely used in AI, ML, and data science.
In 2025, more than 70% developers use Python.
"""

tokens = tokenize_text(text)

print("Original Text:")
print(text)

print("\nTokens with Serial Numbers:")
print("-" * 35)

for i, token in enumerate(tokens, 1):
    print(f"{i:2}. {token:<12} ({classify_token(token)})")

# Output:
# Original Text:
#
# Tokenization is a key step in NLP!
# Python 3 is widely used in AI, ML, and data science.
# In 2025, more than 70% developers use Python.
#
# Tokens with Serial Numbers:
# -----------------------------------
#  1. Tokenization (Word)
#  2. is           (Word)
#  3. a            (Word)
#  4. key          (Word)
#  5. step         (Word)
#  6. in           (Word)
#  7. NLP          (Word)
#  8. !            (Symbol)
#  9. Python       (Word)
# 10. 3            (Number)
# 11. is           (Word)
# 12. widely       (Word)
# 13. used         (Word)
# 14. in           (Word)
# 15. AI           (Word)
# 16. ,            (Symbol)
# 17. ML           (Word)
# 18. ,            (Symbol)
# 19. and          (Word)
# 20. data         (Word)
# 21. science      (Word)
# 22. .            (Symbol)
# 23. In           (Word)
# 24. 2025         (Number)
# 25. ,            (Symbol)
# 26. more         (Word)
# 27. than         (Word)
# 28. 70           (Number)
# 29. %            (Symbol)
# 30. developers   (Word)
# 31. use          (Word)
# 32. Python       (Word)
# 33. .            (Symbol)
