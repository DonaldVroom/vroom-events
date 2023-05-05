from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_babel import _, lazy_gettext as _l


class QteamForm(FlaskForm):
    how_many_centers = StringField(_l('Hoeveel Q Team service centers zijn er in België aanwezig?'), validators=[DataRequired()])
    which_type_car = StringField(_l('Met welk type wagen kan je bij een Q Team service center terecht?'), validators=[DataRequired()])
    when_summer_tires = StringField(_l('Vanaf wanneer is het aangeraden om op zomerbanden om te schakelen?'), validators=[DataRequired()])
    how_many_people = IntegerField(
        _l('Hoeveel personen zullen aan deze competitie deelnemen?'),
         validators=[DataRequired()])
    email = StringField(_l('Email'), validators=[DataRequired(), Email()])
    first_name = StringField(_l('Voornaam'), validators=[DataRequired()])
    last_name = StringField(_l('Familienaam'), validators=[DataRequired()])
    submit = SubmitField(_l('Indienen'))
