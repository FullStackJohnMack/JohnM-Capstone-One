from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, RadioField, SelectField, BooleanField, validators
from utils import get_genres

class SearchForm(FlaskForm):
    """"""
    

    input1 = StringField(render_kw={"placeholder": "Optional artist or song"})
    radio1 = RadioField(choices=[('artist','Artist'),('track','Song')], validators=(validators.Optional(),))

    input2 = StringField(render_kw={"placeholder": "Optional artist or song"})
    radio2 = RadioField(choices=[('artist','Artist'),('track','Song')], validators=(validators.Optional(),))

    input3 = StringField(render_kw={"placeholder": "Optional artist or song"})
    radio3 = RadioField(choices=[('artist','Artist'),('track','Song')], validators=(validators.Optional(),))

    input4 = StringField(render_kw={"placeholder": "Optional artist or song"})
    radio4 = RadioField(choices=[('artist','Artist'),('track','Song')], validators=(validators.Optional(),))

    input5 = StringField(render_kw={"placeholder": "Optional artist or song"})
    radio5 = RadioField(choices=[('artist','Artist'),('track','Song')], validators=(validators.Optional(),))
    