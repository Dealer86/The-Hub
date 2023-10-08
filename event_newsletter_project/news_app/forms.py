from django import forms
from django.conf import settings  # Import Django settings module


class NewsForm(forms.Form):
    COUNTRY_CHOICES = [(code, code.upper()) for code in settings.NEWS_API_COUNTRIES]
    CATEGORY_CHOICES = [
        (category, category.capitalize()) for category in settings.NEWS_API_CATEGORIES
    ]

    country = forms.ChoiceField(
        choices=COUNTRY_CHOICES,
        widget=forms.Select(attrs={"class": "form-input"}),
    )
    category = forms.ChoiceField(
        choices=CATEGORY_CHOICES,
        widget=forms.Select(attrs={"class": "form-input"}),
    )
