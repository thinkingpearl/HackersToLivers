from fastapi import FastAPI, UploadFile, File, Form
from .extractor import extract_text_from_pdf
from .summarizer import summarize_text
from dotenv import load_dotenv
import os

load_dotenv()
app = FastAPI(title="AI Notes Summarizer")

@app.get("/")
def root():
    return {"message": "AI Notes Summarizer backend is running!"}

@app.post("/summarize")
async def summarize(
    file: UploadFile = File(...),
    mode: str = Form("bullets"),
    backend_choice: str = Form("hf"),
    max_bullets: int = Form(6)
):
    if file.content_type != "application/pdf":
        return {"error": "Only PDF files are supported."}

    content = await file.read()
    text = extract_text_from_pdf(content)
    if not text.strip():
        return {"error": "No text could be extracted."}

    result = summarize_text(text, mode=mode, max_bullets=max_bullets, backend=backend_choice)
    return {"summary": result}
