
# Selenium is chosen because it ables to handle automation
# For example log in to Instagram which is needed to web scrape

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import os
import wget

driver = webdriver.Chrome('') # route to driver
driver.get('https://www.instagram.com/') # specify page opened by driver