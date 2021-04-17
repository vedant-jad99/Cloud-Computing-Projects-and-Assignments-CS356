#Creating basic form for uploading images to the app

from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import SubmitField

class UploadPicture(FlaskForm):
    image = FileField('Choose a picture', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    submit = SubmitField("Upload")
