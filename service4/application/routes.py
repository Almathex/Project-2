from application import app
from flask import request, Response
from random import randint

@app.route('/prize1', methods = ['POST'])
def prize1():
    code = request.data.decode('utf-8')
    if code[0] == '3' or code[4] == 'L':
        winning = 'You win 300 pound'
    elif code[0] == '9':
        winning = 'You win 5000 pound'
    elif code[0] == '7' and code[4] == 'A':
        winning = 'You win 70000 pound'
    else: 
        winning = "Unfortunatly you didnt win this time!"
    return Response(winning, mimetype= 'text/plain')
                
