from application import app
from flask import request, Response
import string
import random
from random import randint


@app.route('/generator/four_numbers', methods = ['GET'])
def four_numbers():
    return Response((str(random.randint(1000,9999))), mimetype='text/plain')
