from fastapi import FastAPI
from pydantic import BaseModel
from scraper.scraper import fetch_and_extract_documents
from ai.openai_client import ask_openai
from ai.vector_store import add_document, query_similar_documents

app = FastAPI()

class UserQuery(BaseModel):
    question: str

@app.post("/load-doc")
async def load_doc():
    docs = fetch_and_extract_documents()
    add_document("modulo-contributo", docs)
    return {"message": "Documento aggiunto al vector store"}

@app.post("/ask")
async def ask_ai(query: UserQuery):
    docs = query_similar_documents(query.question)
    response = ask_openai(query.question, "\n".join(docs))
    return {"answer": response}