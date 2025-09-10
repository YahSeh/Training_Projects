"""Utilities for interacting with Outlook via Microsoft Graph.

Requires the ``O365`` package and Azure AD application credentials.
"""

from typing import Iterable

from O365 import Account

from .config import (
    OUTLOOK_CLIENT_ID,
    OUTLOOK_CLIENT_SECRET,
    OUTLOOK_TENANT_ID,
)

_credentials = (OUTLOOK_CLIENT_ID, OUTLOOK_CLIENT_SECRET)
_account = Account(_credentials, auth_flow_type="credentials", tenant_id=OUTLOOK_TENANT_ID)


def fetch_unread_emails(limit: int = 50) -> Iterable[object]:
    """Yield unread messages from the inbox."""
    if not _account.is_authenticated:
        _account.authenticate()
    mailbox = _account.mailbox()
    inbox = mailbox.inbox_folder()
    query = inbox.new_query().on_attribute("isRead").equals(False)
    return inbox.get_messages(limit=limit, query=query)
