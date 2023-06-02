import os
from flask_babel import _, get_locale, Babel
from flask import render_template, g, request, redirect
from app.events import bp
from app.events.qteam import routes
from app.events.suzuki import routes
from app.events.ford import routes

babel = Babel()

@bp.before_app_request
def before_request():
    if 'DYNO' in os.environ: # Only runs when on heroku
            if request.url.startswith('http://'):
                url = request.url.replace('http://', 'https://', 1)
                code = 301
                return redirect(url, code=code)
    g.locale = str(get_locale())

@bp.context_processor
def inject_locale():
    return {'locale': str(get_locale())}

@bp.route('/', methods=['GET', 'POST'])
def main():
        return render_template('events/index.html', title=(_('Welcome')))
