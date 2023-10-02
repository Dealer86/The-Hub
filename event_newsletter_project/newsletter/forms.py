from django import forms


class EventsHubForm(forms.Form):
    google_events_search_query = forms.CharField(
        label="Search Events",
        widget=forms.TextInput(
            attrs={
                "placeholder": 'Get started, enter your event location name and/or category. Ex: "Sibiu", "concerts in Chicago"',
            }
        ),
        max_length=255,
    )
