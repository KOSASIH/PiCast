# moderation/moderation_model.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    podcast_id = db.Column(db.Integer, db.ForeignKey('podcast.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    reason = db.Column(db.String(255))
    description = db.Column(db.String(255))

class Moderation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    podcast_id = db.Column(db.Integer, db.ForeignKey('podcast.id'))
    moderator_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    status = db.Column(db.String(255))  # approved, rejected, pending
