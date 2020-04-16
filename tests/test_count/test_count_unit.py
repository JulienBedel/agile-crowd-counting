import unittest
import random

from src.count.counter import count
from src.webapp import create_app
from src.webapp.db import get_db, init_db

def test_count_base():
    assert(count(None) == -1)
    
