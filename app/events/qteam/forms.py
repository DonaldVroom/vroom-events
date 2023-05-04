from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_babel import _


class QteamForm(FlaskForm):
    how_many_centers = StringField(validators=[DataRequired()])
    which_type_car = StringField(validators=[DataRequired()])
    when_summer_tires = StringField(validators=[DataRequired()])
    how_many_people = IntegerField(
        _('Hoeveel personen zullen aan deze competitie deelnemen?'),
         validators=[DataRequired()])
    email = StringField(_('Email'), validators=[DataRequired(), Email()])
    first_name = StringField(_('Voornaam'), validators=[DataRequired()])
    last_name = StringField(_('Familienaam'), validators=[DataRequired()])
    submit = SubmitField(_('Indienen'))
