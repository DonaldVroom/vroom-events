from flask_babel import _, get_locale, Babel
from flask import render_template, g
from app.events import bp
from app.events.qteam import routes
from app.events.suzuki import routes

babel = Babel()

@bp.before_app_request
def before_request():
    g.locale = str(get_locale())

@bp.context_processor
def inject_locale():
    return {'locale': str(get_locale())}

@bp.route('/', methods=['GET', 'POST'])
def main():
        return render_template('events/index.html', title=(_('Welcome')))
