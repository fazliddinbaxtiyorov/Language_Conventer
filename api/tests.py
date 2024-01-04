from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient


# Create your tests here.
class LanguageConventerTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_home_page(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def testing_none_page(self):
        response = self.client.get('/none/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_text_page(self):
        self.client = APIClient()
        response = self.client.get('/add/')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def testing_files(self):
        response = self.client.get('/file/')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
