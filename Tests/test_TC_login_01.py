import pytest
from config.config import TestData
from Pages.Loginpage import LoginPage
from Tests.test_base import BaseTest
from time import sleep


class Test_Login(BaseTest):

    def test_login_01(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USERNAME, TestData.PASSWORD)
        sleep(3)

