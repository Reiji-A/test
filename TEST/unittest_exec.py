# =*= coding:utf-8 =*=
from hoge import tashizan,hikizan
import unittest

class TestTashizan(unittest.TestCase):
    """test class of tashizan.py
    """

    def test_tashizan(self):
        """test method for tashizan
        """
        value1 = 2
        value2 = 6
        expected = 8
        actual = tashizan(value1, value2)
        self.assertEqual(expected, actual)

class TestKeisan2(unittest.TestCase):

    def test_hikizan(self):
        """test method for hikizan
        """
        value1 = 2
        value2 = 12
        expected = -10
        actual = hikizan(value1, value2)
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
