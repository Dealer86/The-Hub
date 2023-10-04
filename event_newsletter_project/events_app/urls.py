from django.urls import path
from .views import HomePageView, events_hub_views

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("events/", events_hub_views, name="event_hub_views"),
]
