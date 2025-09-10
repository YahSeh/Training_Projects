"""Email summarization utilities."""

from transformers import pipeline


def summarize(text: str) -> str:
    """Return a short summary for the given text."""
    summarizer = pipeline("summarization")
    result = summarizer(text, max_length=60, min_length=5, do_sample=False)
    return result[0]["summary_text"]
