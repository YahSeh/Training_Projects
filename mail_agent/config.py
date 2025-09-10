"""Configuration for the email management agent.

Values are read from environment variables. Replace the defaults with
real credentials before running the agent.
"""

import os

OUTLOOK_CLIENT_ID = os.getenv("OUTLOOK_CLIENT_ID", "your-client-id")
OUTLOOK_CLIENT_SECRET = os.getenv("OUTLOOK_CLIENT_SECRET", "your-client-secret")
OUTLOOK_TENANT_ID = os.getenv("OUTLOOK_TENANT_ID", "your-tenant-id")

TEAMS_WEBHOOK_URL = os.getenv("TEAMS_WEBHOOK_URL", "https://outlook.office.com/webhook/...")

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID", "your-twilio-sid")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN", "your-twilio-token")
TWILIO_WHATSAPP_FROM = os.getenv("TWILIO_WHATSAPP_FROM", "whatsapp:+14155238886")
WHATSAPP_TO = os.getenv("WHATSAPP_TO", "whatsapp:+33XXXXXXXXX")
