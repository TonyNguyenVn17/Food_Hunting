from selenium import webdriver
from dotenv import load_dotenv
import os

load_dotenv()
CHROME_PROFILE_PATH = os.getenv('CHROME_PROFILE_PATH')
# CHROME_PROFILE_PATH = '/home/<username>/.config/google-chrome/Default'

options = webdriver.ChromeOptions()
# Path to your chrome profile (Either Linux/Mac/Windows)
# How to find chrome profile https://www.howtogeek.com/255653/how-to-find-your-chrome-profile-folder-on-windows-mac-and-linux/
options.add_argument(f'--user-data-dir={CHROME_PROFILE_PATH}')
driver = webdriver.Chrome(options)
