from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Account(db.Model):
    name = db.Column(db.String, primary_key=True)
    seed = db.Column(db.String, nullable=False)
