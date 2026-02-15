import chromadb

client = chromadb.Client()
collection = client.get_or_create_collection("documents")

def add_sentences(ids, sentences, embeddings):
    collection.add(
        ids=ids,
        documents=sentences,
        embeddings=embeddings
    )

def search(query_embedding, k=5):
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=k
    )
    return results
