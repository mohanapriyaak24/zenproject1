from config.config import TestData
from Pages.Loginpage import LoginPage
from Pages.Homepage import HomePage
from Tests.test_base import BaseTest
import pyautogui
from time import sleep


class Test_pim_02(BaseTest):

    def test_login_02(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USERNAME, TestData.PASSWORD)
        sleep(3)

    def test_del_emp(self):
        self.homePage = HomePage(self.driver)
        self.homePage.do_click_pim()
        sleep(3)
        self.homePage.edit_emp(TestData.ID01,TestData.FIRSTNAME01)
        sleep(5)


