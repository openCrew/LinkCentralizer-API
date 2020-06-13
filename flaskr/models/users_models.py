from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    sobrenome = db.Column(db.String)
    catalog = db.relationship('Catalog', backref='user', lazy=True)
