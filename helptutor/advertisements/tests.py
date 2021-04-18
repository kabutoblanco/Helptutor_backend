from django.test import RequestFactory, TestCase
from django.urls import reverse
from model_mommy import mommy

from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.test import APIRequestFactory, APITestCase

from helptutor.advertisements.api import *
from helptutor.users.models import *

# Create your tests here.

class TestApitAdvertisement(APITestCase):

    def setUp(self):

        self.client = APIClient()

        self.url = "/api/advertisement/"
        
        self.advertisement = mommy.make(Advertisement)

    def test_get_advertisement(self):

        # process
        response = self.client.get(self.url)
        result = response.json()

        # assert
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertIsInstance(result,list)
        self.assertEqual(result[0]["title"],self.advertisement.title)

    def test_post_advertisement(self):
        
        # definition
        student = mommy.make(Student)
        data = {
            "title": "Texto de prueba",
            "description": "Texto de prueba",
            "student": student.id
        }

        # process
        response = self.client.post(self.url, data)
        result = response.json()

        # assert
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        self.assertEqual(result["title"],"Texto de prueba")

    def test_put_advertisement(self):
        pk = "1"
        data = {
            "title":"Texto de prueba 2"
        }

        # process
        response = self.client.patch(self.url + f"{pk}/", data=data)
        result = response.json()

        # assert
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(result["title"],"Texto de prueba 2")

    def test_delete_advertisement(self):
        # process
        response = self.client.delete(self.url + f"{self.advertisement.id}/")

        # assert
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)

class TestApitAnswer(APITestCase):

    def setUp(self):

        self.client = APIClient()

        self.url = "/api/answer/"
        
        self.answer = mommy.make(Answer)

    def test_get_answer(self):

        # process
        response = self.client.get(self.url)
        result = response.json()

        # assert
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertIsInstance(result,list)
        self.assertEqual(result[0]["description"],self.answer.description)

    def test_post_answer(self):
        
        # definition
        advertisement = mommy.make(Advertisement)
        user = mommy.make(User)
        data = {
            "likes": 3,
            "description": "Texto de prueba",
            "advertisement": advertisement.id,
            "user":user.id
        }

        # process
        response = self.client.post(self.url, data)
        result = response.json()

        # assert
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        self.assertEqual(result["likes"],3)

    def test_put_answer(self):
        pk = "1"
        data = {
            "likes":7
        }

        # process
        response = self.client.patch(self.url + f"{pk}/", data=data)
        result = response.json()

        # assert
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(result["likes"],7)

    def test_delete_answer(self):
        # process
        response = self.client.delete(self.url + f"{self.answer.id}/")

        # assert
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)
