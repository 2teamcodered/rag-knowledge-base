from .core import chunk, retrieve
chunks = chunk("Agents use tools. Retrieval grounds model responses in evidence.", "demo.txt", 8)
print(retrieve("how does retrieval ground agents", chunks))
