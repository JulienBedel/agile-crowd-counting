import unittest
import random

from src.count.counter import count

def test_count_base():
    assert(count(None) == -1)
    
