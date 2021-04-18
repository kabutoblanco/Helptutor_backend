from django.test import RequestFactory, TestCase
from django.urls import reverse
from model_mommy import mommy

from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.test import APIRequestFactory, APITestCase

from helptutor.places.api import *

# Create your tests here.
class TestApitCountry(APITestCase):

    def setUp(self):

        self.client = APIClient()

        self.url = "/api/country/"
        
        Country.objects.create(name="Colombia",cod="30")
    
    def test_get_country(self):

        # process
        response = self.client.get(self.url)
        result = response.json()
        
        # assert
        self.assertEqual(response.status_code,status.HTTP_200_OK)
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
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
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
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(result["name"],"Ecuador")

    def test_delete_country(self):
        # definition
        country = Country.objects.create(name="Mexico",cod="30")

        # process
        response = self.client.delete(self.url + f"{country.id}/")

        # assert
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)

class TestApitEstate(APITestCase):

    def setUp(self):

        self.client = APIClient()

        self.url = "/api/state/"
        
        self.state = mommy.make(State)

    def test_get_state(self):

        # process
        response = self.client.get(self.url)
        result = response.json()

        # assert
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertIsInstance(result,list)
        self.assertEqual(result[0]["name"],self.state.name)

    def test_post_state(self):
        
        # definition
        country = mommy.make(Country)
        data = {
            "name": "Putumayo",
            "cod": "33",
            "country": country.id
        }

        # process
        response = self.client.post(self.url, data)
        result = response.json()

        # assert
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        self.assertEqual(result["name"],"Putumayo")

    def test_put_state(self):
        pk = "1"
        data = {
            "name":"Huila"
        }

        # process
        response = self.client.patch(self.url + f"{pk}/", data=data)
        result = response.json()

        # assert
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(result["name"],"Huila")

    def test_delete_state(self):
        # process
        response = self.client.delete(self.url + f"{self.state.id}/")

        # assert
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)
        
class TestApitCity(APITestCase):

    def setUp(self):

        self.client = APIClient()

        self.url = "/api/city/"
        
        self.city = mommy.make(City)

    def test_get_city(self):

        # process
        response = self.client.get(self.url)
        result = response.json()

        # assert
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertIsInstance(result,list)
        self.assertEqual(result[0]["name"],self.city.name)

    def test_post_city(self):
        
        # definition
        city = mommy.make(State)
        data = {
            "name": "Orito",
            "cod": "23",
            "state": city.id
        }

        # process
        response = self.client.post(self.url, data)
        result = response.json()

        # assert
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        self.assertEqual(result["name"],"Orito")

    def test_put_city(self):
        pk = "1"
        data = {
            "name":"Mocoa"
        }

        # process
        response = self.client.patch(self.url + f"{pk}/", data=data)
        result = response.json()

        # assert
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(result["name"],"Mocoa")

    def test_delete_city(self):
        # process
        response = self.client.delete(self.url + f"{self.city.id}/")

        # assert
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)

class TestApitUniversity(APITestCase):

    def setUp(self):

        self.client = APIClient()

        self.url = "/api/university/"
        
        self.university = mommy.make(University)

    def test_get_university(self):

        # process
        response = self.client.get(self.url)
        result = response.json()

        # assert
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertIsInstance(result,list)
        self.assertEqual(result[0]["name"],self.university.name)

    def test_post_university(self):
        
        # definition
        city = mommy.make(City)
        data = {
            "name": "Unicauca",
            "cod": "12",
            "city": city.id
        }

        # process
        response = self.client.post(self.url, data)
        result = response.json()

        # assert
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        self.assertEqual(result["name"],"Unicauca")

    def test_put_university(self):
        pk = "1"
        data = {
            "name":"Univalle"
        }

        # process
        response = self.client.patch(self.url + f"{pk}/", data=data)
        result = response.json()

        # assert
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(result["name"],"Univalle")

    def test_delete_university(self):
        # process
        response = self.client.delete(self.url + f"{self.university.id}/")

        # assert
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)
        
class TestApitPlaces(APITestCase):

    def setUp(self):

        self.client = APIClient()
        self.country = mommy.make(Country)
        self.state = State.objects.create(name="Cauca",cod="10",country=self.country)
        self.city = City.objects.create(name="Popayan",state=self.state)
        self.university = University.objects.create(name="Unicauca",city=self.city)

    def test_get_country_state(self):

        # process
        url = "/api/country/" + f"{self.country.id}" + "/state/"
        response = self.client.get(url)
        result = response.json()
        
        # assert
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertIsInstance(result,list)
        self.assertEqual(result[0]["name"],self.state.name)

    def test_get_state_city(self):

        # process
        url = "/api/state/" + f"{self.state.id}" + "/city/"
        response = self.client.get(url)
        result = response.json()
        
        # assert
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertIsInstance(result,list)
        self.assertEqual(result[0]["name"],self.city.name)

    def test_get_city_university(self):

        # process
        url = "/api/city/" + f"{self.city.id}" + "/university/"
        response = self.client.get(url)
        result = response.json()
        
        # assert
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertIsInstance(result,list)
        self.assertEqual(result[0]["name"],self.university.name)
