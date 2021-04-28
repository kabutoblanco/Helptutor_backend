from django.test import RequestFactory, TestCase
from django.urls import reverse
from model_mommy import mommy

# Python
import json
  
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.test import APIRequestFactory, APITestCase

from helptutor.users.models import Student
from django.contrib.auth.models import User

# Create your tests here.

class TestApitOffer(APITestCase):

    def setUp(self):

        # Creamos un usuario y generamos el acceso a la api para hacer pruebas de forma general
        user = User(
            email='testing_login@cosasdedevs.com',
            first_name='Testing',
            last_name='Testing',
            username='testing_login'
        )
        user.set_password('admin123')
        user.save()
        
        client = APIClient()
        response = client.post(
                '/auth/user', {
                'email': 'testing_login@cosasdedevs.com',
                'password': 'admin123',
            },
            format='json'
        )

        result = json.loads(response.content)
        self.access_token = result['access_token']
        self.user = user
        self.url = "/api/offer/"

    """
    def test_get_offer(self):

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + self.access_token)

        # process
        response = self.client.get(self.url)
        result = response.json()
        
        # assert
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertIsInstance(result,list)
        self.assertEqual(result[0]["title"],self.offer.title)
    """
    def test_post_offer(self):

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + self.access_token)
        
        # definition
        student = mommy.make(Student)
        data = {
            "title":"Testo de prueba",
            "description":"Testo de prueba",
            "student":student.id
        }

        # process
        response = self.client.post(self.url, data)
        result = response.json()

        # assert
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        self.assertEqual(result["title"],data["title"])
    """
    def test_put_offer(self):
        pk = self.offer.id
        data = {
            "title":"Matematicas"
        }

        # process
        response = self.client.patch(self.url + f"{pk}/", data=data)
        result = response.json()

        # assert
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(result["title"],data["title"])
    
    def test_delete_offer(self):

        # process
        response = self.client.delete(self.url + f"{self.offer.id}/")

        # assert
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)
    """
