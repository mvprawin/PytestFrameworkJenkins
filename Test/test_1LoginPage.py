from Config.config import TestData
from Test.test_base import BaseTest
from PageObjects.LoginPage import LoginPage
import allure


@allure.epic("OrangeHRM web Application")
@allure.feature("OrangeHRM Login Page test")
class Test_LoginPage(BaseTest):

    @allure.story("Login Page test with valid data testcases")
    @allure.severity(allure.severity_level.NORMAL)
    def test_loginpage_testcase(self):
        global loginpage
        self.loginpage = LoginPage(self.driver)
        self.login_page_title()
        self.login_with_credentials()

    @allure.step("Login Page title check")
    def login_page_title(self):
        title = self.loginpage.get_login_page_title(TestData.LOGIN_PAGE_TITLE)
        assert title == TestData.LOGIN_PAGE_TITLE

    @allure.step("Login with valid data")
    def login_with_credentials(self):
        self.loginpage.do_login(TestData.USERNAME, TestData.PASSWORD)

