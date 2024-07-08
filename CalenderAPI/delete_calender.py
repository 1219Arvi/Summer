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
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

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
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json',  # Specify the path to your client secret JSON file
                scopes=SCOPES
            )
            credentials = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with open(token_file, 'wb') as token:
            pickle.dump(credentials, token)

    return credentials

def delete_secondary_calendar(calendar_id):
    """
    Delete a secondary calendar using its calendar ID.
    """
    try:
        # Use the create_oauth2_credentials function to obtain credentials
        credentials = create_oauth2_credentials()

        # Build the Calendar API service using the obtained credentials
        service = build("calendar", "v3", credentials=credentials)

        # Delete the calendar using Calendar API
        service.calendars().delete(calendarId=calendar_id).execute()
        print(f'Calendar with ID {calendar_id} deleted successfully.')

    except HttpError as error:
        print(f"An error occurred: {error}")

if __name__ == "__main__":
    # Example calendar ID to be deleted
    calendar_id = 'd4987aa38b62057cf4e8690677f6fe2fcfe34ac9dbc411628ccaf7a56e6ee7ce@group.calendar.google.com'  # Replace with the actual calendar ID

    # Delete the secondary calendar
    delete_secondary_calendar(calendar_id)
