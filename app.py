from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# simple dataset
data = [
    {
        "context": "Document intelligence systems use OCR to extract text.",
        "question": "What is OCR?",
        "answer": "OCR extracts text from scanned documents."
    },
    {
        "context": "RAG combines retrieval and generation.",
        "question": "Why is RAG used?",
        "answer": "To improve accuracy using external data."
    },
    {
        "context": "Vector databases store embeddings.",
        "question": "What is a vector database?",
        "answer": "It stores embeddings for similarity search."
    }
]

class Query(BaseModel):
    question: str

# simple retrieval (keyword match)
def retrieve(query):
    for item in data:
        if query.lower() in item["question"].lower():
            return item
    return None

@app.post("/ask")
def ask(query: Query):
    result = retrieve(query.question)
    if result:
        return {
            "question": query.question,
            "answer": result["answer"],
            "context": result["context"]
        }
    return {"message": "No relevant answer found"}
