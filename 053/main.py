from bs4 import BeautifulSoup
import requests
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

SF_RENT_URL = "https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22isMapVisible%22%3Atrue%2C%22mapBounds%22%3A%7B%22north%22%3A37.85665779339626%2C%22south%22%3A37.6938364677167%2C%22east%22%3A-122.29840365771484%2C%22west%22%3A-122.56825534228516%7D%2C%22mapZoom%22%3A12%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22price%22%3A%7B%22min%22%3Anull%2C%22max%22%3A872627%7D%2C%22mp%22%3A%7B%22min%22%3Anull%2C%22max%22%3A3000%7D%2C%22beds%22%3A%7B%22min%22%3A1%2C%22max%22%3Anull%7D%7D%2C%22isListVisible%22%3Atrue%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22pagination%22%3A%7B%7D%7D"
FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSfcO4zBum37hpfGhpwNgb-yvMqBjFLFNogri9gxdekrYVnd4g/viewform?usp=sf_link"

headers = {
    "Accept-Language": "en-US,en;q=0.5",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
}

response = requests.get(url=SF_RENT_URL, headers=headers)
rent_data = response.content

soup = BeautifulSoup(rent_data, "lxml")

# scraping the rent price of the listings
price_elements = soup.select(selector=".property-card-data span")
rent_prices = []
for price in price_elements:
    # splitting string using regual expression
    rent_prices.append(re.split(r"[+/]", price.getText())[0])

# scrapping addresses of the listings
address_elements = soup.select(selector=".property-card-data address")
address_list = []
for address in address_elements:
    if "|" in address.getText():
        address_list.append(address.getText().split("|")[1])
    else:
        address_list.append(address.getText())

# scraping links of the listings:
hyperlink_elements = soup.select(selector=".property-card-data a")
link_list = []
# link_starter = "https://www.zillow.com"
for link in hyperlink_elements:
    if "zillow" not in link.get('href'):
        link_list.append(f"https://www.zillow.com{link.get('href')}")
    else:
        link_list.append(link.get("href"))

# Using Selenium to fill out the form
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--ignore-ssl-errors")

driver = webdriver.Chrome(options)
driver.get(FORM_URL)


for i in range(len(rent_prices)):
    sleep(1)
    address_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_input.send_keys(address_list[i])

    price_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input.send_keys(rent_prices[i])

    link_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input.send_keys(link_list[i])

    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    submit_button.click()

    new_entry = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    new_entry.click()

driver.quit()