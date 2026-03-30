from . import db

class Property(db.Model):
    __tablename__ = 'properties'

    id = db.Column(db.Integer, primary_key=True)   # auto-increment ID
    title = db.Column(db.String(80))
    description = db.Column(db.String(80))
    bedrooms = db.Column(db.String(80), unique=True)
    bathrooms = db.Column(db.String(128))
    price = db.Column(db.String(128))
    type = db.Column(db.String(128))
    location = db.Column(db.String(128))
    photo = db.Column(db.String(128))  # store filename
    
    def __init__(self, first_name, last_name, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        