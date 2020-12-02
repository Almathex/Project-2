from application import app
from flask import request, Response
from random import randint

@app.route('/prize1', methods = ['POST'])
def prize1():
    amount = request.data.decode('utf-8')
    if amount[0] == '3' or amount[4] == 'L':
        prize = 'You win £300'
    elif amount[0] == '5' or amount[4] == 'o':
        prize = 'You win £5000'
    elif amount[0] == '7' or amount[4] == 'A':
        prize = 'You win £70000'
    else: 
        prize = "Unfortunatly you didnt win this time!"
    return Response(prize, mimetype= 'text/plain')
                
