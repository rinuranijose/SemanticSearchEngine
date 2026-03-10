import requests

OLLAMA_URL = "http://localhost:11434/api/embeddings"

def get_embedding(text):

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "nomic-embed-text",
            "prompt": text
        }
    )

    return response.json()["embedding"]