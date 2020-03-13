from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, RadioField, SelectField, BooleanField, validators
from utils import get_genres

class SearchForm(FlaskForm):
    """"""
    genre = SelectField(coerce=str)
    acousticness = BooleanField("Acousticness?")

    input1 = StringField("Artist or Track (optional)")
    radio1 = RadioField(choices=[('artist','Artist'),('track','Track')], validators=(validators.Optional(),))

    input2 = StringField("Artist or Track (optional)")
    radio2 = RadioField(choices=[('artist','Artist'),('track','Track')], validators=(validators.Optional(),))

    input3 = StringField("Artist or Track (optional)")
    radio3 = RadioField(choices=[('artist','Artist'),('track','Track')], validators=(validators.Optional(),))

    input4 = StringField("Artist or Track (optional)")
    radio4 = RadioField(choices=[('artist','Artist'),('track','Track')], validators=(validators.Optional(),))

    input5 = StringField("Artist or Track (optional)")
    radio5 = RadioField(choices=[('artist','Artist'),('track','Track')], validators=(validators.Optional(),))
    