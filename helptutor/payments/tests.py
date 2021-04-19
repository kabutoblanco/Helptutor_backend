from django.test import RequestFactory, TestCase
from django.urls import reverse
from model_mommy import mommy

from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.test import APIRequestFactory, APITestCase

from helptutor.payments.api import *
from helptutor.services.models import *

class TestApitPayment(APITestCase):

    def setUp(self):

        self.client = APIClient()

        self.url = "/api/payment/"
        
        self.payment = mommy.make(Payment)
    
    def test_get_payment(self):

        # process
        response = self.client.get(self.url)
        result = response.json()
        
        # assert
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertIsInstance(result,list)
        self.assertEqual(result[0]["num_invoice"],self.payment.num_invoice)

    def test_post_payment(self):
        
        # definition
        contract = mommy.make(Contract)
        data = {
            "num_invoice":"Testo de prueba",
            "contract":contract.id
        }

        # process
        response = self.client.post(self.url, data)
        result = response.json()

        # assert
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        self.assertEqual(result["num_invoice"],data["num_invoice"])

    def test_put_payment(self):
        pk = self.payment.id
        data = {
            "payment":10000
        }

        # process
        response = self.client.patch(self.url + f"{pk}/", data=data)
        result = response.json()

        # assert
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(result["payment"],data["payment"])

    def test_delete_payment(self):

        # process
        response = self.client.delete(self.url + f"{self.payment.id}/")

        # assert
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)
