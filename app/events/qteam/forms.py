from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email
from flask_babel import _


how_many_centers_choices = [
    ('0', _('Bijna 50')),
    ('1', _('Bijna 70')),
    ('2', _('Bijna 100'))
]
which_type_car_choices = [
    ('0', _('Particuliere wagen')),
    ('1', _('Particuliere wagen en bedrijfswagen')),
    ('2', _('Particuliere wagen, bedrijfswagen en leasewagen'))
]
when_summer_tires_choices = [
    ('0', _('2 graden celsius')),
    ('1', _('7 graden celsius')),
    ('2', _('15 graden celcius'))
]

class QteamForm(FlaskForm):
    how_many_centers = SelectField(
        _('Hoeveel Q-Team service centers zijn er in België aanwezig'),
        choices=how_many_centers_choices,
        validators=[DataRequired()])
    which_type_car = SelectField(
        _('Met welk type wagen kan je bij een QTeam service center terecht'),
        choices=which_type_car_choices,
        validators=[DataRequired()])
    when_summer_tires = SelectField(
        _('Vanaf wanneer is het aangeraden om op zomerbanden om te schakelen'),
        choices=when_summer_tires_choices,
        validators=[DataRequired()])
    how_many_people = IntegerField(
        _('Hoeveel personen zullen aan deze competitie deelnemen'),
         validators=[DataRequired()])
    email = StringField(_('Email'), validators=[DataRequired(), Email()])
    first_name = StringField(_('Voornaam'), validators=[DataRequired()])
    last_name = StringField(_('Familienaam'), validators=[DataRequired()])
    submit = SubmitField(_('Indienen'))