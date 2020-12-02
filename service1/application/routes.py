from application import app, db
from flask import render_template, request, Response, redirect, url_for
import requests
from application.models import Prize


@app.route('/')
@app.route('/home', methods=['GET'])
def home():
    four_numbers = requests.get('http://service2:5001/generator/four_numbers')
    four_letters = requests.get('http://service3:5002/generator/four_letters')
    username = str(four_numbers.text)+four_letters.text
    return render_template('home.html',title='home', username=username)

@app.route('/prize/<prizename>', methods=['GET', 'POST'])
def prize(prizename):
    prize = requests.post('http://service4:5003/prize1', data=prizename)
    info = Prize(username=prizename, prize=prize.text)
    db.session.add(info)
    db.session.commit()
    return render_template('prize.html', title='prize', prizename=prizename, prize=prize.text)
