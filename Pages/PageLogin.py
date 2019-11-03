from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys


class PageLogin:
    def __init__(self, myDriver):
        self.driver = myDriver
        self.userName_box = (
            By.XPATH,
            '//*[@id="page-container"]/div/div[1]/form/fieldset/div[1]/input',
        )
        self.password_box = (By.CLASS_NAME, "js-password-field")
        self.login_button = (
            By.XPATH,
            '//*[@id="page-container"]/div/div[1]/form/div[2]/button',
        )

    def login(self, user_name, password):
        self.driver.implicitly_wait(5)
        self.driver.find_element(*self.userName_box).send_keys(user_name)
        self.driver.find_element(*self.password_box).send_keys(password)
        self.driver.find_element(*self.login_button).click()
