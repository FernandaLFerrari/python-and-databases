import unittest

class Teste(unittest.TestCase):
    
    def test_A(v1=2, v2=3):
        v1=2
        v2=2
        assert(v1 == v2)
        