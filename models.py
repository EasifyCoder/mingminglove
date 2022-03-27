from db import db


class User(db.Model):
    __tablename__ = 'user'

    username = db.Column(db.String(20), primary_key=True, unique=True, index=True)
    password = db.Column(db.String(30))
    gender = db.Column(db.Integer)
    email = db.Column(db.String(50))
    telephone = db.Column(db.String(11))

class HundredThings(db.Model):
    __tablename__ = 'hundredthings'

    id = db.Column(db.String(100), primary_key=True)
    username = db.Column(db.String(20), index=True)
    thing = db.Column(db.String(20))
    done = db.Column(db.Integer)

class DaysMatter(db.Model):
    __tablename__ = 'daysmatter'

    username = db.Column(db.String(20), primary_key=True, index=True)
    description = db.Column(db.String(10))
    date = db.Column(db.Date)












