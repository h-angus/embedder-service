from fastapi import FastAPI
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer

app = FastAPI()
model = SentenceTransformer("all-MiniLM-L6-v2")

class EmbedRequest(BaseModel):
    texts: list[str]

@app.post("/embed")
def embed(request: EmbedRequest):
    # Force list conversion to ensure JSON serializability
    embeddings = model.encode(request.texts, convert_to_tensor=False)
    return {"embeddings": [e.tolist() if hasattr(e, "tolist") else list(e) for e in embeddings]}
