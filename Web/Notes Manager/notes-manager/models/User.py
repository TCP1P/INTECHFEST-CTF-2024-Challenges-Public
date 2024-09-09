from app import db
from sqlalchemy import *

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=True)
    gender = db.Column(Enum('male', 'female', 'attack_helicopter', name='gender'), nullable=True)
    role = db.Column(Enum('admin', 'user', name='role'), nullable=False)
    status = db.Column(Enum('active', 'blocked', name='status'), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return '<User %r>' % self.username