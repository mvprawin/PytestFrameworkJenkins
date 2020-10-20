from selenium.webdriver.common.by import By

from Config.config import TestData
from PageObjects.BasePage import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    # Page Objects or Elements #
    # =========================

        self.ACCOUNT = driver.find_element(By.ID, "welcome")
        self.MARKET_LINK = driver.find_element(By.ID, "MP_link")

    # Methods #
    # ==========
    def click_marketplace(self):
        self.MARKET_LINK.click()

    # Actions #
    # =========
    def get_home_page_title(self, title):
        return self.get_title(title)

    def get_account_name(self):
        return self.ACCOUNT.text
