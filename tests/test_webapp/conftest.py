import os
import tempfile

import pytest
from src.webapp import create_app
from src.webapp.db import get_db, init_db

with open(os.path.join(os.path.dirname(__file__), 'data.sql'), 'rb') as f:
    _data_sql = f.read().decode('utf8')


""""
    Pytest fixtures are used to specify environments in which the tests will be executed.
    We have created the following scenarios :
        - app = application database contains sample data from the data.sql to work on
        - nodata = application database is empty (no tables)
        - empty = application database has tables but no record
        - client and runner = used to test the environment deployment
    See : https://flask.palletsprojects.com/en/1.1.x/tutorial/tests/
"""

@pytest.fixture
def app():
    db_fd, db_path = tempfile.mkstemp()

    app = create_app({
        'TESTING': True,
        'DATABASE': db_path,
    })

    with app.app_context():
        init_db()
        get_db().executescript(_data_sql)

    yield app

    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture
def nodata():
    db_fd, db_path = tempfile.mkstemp()

    app = create_app({
        'TESTING': True,
        'DATABASE': db_path,
    })

    with app.app_context():
        init_db()
        
    yield app

    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture
def empty():
    db_fd, db_path = tempfile.mkstemp()

    app = create_app({
        'TESTING': True,
        'DATABASE': db_path,
    })

    yield app

    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner() 
