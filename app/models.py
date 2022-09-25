from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    phone = db.Column(db.Integer)

class Seller(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(1000))
    password = db.Column(db.String(1000))
    name = db.Column(db.String(1000))
    username = db.Column(db.String(1000), unique=True)
    phone = db.Column(db.Integer)
    best_printer = []


