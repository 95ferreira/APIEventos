from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from model_mommy import mommy
from eventManager.models import Event, Type, Prog, Service, Images, Editor, Location
from eventManager.serializers import EventSerializer
import random, string, json, datetime

# Create your tests here.

class ClientBaseManagerOperationsTests():

	USERNAME1 = 'testCase1'
	USERNAME2 = 'testCase2'
	EMAIL1 = 'test1'
	EMAIL2 = 'test2'
	PASSWORD = 'testtest'
	BASEURL = "APITestCaseEvent"

	classSet = None
	data = None
	badData = None
	url = None

	def setUp(self):
		user = User.objects.create_user(self.USERNAME1, self.EMAIL1, self.PASSWORD)
		event = mommy.make(Event, url=self.BASEURL, user=user)
		event.save()
		selectClass = mommy.make(self.classSet, eventFk_id=event.id)
		self.idClass = '/' + str(selectClass.id)
		user2 = User.objects.create_user(self.USERNAME2, self.EMAIL2, self.PASSWORD)
		
	def login(self):
		self.assertTrue(self.client.login(username=self.USERNAME1, password=self.PASSWORD))

	def login2(self):
		self.client.logout()
		self.assertTrue(self.client.login(username=self.USERNAME2, password=self.PASSWORD))

	def test_auth_user_bad_data_insert_(self):
		self.login()
		finalUrl = '/' + self.BASEURL + self.url
		response = self.client.post(finalUrl, self.badData, format='json')
		self.assertEqual(response.status_code, 400, msg=self.url+str(response.content))
		self.client.logout()

	def test_auth_user_insert_(self):
		self.login()
		finalUrl = '/' + self.BASEURL + self.url
		response = self.client.post(finalUrl, self.data, format='json')
		self.assertEqual(response.status_code, 201, msg=self.url+str(response.content))
		self.client.logout()

	def test_auth_user_update_(self):
		self.login()
		finalUrl = '/' + self.BASEURL + self.url + self.idClass
		response = self.client.patch(finalUrl, self.data, format='json')
		self.assertEqual(response.status_code, 200, msg=self.url+str(response.content))
		self.client.logout()

	def test_auth_user_bad_data_update(self):
		self.login()
		finalUrl = '/' + self.BASEURL + self.url + self.idClass
		response = self.client.patch(finalUrl, self.badData, format='json')
		self.assertEqual(response.status_code, 400, msg=self.url+str(response.content))
		self.client.logout()

	def test_auth_user_delete_(self):
		self.login()
		finalUrl = '/' + self.BASEURL + self.url + self.idClass
		response = self.client.delete(finalUrl)
		self.assertEqual(response.status_code, 204, msg=self.url+str(response.content))
		self.client.logout()

	def test_not_auth_user_insert_(self):
		finalUrl = '/' + self.BASEURL + self.url
		response = self.client.post(finalUrl, self.data, format='json')
		self.assertEqual(response.status_code, 401, msg=self.url+str(response.content))

	def test_not_auth_user_update_(self):
		finalUrl = '/' + self.BASEURL + self.url + self.idClass
		response = self.client.patch(finalUrl, self.data, format='json')
		self.assertEqual(response.status_code, 401, msg=self.url+str(response.content))

	def test_not_auth_user_delete_(self):
		finalUrl = '/' + self.BASEURL + self.url + self.idClass
		response = self.client.delete(finalUrl)
		self.assertEqual(response.status_code, 401, msg=self.url+str(response.content))

	def test_other_auth_user_insert_(self):
		self.login2()
		finalUrl = '/' + self.BASEURL + self.url
		response = self.client.post(finalUrl, self.data, format='json')
		self.assertEqual(response.status_code, 403, msg=self.url+str(response.content))
		self.client.logout()

	def test_other_auth_user_update_(self):
		self.login2()
		finalUrl = '/' + self.BASEURL + self.url + self.idClass
		response = self.client.patch(finalUrl, self.data, format='json')
		self.assertEqual(response.status_code, 403, msg=self.url+str(response.content))
		self.client.logout()

	def test_other_auth_user_delete_(self):
		self.login2()
		finalUrl = '/' + self.BASEURL + self.url + self.idClass
		response = self.client.delete(finalUrl)
		self.assertEqual(response.status_code, 403, msg=self.url+str(response.content))
		self.client.logout()

class ProgTests(APITestCase, ClientBaseManagerOperationsTests):

	classSet = Prog
	data = {"time":"12:00:00","descr":"test1"}
	badData = {"time":"asdwasdw","desc":"teasdst1"}
	url = '/prog'

	def setUp(self):
		ClientBaseManagerOperationsTests.setUp(self)

class ServiceTests(APITestCase, ClientBaseManagerOperationsTests):

	classSet = Service
	data = {
		"name":"testService",
		"address":"tallugar",
		"email":"test@tst.com",
		"descr":"Fazalgo"
	}
	badData = {
		"name":"testService",
		"address":"tallugar",
		"email":"tes"
	}
	url = '/service'

	def setUp(self):

		ClientBaseManagerOperationsTests.setUp(self)

class LocationTests(APITestCase, ClientBaseManagerOperationsTests):

	classSet = Location
	data = {"address":"testAddr", "num":"123"}
	badData = {"address":"test", "num":"badnum"}
	url = '/location'

	def setUp(self):

		ClientBaseManagerOperationsTests.setUp(self)

class EditorsTests(APITestCase, ClientBaseManagerOperationsTests):

	classSet = Editor
	
	data = {"user":{"username":"testEditor", "email":"testEditor@test.com", "password":"testTest"}}
	badData = {"user":{"username":"testEditor", "email":"test", "password":"testTest"}}
	url = '/editor'

	def setUp(self):

		ClientBaseManagerOperationsTests.setUp(self)

class EditorBaseTests():

	def setUp(self):
		eventUser = User.objects.create_user("testuser", "testemail@email.com", "testtest")
		user = User.objects.create_user(self.USERNAME1, self.EMAIL1, self.PASSWORD)
		event = mommy.make(Event, url=self.BASEURL, user=eventUser)
		event.save()
		selectClass = mommy.make(self.classSet, eventFk_id=event.id)
		self.idClass = '/' + str(selectClass.id)
		user2 = User.objects.create_user(self.USERNAME2, self.EMAIL2, self.PASSWORD)
		editor = Editor.objects.create(user=user, eventFk=event)

class EditorProgTests(EditorBaseTests, ProgTests):
	pass

class EditorServiceTests(EditorBaseTests, ServiceTests):
	pass

class EditorLocationTests(EditorBaseTests, LocationTests):
	pass


class ClientOperationsTest(APITestCase):

	def login(self):
		self.assertTrue(self.client.login(username='test', password='testtest'))

	def login2(self):
		User.objects.create_user('test2', 'test2@test.com', 'testtest')
		self.assertTrue(self.client.login(username='test', password='testtest'))

	def setUp(self):
		user = User.objects.create_user('test', 'test@test.com', 'testtest')
		url = "APITestCaseEvent"
		self.event = mommy.make(Event, url=url, user=user)
		self.event.save()
		self.url = "/" + url

	def test_admin_event_page(self):
		self.login()
		response = self.client.get(self.url+'/admin')
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'test')
		self.client.logout()

	def test_not_log_admin_event_page(self):
		response = self.client.get(self.url+'/admin')
		self.assertEqual(response.status_code, 401)

	def test_diferent_client_admin_event_page(self):
		self.login2()
		response = self.client.get(self.url+'/admin')
		self.assertEqual(response.status_code, 403)
		self.client.logout()

	def test_auth_user_update_event(self):
		self.login()
		data = {'text':'textChange'}
		response = self.client.patch(self.url, data, format='json')
		self.assertEqual(response.status_code, 200)
		self.client.logout()

	def test_not_auth_user_update_event(self):
		data = {'text':'textChange'}
		response = self.client.patch(self.url, data, format='json')
		self.assertEqual(response.status_code, 401)

	def test_other_auth_user_update_event(self):
		self.login2()
		data = {'text':'textChange'}
		response = self.client.patch(self.url, data, format='json')
		self.assertEqual(response.status_code, 403)
		self.client.logout()

	def test_auth_user_delete_event(self):
		self.login()
		response = self.client.delete(self.url)
		self.assertEqual(response.status_code, 204)
		self.client.logout()

	def test_other_auth_user_delete_event(self):
		self.login2()
		response = self.client.delete(self.url)
		self.assertEqual(response.status_code, 403)
		self.client.logout()

	def test_not_auth_user_delete_event(self):
		response = self.client.delete(self.url)
		self.assertEqual(response.status_code, 401)

	def test_image_upload_and_delete(self):
		self.login()
		f = open('eventManager/tests/imgtest.png', 'rb')
		data = {'image':f}
		response = self.client.post(self.url+'/image', data, format='multipart')
		self.assertEqual(response.status_code, 201)
		#response = self.client.delete(self.url+'/image/1')
		#self.assertEqual(response.status_code, 204)	
		self.client.logout()

	def test_bad_image_upload(self):
		self.login()
		f = open('eventManager/tests/file', 'rb')
		data = {'image':f}
		response = self.client.post(self.url+'/image', data, format='multipart')
		self.assertEqual(response.status_code, 400)
		self.client.logout()	
