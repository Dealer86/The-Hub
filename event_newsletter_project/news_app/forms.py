from django import forms
from django.utils.translation import gettext_lazy as _
from django.conf import settings  # Import Django settings module


class NewsForm(forms.Form):
    country = forms.CharField(
        max_length=2, widget=forms.TextInput(attrs={"class": "form-input"})
    )
    category = forms.CharField(
        max_length=30, widget=forms.TextInput(attrs={"class": "form-input"})
    )

    def clean_country(self):
        """
        Custom validation for the 'country' field.
        """
        country = self.cleaned_data["country"]

        # Check if the entered country is in the list of valid countries
        if country not in settings.NEWS_API_COUNTRIES:
            raise forms.ValidationError(
                _("Invalid country. Please choose a valid country.")
            )

        return country

    def clean_category(self):
        """
        Custom validation for the 'category' field.
        """
        category = self.cleaned_data["category"]

        # Check if the entered category is in the list of valid categories
        if category not in settings.NEWS_API_CATEGORIES:
            raise forms.ValidationError(
                _("Invalid category. Please choose a valid category.")
            )

        return category
