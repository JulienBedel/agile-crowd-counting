import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext

"""
    Initiates the database and adds various functions to makes it easier to handle.
    See : https://flask.palletsprojects.com/en/1.1.x/tutorial/database/
"""

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def query_db(query, args=(), one=False):
    try:
        cur = get_db().execute(query, args)
        rv = cur.fetchall()
        cur.close()
        results = (rv[0] if rv else None) if one else rv
        rows = []
        for result in results:
            rows.append(dict(result))
        return rows
    except sqlite3.OperationalError:
        return []


def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


def insert_db():
    db = get_db()

    with current_app.open_resource('sample.sql') as f:
        db.executescript(f.read().decode('utf8'))

# adds flask functions to initiate the db and insert sample data in it

@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

@click.command('insert-db')
@with_appcontext
def insert_db_command():
    """Inserts sample data into the database."""
    insert_db()
    click.echo('Samples inserted into the database.')


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
    app.cli.add_command(insert_db_command)