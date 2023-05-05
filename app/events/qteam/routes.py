from flask_babel import _
from datetime import datetime
from flask import render_template, url_for, redirect, request
from app.events import bp
from app.events.forms import QteamForm
from app.models import QteamEvent
from app import db

@bp.route('/q-team/', methods=['GET', 'POST'])
def qteam_main():
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
            
            return redirect(url_for('events.qteam_success'))
    elif request.method == 'GET': 
        return render_template('events/qteam/index.html', title=(_('Q Team')), form=form)

@bp.route('/q-team/success', methods=['GET'])
def qteam_success():
    return render_template('events/qteam/thank-you.html', title=(_('Success')))

@bp.route('/q-team/ended', methods=['GET'])
def qteam_ended():
    return render_template('events/qteam/ended.html', title=(_('Ended')))

@bp.route('/q-team/results', methods=['GET', 'POST'])
def validate_password():
    if request.method == 'POST':
        password = request.form['password']
        if password == 'QteamVroom2023':
            events = QteamEvent.query.all()
            data = '<table>'
            data += '<tr><th>ID</th><th>How Many Centers</th><th>Which Type Car</th><th>When Summer Tires</th><th>How Many People</th><th>Email</th><th>First Name</th><th>Last Name</th><th>Created</th></tr>'
            for event in events:
                created_date = datetime.strftime(event.created, '%d-%m-%Y')
                data += f'<tr><td>{event.id}</td><td>{event.how_many_centers}</td><td>{event.which_type_car}</td><td>{event.when_summer_tires}</td><td>{event.how_many_people}</td><td>{event.email}</td><td>{event.first_name}</td><td>{event.last_name}</td><td>{created_date}</td></tr>'
            data += '</table>'
            return data
        else:
            return 'Invalid password'
    elif request.method == 'GET': 
        return render_template('events/qteam/results.html', title=(_('Resultaten')))
    
@bp.route('/q-team/rules', methods=['GET', 'POST'])
def qteam_rules():
        return render_template('events/qteam/rules.html', title=(_('Regels')))