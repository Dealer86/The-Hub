from django.shortcuts import render
from .models import Event
import requests


# Function to fetch local weekend events from the SerpWow service
def fetch_local_events():
    url = "https://serpapi.com/search?engine=google_events"

    payload = {
        "api_key": "ADI coder nebun ce esti, replace with real SERPI API_KEY",
        "engine": "google",
        "q": "Events in Sibiu",
    }
    response = requests.get(url, params=payload)
    data = response.json()
    events_data = []
    if data:
        for event in data["events_results"]:
            a_dict = {
                "title": event["title"],
                "date": event["date"],
                "address": event["address"],
                "link": event["link"],
            }
            events_data.append(a_dict)
    else:
        return []
    return events_data


# View to display the newsletter
def newsletter(request):
    # Fetch local weekend events
    events = fetch_local_events()

    # Query the Event model to get existing events from the database
    database_events = Event.objects.all()

    # Combine the fetched API events with database events
    combined_events = events + list(database_events)

    return render(request, "newsletter/newsletter.html", {"events": combined_events})
