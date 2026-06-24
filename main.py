from fastapi import FastAPI
from pydantic import BaseModel
import hashlib

app = FastAPI()

# Pydantic model for JSON input
class TextRequest(BaseModel):
    text: str

# Welcome message
@app.get("/")
def home():
    return {"message": "Welcome Asha to GitHub Copilot Python Lab"}

# FastAPI endpoint to return checksum
@app.post("/checksum")
def checksum(request: TextRequest):
    checksum_value = hashlib.md5(
        request.text.encode()
    ).hexdigest()

    return {
        "text": request.text,
        "checksum": checksum_value
    }
