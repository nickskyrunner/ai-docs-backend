import chromadb
from chromadb.config import Settings

client = chromadb.Client(Settings(
    chroma_db_impl="duckdb+parquet",
    persist_directory="./data/chroma"
))

collection = client.get_or_create_collection("documents")

def add_document(doc_id: str, text: str):
    collection.add(
        documents=[text],
        ids=[doc_id],
        metadatas=[{"source": "pdf"}]
    )

def query_similar_documents(query: str, n_results: int = 3):
    results = collection.query(
        query_texts=[query],
        n_results=n_results
    )
    return results['documents'][0]