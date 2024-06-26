from datetime import datetime

from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from apps.app import db, login_manager


# User model
class User(db.Model, UserMixin):
    # tablename
    __tablename__ = "users"

    # column
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, index=True)
    email = db.Column(db.String, unique=True, index=True)
    password_hash = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    # Property for password
    @property
    def password(self):
        raise AttributeError("Unreadable")

    # Hashed password
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    # Check password
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    # Check for email address duplicates
    def is_duplicate_email(self):
        return User.query.filter_by(email=self.email).first() is not None


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
