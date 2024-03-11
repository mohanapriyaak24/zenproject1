from Pages.Homepage import HomePage
from config.config import TestData
from Pages.Loginpage import LoginPage
from Pages.Homepage import HomePage
from Tests.test_base import BaseTest
from time import sleep


class Test_pim_01(BaseTest):

    def test_login_01(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USERNAME, TestData.PASSWORD)
        sleep(3)

    def test_pim_01(self):
        self.homePage = HomePage(self.driver)
        self.homePage.do_click_pim()
        sleep(5)
        self.homePage.delete_emp(TestData.ID)
        sleep(5)








