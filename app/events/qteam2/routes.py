from flask_babel import _, get_locale
from datetime import datetime
from flask import render_template, url_for, redirect, request
from app.events import bp
from app.events.forms import QteamForm2
from app.models import QteamEvent2
from app import db

@bp.route('/q-team/f1/', methods=['GET', 'POST'])
def qteam_main2():
    form = QteamForm2()
    if request.method == 'POST':
        try:
            if form.validate_on_submit():
                locale = str(get_locale())
                entry = QteamEvent2()
                form.populate_obj(entry)
                entry.created = datetime.utcnow()
                entry.locale = locale
                db.session.add(entry)
                db.session.commit()
                return redirect(url_for('events.qteam_success2'))
        except Exception as e:
            db.session.rollback()
            print(e)
            return redirect(url_for('events.qteam_main2'))
    elif request.method == 'GET': 
        return render_template('events/qteam2/index.html', title=(_('QTeam')), form=form)

@bp.route('/q-team/f1/success', methods=['GET'])
def qteam_success2():
    return render_template('events/qteam2/thank-you.html', title=(_('Success')))

@bp.route('/q-team/f1/ended', methods=['GET'])
def qteam_ended2():
    return render_template('events/qteam2/ended.html', title=(_('Ended')))

@bp.route('/q-team/f1/results', methods=['GET', 'POST'])
def qteam_results2():
    if request.method == 'POST':
        password = request.form['password']
        if password == 'Qteam2Vroom2023':
            events = QteamEvent2.query.all()
            data = '<table>'
            data += '<tr><th>ID</th><th>Q1</th><th>Q2</th><th>Q3</th><th>Q4</th><th>How Many People</th><th>Email</th><th>First Name</th><th>Last Name</th><th>Created</th><th>Locale</th></tr>'
            for event in events:
                created_date = datetime.strftime(event.created, '%d-%m-%Y')
                data += f'<tr><td>{event.id}</td><td>{event.q1}</td><td>{event.q2}</td><td>{event.q3}</td><td>{event.q4}</td><td>{event.how_many_people}</td><td>{event.email}</td><td>{event.first_name}</td><td>{event.last_name}</td><td>{created_date}</td><td>{event.locale}</td></tr>'
            data += '</table>'
            return data
        else:
            return 'Invalid password'
    elif request.method == 'GET': 
        return render_template('events/qteam2/results.html', title=(_('Resultaten')))
    
@bp.route('/q-team/f1/rules', methods=['GET', 'POST'])
def qteam_rules2():
        return render_template('events/qteam2/rules.html', title=(_('Regels')))