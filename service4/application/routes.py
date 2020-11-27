from application import application
from flask import request, Response
from random import randint

@app.route('prize_one', methods = ['POST'])
def prize_one():
    prizeusername = request.data.decode('utf-8')
    if prizeusername[0] == '3':
        prize = 'You win £300'
    elif prizeusername[0] == '5':
        prize = 'You win £5000'
    elif prizeusername[0] == '7'
        prize = 'You win £70000'
    else: 
        prize = "Unfortunatly you didnt win this time!"
    return Response(prize, mimetype= 'text/plain')
                