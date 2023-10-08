from django import forms


class EventsHubForm(forms.Form):
    google_events_search_query = forms.CharField(
        label="Search Events",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search Events",
            }
        ),
        max_length=255,
    )
