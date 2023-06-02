from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email
from flask_babel import _
from app.events.qteam.forms import (QteamForm)
from app.events.suzuki.forms import (SuzukiLeadForm)
from app.events.ford.forms import (FordForm)