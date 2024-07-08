import os
import pickle
from dotenv import load_dotenv
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.errors import HttpError

# Load environment variables from .env file
load_dotenv()

# OAuth2 scopes for Google Calendar API
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly', 'https://www.googleapis.com/auth/calendar.events']

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
                'cCalendarAPI/credentials.json',  # Specify the path to your client secret JSON file
                scopes=SCOPES
            )
            credentials = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with open(token_file, 'wb') as token:
            pickle.dump(credentials, token)

    return credentials


def set_reminder_for_event(calendar_id, event_id, reminder_minutes):
    """
    Set up a reminder for an existing event.
    """
    try:
        # Use the create_oauth2_credentials function to obtain credentials
        credentials = create_oauth2_credentials()

        # Build the Calendar API service using the obtained credentials
        service = build("calendar", "v3", credentials=credentials)

        # Fetch the event details
        event = service.events().get(calendarId=calendar_id, eventId=event_id).execute()

        # Set the reminder
        event['reminders'] = {
            'useDefault': False,
            'overrides': [
                {'method': 'email', 'minutes': reminder_minutes},
                {'method': 'popup', 'minutes': 10},
            ],
        }

        # Update the event with the new reminder settings
        updated_event = service.events().update(calendarId=calendar_id, eventId=event_id, body=event).execute()
        print(f'Reminder set for event: {updated_event.get("htmlLink")}')

        return updated_event

    except HttpError as error:
        print(f"An error occurred: {error}")
        return None

if __name__ == "__main__":
    # Set a reminder for the newly created event
    calendar_id="1b90945a4bbd496d3efa45dbe482c0e315288f68a9a1cafbe0c8d329012836e7@group.calendar.google.com" #write calender id here
    event_id="7fmd579u06u59iee2r024ticfo" # write event id here
    set_reminder_for_event(calendar_id, event_id, 60)
