import unittest
from main import add

class TestAdd(unittest.TestCase):
    def test_main(self):
        self.assertEqual(add(2,3),6)
        self.assertEqual(add(-1,1),0)
        self.assertEqual(add(0,0),0)
        
if __name__=="__main__":

    unittest.main
