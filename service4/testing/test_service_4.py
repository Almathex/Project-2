from flask import url_for
from flask_testing import TestCase
from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
   
    def test_prize1number(self):
        response = self.client.post(
            url_for('prize1'),
            data="3123BRtf",
            follow_redirects=True
        )
        self.assertIn(b"You win 300 pound", response.data)


    def test_prize1letter(self):
        response = self.client.post(
            url_for('prize1'),
            data="2674LJlw",
            follow_redirects=True
        )
        self.assertIn(b"You win 300 pound", response.data)
    

    def test_prize2letter(self):
        response = self.client.post(
            url_for('prize1'),
            data="9674OJlw",
            follow_redirects=True
        )
        self.assertIn(b"You win 5000 pound", response.data)

    def test_prize3numberandletter(self):
        response = self.client.post(
            url_for('prize1'),
            data="7999AYup",
            follow_redirects=True
        )
        self.assertIn(b"You win 70000 pound", response.data)


    def test_prizenone(self):
        response = self.client.post(
            url_for('prize1'),
            data="2345ZIps",
            follow_redirects=True
        )
        self.assertIn(b"Unfortunatly you didnt win this time!", response.data)

