from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from model_mommy import mommy
from eventManager.models import Event, Type, Prog, Service, Images, Editor, Location
from eventManager.serializers import EventSerializer
import random, string, json, datetime

class DataValidationTests(APITestCase):

	def setUp(self):
		url = "APITestCaseEvent"
		event = mommy.make(Event, url=url)
		event.save()
		self.url = "/" + url + '/guestconfirm'
		self.letters = string.ascii_letters

	def test_good_data_Guest_return_ok(self):
		data = {"name": "TestName", "tel":"55999999999", "email":"test@test.com", "companions":[]}
		response = self.client.post(self.url, data, format='json')
		self.assertEqual(response.status_code, 201, msg=response.content)

	def test_bad_event_good_data_Guest_and_Companion_return(self):
		companion_data = {"name":"testComp","tp":"1"}
		data = {"name": "TestName", "tel":"55999999999", "email":"test@test.com","companions":companion_data}
		response = self.client.post('/eventfail/guestconfirm', data, format='json')
		self.assertEqual(response.status_code, 404)

	def test_null_data(self):
		response = self.client.post(self.url, {})
		self.assertEqual(response.status_code, 400)

	def test_random_data(self):
		data = {"teste": "".join(random.choice(self.letters) for i in range(40))}
		response = self.client.post(self.url, data, format='json')
		self.assertEqual(response.status_code, 400)

	def test_larger_data(self):
		data = {"name" : ''.join(random.choice(self.letters) for i in range(200)),
			"tel": ''.join(random.choice(self.letters) for i in range(200)),
			"email": ''.join(random.choice(self.letters) for i in range(200))}
		response = self.client.post(self.url, data, format='json')
		self.assertEqual(response.status_code, 400)

	def test_bad_email_data(self):
		data = {"name" : "foo",
			"tel": '53984984444',
			"email": 'testBadEmail'}
		response = self.client.post(self.url, data, format='json')
		self.assertEqual(response.status_code, 400)

	def test_bad_adult_kid_select_field_data(self):
		data = {"name": "TestName", "tel":"55999999999", "email":"test@test.com","companions":{"name":"testComp","tp":"asd"}}
		response = self.client.post(self.url, data, format='json')
		self.assertEqual(response.status_code, 400)

