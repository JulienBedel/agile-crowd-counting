import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from src.webapp.db import get_db, query_db

"""
    Adds a main Blueprint for use in the app.
    See : https://flask.palletsprojects.com/en/1.1.x/tutorial/views/
"""

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def home():
    return ""