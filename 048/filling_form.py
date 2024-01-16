from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--ignore-ssl-errors")

driver = webdriver.Chrome(options=options)

driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(by=By.NAME, value="fName")
first_name.send_keys("John")

last_name = driver.find_element(by=By.NAME, value="lName")
last_name.send_keys("Doe")

email = driver.find_element(by=By.NAME, value="email")
email.send_keys("johndoe@gmail.com")

signup_button = driver.find_element(by=By.TAG_NAME, value="button")
signup_button.send_keys(Keys.ENTER)
