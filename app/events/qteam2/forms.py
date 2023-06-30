from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_babel import _, lazy_gettext as _l


class QteamForm2(FlaskForm):
    q1 = StringField(_l('Het circuit van Spa-Francorchamps is werkelijk iconisch. Welke coureur kan er vandaag de dag de meeste F1 overwinningen claimen?'), validators=[DataRequired()])
    q2 = StringField(_l("Pirelli was in de jaren '50, '80 en '90 reeds actief in de F1, maar in welk seizoen maakte het zijn comeback als exclusieve F1 bandenleverancier?"), validators=[DataRequired()])
    q3 = StringField(_l("De 1998 editie van de Belgian Grand Prix was werkelijk legendarisch. 22 auto's gingen van start, maar hoeveel daarvan haalden officieel de finishlijn?"), validators=[DataRequired()])
    q4 = StringField(_l('Na een tijdperk van 13-inch wielen produceert Pirelli vanaf 2022 een geheel nieuwe F1 bandenmaat als onderdeel van ingrijpende wijzigingen in de technische voorschriften. Welke maat is dit?'), validators=[DataRequired()])
    how_many_people = IntegerField(
        _l('Hoeveel personen zullen aan deze competitie deelnemen?'),
         validators=[DataRequired()])
    email = StringField(_l('Email'), validators=[DataRequired(), Email()])
    first_name = StringField(_l('Voornaam'), validators=[DataRequired()])
    last_name = StringField(_l('Familienaam'), validators=[DataRequired()])
    phone = StringField(_l('Telefoon'), validators=[DataRequired()])
    submit = SubmitField(_l('Indienen'))
