from app import db
from sqlalchemy import *

class Note(db.Model):
    __tablename__ = 'note'

    id = db.Column(db.String, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.Text, nullable=False)
    password = db.Column(db.String, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return '<Note %r>' % self.title