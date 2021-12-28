import pytest
from base.webdriver_wrapper import WebDriverWrapper


class TestLogin(WebDriverWrapper):

    # def setup_method(self):
    #     print("start browser")

    def test_valid(self):
        print("test it")

    def test_invalid(self):
        print("test it")

    # def teardown_method(self):
    #     print("end browser")
