import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

FB_EMAIL = YOUR EMAIL
FB_PASSWORD = FACEBOOK_PASSWORD

s = Service(YOUR PATH)
driver = webdriver.Chrome(service=s)

driver.get("http://www.tinder.com")

sleep(2)
login_button = driver.find_element(By.XPATH, '//*[@id="s-138260025"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
login_button.click()

sleep(2)
fb_login = driver.find_element(By.XPATH, '//*[@id="s-1866641101"]/div/div/div[1]/div/div[3]/span/div[2]/button')
fb_login.click()

#Switch to Facebook login window
sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

#Login and hit enter
email = driver.find_element(By.XPATH, '//*[@id="email"]')
password = driver.find_element(By.XPATH, '//*[@id="pass"]')
email.send_keys(FB_EMAIL)
password.send_keys(FB_PASSWORD)
password.send_keys(Keys.ENTER)

#Switch back to Tinder window
driver.switch_to.window(base_window)
print(driver.title)
sleep(5)

# Pop up cookies
location_popup = driver.find_element(By.XPATH, '//*[@id="s-1866641101"]/div/div/div/div/div[3]/button[1]')
location_popup.click()
sleep(3)
notification_popup = driver.find_element(By.XPATH, '//*[@id="s-1866641101"]/div/div/div/div/div[3]/button[2]')
notification_popup.click()
sleep(3)
cookies_popup = driver.find_element(By.XPATH, '//*[@id="s-138260025"]/div/div[2]/div/div/div[1]/button')
cookies_popup.click()
sleep(5)

x = 100
while x != 0:
    x -= 1
    try:
        sleep(2)
        body = driver.find_element(By.CSS_SELECTOR, 'body')
        body.send_keys(Keys.RIGHT)
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, ".itsAMatch a")
            match_popup.click()
        except NoSuchElementException:
            continue
