import os
import pickle
from dotenv import load_dotenv
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.exceptions import RefreshError
from googleapiclient.errors import HttpError

# Load environment variables from .env file
load_dotenv()

# OAuth2 scopes for Google Calendar API
SCOPES = ['https://www.googleapis.com/auth/calendar']

def create_oauth2_credentials():
    """
    Create OAuth2 credentials using the installed application flow.
    Save and reuse credentials to avoid re-authenticating each time.
    """
    credentials = None

    # Token file to store the user's access and refresh tokens
    token_file = 'token.pickle'

    # Check if the token file exists and is not empty
    if os.path.exists(token_file) and os.path.getsize(token_file) > 0:
        try:
            with open(token_file, 'rb') as token:
                credentials = pickle.load(token)
        except Exception as e:
            print(f"Error loading token file: {e}")
            credentials = None

    # If there are no valid credentials available, prompt the user to log in
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            try:
                credentials.refresh(Request())
            except RefreshError as e:
                print(f"Error refreshing credentials: {e}")
                return None
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json',  # Specify the path to your client secret JSON file
                scopes=SCOPES,
            )
            credentials = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with open(token_file, 'wb') as token:
            pickle.dump(credentials, token)

    return credentials

def share_calendar(calendar_id, email, role='reader'):
    """
    Share a Google Calendar with another user.
    Args:
        calendar_id (str): The ID of the calendar to be shared.
        email (str): The email address of the user to share the calendar with.
        role (str): The role for the user (default: 'reader', options: 'owner', 'writer', 'reader').
    """
    try:
        # Use the create_oauth2_credentials function to obtain credentials
        credentials = create_oauth2_credentials()

        if not credentials:
            print("Failed to obtain valid credentials.")
            return

        # Build the Calendar API service using the obtained credentials
        service = build("calendar", "v3", credentials=credentials)

        # Define the permission body
        rule = {
            'scope': {
                'type': 'user',
                'value': email,
            },
            'role': role,
        }

        # Insert the rule (share the calendar)
        created_rule = service.acl().insert(calendarId=calendar_id, body=rule).execute()

        print(f"Calendar shared successfully with {email} with role {role}.")

    except HttpError as error:
        print(f"An error occurred: {error}")

if __name__ == "__main__":
    # Example usage: Share a calendar with a specific email address
    calendar_id_to_share = '1b90945a4bbd496d3efa45dbe482c0e315288f68a9a1cafbe0c8d329012836e7@group.calendar.google.com'
    email_to_share_with = 'abhinavxt456@gmail.com'
    role = 'writer'
    share_calendar(calendar_id_to_share, email_to_share_with, role)

