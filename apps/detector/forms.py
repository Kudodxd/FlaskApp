from flask_wtf.file import FileAllowed, FileField, FileRequired
from flask_wtf.form import FlaskForm
from wtforms.fields.simple import SubmitField


class UpLoadImageForm(FlaskForm):
    image = FileField(
        validators=[
            FileRequired("Fucking choose image file"),
            FileAllowed(["png", "jpg", "jpeg"], "Unsupported image format"),
        ]
    )
    submit = SubmitField("Upload")


class DetectorForm(FlaskForm):
    submit = SubmitField("Detect")
