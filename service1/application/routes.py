from application import app, db
from flask import render_template, request, Response, redirect, url_for
import requests
from application.models import prizedb


@app.route('/', methods=['GET'])
def home():
    four_numbers = requests.get('http://service2:5001/four_numbers')
    four_letters = requests.get('http://service3:5002/four_letters')
    code = str(four_numbers.text)+four_letters.text
    return render_template('home.html',title='home')

@app.route('/prize/<code>', methods=['GET', 'POST'])
def prize(amount):
    winning = requests.post('http://service4:5003/prize1', data=amount)
    prizes = prizedb(code=amount,reward=winning)    
    db.session.add(prizes)
    db.session.commit()
    return render_template('prize.html', title='prize', amount=amount, winning=winning.text)
