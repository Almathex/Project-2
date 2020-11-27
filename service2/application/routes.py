from application import app
from flask import request, Response
import random


@app.route('/generator/four_numbers', methods = ['GET'])
def four_numbers():
    return Response((str(random.randint(1000),(9999))), mimetype='text/plain')




