import pytest
from src.webapp.db import get_db, query_db

def test_index_normal(client):
    """
        Tests that the list of image is returned in normal conditions
    """
    response = client.get('/')
    assert b'web-data' in response.data
    assert b'Path' in response.data


def test_image_normal(client):
    """
        Tests that information on one image is returned in normal conditions
    """
    response = client.get('/image?id=1')
    assert b'user1' in response.data
    assert b'user2' in response.data

    
def test_image_missing(client):
    """
        Tests that information on one image is returned in normal conditions
    """
    response = client.get('/image?id=4')
    assert b'not found' in response.data


def test_image_score_missing(client):
    """
        Tests that information on one image is returned in normal conditions
    """
    response = client.get('/image?id=3')
    assert b'No score' in response.data
