import fitz  # PyMuPDF
from typing import List

def extract_text_from_pdf(bytes_content: bytes) -> str:
    """Extracts text from each page of a PDF file."""
    doc = fitz.open(stream=bytes_content, filetype="pdf")
    pages: List[str] = []
    for page in doc:
        try:
            pages.append(page.get_text("text"))
        except Exception:
            pages.append("")
    return "\n\n".join(pages)
