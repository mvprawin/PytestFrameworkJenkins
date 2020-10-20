from selenium.webdriver.common.by import By
from Config.config import TestData
from PageObjects.BasePage import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    # Page Objects or Elements #
    # =========================

        self.USERNAME = driver.find_element(By.NAME, "txtUsername")
        self.PASSWORD = driver.find_element(By.NAME, "txtPassword")
        self.SUBMIT_BUTTON = driver.find_element(By.NAME, "Submit")

    # Methods #
    # ==========

    def enter_username(self, username):
        self.USERNAME.clear()
        self.USERNAME.send_keys(username)

    def enter_password(self, password):
        self.PASSWORD.clear()
        self.PASSWORD.send_keys(password)

    def click_login(self):
        self.SUBMIT_BUTTON.click()

    # Actions
    # ========

    def get_login_page_title(self, title):
        return self.get_title(title)

    def do_login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

