# app.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from rag_query import query_rag

app = FastAPI(title="CRIMENET AI - Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"status": "ok", "service": "CRIMENET AI Backend"}


@app.get("/search")
def search(q: str, k: int = 3):
    """
    Simple GET endpoint for quick queries:
    Example: /search?q=ATM+theft&k=3
    """
    result = query_rag(q, k=k)
    return {"query": q, "k": k, "result": result}
