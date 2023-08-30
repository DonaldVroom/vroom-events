from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_babel import _, lazy_gettext as _l


class VwCupForm(FlaskForm):
    q1 = StringField(_l('Indien je een 2de hands auto koopt:'), validators=[DataRequired()])
    q2 = StringField(_l("Er staat naast de kilometerhistoriek, extra informatie op de Car-Pass. Welke van de onderstaande gegevens vindt u NIET op de Car-Pass?"), validators=[DataRequired()])
    how_many_people = IntegerField(
        _l('Hoeveel personen zullen aan deze competitie deelnemen?'),
         validators=[DataRequired()])
    email = StringField(_l('Email'), validators=[DataRequired(), Email()])
    first_name = StringField(_l('Voornaam'), validators=[DataRequired()])
    last_name = StringField(_l('Familienaam'), validators=[DataRequired()])
    phone = StringField(_l('Telefoon'), validators=[DataRequired()])
    submit = SubmitField(_l('Indienen'))
