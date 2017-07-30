from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length, Email

class SubscribeForm(FlaskForm):
    email = StringField('Email Address', validators = [DataRequired(), Length(max = 120), Email()])

class UnsubscribeForm(FlaskForm):
    email = StringField('Email Address', validators = [DataRequired(), Length(max = 120), Email()])
