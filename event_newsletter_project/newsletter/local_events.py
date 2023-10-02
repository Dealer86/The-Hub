import requests
import pandas as pd

URL = "https://serpapi.com/search?engine=google_events"
API_KEY = "Enter real api KEY"


class EventsHub:
    def __init__(self, city_location: str = "Sibiu"):
        self.url = URL
        self.api_key = API_KEY
        self.city_location = city_location

    # Function to fetch local weekend events from the SerpWow service
    def fetch_local_events(self):
        payload = {
            "api_key": API_KEY,
            "engine": "google",
            "q": f"{self.city_location}",
        }
        response = requests.get(self.url, params=payload)
        data = response.json()
        events_data = []
        if data:
            for event in data["events_results"]:
                description = event.get("description", "No description available")
                description = "".join(description.split(".")[0] + ".")
                image = event.get("image", "No image")

                title = event.get("title", "Unknown Title")
                date = event.get("date", "Unknown Date")
                date = date["when"]
                address = event.get("address", "Unknown Address")
                address = "".join(address)
                link = event.get("link", "Unknown Link")
                event_dict = {
                    "title": title,
                    "description": description,
                    "image": image,
                    "date": date,
                    "address": address,
                    "link": link,
                }
                events_data.append(event_dict)
        else:
            return []
        return pd.DataFrame(events_data)


if __name__ == "__main__":
    events_hub = EventsHub("Sibiu")
    print(events_hub.fetch_local_events())
