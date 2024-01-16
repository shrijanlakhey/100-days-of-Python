from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--ignore-ssl-errors")

driver = webdriver.Chrome(options=options)

driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(by=By.ID, value="cookie")

# scraping the ids the of the items from the store
store = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")
item_ids = [item.get_attribute("id") for item in store]

five_sec_check = time.time() + 30  # 30 seconds from now
five_min_timeout = time.time() + 60 * 5  # 5 minutes from now
while True:
    cookie.click()
    if time.time() > five_sec_check:
        # scrapting the prices of the items
        all_prices = driver.find_elements(by=By.CSS_SELECTOR, value="#store div b")
        item_prices = []
        for item in all_prices:
            if item.text != "":
                price = int(item.text.split("-")[1].replace(",", ""))
                item_prices.append(price)

        # creating a dictionary of upgrades with the id of the items and its prices
        upgrades = {}
        for n in range(len(item_prices)):
            upgrades[item_ids[n]] = item_prices[n]

        # scraping the money and converting into int type
        money_text = driver.find_element(by=By.ID, value="money").text
        if "," in money_text:
            money_text = money_text.replace(",", "")
        money = int(money_text)

        # creating a dictionay of affordable upgrades with cost as the key and the upgrade's id as the values
        can_upgrade = {}
        for id, cost in upgrades.items():
            if money > cost:
                can_upgrade[cost] = id

        highest_affordable_price = max(can_upgrade)

        # clicking on the upgrade with the highest price
        to_upgrade = can_upgrade[highest_affordable_price]
        driver.find_element(by=By.ID, value=to_upgrade).click()
        # adding 15 seconds until the next check
        five_sec_check = time.time() + 15

    # breaks out of loop if 5 minutes have passed
    if time.time() > five_min_timeout:
        cookie_per_second = driver.find_element(by=By.ID, value="cps").text
        print(cookie_per_second)
        break


driver.quit()
