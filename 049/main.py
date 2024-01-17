from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
from dotenv import load_dotenv
from os import getenv

load_dotenv()
LINKEDIN_EMAIL = getenv("LINKEDIN_EMAIL")
LINKEDIN_PASSWORD = getenv("LINKEDIN_PASSWORD")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--ignore-ssl-errors")


driver = webdriver.Chrome(options=options)

driver.get(
    "https://www.linkedin.com/jobs/search/?currentJobId=3799287133&keywords=Python%20Developer&origin=JOBS_HOME_KEYWORD_AUTOCOMPLETE&refresh=true"
)

# clicking on sign in button
sign_in_button = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in_button.click()

# wait 3 seconds for the sign in page to load
time.sleep(3)

# Signing in using email and password
email = driver.find_element(By.ID, "username")
email.send_keys(LINKEDIN_EMAIL)

password = driver.find_element(By.ID, "password")
password.send_keys(LINKEDIN_PASSWORD)

# press enter to sign in to the account
password.send_keys(Keys.ENTER)


# Job search page
time.sleep(15) # initially, the time set before opening the job search page was 5 sec but due to time allocated to solving captcha, it has been raisd to 15 seconds

# scraping list of jobs
job_list = driver.find_elements(By.CLASS_NAME, "job-card-container--clickable")

for list in job_list:
    # scrolls down until the current job listing is visible
    driver.execute_script("arguments[0].scrollIntoView(true);", list)
    list.click()
    time.sleep(2)
    try:
        # save the job
        save_button = driver.find_element(By.CLASS_NAME, "jobs-save-button")
        save_button_text = driver.find_element(By.CSS_SELECTOR, ".jobs-save-button span").text

        if save_button_text == "Saved":
            continue
        else:
            save_button.click()


        # follow the company that posted for the job
        follow_button = driver.find_element(By.CLASS_NAME, "follow")

        # scrolls down until the follow button is visible
        driver.execute_script("arguments[0].scrollIntoView(true);", follow_button)

        follow_button_text = driver.find_element(By.CSS_SELECTOR, ".follow span").text
        if follow_button_text == "Following":
            continue
        else:
            follow_button.click()
    except NoSuchElementException:
        print("Already saved the post or followed the account")
        continue

# wait 7 seconds before closing the tab
time.sleep(7)

driver.quit()
