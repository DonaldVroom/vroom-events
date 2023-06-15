from flask_babel import _, get_locale
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
        try:
            if form.validate_on_submit():
                locale = str(get_locale())
                entry = QteamEvent()
                form.populate_obj(entry)
                entry.created = datetime.utcnow()
                entry.locale = locale
                db.session.add(entry)
                db.session.commit()
                return redirect(url_for('events.qteam_success'))
        except Exception as e:
            db.session.rollback()
            print(e)
            return redirect(url_for('events.qteam_main'))
    elif request.method == 'GET': 
        #return render_template('events/qteam/index.html', title=(_('QTeam')), form=form)
        return render_template('events/qteam/ended.html', title=(_('Ended')))

@bp.route('/q-team/success', methods=['GET'])
def qteam_success():
    return render_template('events/qteam/thank-you.html', title=(_('Success')))

@bp.route('/q-team/ended', methods=['GET'])
def qteam_ended():
    return render_template('events/qteam/ended.html', title=(_('Ended')))

@bp.route('/q-team/results', methods=['GET', 'POST'])
def qteam_results():
    if request.method == 'POST':
        password = request.form['password']
        if password == 'QteamVroom2023':
            events = QteamEvent.query.all()
            data = '<table>'
            data += '<tr><th>ID</th><th>How Many Centers</th><th>Which Type Car</th><th>When Summer Tires</th><th>How Many People</th><th>Email</th><th>First Name</th><th>Last Name</th><th>Created</th><th>Locale</th></tr>'
            for event in events:
                created_date = datetime.strftime(event.created, '%d-%m-%Y')
                data += f'<tr><td>{event.id}</td><td>{event.how_many_centers}</td><td>{event.which_type_car}</td><td>{event.when_summer_tires}</td><td>{event.how_many_people}</td><td>{event.email}</td><td>{event.first_name}</td><td>{event.last_name}</td><td>{created_date}</td><td>{event.locale}</td></tr>'
            data += '</table>'
            return data
        else:
            return 'Invalid password'
    elif request.method == 'GET': 
        return render_template('events/qteam/results.html', title=(_('Resultaten')))
    
@bp.route('/q-team/rules', methods=['GET', 'POST'])
def qteam_rules():
        return render_template('events/qteam/rules.html', title=(_('Regels')))