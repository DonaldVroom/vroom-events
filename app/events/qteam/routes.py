from flask_babel import _, get_locale
from langdetect import detect, LangDetectException
from datetime import datetime
from flask import render_template, url_for, redirect, request, current_app, g
from app.events import bp
from app.events.forms import QteamForm
from app.models import QteamEvent
from app import db

@bp.route('/q-team/', methods=['GET', 'POST'])
def index():
    form = QteamForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            entry = QteamEvent(
                how_many_centers=form.how_many_centers.data,
                which_type_car=form.which_type_car.data,
                when_summer_tires=form.when_summer_tires.data,
                how_many_people=form.how_many_people.data,
                email=form.email.data,
                first_name=form.first_name.data,
                last_name=form.last_name.data,
                created=datetime.utcnow()
            )
            db.session.add(entry)
            db.session.commit()
            
            return redirect(url_for('events.success'))
    elif request.method == 'GET': 
        return render_template('events/index.html', title=(_('Welcome')), form=form)

@bp.route('/q-team/success', methods=['GET'])
def success():
    return render_template('events/thank-you.html', title=(_('Success')))

@bp.route('/q-team/ended', methods=['GET'])
def ended():
    return render_template('events/ended.html', title=(_('Ended')))