import pytest
from base.webdriver_wrapper import WebDriverWrapper
from orange_pages.login_page import LoginPage
from orange_pages.main_page import MainPage


# from ddt import ddt, data, unpack


class TestLogin(WebDriverWrapper):

    def test_valid_login(self):
        login = LoginPage(self.driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()
        main = MainPage(self.driver)
        assert "My Info" == main.get_my_info_text()

    @pytest.mark.parametrize("username,password", [["bala", "bala123"], ["dina1", "dina2"]])
    def test_invalid_login(self, username, password):
        login = LoginPage(self.driver)
        login.enter_username(username)
        login.enter_password(password)
        login.click_login()
        assert "Invalid credentials" == login.get_error_text()
