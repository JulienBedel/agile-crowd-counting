import pytest
from src.webapp.db import get_db, query_db
import os
import io

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

def test_index_normal(client):
    """
        Tests that the index is responding as expected
    """
    response = client.get('/')
    assert response.status_code == 200
    assert b'Crowd Counting  - The game' in response.data

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

def test_gallery_normal(client):
    """
        Tests that the gallery is effectively displaying images in database
    """
    response = client.get('/play')
    assert response.status_code == 200
    assert b'crowd.png' in response.data
    assert b'/play/1' in response.data
    assert client.get('/images/crowd.png').status_code == 200
    assert b'crowd2.jpg' in response.data
    assert b'/play/2' in response.data
    assert client.get('/images/crowd2.jpg').status_code == 200

def test_play_image_missing(client):
    """
        Tests that play on non-existing image return in not found error
    """
    response = client.get('/play/14')
    assert response.status_code == 404
    assert b'not found' in response.data

def test_post_normal(client):
    """
        Tests that posting new points works as expected
    """
    response = client.post('/play/1', json={"x_coord":1,"y_coord":1,"username":"user1"})
    assert response.status_code == 200
    assert b'score' in response.data

def test_post_missing_image(client):
    """
        Tests that play on non-existing image return in not found error
    """
    response = client.post('/play/14', json={"x_coord":1,"y_coord":1,"username":"user1"})
    assert response.status_code == 404
    assert b'not found' in response.data

def test_post_wrong_json(client):
    """
        Test that if the post data is not in json format, the application will reject it
    """
    response = client.post('/play/1', data='raw_data')
    assert response.status_code == 400
    assert b'Bad Request' in response.data

def test_post_wrong_parameters(client):
    """
        Test that if the json does not provides the proper parameters, it is rejected
    """
    response = client.post('/play/1', json={"x_coord":1,"y_coord":1})
    assert response.status_code == 400
    assert b'Bad Request' in response.data

