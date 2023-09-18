from flask_babel import _, get_locale
from datetime import datetime
from flask import render_template, url_for, redirect, request
from app.events import bp
from app.events.forms import VwCupForm
from app.models import VwCupEvent
from app import db

# @bp.route('/vw-cup/', methods=['GET', 'POST'])
# def vw_cup_main():
#     form = VwCupForm()
#     if request.method == 'POST':
#         try:
#             if form.validate_on_submit():
#                 locale = str(get_locale())
#                 entry = VwCupEvent()
#                 form.populate_obj(entry)
#                 entry.created = datetime.utcnow()
#                 entry.locale = locale
#                 db.session.add(entry)
#                 db.session.commit()
#                 return redirect(url_for('events.vw_cup_success'))
#         except Exception as e:
#             db.session.rollback()
#             print(e)
#             return redirect(url_for('events.vw_cup_main'))
#     elif request.method == 'GET': 
#         return render_template('events/vw-cup/index.html', title=(_('VW Cup')), form=form)

@bp.route('/vw-cup/', methods=['GET'])
def vw_cup_main():
    return render_template('events/vw-cup/ended.html', title=(_('Ended')))

@bp.route('/vw-cup/success', methods=['GET'])
def vw_cup_success():
    return render_template('events/vw-cup/thank-you.html', title=(_('Success')))

@bp.route('/vw-cup/ended', methods=['GET'])
def vw_cup_ended():
    return render_template('events/vw-cup/ended.html', title=(_('Ended')))

@bp.route('/vw-cup/results', methods=['GET', 'POST'])
def vw_cup_results():
    if request.method == 'POST':
        password = request.form['password']
        if password == 'VWCupVroom2023':
            events = VwCupEvent.query.all()
            data = '<table>'
            data += '<tr><th>ID</th><th>Q1</th><th>Q2</th><th>How Many People</th><th>Email</th><th>Phone</th><th>First Name</th><th>Last Name</th><th>Postal code</th><th>DOB</th><th>Created</th><th>Locale</th></tr>'
            for event in events:
                created_date = datetime.strftime(event.created, '%d-%m-%Y')
                data += f'<tr><td>{event.id}</td><td>{event.q1}</td><td>{event.q2}</td><td>{event.how_many_people}</td><td>{event.email}</td><td>{event.phone}</td><td>{event.first_name}</td><td>{event.last_name}</td><td>{event.postal_code}</td><td>{event.dob}</td><td>{created_date}</td><td>{event.locale}</td></tr>'
            data += '</table>'
            return data
        else:
            return 'Invalid password'
    elif request.method == 'GET': 
        return render_template('events/vw-cup/results.html', title=(_('Resultaten')))
    
@bp.route('/vw-cup/rules', methods=['GET', 'POST'])
def vw_cup_rules():
        return render_template('events/vw-cup/rules.html', title=(_('Regels')))