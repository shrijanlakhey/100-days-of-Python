from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from dotenv import load_dotenv
from os import getenv

load_dotenv()
TWITTER_USERNAME = getenv("TWITTER_USERNAME")
TWITTER_PASSWORD = getenv("TWITTER_PASSWORD")

PROMISED_DOWN = 200
PROMISED_UP = 70

class InternetSpeedTwitterBot:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        options.add_argument("--ignore-ssl-errors")
        options.add_argument("--start-maximized")
        
        self.driver = webdriver.Chrome(options)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        """opens the speedtest website and scrapes the download and upload speed of the internet"""
        self.driver.get("https://www.speedtest.net/")
        # clicking the GO button
        go_button = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        go_button.click()
        sleep(80)
        
        # click close button when a modal appears
        close_button = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/div/p[2]/button')
        close_button.click()

        self.download = float(self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text)
        
        self.upload = float(self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text)


    def tweet_at_provider(self):
        """signs into user's twitter account and tweets a complain about the internet speed"""
        self.driver.get("https://twitter.com/")

        sleep(3)
        sign_in_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[5]/a')
        sign_in_button.click()

        sleep(5)
        username = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        username.send_keys(TWITTER_USERNAME)
        username.send_keys(Keys.ENTER)

        sleep(3)
        password = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.send_keys(TWITTER_PASSWORD)
        password.send_keys(Keys.ENTER)

        # creating a complain tweet
        sleep(5)
        tweet = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        complain = f"Hello Internet provider,why is my internet speed {self.download}down/{self.upload}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet.send_keys(complain)
        
        sleep(2)
        post_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]')
        post_button.click()
        
        sleep(5)
        self.driver.quit()

complain_bot = InternetSpeedTwitterBot()

complain_bot.get_internet_speed()
sleep(5)
# complain if the internet speed does not meet the promised download and upload speeds
if PROMISED_DOWN > complain_bot.download or PROMISED_UP > complain_bot.upload:
    complain_bot.tweet_at_provider()
else:
    # exit if speed is satisfactory
    print("No need to complain")
    complain_bot.driver.quit()


