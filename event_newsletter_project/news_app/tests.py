from django.test import TestCase
from django.urls import reverse


class GetNewsTests(TestCase):
    """
    A test suite for the 'get_news' view and related functionality.
    """

    def test_url_exists_at_the_correct_location(self):
        """
        Test whether the URL "/news/" exists and returns a status code of 200 (OK).
        """
        response = self.client.get("/news/")
        self.assertEqual(response.status_code, 200)

    def test_that_the_template_name_is_correct(self):
        """
        Test whether the correct template "news.html" is used when accessing the "get_news" view.
        """
        response = self.client.get(reverse("get_news"))
        self.assertTemplateUsed(response, "news.html")

    def test_template_content(self):
        """
        Test whether the template for "get_news" view contains the expected content, specifically, a title tag with the text "News Hub".
        """
        response = self.client.get(reverse("get_news"))
        self.assertContains(response, "<title>News Hub</title>")

    def test_invalid_form_data_for_country(self):
        """
        Test the handling of invalid form data for the "country" field.
        """
        invalid_data = {
            "country": "xx",  # This should trigger a validation error
            "category": "general",
        }
        response = self.client.post(reverse("get_news"), data=invalid_data)

        self.assertEqual(response.status_code, 200)

        self.assertFalse(response.context["form"].is_valid())

        # Check if the 'country' field has a validation error.
        self.assertTrue("country" in response.context["form"].errors)

        # Check the error message for the 'country' field.
        self.assertEqual(
            response.context["form"].errors["country"][0],
            "Invalid country. Please choose a valid country.",
        )

    def test_valid_form_data(self):
        """
        Test the handling of valid form data for the "country" and "category" fields.
        """
        valid_data = {
            "country": "ro",
            "category": "general",
        }
        response = self.client.post(reverse("get_news"), data=valid_data)

        self.assertEqual(response.status_code, 200)

        self.assertTrue(response.context["form"].is_valid())
