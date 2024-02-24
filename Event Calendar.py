from selenium import webdriver
from time import sleep
def eventCalender():
    options = webdriver.ChromeOptions()
    # Path to your chrome profile (For now its for MacOs)
    # How to find chrome profile https://www.howtogeek.com/255653/how-to-find-your-chrome-profile-folder-on-windows-mac-and-linux/
    options.add_argument('user-data-dir=~/Library/Application Support/Google/Chrome/Default')
    driver = webdriver.Chrome(options)
    driver.get('https://www.campusgroups.com/shibboleth/login?idp=usf') # Auto login
    driver.get('https://bullsconnect.usf.edu/events?topic_tags=7276307') # Opening event calendar with tag food
    sleep(10)