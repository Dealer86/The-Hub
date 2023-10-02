from django.urls import path
from . import views

urlpatterns = [
    path("", views.events_hub_views, name="event_hub_views"),
]
