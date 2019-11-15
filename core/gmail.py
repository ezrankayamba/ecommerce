from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from email.mime.text import MIMEText
import base64

token_storage = 'events.token.pickle'
cred_file = 'ecommerce_credentials.json'


def send_message(service, message):
    try:
        return (service.users().messages().send(userId='me', body=message).execute())
    except Exception as e:
        print(f'An error occurred: {e}')


def create_message(sender, to, subject, message_text):
    message = MIMEText(message_text, 'html')
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    raw = base64.urlsafe_b64encode(message.as_bytes())
    raw = raw.decode()
    return {'raw': raw}


def init_service():
    SCOPES = ['https://www.googleapis.com/auth/gmail.modify',
              'https://www.googleapis.com/auth/gmail.settings.basic']
    creds = None
    if os.path.exists(token_storage):
        with open(token_storage, 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(cred_file, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(token_storage, 'wb') as token:
            pickle.dump(creds, token)
    return build('gmail', 'v1', credentials=creds)
