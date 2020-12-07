from flask import url_for
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_testing import TestCase
from unittest.mock import patch
from requests.api import request
import requests
import unittest
import requests_mock
from application.models import prizedb
from application import app, db

class TestBase(TestCase):
    def create_app(self):
        config_name = 'test'
        app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
        return app
    
    def setUp(self):
        db.session.commit()
        db.drop_all()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestResponse(TestBase):
    def test_home(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code,200)

    def test_prize(self):

        response = self.client.get(url_for('prize'), code = "1111AAaa")
        self.assertEqual(response.status_code, 500)

    def test_endprize(self):

        with requests_mock.mock() as g:
            g.get("http://service2:5001/four_numbers", text="1997")
            g.get("http://service3:5002/four_letters", text="ALex")
            g.get("http://service4:5003/price/1997ALex", text="You win £70000")
            response = self.client.get(url_for('prize'), follow_redirects=True)
            self.assertEqual(response.status_code, 200)
