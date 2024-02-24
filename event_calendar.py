from selenium import webdriver
from time import sleep
from dotenv import load_dotenv
import os
# sign in with usf account then log out then run the program again
#!DO NOT TURN OFF THE COMPUTER

load_dotenv()
CHROME_PROFILE_PATH = os.getenv('CHROME_PROFILE_PATH')
# CHROME_PROFILE_PATH = '/home/<username>/.config/google-chrome/Default'


def eventCalendar():
    options = webdriver.ChromeOptions()
    # Path to your chrome profile (Either Linux/Mac/Windows)
    # How to find chrome profile https://www.howtogeek.com/255653/how-to-find-your-chrome-profile-folder-on-windows-mac-and-linux/
    options.add_argument(f'--user-data-dir={CHROME_PROFILE_PATH}')
    driver = webdriver.Chrome(options)
    # Auto login
    driver.get('https://www.campusgroups.com/shibboleth/login?idp=usf')
    sleep(10)
    # Opening event calendar with tag food
    driver.get('https://bullsconnect.usf.edu/events?topic_tags=7276307')
    sleep(10)


if __name__ == "__main__":
    eventCalendar()
