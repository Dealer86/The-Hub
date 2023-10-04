from django.test import TestCase, SimpleTestCase
from django.urls import reverse


# TestCase its used if it has a database
# SimpleTestCase is used if we do not have a database
# TransactionTestCase is helpful to directly test database transactions
# LiveServerTestCase launches a live server thread for testing with browser based tools like Selenium
# Reverse is used to test the URL name for each page/route


class EventsHubViewsTests(TestCase):
    # test URL location
    def test_url_exists_at_the_correct_location(self):
        #  If we have another route then localhost like about you must end it with a slash /about/
        #  To run test quit server if running and python manage.py test
        response = self.client.get("/events/")
        self.assertEqual(response.status_code, 200)

    # test URL names
    def test_url_available_by_name(self):
        response = self.client.get(reverse("event_hub_views"))
        self.assertEqual(response.status_code, 200)

    # test that the correct templates are used on each page
    def test_template_name_correct(self):
        response = self.client.get(reverse("event_hub_views"))
        self.assertTemplateUsed(response, "events_app.html")

    # test that they display the expected content
    def test_template_content(self):
        response = self.client.get(reverse("event_hub_views"))
        self.assertContains(response, "<title>Events Hub</title>")

    # You can use this to abide by DRY
    # def __get_response(self):
    #     response = self.client.get(reverse("event_hub_views"))
    #     return response

    def test_post_valid_form(self):
        response = self.client.post(
            reverse("event_hub_views"),
            data={"google_events_search_query": "New York"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "events_app.html")
