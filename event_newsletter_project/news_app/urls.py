from django.urls import path
from . import views

urlpatterns = [
    # Add a URL pattern for the news view
    path("", views.get_news, name="get_news"),
]
