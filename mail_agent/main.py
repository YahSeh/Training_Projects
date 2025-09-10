"""Entry point for the email management agent."""

from .classifier import EmailClassifier
from .outlook_client import fetch_unread_emails
from .summarizer import summarize
from .teams_client import send_message
from .whatsapp_client import send_alert


CLASS_TO_ACTION = {
    "urgent": "urgent",
    "pub": "advertisement",
    "copy": "cc",
}


def process_emails(limit: int = 20) -> None:
    """Process unread emails from Outlook."""
    classifier = EmailClassifier()
    for message in fetch_unread_emails(limit=limit):
        content = f"{message.subject}\n{message.body}"
        label = classifier.predict(content)
        summary = summarize(message.body)
        if label == "urgent":
            send_message(f"URGENT: {summary}")
            send_alert(summary)
        elif label == "pub":
            message.delete()
        else:
            send_message(summary)
