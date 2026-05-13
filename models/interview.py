from . import db


class Interview(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    role = db.Column(
        db.String(100),
        nullable=False
    )

    questions = db.Column(
        db.Text,
        nullable=False
    )