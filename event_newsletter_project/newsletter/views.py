from django.shortcuts import render
from django.contrib import messages  # Import messages framework
from .forms import EventsHubForm
from .local_events import EventsHub
from .models import Event


# View to display the newsletter
def newsletter(request):
    if request.method == "POST":
        form = EventsHubForm(request.POST)
        if form.is_valid():
            try:
                city_location = form.cleaned_data["city_location"]
                events_hub = EventsHub(city_location)
                fetch_local_events = events_hub.fetch_local_events()
                Event.objects.all().delete()
                for event in fetch_local_events.itertuples():
                    Event.objects.create(
                        title=event.title,
                        date=event.date,
                        address=event.address,
                        link=event.link,
                    )
            except Exception as e:
                messages.error(request, f"Reason: {str(e)}")
    else:
        form = EventsHubForm()

    database_events = Event.objects.all()

    return render(
        request, "newsletter/newsletter.html", {"form": form, "events": database_events}
    )
