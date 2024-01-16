from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--ignore-ssl-errors")

driver = webdriver.Chrome(options=options)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

total_articles = driver.find_element(by=By.CSS_SELECTOR, value="#articlecount a")
print(total_articles.text)
# total_articles.click() # clicks on the element

# makes it easier to find a link by giving the text that is in between the anchor tag
community_portal = driver.find_element(by=By.LINK_TEXT, value="Community portal")
# community_portal.click()


search = driver.find_element(by=By.NAME, value="search")
search.send_keys("Python")  # it simulates keyboard input into a web element
search.send_keys(Keys.ENTER) # presses the enter key
# driver.close()
