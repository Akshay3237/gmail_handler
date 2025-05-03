import os
import json
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
def get_gmail_service():
    # Gmail API scope for full access
    SCOPES = ['https://mail.google.com/']
    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # OAuth2 client info
    # Build the full path to credential1.json
    CRIDENTIAL1_FILE = os.path.join(script_dir, 'cridentials1.json')


    
    
    
    TOKEN_FILE = os.path.join(script_dir, "token1.json")
    with open(CRIDENTIAL1_FILE, 'r') as file:
        data =(json.load(file))['installed']
    CLIENT_ID = data['client_id']
    CLIENT_SECRET = data['client_secret']
    REDIRECT_URI =data['redirect_uris']
    # print(data['client_id'])
    """Handles authentication, token management, and returns Gmail API service."""
    creds = None

    # Load existing token
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)

    # If no valid credentials, refresh or re-authenticate
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_config(
                {
                    "installed": {
                        "client_id": CLIENT_ID,
                        "client_secret": CLIENT_SECRET,
                        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                        "token_uri": "https://oauth2.googleapis.com/token",
                        "redirect_uris": [REDIRECT_URI]
                    }
                },
                SCOPES
            )
            creds = flow.run_local_server(port=8080, access_type='offline', prompt='consent')

        # Save token
        with open(TOKEN_FILE, 'w') as token_file:
            token_file.write(creds.to_json())

    return build('gmail', 'v1', credentials=creds)

