"""Send notifications to Microsoft Teams via incoming webhook."""

import requests

from .config import TEAMS_WEBHOOK_URL


def send_message(text: str) -> None:
    """Post ``text`` to the configured Teams channel."""
    requests.post(TEAMS_WEBHOOK_URL, json={"text": text})
