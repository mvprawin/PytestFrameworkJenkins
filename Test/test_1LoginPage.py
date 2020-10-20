from Config.config import TestData
from Test.test_base import BaseTest
from PageObjects.LoginPage import LoginPage


class Test_LoginPage(BaseTest):

    def test_loginpage_testcase(self):
        global loginpage
        self.loginpage = LoginPage(self.driver)
        self.login_page_title()
        self.login_with_credentials()

    def login_page_title(self):
        title = self.loginpage.get_login_page_title(TestData.LOGIN_PAGE_TITLE)
        assert title == TestData.LOGIN_PAGE_TITLE

    def login_with_credentials(self):
        self.loginpage.do_login(TestData.USERNAME, TestData.PASSWORD)

