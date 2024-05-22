from datetime import datetime

from werkzeug.security import generate_password_hash

from apps.app import db


# User model
class User(db.Model):
    # tablename
    __tablename__ = "users"

    # column
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, index=True)
    email = db.Column(db.String, unique=True, index=True)
    password_hash = db.Column(db.String)
    created_at = db.Column(db.Datetime, default=datetime.now)
    updated_at = db.Column(db.Datetime, default=datetime.now, onupdate=datetime.now)

    # Property for password
    @property
    def password(self):
        raise AttributeError("Unreadable")

    # Hashed password
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
