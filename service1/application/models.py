from application import db

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), nullable=False)
    prize = db.Column(db.String(100), nullable=False)
    
