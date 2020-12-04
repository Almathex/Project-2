from flask import url_for
from flask_testing import TestCase
from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
   
    def test_prize1number(self):
        response = self.client.post(url_for('prize1'), data="3123BRtf", followredirects=True)
        self.assertIn(b'You win £300',response.data)

    def test_prize1number(self):
        response = self.client.post(url_for('prize1'), data="2674LJlw", followredirects=True)
        self.assertIn(b'You win £300',response.data)    

    def test_prize2letter(self):
        response = self.client.post(url_for('prize1'), data="4674OJlw", followredirects=True )
        self.assertIn(b'You win £5000',response.data)

    def test_prize3numberandletter(self):
        response = self.client.post(url_for('prize1'), data="7999AYup", followredirects=True)
        self.assertIn(b'You win £70000',response.data)

    def test_prizenone(self):
        response = self.client.post(url_for('prize1'), data="2345ZIps", followredirects=True)
        self.assertIn(b'Unfortunatly you didnt win this time!',response.data)
