from application import app
from flask import request, Response
import string
import random
from random import randint

@app.route('/generator/four_letters', methods = ['GET'])
def four_letters():
    result = ''.join(random.choices(string.ascii_uppercase,k=2))
    result = ''.join(random.choices(string.ascii_lowercase,k=2))
    return Response(result, mimetype='text/plain')
