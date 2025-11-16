# ingest.py
from pathlib import Path
import json
from utils import clean_text, safe_id

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
PROCESSED = ROOT / "data" / "processed"
PROCESSED.mkdir(parents=True, exist_ok=True)

def process_txt(fp: Path) -> dict:
    raw = fp.read_text(encoding="utf8", errors="ignore")
    return {
        "id": safe_id(fp.stem),
        "source": str(fp),
        "text": clean_text(raw),
        "type": "txt"
    }

def process_json(fp: Path) -> dict:
    raw_data = json.loads(fp.read_text(encoding="utf8"))
    # flatten / stringify JSON content for RAG text
    text = json.dumps(raw_data, ensure_ascii=False)
    # pick id from known keys or fallback to filename
    doc_id = raw_data.get("id") or raw_data.get("case_id") or fp.stem
    return {
        "id": safe_id(doc_id),
        "source": str(fp),
        "text": clean_text(text),
        "type": "json"
    }

def load_raw_docs():
    docs = []
    for fp in RAW.glob("*"):
        if fp.suffix.lower() == ".txt":
            docs.append(process_txt(fp))
        elif fp.suffix.lower() == ".json":
            docs.append(process_json(fp))
        else:
            # skip unsupported file types
            continue
    return docs

def main():
    docs = load_raw_docs()
    print(f"Loaded {len(docs)} raw documents from {RAW}")
    for d in docs:
        out_path = PROCESSED / f"{d['id']}.json"
        out_path.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf8")
    print(f"Processed {len(docs)} documents → saved in {PROCESSED}")

if __name__ == "__main__":
    main()
