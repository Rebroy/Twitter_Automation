from selenium.webdriver.support.ui import Select
import unittest
from selenium.webdriver.common.by import By


class PageRegister:
    def __init__(self, myDriver):
        self.driver = myDriver
        # self.link_registration_form = (By.LINK_TEXT, "registration form")
        self.user_box = (By.NAME, "name")
        self.email_box = (By.NAME, "email")
        self.link_use_mail = (
            By.XPATH,
            '//*[@id="react-root"]/div/div/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[4]',
        )

    def signUp(self, user_name, email):
        self.driver.implicitly_wait(5)
        self.driver.find_element(*self.link_use_mail).click()
        self.driver.find_element(*self.user_box).send_keys(user_name)
        self.driver.find_element(*self.email_box).send_keys(email)

    # def verify_registration_form(self):
    #     tc = unittest.TestCase("__init__")
    #     self.driver.implicitly_wait(5)
    #     registration_link = self.driver.find_element(*self.link_registration_form)
    #     tc.assertEqual(registration_link.text, "registration form")

