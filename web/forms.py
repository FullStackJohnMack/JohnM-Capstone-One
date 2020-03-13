from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, RadioField, SelectField, BooleanField, validators
from utils import get_genres

class SearchForm(FlaskForm):
    """"""
    

    input1 = StringField("Artist or Song (optional)")
    radio1 = RadioField(choices=[('artist','Artist'),('track','Song')], validators=(validators.Optional(),))

    input2 = StringField("Artist or Song (optional)")
    radio2 = RadioField(choices=[('artist','Artist'),('track','Song')], validators=(validators.Optional(),))

    input3 = StringField("Artist or Song (optional)")
    radio3 = RadioField(choices=[('artist','Artist'),('track','Song')], validators=(validators.Optional(),))

    input4 = StringField("Artist or Song (optional)")
    radio4 = RadioField(choices=[('artist','Artist'),('track','Song')], validators=(validators.Optional(),))

    input5 = StringField("Artist or Song (optional)")
    radio5 = RadioField(choices=[('artist','Artist'),('track','Song')], validators=(validators.Optional(),))

    genre = SelectField(coerce=str)

    acousticness = BooleanField("Acousticness?")
    danceability = BooleanField("Danceability?")
    energy = BooleanField("Energy?")
    instrumentalness = BooleanField("Instrumentalness?")
    liveness = BooleanField("Liveness?")
    