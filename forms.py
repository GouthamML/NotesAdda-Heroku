from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, RadioField
from wtforms.validators import DataRequired



class NameForm(FlaskForm):
    username = StringField('Name', validators=[DataRequired()])
    email = StringField('Email')
    password = PasswordField('Passowrd')
    submit = SubmitField('Submit')
    job = RadioField('Label', choices=[('student','I\'m a Student'),('teacher','I\'m a Lecturer')])
    f_name = StringField('File name')
    #branch = StringField('branch')
    public = RadioField('Label', choices=[(1,'Make it public'),(0,'Keep it private')])