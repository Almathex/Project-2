from application import app, db
from flask import render_template, request, Response
import requests
from application.models import Prize

@app.route('/', methods=['GET'])
def home():
    four_numbers = requests.get('http://service2:5001/generator/four_numbers')
    four_letters = requests.get('http://service3:5002/generator/four_letters')
    username = str(four_numbers.text)+four_letters.text
    return render_template('home.html',title='home', username=username)

