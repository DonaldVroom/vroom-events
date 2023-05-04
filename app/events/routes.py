from flask_babel import _
from flask import render_template, url_for, redirect, g
from app.events import bp
from app.events.qteam import routes
from flask_babel import _, get_locale

@bp.before_app_request
def before_request():
    print(str(get_locale()))
    g.locale = str(get_locale())

@bp.route('/', methods=['GET', 'POST'])
def main():
        return redirect(url_for('events.index'))