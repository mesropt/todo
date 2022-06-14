import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, APIClient, APITestCase, RequestsClient, CoreAPIClient
from mixer.backend.django import mixer
from users.models import User
from .views import ProjectModelViewSet, ToDoModelViewSet
from .models import Project, ToDo

# ------------ Testing ProjectModelViewSet
class TestProjectModelViewSetAPIRequestFactory(TestCase):
    # 1. APIRequestFactory
    def test_get_list(self): # Метод будет проверять страницу со списком проектов.
        factory = APIRequestFactory()
        request = factory.get('/projects/')
        view = ProjectModelViewSet.as_view({'get': 'list'}) # Передаём во вьюшку get-запрос.
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # 2. APIClient
class TestProjectModelViewSetAPIClient(TestCase):
    def test_get_detail(self):
        project = Project.objects.create(project_name='Построить Пизанскую башню', repository_link='https://www.pnp.ru/in-world/pizanskuyu-bashnyu-stroili-pochti-200-let.html')
        client = APIClient()
        response = client.get(f'/projects/{project.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # 3. APITestCase
class TestProjectModelViewSetAPITestCase(APITestCase):
    def test_get_list(self):
        response = self.client.get('/projects/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # 4. Using mixer
class TestProjectModelViewSetAPITestCaseMixer(APITestCase):
    def test_api_admin(self):
        project = mixer.blend(Project)
        client = APIClient()
        response = client.get(f'/projects/{project.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # 5. Live test (RequestsClient)
class TestProjectModelViewSetLiveTest(APITestCase):
    def test_api_admin(self):
        client = RequestsClient()
        response = self.client.get(f'http://127.0.0.1:8000/projects/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

# ------------ Testing ToDoModelViewSet
class TestToDoModelViewSetAPIRequestFactory(TestCase):
    # 1. APIRequestFactory
    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/projects/')
        view = ToDoModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # 2. APIClient
class TestToDoModelViewSetAPIClient(TestCase):
    def test_get_detail(self):
        user = User.objects.create(username='PriCho', first_name='Priyanka', last_name='Chopra', email='chopra@gmail.com')
        client = APIClient()
        response = client.get(f'/users/{user.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # 3. APITestCase
class TestToDoModelViewSetAPITestCase(APITestCase):
    def test_get_list(self):
        response = self.client.get('/todos/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # 4. Using mixer
class TestToDoModelViewSetAPITestCaseMixer(APITestCase):
    def test_api_admin(self):
        user = mixer.blend(User)
        client = APIClient()
        response = client.get(f'/users/{user.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # 5. Live test (CoreAPIClient)
class TestToDoModelViewSetAPITestCaseLiveTest(APITestCase):
    def test_api_admin(self):
        client = CoreAPIClient()
        response = self.client.get(f'http://127.0.0.1:8000/todos/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)