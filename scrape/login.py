from selenium import webdriver
from dotenv import load_dotenv
import os
import psutil
import time
import subprocess
import shutil
# You can either use your own Chrome Browser
# Or use the remote selenium Chrome for isolated environment

# How to find chrome profile
# https://www.howtogeek.com/255653/how-to-find-your-chrome-profile-folder-on-windows-mac-and-linux/

# For Linux
# CHROME_PROFILE_PATH = '/home/<username>/.config/google-chrome/Default'
load_dotenv()
CHROME_PROFILE_PATH = os.getenv('CHROME_PROFILE_PATH').strip()
SELE_HUB_URL = os.getenv('SELE_HUB_URL').strip()
cache_dir = os.path.join(CHROME_PROFILE_PATH, 'Cache')
devtoool_dir = os.path.join(CHROME_PROFILE_PATH, 'DevToolsActivePort')

# print(f"Chrome Profile Path: {CHROME_PROFILE_PATH}")
# print(f"Cache Directory: {cache_dir}")
# print(f"Devtool Directory: {devtoool_dir}")


def kill_chrome_processes():
    """
    Kill all Chrome tasks to prevent selenium from attaching to random user Chrome profile
    """
    subprocess.run(["taskkill", "/F", "/IM", "chrome.exe"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # kill remaining tasks
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'] == 'chrome.exe':
            try:
                process.terminate()
                process.wait(timeout=5)  # wait for the process to terminate
            except psutil.NoSuchProcess:
                pass
            except psutil.TimeoutExpired:
                process.kill()  # force kill if termination times out
    
    # Wait until all Chrome processes are gone
    while any(process.info['name'] == 'chrome.exe' for process in psutil.process_iter(['name'])):
        time.sleep(1)

    print("All Chrome processes have been terminated.")


#! Using Local Chrome
def get_driver():
    kill_chrome_processes()
    try:
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-extensions')
        options.add_argument('--disable-browser-side-navigation')
        options.add_argument('--remote-debugging-port=9222') 
        options.add_argument(f'--user-data-dir={CHROME_PROFILE_PATH}')
        driver = webdriver.Chrome(options)
        print("Chrome driver created successfully")
        print(driver)
        return driver
    except Exception as e:
        print(f"Error creating Chrome driver: {str(e)}")
        
# kill_chrome_processes()
driver = get_driver()

#! using Remote Selenium
#! Mandatory when deployed on AWS
# from selenium.webdriver.chrome.options import Options
# import time
# time.sleep(10) # wait for the selenium hub to start properly
# options = Options()
# options.set_capability("browserName", "chrome")
# driver = webdriver.Remote(
#     command_executor=SELE_HUB_URL,
#     options=options
# )
