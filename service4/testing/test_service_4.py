from flask import url_for
from flask_testing import TestCase
from application import app
from unittest.mock import patch
from requests.api import request
import requests

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
   
    def test_prize1number(self):
        response = self.client.post(url_for('prize1'), data="3123BRtf")
        self.assertIn(b'You win £300',response.data)
        self.assertEqual(response.status_code, 200)

    def test_prize1number(self):
        response = self.client.post(url_for('prize1'), data="2674LJlw")
        self.assertIn(b'You win £300',response.data)
        self.assertEqual(response.status_code, 200)    

    def test_prize2letter(self):
        response = self.client.post(url_for('prize1'), data="4674OJlw")
        self.assertIn(b'You win £5000',response.data)
        self.assertEqual(response.status_code, 200)

    def test_prize3numberandletter(self):
        response = self.client.post(url_for('prize1'), data="7999AYup")
        self.assertIn(b'You win £70000',response.data)
        self.assertEqual(response.status_code, 200)

    def test_prizenone(self):
        response = self.client.post(url_for('prize1'), data="2345ZIps")
        self.assertIn(b'Unfortunatly you didnt win this time!',response.data)
        self.assertEqual(response.staus_code, 200)
