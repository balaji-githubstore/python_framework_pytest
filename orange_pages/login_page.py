from selenium import webdriver
from selenium.webdriver.common.by import By

from base.webdriver_wrapper import WebDriverWrapper


class LoginPage():
    __username_locator="txtUsername"
    __password_locator="txtPassword"
    __logout_locator="//*[@type='submit']"

    def __init__(self,driver):
        self.driver=driver

    def enter_username(self,username):
        self.driver.find_element(By.ID, LoginPage.__username_locator).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element(By.ID, self.__password_locator).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.__logout_locator).click()

    def get_error_text(self):
        return self.driver.find_element(By.ID, "spanMessage").text