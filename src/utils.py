# utils.py
import re
from pathlib import Path

def clean_text(text: str) -> str:
    """
    Basic whitespace normalization and trimming.
    """
    if not isinstance(text, str):
        text = str(text)
    text = text.replace("\r", " ").replace("\n", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def safe_id(value: str) -> str:
    """
    Make an ID filesystem-safe (remove slashes and special chars).
    """
    s = str(value)
    s = s.replace("/", "-")
    s = re.sub(r"[^A-Za-z0-9_\-]", "", s)
    return s[:200]  # limit length
