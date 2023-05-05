from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField, SelectField
from wtforms.validators import DataRequired, Email
from flask_babel import _, lazy_gettext as _l


class SuzukiLeadForm(FlaskForm):
    auto = HiddenField(_l('auto'))
    email = StringField(_l('Email'), validators=[DataRequired(), Email()])
    salutation = SelectField(_l('Aanspreking'), validators=[DataRequired()],
                              choices=[('Mr', _l('Mr')), ('Ms', _l('Ms')), ('Mme', _l('Mme'))])
    first_name = StringField(_l('Voornaam'), validators=[DataRequired()])
    first_name = StringField(_l('Voornaam'), validators=[DataRequired()])
    last_name = StringField(_l('Familienaam'), validators=[DataRequired()])
    postal_code = StringField(_l('Postcode'), validators=[DataRequired()])
    phone = StringField(_l('Telefoonnummer'), validators=[DataRequired()])
    submit = SubmitField(_l('Indienen'))
