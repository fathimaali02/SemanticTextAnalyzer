import re
import nltk

nltk.download("punkt")

def clean_text(text: str):
    text = text.lower()
    text = re.sub(r"[^\w\s]", " ", text)
    return text

def split_sentences(text: str):
    from nltk.tokenize import sent_tokenize
    return sent_tokenize(text)

def lexical_diversity(text: str):
    words = text.split()
    return len(set(words)) / max(len(words), 1)
