import pytest
from config.config import TestData
from Pages.Loginpage import LoginPage
from Tests.test_base import BaseTest
from time import sleep


class Test_Login(BaseTest):

    def test_login_02(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USERNAME01, TestData.PASSWORD01)
        sleep(3)
