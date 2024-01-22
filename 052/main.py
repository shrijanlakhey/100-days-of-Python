from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from time import sleep
from dotenv import load_dotenv
from os import getenv

SIMILAR_ACCOUNT = "spursofficial"
load_dotenv()
INSTAGRAM_EMAIL = getenv("INSTAGRAM_EMAIL")
INSTAGRAM_PASSWORD = getenv("INSTAGRAM_PASSWORD")


class InstaFollower:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        options.add_argument("--ignore-ssl-errors")

        self.driver = webdriver.Chrome(options)

    def login(self):
        """logins into the user's Instagram account"""
        self.driver.get("https://www.instagram.com/accounts/login/")
        sleep(3)
        username = self.driver.find_element(By.NAME, "username")
        username.send_keys(INSTAGRAM_EMAIL)
        
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys(INSTAGRAM_PASSWORD)
        password.send_keys(Keys.ENTER)


    def find_followers(self):
        """opens up the SIMILAR_ACCOUNT and retrieves the list of followers"""
        sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers")
        sleep(7)
        scroll = self.driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]')
        scroll.click()
        
        # scrolling through the follower list
        for i in range(10):
            # scrollTop: sets the number of pixels that an element's content is scrolled vertically
            # scrollHeight: measurement of the height of an element's content, including content not visible on the screen due to overflow
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll)
            sleep(2)

    def follow(self):
        """follows the accounts that are following the SIMILAR_ACCOUNT"""
        follow_buttons = self.driver.find_elements(By.CSS_SELECTOR, "._aano ._acan")
        for button in follow_buttons:
            try:
                button.click()
                sleep(2)
            except ElementClickInterceptedException:
                # if the acount has already been followed, then it will click 'cancel' when a modal appears asking if it wants to unfollow the account
                cancel_button = self.driver.find_element(By.XPATH, '/html/body/div[7]/div[1]/div/div[2]/div/div/div/div/div/div/button[2]')
                cancel_button.click()                


follower_bot = InstaFollower()

follower_bot.login()
follower_bot.find_followers()
follower_bot.follow()
