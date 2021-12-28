from selenium.webdriver.common.by import By


class MainPage():
    def __init__(self, driver):
        self.driver = driver

    def get_my_info_text(self):
        return self.driver.find_element(By.XPATH, "//*[text()='My Info']").text
