from chromadb import PersistentClient
from pathlib import Path

# Path for DB
ROOT = Path(__file__).resolve().parents[1]
CHROMA_DIR = ROOT / "db" / "chroma"

def get_chroma_client():
    """
    Returns a persistent Chroma client using modern API.
    """
    CHROMA_DIR.mkdir(parents=True, exist_ok=True)
    return PersistentClient(path=str(CHROMA_DIR))

def get_collection(name: str = "crimenet_cases"):
    """
    Create or load a Chroma collection (new API).
    """
    client = get_chroma_client()

    # New API: .get_or_create_collection()
    collection = client.get_or_create_collection(
        name=name,
        metadata={"hnsw:space": "cosine"}
    )
    return collection
