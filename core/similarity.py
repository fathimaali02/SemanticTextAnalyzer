from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def tfidf_similarity(query, corpus):
    if not corpus:
        return []

    vect = TfidfVectorizer()
    tfidf = vect.fit_transform([query] + corpus)
    scores = cosine_similarity(tfidf[0:1], tfidf[1:]).flatten()
    return scores.tolist()
