from application import db
from application.models import Prize

db.drop_all()
db.create_all()
