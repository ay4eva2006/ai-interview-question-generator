from . import db
from datetime import datetime


class Analytics(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    searched_role = db.Column(
        db.String(100),
        nullable=False
    )

    timestamp = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )