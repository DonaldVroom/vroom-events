
from flask import render_template, flash, url_for, redirect, request, current_app
from app.events import bp
from app import db


@bp.route('/', methods=['GET'])
def index():
    return render_template('events/index.html', title='Welcome')
