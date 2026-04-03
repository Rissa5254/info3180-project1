from . import db

class Property(db.Model):
    __tablename__ = 'properties'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)   # auto-increment ID
    title = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text, nullable=False)
    bedrooms = db.Column(db.Integer, nullable=False)
    bathrooms = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Numeric(precision=18, scale=2), nullable=False)
    type = db.Column(db.String(30), nullable=False)
    location = db.Column(db.String(128), nullable=False)
    photo = db.Column(db.String(120), nullable=False)  # store filename
    
    def __init__(self, title, description, bedrooms, bathrooms, price, type, location, photo):
        self.title = title
        self.description = description
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.price = price
        self.type = type
        self.location = location
        self.photo = photo
        