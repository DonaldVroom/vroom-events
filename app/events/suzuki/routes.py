from flask_babel import _
from datetime import datetime
from flask import render_template, url_for, redirect, request
from app.events import bp
from app.events.forms import QteamForm
from app.models import QteamEvent
from app import db

@bp.route('/suzuki/', methods=['GET'])
def suzuki_main():
        return render_template('events/suzuki/index.html', title=(_('Suzuki')))

@bp.route('/suzuki/s-cross', methods=['GET', 'POST'])
def suzuki_s_cross():
        return render_template('events/suzuki/s-cross.html', title=(_('S Cross')))
