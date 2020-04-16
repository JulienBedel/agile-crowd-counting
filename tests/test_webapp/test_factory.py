from src.webapp import create_app

"""
    Tests for the factory configuration.
    In other words makes sure that the Flask environemnt is running as expected.
"""

def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing


def test_hello(client):
    response = client.get('/hello')
    assert response.data == b'Hello, World!'