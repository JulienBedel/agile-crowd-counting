import pytest
from src.webapp.db import get_db, query_db

def test_image_normal(client):
    """
        Tests that accessing an image directly results in displaying the image
    """
    response = client.get('/images/crowd.png')
    assert response.status_code == 200
    assert b'PNG' in response.data

def test_image_missing(client):
    """
        Tests that accessing a missing image directly results in not found message
    """
    response = client.get('/images/crowd8.png')
    assert response.status_code == 404
    assert b'not found' in response.data
