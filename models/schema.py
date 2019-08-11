from db import db


class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String(1000))
    category = db.Column(db.String(255))

