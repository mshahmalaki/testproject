from auth import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), index=True, unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    address = db.Column(db.String(50))
