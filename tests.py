import unittest
from addition import *

class Tests(unittest.TestCase):

    def test_int(self):
        a=addition(1,1)
        self.assertEqual(a,2)


    def test_float(self):
        a=addition(3.14,1.86)
        self.assertEqual(a,5)


    def test_str(self):
        a=addition("at","choum")
        self.assertEqual(a,"atchoum")


    def __main__(self):
        self.test_int()
        self.test_float()
        self.test_str()

if __name__ == '__main__':
    unittest.main()

