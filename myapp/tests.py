from django.test import TestCase
from django.urls import reverse


class HomeViewTests(TestCase):
	def test_home_page_returns_greeting(self):
		response = self.client.get(reverse("home"))

		self.assertEqual(response.status_code, 200)
		self.assertEqual(
			response.content.decode(),
			"<h1>Hello, World! This is the home page of my app.</h1>",
		)


class AboutViewTests(TestCase):
	def test_about_page_returns_description(self):
		response = self.client.get(reverse("about"))

		self.assertEqual(response.status_code, 200)
		self.assertEqual(
			response.content.decode(),
			"<h1>About Page</h1><p>This is the about page of my Django application.</p>",
		)

class ContactViewTests(TestCase):
    def test_contact_page_returns_contact_information(self):
        response = self.client.get(reverse("contact"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.content.decode(),
            "<h1>Contact Page</h1><p>This is the contact page of my Django application.</p>",
        )


