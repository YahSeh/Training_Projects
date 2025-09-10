"""Send WhatsApp alerts using Twilio."""

from twilio.rest import Client

from .config import (
    TWILIO_ACCOUNT_SID,
    TWILIO_AUTH_TOKEN,
    TWILIO_WHATSAPP_FROM,
    WHATSAPP_TO,
)


def send_alert(text: str) -> None:
    """Send ``text`` to the configured WhatsApp recipient."""
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    client.messages.create(body=text, from_=TWILIO_WHATSAPP_FROM, to=WHATSAPP_TO)
