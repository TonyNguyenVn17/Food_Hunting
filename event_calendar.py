from selenium import webdriver
from selenium.webdriver.common.by import By
import time
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

    def check_exists_by_ID(ID):
        try:
            driver.find_element(By.ID, ID)
        except:
            return False
        return True

    # Auto login
    driver.get('https://www.campusgroups.com/shibboleth/login?idp=usf')
    time.sleep(10)
    # Loop until a hooman log in and authenticate
    while check_exists_by_ID("i011") == True or check_exists_by_ID("displayName")==True:  # A random element in the USF login website
        print('Error: Need hooman authentication')
        driver.get('https://www.campusgroups.com/shibboleth/login?idp=usf')
        time.sleep(100)  # 100 seconds to enter username, password and authenticate
    else:
        driver.get('https://bullsconnect.usf.edu/events?topic_tags=7276307')
        time.sleep(1)
if __name__ == "__main__":
    eventCalendar()