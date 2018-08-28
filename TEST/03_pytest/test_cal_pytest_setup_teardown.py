import pytest
import calculation

is_release = True

class TestCal(object):

    def setup_method(self,method):
        print("method={}".format(method.__name__))
        self.cal = calculation.Cal()

    def tearDown_method(self,method):
        print("method={}".format(method.__name__))
        del self.cal

    def test_add_num_and_double(self):
        assert self.cal.add_num_and_dobule(1,1) == 4

    def test_add_num_and_double_raise(self):
        with pytest.raises(ValueError):
            self.cal.add_num_and_dobule("1","1")
