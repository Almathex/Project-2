from application import app
from flask import request, Response
from random import randint

@app.route('/prize1', methods = ['POST'])
def prize1():
    amount = request.data.decode('utf-8')
    if amount[0] == '3' or amount[4] == 'L':
        prize = 'You win 300 pound'
    elif amount[4] == 'O':
        prize = 'You win 5000 pound'
    elif amount[0] == '7' and amount[4] == 'A':
        prize = 'You win 70000 pound'
    else: 
        prize = "Unfortunatly you didnt win this time!"
    return Response(prize, mimetype= 'text/plain')
                
