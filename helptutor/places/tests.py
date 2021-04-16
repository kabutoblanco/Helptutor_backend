from django.test import RequestFactory, TestCase
from django.urls import reverse
# Nos ayuda a crear nuestros objetos
#from django_dynamic_fixture import G, F

from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.test import APIRequestFactory, APITestCase

from helptutor.places.models import Country
from helptutor.places.api import CountryViewSet

# Create your tests here.
class TestAPITCountry(APITestCase):

    url = "/api/country/"

    def setUp(self):
        
        Country.objects.create(name="Colombia",cod="30")

    def test_get_country(self):

        # process
        response = self.client.get(self.url)
        result = response.json()
        
        # assert
        self.assertEqual(response.status_code,200)
        self.assertIsInstance(result,list)
        self.assertEqual(result[0]["name"],"Colombia")

    def test_post_country(self):
        
        # definition
        data = {
            "name":"Peru",
            "cod":"30"
        }

        # process
        response = self.client.post(self.url, data)
        result = response.json()

        # assert
        self.assertEqual(response.status_code,201)
        self.assertEqual(result["name"],"Peru")


    def test_put_country(self):
        pk = "1"
        data = {
            "name":"Ecuador"
        }

        # process
        response = self.client.patch(self.url + f"{pk}/", data=data)
        result = response.json()

        # assert
        self.assertEqual(response.status_code,200)
        self.assertEqual(result["name"],"Ecuador")
