# Mail Management Agent

This prototype demonstrates how to build a Python agent that classifies
incoming Outlook e-mails, generates summaries, and notifies other
channels like Microsoft Teams and WhatsApp.

## Features

* Fetch unread e-mails from Outlook using the `O365` library.
* Classify messages with a scikit-learn model.
* Summarize important e-mails using a transformer model.
* Send summaries to Microsoft Teams and urgent alerts to WhatsApp.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Provide the necessary credentials via environment variables (see
   `config.py`).
3. Run the processor:
   ```python
   from mail_agent.main import process_emails
   process_emails()
   ```

This code is provided as a starting point and requires valid API
credentials and a trained classification model to be fully functional.
