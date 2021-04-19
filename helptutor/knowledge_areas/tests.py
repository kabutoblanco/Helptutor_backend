from django.test import RequestFactory, TestCase
from django.urls import reverse
from model_mommy import mommy
  
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.test import APIRequestFactory, APITestCase

from helptutor.knowledge_areas.api import *
from helptutor.users.models import Tutor, Student, Moderator

class TestApitKnowledgeArea(APITestCase):

    def setUp(self):

        self.client = APIClient()

        self.url = "/api/knowledgearea/"
        
        self.knowledgearea = mommy.make(KnowledgeArea)
    
    def test_get_knowledgearea(self):

        # process
        response = self.client.get(self.url)
        result = response.json()
        
        # assert
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertIsInstance(result,list)
        self.assertEqual(result[0]["name"],self.knowledgearea.name)

    def test_post_knowledgearea(self):
        
        # definition
        data = {
            "name":"Testo de prueba",
            "description":"Testo de prueba",
            "knowledge_area":self.knowledgearea.id
        }

        # process
        response = self.client.post(self.url, data)
        result = response.json()

        # assert
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        self.assertEqual(result["name"],data["name"])

    def test_put_knowledgearea(self):
        pk = self.knowledgearea.id
        data = {
            "name":"Matematicas"
        }

        # process
        response = self.client.patch(self.url + f"{pk}/", data=data)
        result = response.json()

        # assert
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(result["name"],data["name"])

    def test_delete_knowledgearea(self):

        # process
        response = self.client.delete(self.url + f"{self.knowledgearea.id}/")

        # assert
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)

class TestApitKnowledgeArea_Tutor(APITestCase):

    def setUp(self):

        self.client = APIClient()

        self.url = "/api/knowledgearea_tutor/"
        
        self.knowledgearea_tutor = mommy.make(KnowledgeArea_Tutor)
    
    def test_get_knowledgearea_tutor(self):

        # process
        response = self.client.get(self.url)
        result = response.json()
        
        # assert
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertIsInstance(result,list)
        self.assertEqual(result[0]["tags"],self.knowledgearea_tutor.tags)
    """
    def test_post_knowledgearea_tutor(self):
        
        # definition
        tutor = mommy.make(Tutor)
        knowledge_area = mommy.make(KnowledgeArea)
        data = {
            "tags":"Testo de prueba",
            "description":"Testo de prueba",
            "knowledge_area":knowledge_area.id,
            "tutor":tutor.id
        }

        # process
        response = self.client.post(self.url, data)
        result = response.json()

        # assert
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        self.assertEqual(result["tags"],data["tags"])
    """
    def test_put_knowledgearea_tutor(self):
        pk = self.knowledgearea_tutor.id
        data = {
            "description":"Matematicas"
        }

        # process
        response = self.client.patch(self.url + f"{pk}/", data=data)
        result = response.json()

        # assert
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(result["description"],data["description"])

    def test_delete_knowledgearea_tutor(self):

        # process
        response = self.client.delete(self.url + f"{self.knowledgearea_tutor.id}/")

        # assert
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)

class TestApitKnowledgeArea_Student(APITestCase):

    def setUp(self):

        self.client = APIClient()

        self.url = "/api/knowledgearea_student/"
        
        self.knowledgearea_student = mommy.make(KnowledgeArea_Student)
    
    def test_get_knowledgearea_student(self):

        # process
        response = self.client.get(self.url)
        result = response.json()
        
        # assert
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertIsInstance(result,list)
        self.assertEqual(result[0]["knowledge_area"],self.knowledgearea_student.knowledge_area.id)
    
    def test_post_knowledgearea_student(self):
        
        # definition
        knowledge_area_1 = mommy.make(KnowledgeArea)
        student_1 = mommy.make(Student)
        data = {
            "knowledge_area":knowledge_area_1.id,
            "student":student_1.id
        }

        # process
        response = self.client.post(self.url, data)
        result = response.json()

        # assert
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        self.assertEqual(result["knowledge_area"],data["knowledge_area"])
    
    def test_put_knowledgearea_student(self):
        pk = self.knowledgearea_student.id
        knowledge_area_2 = mommy.make(KnowledgeArea)
        data = {
            "knowledge_area":knowledge_area_2.id,
        }

        # process
        response = self.client.patch(self.url + f"{pk}/", data=data)
        result = response.json()

        # assert
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(result["knowledge_area"],data["knowledge_area"])

    def test_delete_knowledgearea_student(self):

        # process
        response = self.client.delete(self.url + f"{self.knowledgearea_student.id}/")

        # assert
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)

class TestApitCertificate(APITestCase):

    def setUp(self):

        self.client = APIClient()

        self.url = "/api/certificate/"
        
        self.certificate = mommy.make(Certificate)
    
    def test_get_certificate(self):

        # process
        response = self.client.get(self.url)
        result = response.json()
        
        # assert
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertIsInstance(result,list)
        self.assertEqual(result[0]["name"],self.certificate.name)
    """
    def test_post_certificate(self):
        
        # definition
        knowledge_area_tutor = mommy.make(KnowledgeArea_Tutor)
        moderator = mommy.make(Moderator)
        data = {
            "name": "string",
            "entity": "string",
            "issue_year": "2021-04-18",
            "description": "string",
            "knowledge_area_tutor": knowledge_area_tutor.id,
            "moderator": moderator.id
        }

        # process
        response = self.client.post(self.url, data)
        result = response.json()

        # assert
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        self.assertEqual(result["name"],data["name"])
    """
    def test_put_certificate(self):
        pk = self.certificate.id
        data = {
            "name":"Texto de prueba 2",
        }

        # process
        response = self.client.patch(self.url + f"{pk}/", data=data)
        result = response.json()

        # assert
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(result["name"],data["name"])
    """
    def test_delete_certificate(self):

        # process
        response = self.client.delete(self.url + f"{self.certificate.id}/")

        # assert
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)
    """
class TestApitContent(APITestCase):

    def setUp(self):

        self.client = APIClient()

        self.url = "/api/content/"
        
        self.content = mommy.make(Content)
    
    def test_get_content(self):

        # process
        response = self.client.get(self.url)
        result = response.json()
        
        # assert
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertIsInstance(result,list)
        self.assertEqual(result[0]["name"],self.content.name)
    """
    def test_post_content(self):
        
        # definition
        knowledge_area_tutor_1 = mommy.make(KnowledgeArea_Tutor)
        data = {
            "name":"Texto de prueba",
            "description":"Texto de prueba",
            "knowledge_area_tutor":knowledge_area_tutor_1.id
        }

        # process
        response = self.client.post(self.url, data)
        result = response.json()

        # assert
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        self.assertEqual(result["name"],data["name"])
    """
    def test_put_content(self):
        pk = self.content.id
        data = {
            "name":"Texto de prueba",
        }

        # process
        response = self.client.patch(self.url + f"{pk}/", data=data)
        result = response.json()

        # assert
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(result["name"],data["name"])

    def test_delete_content(self):

        # process
        response = self.client.delete(self.url + f"{self.content.id}/")

        # assert
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)

class TestApitKnowledge_Areas(APITestCase):

    def setUp(self):

        self.client = APIClient()
        self.tutor = mommy.make(Tutor)
        self.knowledge_area = mommy.make(KnowledgeArea)
        """
        self.sub_knowledge_area = KnowledgeArea.objects.create(
            name="Texto de prueba",
            level=1,
            description="Texto de prueba",
            knowledge_area=10
        )
        """
        self.speciality = KnowledgeArea_Tutor.objects.create(
            tags="Texto de prueba",
            description="Texto de prueba",
            knowledge_area=self.knowledge_area,
            tutor=self.tutor
        )
    """
    def test_get_knowledgearea_knowledgearea(self):

        # process
        print("1. ",self.knowledge_area.id)
        url = "/api/knowledgearea/10/knowledgearea/"
        response = self.client.get(url)
        result = response.json()
        
        # assert
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertIsInstance(result,list)
        self.assertEqual(result[0]["name"],self.sub_knowledge_area.name)
    """
    def test_get_tutor_speciality(self):

        # process
        url = "/api/tutor/" + f"{self.tutor.id}" + "/speciality/"
        response = self.client.get(url)
        result = response.json()
        
        # assert
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertIsInstance(result,list)
        self.assertEqual(result[0]["tags"],self.speciality.tags)
