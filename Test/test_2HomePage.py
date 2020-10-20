import allure

from Config.config import TestData
from PageObjects.HomePage import HomePage
from PageObjects.LoginPage import LoginPage
from Test.test_base import BaseTest


@allure.epic("OrangeHRM web Application")
@allure.feature("OrangeHRM Home Page test")
class Test_HomePage(BaseTest):

    @allure.story("Home Page test testcases")
    @allure.severity(allure.severity_level.NORMAL)
    def test_homepage_testcase(self):
        global loginpage
        self.loginpage = LoginPage(self.driver)
        self.login_check()

        global homepage
        self.homepage = HomePage(self.driver)
        self.home_page_title_check()
        self.account_name_check()
        self.marketplace_link_check()

    @allure.step("Login with valid data")
    def login_check(self):
        self.loginpage.do_login(TestData.USERNAME, TestData.PASSWORD)

    @allure.step("Home Page title check")
    def home_page_title_check(self):
        title = self.homepage.get_home_page_title(TestData.HOME_PAGE_TITLE)
        assert title == TestData.HOME_PAGE_TITLE

    @allure.step("Account name displayed check")
    def account_name_check(self):
        account = self.homepage.get_account_name()
        assert account == TestData.ACCOUNT_NAME

    @allure.step("Marketplace link redirection check")
    def marketplace_link_check(self):
        self.homepage = HomePage(self.driver)
        self.homepage.click_marketplace()


