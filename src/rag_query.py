# src/rag_query.py

import json
from sentence_transformers import SentenceTransformer
from chroma_client import get_collection


# ---------------------------------------------------------
# 1. Retrieve similar documents from Chroma
# ---------------------------------------------------------
def retrieve_similar(query: str, k: int = 3):
    model = SentenceTransformer("all-MiniLM-L6-v2")

    # Encode query
    q_emb = model.encode([query], convert_to_numpy=True)[0]

    col = get_collection()

    # Query Chroma (latest API)
    res = col.query(
        query_embeddings=[q_emb],
        n_results=k,
        include=["documents", "metadatas", "distances"]     # <-- FIXED
    )

    docs = res["documents"][0]
    metas = res["metadatas"][0]
    distances = res["distances"][0]

    # IDs stored inside metadata
    ids = [m.get("doc_id") for m in metas]

    results = []
    for i in range(len(docs)):
        results.append({
            "id": ids[i],
            "text": docs[i],
            "meta": metas[i],
            "distance": distances[i]
        })

    return results


# ---------------------------------------------------------
# 2. Create final RAG response (retrieval only)
# ---------------------------------------------------------
def query_rag(query: str, k: int = 3):
    retrieved = retrieve_similar(query, k)

    return {
        "query": query,
        "results": retrieved,
        "count": len(retrieved)
    }


# ---------------------------------------------------------
# 3. Run standalone mode for testing
# ---------------------------------------------------------
if __name__ == "__main__":
    print("CrimeNet RAG Search")
    print("Type your question. Example: Show me all theft cases.\n")

    while True:
        q = input("Query: ").strip()
        if not q:
            print("Goodbye!")
            break

        result = query_rag(q, k=3)
        print(json.dumps(result, indent=2, ensure_ascii=False))
        print("\n----------------------------------------\n")
