import os
from transformers import pipeline
from openai import OpenAI
from .utils import safe_truncate

# Initialize Hugging Face summarizer
hf_summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text, mode="bullets", max_bullets=6, backend="hf"):
    """Summarize text using either Hugging Face or OpenAI backend."""
    text = safe_truncate(text)

    if backend == "openai":
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        prompt = (
            f"Summarize the following notes into {max_bullets} key bullet points:\n{text}"
            if mode == "bullets"
            else f"Provide a concise paragraph summary of the following:\n{text}"
        )

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an academic note summarizer."},
                {"role": "user", "content": prompt},
            ],
        )
        return response.choices[0].message.content.strip()

    else:
        # Hugging Face summarization
        summary = hf_summarizer(
            text, max_length=180, min_length=60, do_sample=False
        )[0]["summary_text"]

        if mode == "bullets":
            bullets = summary.replace(". ", ".\n• ")
            return "• " + bullets.strip("• ")
        return summary
