import unittest
from math import *

class TestMath(unittest.TestCase):

    def setUp(self):
        print("setup!!")

    def test_add(self):
        print("add!")
        value1 = 2
        value2 = 6
        expected = 8
        actual = add(value1, value2)
        self.assertEqual(expected, actual)

    def test_sub(self):
        print("sub!")
        value1 = 6
        value2 = 2
        expected = 4
        actual = sub(value1, value2)
        self.assertEqual(expected, actual)

    def tearDown(self):
        print("teardown!!\n")

if __name__ == "__main__":
    unittest.main()
