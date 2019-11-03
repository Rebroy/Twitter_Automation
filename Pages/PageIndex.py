from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys


class PageIndex:
    def __init__(self, myDriver):
        self.driver = myDriver
        self.register_link = (By.LINK_TEXT, "Regístrate")
        self.login_link = (By.LINK_TEXT, "Iniciar sesión")
        self.userName_box = (By.NAME, "session[username_or_email]")
        self.password_box = (By.NAME, "session[password]")

    # def click_register(self):
    #     self.driver.implicitly_wait(5)
    #     self.driver.find_element(*self.register_link).click()

    def go_to_login(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(*self.login_link).click()
