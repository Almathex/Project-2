from application import application
from flask import request, Response
from random import randint

@app.route('prize1', methods = ['POST'])
def prize_one():
    prizeusername = request.data.decode('utf-8')
    if prizename[0] == '3' or prizename[5] == 'L':
        prize = 'You win £300'
    elif prizename[0] == '5' or prizename[7] == 'o':
        prize = 'You win £5000'
    elif prizename[0] == '7' or prizename[4] == 'A':
        prize = 'You win £70000'
    else: 
        prize = "Unfortunatly you didnt win this time!"
    return Response(prize, mimetype= 'text/plain')
                