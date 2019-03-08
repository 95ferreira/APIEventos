from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from eventManager.models import Type

# Create your tests here.

class ClientEventOperationsTest(APITestCase):

	def login(self):
		username = 'test'
		email = 'test@test.com'
		password = 'testtest'
		user = User.objects.create_user(username, email, password)
		self.assertTrue(self.client.login(username=username, password=password))

	def test_login_client(self):
		url = '/client/'
		self.login()
		response = self.client.get(url, follow=True)
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "client")
		self.client.logout()

	def test_open_client_page_not_log(self):
		response = self.client.get('/client/', follow=True)
		self.assertEqual(response.status_code, 401) 

	def test_auth_user_insert_event(self):
		url = '/client/create'
		tp = Type.objects.create(tp="test1")
		self.login()
		data = {"text":"eventTextTest", "numInvitation":20, 'url':'newEventTest', 'tp':tp.id}
		response = self.client.post(url, data, format='json')
		self.assertEqual(response.status_code, 201, msg=response.data)
		self.client.logout()

	def test_not_auth_user_insert_event(self):
		url = '/client/create'
		tp = Type.objects.create(tp="test1")
		data = {"text":"eventTextTest", "numInvitation":20, 'url':'newEventTest', 'tp':tp.id}
		response = self.client.post(url, data, format='json')
		self.assertEqual(response.status_code, 401, msg=response.data)
