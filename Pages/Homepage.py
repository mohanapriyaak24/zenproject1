from selenium.webdriver.chrome import webdriver
from Pages.Basepage import BasePage
from selenium.webdriver.common.by import By
from config.config import TestData
from selenium.common.exceptions import TimeoutException
from time import sleep


class HomePage(BasePage):
    PIM = (By.XPATH, "//a[contains(.,'PIM')]")
    ADD_BUTTON = (By.XPATH, "//button[contains(.,'Add')]")
    FIRST_NAME = (By.XPATH, "//input[@name='firstName']")
    MIDDLE_NAME = (By.XPATH, "//input[@name='middleName']")
    LAST_NAME = (By.XPATH, "//input[@name='lastName']")
    SAVE_BUTTON = (By.XPATH, "//button[@type='submit']")
    ADMIN = (By.XPATH, "//span[text()='Admin']")
    DELETE_EMP = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div['
                            '9]/div/button[1]')
    DELETE_BUTTON = (By.XPATH, '//*[@id="app"]/div[3]/div/div/div/div[3]/button[2]')
    SEARCH = (By.XPATH, "//button[.=' Search ']")
    EMP_ID = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/input")
    EDIT_EMP = (By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div')
    SAVE_EMP = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)
        self.do_max()

    def do_click_pim(self):
        self.do_click(self.PIM)

    def do_click_add_button(self):
        self.do_click(self.ADD_BUTTON)

    def enter_name(self, firstname, middlename, lastname):
        self.do_sendkeys(self.FIRST_NAME, firstname)
        self.do_sendkeys(self.MIDDLE_NAME, middlename)
        self.do_sendkeys(self.MIDDLE_NAME, lastname)
        self.do_click(self.SAVE_BUTTON)

    def delete_emp(self, emp_id):
        self.do_sendkeys(self.EMP_ID, emp_id)
        self.do_click(self.SEARCH)
        self.do_click(self.DELETE_EMP)
        self.do_click(self.DELETE_BUTTON)

    def edit_emp(self, emp_id, name):
        self.do_sendkeys(self.EMP_ID, emp_id)
        self.do_click(self.SEARCH)
        self.do_click(self.EDIT_EMP)
        self.do_sendkeys(self.FIRST_NAME,name)
        self.do_scroll()
        self.do_click(self.SAVE_EMP)