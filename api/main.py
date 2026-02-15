from fastapi import FastAPI
from pydantic import BaseModel
import uuid

from core.preprocessing import clean_text, split_sentences
from core.embedding_engine import embed
from core.similarity import tfidf_similarity
from db.vector_store import add_sentences, search

app = FastAPI()

class TextInput(BaseModel):
    text: str


@app.post("/index")
def index_text(data: TextInput):
    text = clean_text(data.text)
    sentences = split_sentences(text)

    ids = [str(uuid.uuid4()) for _ in sentences]
    embeddings = embed(sentences)

    add_sentences(ids, sentences, embeddings)
    return {"indexed": len(sentences)}


@app.post("/check")
def check_plagiarism(data: TextInput):
    text = clean_text(data.text)
    sentences = split_sentences(text)
    embeddings = embed(sentences)

    results = []

    for s, e in zip(sentences, embeddings):
        vec_hits = search(e)

        corpus = []
        if vec_hits and "documents" in vec_hits:
            docs = vec_hits.get("documents")
            if docs and len(docs) > 0:
                corpus = docs[0]

        tfidf_scores = tfidf_similarity(s, corpus)

        results.append({
            "sentence": s,
            "semantic_matches": corpus,
            "lexical_scores": tfidf_scores
        })

    avg_tfidf = 0
    count = 0
    for r in results:
        if r["lexical_scores"]:
            avg_tfidf += max(r["lexical_scores"])
            count += 1

    avg_tfidf = avg_tfidf / count if count > 0 else 0

    if avg_tfidf > 0.75:
        similarity_result = "High textual similarity"
    elif avg_tfidf > 0.4:
        similarity_result = "Moderate similarity"
    else:
        similarity_result = "Low similarity"

    summary = {
        "similarity_result": similarity_result,
        "ai_interpretation": "AI detection temporarily disabled"
    }

    return {
        "summary": summary,
        "results": results
    }
