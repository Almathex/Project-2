from application import app, db
from flask import render_template, request, Response, redirect, url_for
import requests
from application.models import Prize


@app.route('/', methods=['GET'])
def home():
    four_numbers = requests.get('http://localhost:5001/generator/four_numbers')
    four_letters = requests.get('http://localhost:5002/generator/four_letters')
    string = str(four_numbers.text)+""+four_letters.text
    return render_template('home.html',title='home', string=string)

@app.route('/prize/<amount>', methods=['GET', 'POST'])
def prize(amount):
    prize = requests.post('http://service4:5003/prize1', data=amount)
    info = Prize(string=string, prize=str(prize.text))
    db.session.add(info)
    db.session.commit()
    return render_template('prize.html', title='prize', amount=amount, prize=prize.text)
