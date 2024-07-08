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

def create_calendar_event():
    """
    Create and insert a calendar event.
    Print the returned event's id and link.
    Returns: Event object, including event id and link.
    """
    try:
        # Use the create_oauth2_credentials function to obtain credentials
        credentials = create_oauth2_credentials()

        # Build the Calendar API service using the obtained credentials
        service = build("calendar", "v3", credentials=credentials)

        # Event details
        event = {
            'summary': 'Google I/O 2024',
            'location': '800 Howard St., San Francisco, CA 94103',
            'description': 'A chance to hear more about Google\'s developer products.',
            'start': {
                'dateTime': '2024-07-09T09:00:00-07:00',
                'timeZone': 'America/Los_Angeles',
            },
            'end': {
                'dateTime': '2024-07-09T17:00:00-07:00',
                'timeZone': 'America/Los_Angeles',
            },
            'recurrence': [
                'RRULE:FREQ=DAILY;COUNT=2'
            ],
            'attendees': [
                {'email': 'abhinavxt456@gmail.com'},
                {'email': 'avi051023@gmail.com'},
            ],
            'reminders': {
                'useDefault': False,
                'overrides': [
                    {'method': 'email', 'minutes': 24 * 60},
                    {'method': 'popup', 'minutes': 10},
                ],
            },
        }

        # Create the event using Calendar API
        event = service.events().insert(calendarId='primary', body=event).execute()
        print(f'Event created: {event.get("htmlLink")}')

        return event

    except HttpError as error:
        print(f"An error occurred: {error}")
        return None

if __name__ == "__main__":
    # Example usage
    create_calendar_event()
