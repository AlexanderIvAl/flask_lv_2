from api import db
from email.policy import default


class AuthorModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32),)
    surname = db.Column(db.String(32),)
    quotes = db.relationship('QuoteModel', backref='author', lazy='dynamic')

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
