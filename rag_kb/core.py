import re
from dataclasses import dataclass
@dataclass
class Chunk: text: str; source: str
def chunk(text: str, source: str, size: int = 80) -> list[Chunk]:
    words = text.split(); return [Chunk(" ".join(words[i:i+size]), source) for i in range(0, len(words), size)]
def retrieve(query: str, chunks: list[Chunk], k: int = 3) -> list[Chunk]:
    q = set(re.findall(r"\w+", query.lower()))
    scored = [(len(q & set(re.findall(r"\w+", c.text.lower()))), c) for c in chunks]
    return [c for score, c in sorted(scored, key=lambda x:x[0], reverse=True)[:k] if score]
