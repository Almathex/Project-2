from application import db

class prize(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    random_string =  db.Column(db.String(40), nullable=False)
    winnings = db.Column(db.String(100), nullable=False)
    
