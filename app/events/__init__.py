from flask import Blueprint

bp = Blueprint('errors', __name__)

from app.events import routes