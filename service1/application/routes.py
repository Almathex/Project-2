from application import app, db
from flask import render_template, request, Response, redirect, url_for
import requests
from application.models import prize


@app.route('/', methods=['GET'])
def home():
    return render_template('home.html',title='home')

@app.route('/prize/', methods=['GET', 'POST'])
def prize():
    four_numbers = requests.get('http://service2:5001/generator/four_numbers')
    four_letters = requests.get('http://service3:5002/generator/four_letters')
    string = str(four_numbers.text)+four_letters.text
    prize = requests.post('http://service4:5003/prize1', data=string)
    prizes = prize(
            random_string = str(string),
            winnings = prize
    )    
    db.session.add(prizes)
    db.session.commit()
    return render_template('prize.html', title='prize', string=string, prize=prize.text)
