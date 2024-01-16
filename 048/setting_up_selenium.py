from selenium import webdriver

# adding these two lines to stop the browser from closing automatically
# Detaching means that even if the WebDriver process (your Python script) finishes execution, the Chrome browser window will continue to run independently.
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

driver.get("https://www.google.com")

# closes a single tab (active tab)
driver.close()

# closes the entire browser
# driver.quit()
