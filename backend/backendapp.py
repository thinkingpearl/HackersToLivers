import re

def safe_truncate(text: str, max_chars: int = 30000) -> str:
    """Truncate long text safely without cutting sentences mid-way."""
    if len(text) <= max_chars:
        return text
    truncated = text[:max_chars]
    idx = truncated.rfind('. ')
    return truncated[:idx + 1] if idx != -1 else truncated
