from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, RadioField

class SearchForm(FlaskForm):
    """"""

    input1 = StringField("Artist/Album/Track (optional)")
    radio1 = RadioField(choices=[('artist','Artist'),('album','Album'),('track','Track')])

    input2 = StringField("Artist/Album/Track (optional)")
    radio2 = RadioField(choices=[('artist','Artist'),('album','Album'),('track','Track')])

    # input3 = StringField("Artist/Album/Track (optional)")
    # radio3 = RadioField(choices=[('i3artist','Artist'),('i3album','Album'),('i3track','Track')])

    # input4 = StringField("Artist/Album/Track (optional)")
    # radio4 = RadioField(choices=[('i4artist','Artist'),('i4album','Album'),('i4track','Track')])

    # input5 = StringField("Artist/Album/Track (optional)")
    # radio5 = RadioField(choices=[('i5artist','Artist'),('i5album','Album'),('i5track','Track')])