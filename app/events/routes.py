from flask_babel import _, get_locale
from langdetect import detect, LangDetectException
from datetime import datetime
from flask import render_template, url_for, redirect, request, current_app, g
from app.events import bp
from app.events.forms import QteamForm
from app.models import QteamEvent
from app import db
from app.events.qteam import routes

@bp.before_app_request
def before_request():
    g.locale = str(get_locale())

@bp.route('/', methods=['GET', 'POST'])
def main():
        return redirect(url_for('events.index'))