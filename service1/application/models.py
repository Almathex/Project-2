from application import db

class Prize(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    random_string =  db.Column(db.String(40), nullable=False)
    prize = db.Column(db.String(100), nullable=False)
    
