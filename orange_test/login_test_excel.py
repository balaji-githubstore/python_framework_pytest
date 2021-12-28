import pytest

from base.webdriver_wrapper import WebDriverWrapper
from orange_pages.login_page import LoginPage
from orange_pages.main_page import MainPage
from utilities import read_data


class Test1Login(WebDriverWrapper):

    @pytest.mark.parametrize("username,password,expectedtext",
                             read_data.get_sheet_data('../data/OrangeHrmData.xlsx', "VerifyValidCredentialTemplate"))
    def test_invalid_login(self, username, password, expectedtext):
        login = LoginPage(self.driver)
        login.enter_username(username)
        login.enter_password(password)
        login.click_login()
        assert "Invalid credentials" == login.get_error_text()
