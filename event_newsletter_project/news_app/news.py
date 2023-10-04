"""
  A simple Python script to retrieve and display news articles based on user-specified country and category.
"""
import requests
import pandas as pd
from django.conf import settings  # Import Django settings module


class CountryNotFoundError(Exception):
    pass


class CategoryNotFoundError(Exception):
    pass


class News:
    """
    A class for retrieving and displaying news articles based on user-specified criteria.
    """

    def __init__(self, country: str, category: str):
        """
        Initialize a News object.

        Args:
            country (str): The country code for news retrieval (e.g., "ro", "gb", "us").
            category (str): The news category (e.g., "sports", "technology").

        Raises:
            CountryNotFoundError: If the specified country code is not valid.
            CategoryNotFoundError: If the specified category does not exist.
        """
        self.url = settings.NEWS_API_URL
        self.api = settings.NEWS_API_KEY
        self.country = country
        self.category = category

        if self.country not in settings.NEWS_API_COUNTRIES:
            raise CountryNotFoundError("Country is not valid")
        if self.category not in settings.NEWS_API_CATEGORIES:
            raise CategoryNotFoundError("Category does not exist")

        self.response = requests.get(
            self.url, params=self.set_parameters_for_news_api_request()
        ).json()

    def set_parameters_for_news_api_request(self):
        """
        Define the parameters for the news API request.

        Returns:
            dict: A dictionary containing the request parameters.
        """
        return {"country": self.country, "category": self.category, "apiKey": self.api}

    def save_get_news(self):
        """
        Extract and save news articles as a DataFrame.

        Returns:
            pandas.DataFrame: A DataFrame containing news article information (author, title, URL).
        """
        news = []
        for item in self.response["articles"]:
            author = item.get("author", "Unknown Author")
            title = item.get("title", "Unknown Title")
            url = item.get("url", "Unknown Url")
            dict_news = {
                "author": author,
                "title": title,
                "url": url,
            }
            news.append(dict_news)
        df = pd.DataFrame(news)
        return df
