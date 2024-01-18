from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
import time
from dotenv import load_dotenv
from os import getenv

load_dotenv()
TINDER_EMAIL = getenv("TINDER_EMAIL")
TINDER_PASSWORD = getenv("TINDER_PASSWORD")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--ignore-ssl-errors")


driver = webdriver.Chrome(options=options)

driver.get("https://tinder.com/")
# Delay by 4 seconds to allow the page to load
time.sleep(4)
log_in_button = driver.find_element(By.LINK_TEXT, "Log in")
log_in_button.click()

time.sleep(3)
log_in_with_facebook = driver.find_element(
    By.XPATH,
    '//*[@id="s104987503"]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button',
)
log_in_with_facebook.click()

time.sleep(3)

# switching windows to Facebook login page window
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)
email = driver.find_element(By.NAME, "email")
email.send_keys(TINDER_EMAIL)
password = driver.find_element(By.NAME, "pass")
password.send_keys(TINDER_PASSWORD)
password.send_keys(Keys.ENTER)

# swtiching back to the Tinder page window
base_window = driver.window_handles[0]
driver.switch_to.window(base_window)
print(driver.title)
# adding multiple delays below to allow the elements to load properly
time.sleep(5)


# allowing Tinder to share my location
allow_button = driver.find_element(
    By.XPATH, '//*[@id="s104987503"]/main/div[1]/div/div/div[3]/button[1]'
)
allow_button.click()
time.sleep(3)


# accepting cookies
accept_cookies_button = driver.find_element(
    By.XPATH, '//*[@id="s104987503"]/main/div[2]/div/div/div[1]/div[1]/button'
)
accept_cookies_button.click()

# disabling nptifications
disable_notif_button = driver.find_element(
    By.XPATH, '//*[@id="s104987503"]/main/div[1]/div/div/div[3]/button[2]'
)
disable_notif_button.click()
time.sleep(3)

# ActionChains are a way to automate low level interactions such as mouse movements, mouse button actions, key press,etc.
action = ActionChains(driver)

# executing this block of code 100 times only because Tinder allows 100 swipes per day for free tier accounts
for i in range(100):
    time.sleep(1)

    try:
        print("working")
        # pressing left arrow keys
        action.send_keys(Keys.ARROW_LEFT)
        action.perform()

    except NoSuchElementException:
        time.sleep(3)

driver.quit()
