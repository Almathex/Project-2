from application import app
from flask import request, Response
import string
import random
from random import randint

@app.route('/four_letters', methods = ['GET'])
def four_letters():
    result = ''.join(random.choices(string.ascii_uppercase,k=2))
    result1 = ''.join(random.choices(string.ascii_lowercase,k=2))
    result2 = result + result1
    return Response(result2, mimetype='text/plain')
