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
                scopes=SCOPES
            )
            credentials = flow.run_local_server(port=0, prompt='consent', include_granted_scopes='true')

        # Save the credentials for the next run
        with open(token_file, 'wb') as token:
            pickle.dump(credentials, token)

    return credentials

def delete_event(event_id):
    """
    Delete an event from the Google Calendar.
    Args:
        event_id (str): The ID of the event to be deleted.
    """
    try:
        # Use the create_oauth2_credentials function to obtain credentials
        credentials = create_oauth2_credentials()

        if not credentials:
            print("Failed to obtain valid credentials.")
            return

        # Build the Calendar API service using the obtained credentials
        service = build("calendar", "v3", credentials=credentials)

        # Delete the event
        service.events().delete(calendarId='primary', eventId=event_id).execute()
        
        print(f"Event with ID {event_id} deleted successfully.")

    except HttpError as error:
        print(f"An error occurred: {error}")

if __name__ == "__main__":
    # Example usage: Delete an event with a specific event ID
    event_id_to_delete = '05rcu5nikd8djole1j8sbf5agc'
    delete_event(event_id_to_delete)
