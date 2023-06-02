from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_babel import _, lazy_gettext as _l


class FordForm(FlaskForm):
    first_generation = StringField(_l('De Ford Bronco is een icoon... wanneer werd de eerste generatie gelanceerd?'), validators=[DataRequired()])
    goat_meaning = StringField(_l('In 1963 werd in een interne memo naar de Bronco verwezen als "GOAT". Wat wou dit zeggen?'), validators=[DataRequired()])
    famous_person = StringField(_l('Een beroemd persoon gebruikte de Bronco op het einde van de jaren 1970 in de VS. Wie was het?'), validators=[DataRequired()])
    how_old = StringField(_l('Hoe oud wordt de eerste Ford Ranger dit jaar?'), validators=[DataRequired()])
    towing_capacity = StringField(_l('Wat is het trekvermogen van de nieuwe Ford Ranger?'), validators=[DataRequired()])
    total_gears = StringField(_l('Hoeveel versnellingen heeft de Ford EcoBlue Dieselmotor?'), validators=[DataRequired()])
    how_many_people = IntegerField(
        _l('Hoeveel personen zullen aan deze competitie deelnemen?'),
         validators=[DataRequired()])
    email = StringField(_l('Email'), validators=[DataRequired(), Email()])
    first_name = StringField(_l('Voornaam'), validators=[DataRequired()])
    last_name = StringField(_l('Familienaam'), validators=[DataRequired()])
    phone = StringField(_l('Telefoon'), validators=[DataRequired()])
    submit = SubmitField(_l('Indienen'))
