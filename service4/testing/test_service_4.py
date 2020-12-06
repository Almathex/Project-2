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
        self.assertIn(b"You won 300 pounds!", response.data)


    def test_prize1letter(self):
        response = self.client.post(
            url_for('prize1'),
            data="2674LJlw",
            follow_redirects=True
        )
        self.assertIn(b"You won 300 pounds!", response.data)
    

    def test_prize2letter(self):
        response = self.client.post(
            url_for('prize1'),
            data="9674OJlw",
            follow_redirects=True
        )
        self.assertIn(b"You won 5000 pounds!", response.data)

    def test_prize3numberandletter(self):
        response = self.client.post(
            url_for('prize1'),
            data="7999AYup",
            follow_redirects=True
        )
        self.assertIn(b"You won 70000 pounds!", response.data)


    def test_prizenone(self):
        response = self.client.post(
            url_for('prize1'),
            data="2345ZIps",
            follow_redirects=True
        )
        self.assertIn(b"Unfortunatly you didnt win this time!", response.data)

#    def test_prizelapnumber(self):
#        response = self.client.post(
#            url_for('prize2'),
#            data="1123BRtf",
#            follow_redirects=True
#        )
#        self.assertIn(b"You won a laptop!", response.data)

#    def test_prizelapletter(self):
#        response = self.client.post(
#            url_for('prize2'),
#            data="2674EJlw",
#            follow_redirects=True
#        )
#        self.assertIn(b"You won a laptop!", response.data)
#
#    def test_prizecarnumber(self):
#        response = self.client.post(
#            url_for('prize2'),
#            data="2674WJlw",
#            follow_redirects=True
#        )
#        self.assertIn(b"You won a car!", response.data)
#   
#   def test_prizehouse(self):
#       response = self.client.post(
#           url_for('prize2'),
#           data="4444CAsh",
#           follow_redirects=True
#       )
#       self.assertIn(b"You won a house!", response.data)