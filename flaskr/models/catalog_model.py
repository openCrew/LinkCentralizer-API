from app import db
from .users_models import User


class Catalog(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
                        nullable=False)
    background = db.Column(db.Integer, db.ForeignKey('user.id'),
                           nullable=False)
    logo = db.Column(db.Integer, db.ForeignKey('user.id'),
                     nullable=False)
    links = db.relationship('Links', backref='catalog', lazy=True)


class Background(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    color = db.Column(db.ARRAY(db.String), nullable=True)
    images = db.Column(db.ARRAY(db.String), nullable=True)
    catalog = db.relationship('Catalog', backref='background', lazy=True)


class Links(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=True)
    value = db.Column(db.String, nullable=True)
    catalog = db.Column(db.Integer, db.ForeignKey('catalog.id'),
                        nullable=False)


class Logo(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url = db.Column(db.String, nullable=True)
    catalog = db.relationship('Catalog', backref='logo', lazy=True)


