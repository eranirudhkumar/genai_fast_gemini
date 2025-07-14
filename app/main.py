from fastapi import FastAPI
from app.schemas import PromptRequest
from app.gemini_client import generate_text

app = FastAPI(
    title="Gemini FastAPI GenAI",
    description="A simple API using Google Gemini and FastAPI",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Gemini GenAI API!"}

@app.post("/generate/")
def generate_response(data: PromptRequest):
    output = generate_text(data.prompt)
    return {"response": output}
