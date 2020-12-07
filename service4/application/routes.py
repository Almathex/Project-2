from application import app
from flask import request, Response
from random import randint

#@app.route('/prize1', methods = ['POST'])
#def prize1():
#    code = request.data.decode('utf-8')
#    if code[0] == '3' or code[4] == 'L':
#        winning = 'You won 300 pounds!'
#    elif code[0] == '9':
#        winning = 'You won 5000 pounds!'
#    elif code[0] == '7' and code[4] == 'A':
#        winning = 'You won 70000 pounds!'
#    else: 
#        winning = "Unfortunatly you didnt win this time!"
#    return Response(winning, mimetype= 'text/plain')
@app.route('/prize2', methods = ['POST'])
def prize2():
   code = request.data.decode('utf-8')
   if code[0] == '1' or code[4] == 'E':
      winning = 'You won a laptop!'
   elif code[0] == '2':
      winning = 'You won a car!'
   elif code [0] == '4':
      winning = 'You won a house!'
   else:
      winning = "Unfortunatly you didnt win this time!"
   return Response(winning, mimetype= 'text/plain')                
