from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,DateField
from wtforms.validators import DataRequired, EqualTo

class Add(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    retype = PasswordField('retype',validators=[DataRequired(), EqualTo('password', message="Passwords must match.")])
    First_name = StringField('First_name', validators=[DataRequired()])
    Last_name = StringField('Last_name', validators=[DataRequired()])
    id_number = StringField('id_number', validators=[DataRequired()])
    date_of_birth = DateField('date_of_birth', validators=[DataRequired()])
    submit = SubmitField('submit')

class Fetch(FlaskForm):
    id_number = StringField('id_number', validators=[DataRequired()])
    submit = SubmitField('submit')