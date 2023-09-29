from django.shortcuts import render
from .models import Event
import requests


# Function to fetch local weekend events from the SerpApi Google Events API
def fetch_local_events():
    api_key = "YOUR_SERPAPI_API_KEY"  # Replace with your actual SerpApi API key
    api_url = (
        f"https://serpapi.com/google-events-api?q=weekend%20events&api_key={api_key}"
    )

    try:
        response = requests.get(api_url)

        if response.status_code == 200:
            events_data = response.json().get("events", [])
            return events_data
        else:
            print(f"Failed to fetch events. Status code: {response.status_code}")
            return []
    except requests.exceptions.RequestException as e:
        print(f"Error fetching events: {e}")
        return []


# View to display the newsletter
def newsletter(request):
    # Fetch local weekend events
    events = fetch_local_events()

    # Query the Event model to get existing events from the database
    database_events = Event.objects.all()

    # Combine the fetched API events with database events
    combined_events = events + list(database_events)

    return render(request, "newsletter/newsletter.html", {"events": combined_events})
