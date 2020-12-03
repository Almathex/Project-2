from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
import requests_mock
from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_home(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code,200)

    def test_prize(self):

        response = self.client.get(url_for('prize'), amount = "1111AAaa")
        self.assertEqual(response.status_code, 500)

    def test_endprize(self):

        with requests_mock.mock() as g:
            g.get("http://service2:5001/four_numbers", text="1997")
            g.get("http://service3:5002/four_letters", text="ALex")
            g.get("http://service4:5003/price/1997ALex", text="You win £70000")
            response = self.client.get(url_for('prize'))
            self.assertEqual(response.status_code, 200)

