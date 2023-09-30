from django import forms


class EventsHubForm(forms.Form):
    city_location = forms.CharField(max_length=100)
