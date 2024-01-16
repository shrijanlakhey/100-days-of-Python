from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--ignore-ssl-errors")

driver = webdriver.Chrome(options=options)

# driver.get("https://www.amazon.com/Kindle-Paperwhite-adjustable-Ad-Supported/dp/B08KTZ8249")

# # delaying code execution to solve captcha manually
# time.sleep(10)

# title = driver.find_element(by=By.ID, value="productTitle")
# print(title.text)

# price = driver.find_element(by=By.CLASS_NAME, value="apexPriceToPay")
# print(price.text)


driver.get("https://www.python.org/")

search_bar = driver.find_element(by=By.NAME, value="q")
# print(search_bar.tag_name)
print(search_bar.get_attribute("placeholder"))  # returns the value of an attribute of the selected element

logo = driver.find_element(by=By.CLASS_NAME, value="python-logo")
print(logo.size)  # returns size of the logo

documentation_link = driver.find_element(by=By.CSS_SELECTOR, value=".documentation-widget a")
print(documentation_link.text)

# XPATH = way of locating specific HTML element by a path structure 
bug_link = driver.find_element(by=By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text)


# closes a single tab (active tab)
driver.close()

# closes the entire browser
# driver.quit()
