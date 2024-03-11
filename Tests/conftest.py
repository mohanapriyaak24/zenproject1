import pytest
from selenium import webdriver
from config.config import TestData


@pytest.fixture(params=["chrome", "firefox"], scope='class')
def init_driver(request):
    if request.param == "chrome":
        web_driver = TestData.CHROME_EXECUTABLE_PATH
    if request.param == "firefox":
        web_driver = TestData.FIREFOX_EXECUTABLE_PATH
    request.cls.driver = web_driver
    yield
    web_driver.close()