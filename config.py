from selenium import webdriver
from dotenv import load_dotenv
import os

load_dotenv()
CHROME_PROFILE_PATH = os.getenv('CHROME_PROFILE_PATH')
# How to find chrome profile
# https://www.howtogeek.com/255653/how-to-find-your-chrome-profile-folder-on-windows-mac-and-linux/

# For Linux
# CHROME_PROFILE_PATH = '/home/<username>/.config/google-chrome/Default'

SELE_HUB_URL = os.getenv('SELE_HUB_URL')


# You can either use your own Chrome Browser
# Or use the remote selenium Chrome for isolated environment

#! Using Local Chrome
#options = webdriver.ChromeOptions()
#options.add_argument(f'--user-data-dir={CHROME_PROFILE_PATH}')
#driver = webdriver.Chrome(options)


#! using Remote Selenium
#! Mandatory when deployed on AWS
from selenium.webdriver.chrome.options import Options
import time
time.sleep(5) # wait for the selenium hub to start properly
options = Options()
options.set_capability("browserName", "chrome")
driver = webdriver.Remote(
    command_executor=SELE_HUB_URL,
    options=options
)
