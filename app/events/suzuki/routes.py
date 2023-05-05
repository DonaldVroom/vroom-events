from flask_babel import _
from datetime import datetime
from flask import render_template, url_for, redirect, request
from app.events import bp
from app.events.forms import SuzukiLeadForm
from app.models import QteamEvent, SuzukiLead
from app import db

@bp.route('/suzuki/', methods=['GET'])
def suzuki_main():
        return render_template('events/suzuki/index.html', title=(_('Suzuki')))

@bp.route('/suzuki/s-cross', methods=['GET', 'POST'])
def suzuki_s_cross():
        form = SuzukiLeadForm()
        if request.method == 'POST':
                if form.validate_on_submit():
                        suzuki_lead = SuzukiLead(
                        auto="S-Cross",
                        email=form.email.data,
                        salutation=form.salutation.data,
                        first_name=form.first_name.data,
                        last_name=form.last_name.data,
                        postal_code=form.postal_code.data,
                        phone=form.phone.data,
                        created=datetime.utcnow()
                        )
                        db.session.add(suzuki_lead)
                        db.session.commit()
                        return redirect(url_for('suzuki_s_cross'))
        elif request.method == 'GET': 
                return render_template('events/suzuki/s-cross.html', title=(_('S Cross')), form=form)

