from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from .models import LanguageModels


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


class TestModels(TestCase):
    def setUp(self) -> None:
        LanguageModels.objects.create(context='Salom', pattern='latin')
        LanguageModels.objects.create(context='Xayr', pattern='cyrillic')
        LanguageModels.objects.create(context='Эрталаб', pattern='latin')
        LanguageModels.objects.create(context='Shaxmat', pattern='cyrillic')
        LanguageModels.objects.create(context='лайлак', pattern='latin')

    def test_context(self):
        obj1 = LanguageModels.objects.get(context='Salom')
        obj2 = LanguageModels.objects.get(context='Xayr')
        obj3 = LanguageModels.objects.get(context='Эрталаб')
        obj4 = LanguageModels.objects.get(context='Shaxmat')
        self.assertEquals(obj1.context, "Salom")
        self.assertEquals(obj2.context, "Xayr")
        self.assertEquals(obj3.context, "Эрталаб")
        self.assertEquals(obj4.context, "Shaxmat")

