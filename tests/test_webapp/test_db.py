import sqlite3

import pytest
from src.webapp.db import get_db, query_db


"""
    Tests for the database in various scenarios.
    Test argument is the pytest fixture in use.
    See : https://flask.palletsprojects.com/en/1.1.x/tutorial/tests/
"""

def test_get_close_db(app):
    """
    	Tests the database is closing well.
    """
    with app.app_context():
        db = get_db()
        assert db is get_db()

    with pytest.raises(sqlite3.ProgrammingError) as e:
        db.execute('SELECT 1')

    assert 'closed' in str(e.value)


def test_init_db_command(runner, monkeypatch):
    """
    	Tests the database initiates well with flask command
    """
    class Recorder(object):
        called = False

    def fake_init_db():
        Recorder.called = True

    monkeypatch.setattr('src.webapp.db.init_db', fake_init_db)
    result = runner.invoke(args=['init-db'])
    assert 'Initialized' in result.output
    assert Recorder.called

def test_insert_db_command(runner, monkeypatch):
    """
    	Tests the sample inserts well with flask command
    """
    class Recorder(object):
        called = False

    def fake_insert_db():
        Recorder.called = True

    monkeypatch.setattr('src.webapp.db.insert_db', fake_insert_db)
    result = runner.invoke(args=['insert-db'])
    assert 'Samples' in result.output
    assert Recorder.called

def test_request_simple(app):
    """
        Tests the result of a simple request in normal conditions.
    """
    with app.app_context():
        result = query_db('select * from users')
        assert result[0]['username'] == 'user1'

def test_request_empty(empty):
    """
        Tests the result of a request if the database is empty.
    """
    with empty.app_context():
        result = query_db('select * from users')
        assert result == []

def test_request_nodata(nodata):
    """
        Tests the result of a request if there are no records in the database.
    """
    with nodata.app_context():
        result = query_db('select * from users')
        assert result == []
        