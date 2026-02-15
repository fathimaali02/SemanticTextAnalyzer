from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def embed(sentences):
    return model.encode(sentences).tolist()
