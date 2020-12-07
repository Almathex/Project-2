from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)
pw = getenv('MYSQL_ROOT_PASSWORD')
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:' + pw + '@database:3306/database'
db = SQLAlchemy(app)
from application import routes
