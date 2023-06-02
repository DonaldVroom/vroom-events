from flask_babel import _, get_locale
from datetime import datetime
from flask import render_template, url_for, redirect, request
from app.events import bp
from app.events.forms import FordForm
from app.models import FordBroncoEvent
from app import db

@bp.route('/ford/', methods=['GET', 'POST'])
def ford_main():
    form = FordForm()
    if request.method == 'POST':
        try:
            if form.validate_on_submit():
                locale = str(get_locale())
                entry = FordBroncoEvent()
                form.populate_obj(entry)
                entry.created = datetime.utcnow()
                entry.locale = locale
                db.session.add(entry)
                db.session.commit()
                return redirect(url_for('events.ford_success'))
        except Exception as e:
            db.session.rollback()
            print(e)
            return redirect(url_for('events.ford_main'))
    elif request.method == 'GET': 
        return render_template('events/ford/index.html', title=(_('Ford')), form=form)

@bp.route('/ford/success', methods=['GET'])
def ford_success():
    return render_template('events/ford/thank-you.html', title=(_('Success')))

@bp.route('/ford/ended', methods=['GET'])
def ford_ended():
    return render_template('events/ford/ended.html', title=(_('Ended')))

@bp.route('/ford/results', methods=['GET', 'POST'])
def ford_results():
    if request.method == 'POST':
        password = request.form['password']
        if password == 'FordVroom2023':
            events = FordBroncoEvent.query.all()
            data = '<table>'
            data += '<tr><th>ID</th><th>Generation</th><th>GOAT</th><th>Famous person</th><th>Age</th><th>Towing</th><th>Gears</th><th>How Many People</th><th>First Name</th><th>Last Name</th><th>Email</th><th>Phone</th><th>Created</th><th>Locale</th></tr>'
            for event in events:
                created_date = datetime.strftime(event.created, '%d-%m-%Y')
                data += f'<tr><td>{event.id}</td><td>{event.first_generation}</td><td>{event.goat_meaning}</td><td>{event.famous_person}</td><td>{event.how_old}</td><td>{event.towing_capacity}</td><td>{event.total_gears}</td><td>{event.how_many_people}</td><td>{event.first_name}</td><td>{event.last_name}</td><td>{event.email}</td><td>{event.phone}</td><td>{created_date}</td><td>{event.locale}</td></tr>'
            data += '</table>'
            return data
        else:
            return 'Invalid password'
    elif request.method == 'GET': 
        return render_template('events/ford/results.html', title=(_('Resultaten')))
    
@bp.route('/ford/rules', methods=['GET', 'POST'])
def ford_rules():
        return render_template('events/ford/rules.html', title=(_('Regels')))