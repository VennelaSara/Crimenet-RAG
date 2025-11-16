# embed.py
from sentence_transformers import SentenceTransformer
from pathlib import Path
import json
from chroma_client import get_collection

ROOT = Path(__file__).resolve().parents[1]
PROCESSED = ROOT / "data" / "processed"
MODEL_NAME = "all-MiniLM-L6-v2"   # lightweight CPU-friendly

def load_processed_docs():
    docs = []
    for fp in PROCESSED.glob("*.json"):
        docs.append(json.loads(fp.read_text(encoding="utf8")))
    return docs

def main():
    docs = load_processed_docs()
    if not docs:
        print("No processed docs found — run ingest.py first.")
        return

    print(f"Loading embedding model: {MODEL_NAME}")
    model = SentenceTransformer(MODEL_NAME)

    col = get_collection()

    texts = [d["text"] for d in docs]
    ids = [d["id"] for d in docs]
    metadatas = [{"source": d.get("source"), "type": d.get("type")} for d in docs]

    print(f"Computing embeddings for {len(texts)} documents (this may take a moment)...")
    embs = model.encode(texts, show_progress_bar=True, convert_to_numpy=True)

    # Upsert into Chroma
    col.add(documents=texts, metadatas=metadatas, ids=ids, embeddings=embs.tolist())
    print("Embeddings written to Chroma collection.")

if __name__ == "__main__":
    main()
