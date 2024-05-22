from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, length


# Class creates and edits new users
class UserForm(FlaskForm):
    # Label and validator of username attribute in user form
    username = StringField(
        "User name",
        validators=[
            DataRequired(message="Username is required."),
            length(max=30, message="Please enter within 30 characters."),
        ],
    )
    # Label and validator of email attribute in user form
    email = StringField(
        "Mail address",
        validators=[
            DataRequired(message="Email is required."),
            Email(message="Please enter in email address format."),
        ],
    )
    # Label and validator of password attribute in user form
    password = PasswordField(
        "Password", validators=[DataRequired(message="Password is required.")]
    )
    # Submit text of user form
    submit = SubmitField("Register", render_kw={"class": "btn btn-green"})
