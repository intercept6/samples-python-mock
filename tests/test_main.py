from unittest.mock import patch

import pytest

from main import MyClass

params = {
    "1": ("in_value1", "out_value1")
}


class TestClass(object):

    @patch("main.MyClass.sample_method", return_value="mocked")
    @pytest.mark.parametrize('in_value, out_value', list(params.values()), ids=list(params.keys()))
    def test_method(self, mock, in_value, out_value):
        m = MyClass()
        assert m.sample_method() == "mocked"

    @patch.object(MyClass, "sample_static_method", return_value="mocked")
    def test_static_method(self, mock):
        assert MyClass.sample_static_method() == "mocked"

    @patch.object(MyClass, "sample_class_method", return_value="mocked")
    def test_class_method(self, mock):
        assert MyClass.sample_class_method() == "mocked"

    @pytest.mark.parametrize('in_value, out_value', [("1", "2")])
    def test_parametrize(self, in_value, out_value):
        return in_value
