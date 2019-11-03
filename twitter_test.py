import unittest
import time
from selenium import webdriver
from Pages.PageIndex import *
from Pages.PageLogin import *
from Pages.PageHome import *
from Pages.PageRegister import *


class twitter(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("/usr/local/bin/chromedriver")
        self.driver.get("https://twitter.com/?lang=es")
        self.page_index = PageIndex(self.driver)
        self.page_register = PageRegister(self.driver)
        self.page_login = PageLogin(self.driver)
        self.page_home = PageHome(self.driver)

    # def test_register(self):
    #     self.page_index.click_register()
    #     self.page_register.signUp("AutomationTest","yorberunet@gmail.com")

    def test_login(self):
        self.page_index.go_to_login()
        self.page_login.login("pruebaautomati1", "Liftit123")

    def test_tweet_text(self):
        self.page_index.go_to_login()
        self.page_login.login("pruebaautomati1", "Liftit123")

        self.page_home.tweet_text()

    def test_tweet_image(self):
        self.page_index.go_to_login()
        self.page_login.login("pruebaautomati1", "Liftit123")

        self.page_home.tweet_image()

    def test_tweet_video(self):
        self.page_index.go_to_login()
        self.page_login.login("pruebaautomati1", "Liftit123")

        self.page_home.tweet_video()

    def test_tweet_link(self):
        self.page_index.go_to_login()
        self.page_login.login("pruebaautomati1", "Liftit123")

        self.page_home.tweet_link()

    def tearDown(self):
        time.sleep(10)
        self.driver.quit()
