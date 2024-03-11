from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep
import pytest


class TestData:
    CHROME_EXECUTABLE_PATH = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    FIREFOX_EXECUTABLE_PATH = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    BASE_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    USERNAME = "Admin"
    PASSWORD = "admin123"
    USERNAME01 = "Admin"
    PASSWORD01 = "Invalid Password"
    FIRSTNAME = "sarath"
    MIDDLENAME = "m"
    LASTNAME = "kumar"
    FIRSTNAME01 = "ilaya"
    MIDDLENAME01 = "raja"
    LASTNAME01 = "raja"
    EDIT_NAME = "VANA"
    ID = "0295"
    ID01 = "0357"



