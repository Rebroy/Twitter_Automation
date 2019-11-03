from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys


class PageHome:
    def __init__(self, myDriver):
        self.driver = myDriver
        self.text_box_tweet = (
            By.XPATH,
            '//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[2]/div[2]/div[1]/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div',
        )
        self.button_tweet = (
            By.XPATH,
            '//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div/div/div[2]/div[3]',
        )
        self.upload_image = (By.XPATH, "//input[@type='file']")
        self.play_video = (
            By.XPATH,
            '//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[2]/div[2]/div[1]/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[2]/div/div/video',
        )

    def tweet_text(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(*self.text_box_tweet).send_keys("¡ HOLA MUNDO !")
        self.driver.find_element(*self.button_tweet).click()

    def tweet_image(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(*self.text_box_tweet).send_keys("¡ MEME TIME !")
        self.driver.find_element(*self.upload_image).send_keys(
            "/home/yorber/Imágenes/memeqa.jpeg"
        )
        self.driver.implicitly_wait(10)
        self.driver.find_element(*self.button_tweet).click()

    def tweet_video(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(*self.text_box_tweet).send_keys("¡ VIDEO TIME !")
        self.driver.find_element(*self.upload_image).send_keys(
            "/home/yorber/Imágenes/videoTweet.mp4"
        )
        self.driver.find_element(*self.play_video).click()
        time.sleep(10)
        self.driver.find_element(*self.button_tweet).click()
        time.sleep(25)

    def tweet_link(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(*self.text_box_tweet).send_keys(
            "¡ GO TO! www.liftit.co"
        )
        self.driver.find_element(*self.button_tweet).click()
