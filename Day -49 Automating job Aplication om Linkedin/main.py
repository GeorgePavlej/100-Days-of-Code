import selenium
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

MY_EMAIL = "gyorgypavlej@yahoo.com"
PASSWORD = "13570530"
PHONE_NUMBER = "+4478596545"

s = Service("C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")

time.sleep(2)
email = driver.find_element(By.XPATH, '//*[@id="username"]')
email.send_keys(MY_EMAIL)
password = driver.find_element(By.XPATH, '//*[@id="password"]')
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)
time.sleep(2)
driver.get("https://www.linkedin.com/jobs/search/?f_AL=true&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom")
time.sleep(2)

all_jobs = driver.find_elements(By.CSS_SELECTOR, '.job-card-container--clickable')

for job in all_jobs:
    print("done")
    job.click()
    try:
        apply_button = driver.find_element(By.CSS_SELECTOR, '.jobs-apply-button--top-card')
        apply_button.click()
        time.sleep(2)

        phone = driver.find_element(By.CSS_SELECTOR, '.display-flex input')
        if phone.text == " ":
            phone.send_keys(PHONE_NUMBER)

        submit_button = driver.find_element(By.CSS_SELECTOR, '.artdeco-button--primary')
        submit_button.click()
        time.sleep(2)
        try:
            radio_button = driver.find_element(By.CSS_SELECTOR, '.fb-radio display-flex input').click()
            print(radio_button)
            time.sleep(1)
        except NoSuchElementException:
            continue
        submit_button.click()
        
    except NoSuchElementException:
        print("No application button, skipped.")
        continue
