# Web Scrap Insta

# Selenium is chosen because it ables to handle automation
# For example log in to Instagram which is needed to web scrape

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from scrape.login import driver
import time



# Create a new instance of the Chrome driver to open the browser
driver.get('https://www.instagram.com/') # specify page opened by driver


# Set up the username and password
# username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name= 'username']")))
# password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name= 'password']")))

# # Clear the input fields and enter the username and password
# username.clear()
# password.clear()
# username.send_keys("Tgiao9123@gmail.com")
# password.send_keys("Usf12345678^")


# # Make the driver click the login button
# log_in = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
# time.sleep(3)

# # Make the driver click the not now button
# not_now = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[contains(text(), "Not now") and @role="button"]'))).click()
# time.sleep(3)

# # Make the driver click the second not now button
# not_now2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button._a9--._ap37._a9_1'))).click()

# Change window size to iphone size
driver.set_window_size(450, 800)

# Wait for the search icon to be visible and clickable
searchbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))
searchbox.clear()
keyword = "shpeusf"
searchbox.send_keys(keyword)
searchbox.send_keys(Keys.ENTER)

# Wait for the search results to load
time.sleep(3)

# Click on the first account
account = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/shpeusf/']")))
account.click()


# if close window is click stopped the program
while True:
    pass

    
