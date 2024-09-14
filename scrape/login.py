from selenium import webdriver
from dotenv import load_dotenv
import os
import psutil
import time
import subprocess
from selenium.webdriver.chrome.options import Options
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


ARGUMENTS = [
    "--headless",  # Runs Chrome in headless mode
    "--disable-gpu",  # Disables GPU hardware acceleration
    "--blink-settings=imagesEnabled=false",  # Disables image loading
    "--disable-extensions",  # Disables all extensions
    "--disable-javascript",  # Disables JavaScript execution (if not needed)
    "--disable-notifications",  # Disables browser notifications
    "--disable-popup-blocking",  # Disables pop-up blocking
    "--no-sandbox",  # Disables the sandbox (not recommended for untrusted environments)
    "--disable-infobars",  # Disables the "Chrome is being controlled" info bar
    "--disable-software-rasterizer",  # Disables software rasterization
    "--disable-dev-shm-usage",  # Avoids low disk space issues in some environments (e.g., Docker)
    "--disable-smooth-scrolling",  # Disables smooth scrolling for better performance
    "--incognito",  # Runs Chrome in incognito mode
    "--disable-background-timer-throttling",  # Disables background tasks throttling
    "--disable-backgrounding-occluded-windows",  # Disables background occluded windows
    "--disable-breakpad",  # Disables crash reporting to save resources
    "--disable-component-extensions-with-background-pages",  # Disables extensions with background pages
    "--disable-sync",  # Disables Chrome sync
    "--mute-audio",  # Mutes audio
    "--autoplay-policy=no-user-gesture-required",  # Prevents videos from auto-playing
    "--disable-features=NetworkService,NetworkServiceInProcess",  # Reduces resource usage for network service
    "--disable-features=VizDisplayCompositor",  # Disables the display compositor
    "--window-size=800,600",  # Reduces window size for less rendering
    "--log-level=3",  # Reduces logging output (ERROR level)
    "user-agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Mobile Safari/537.36",  # Simulates mobile device to use fewer resources
    "--js-flags=--max_old_space_size=1024"  # Limits JavaScript heap size
]



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
def get_local_driver():
    kill_chrome_processes()
    try:
        options = webdriver.ChromeOptions()
        for arg in ARGUMENTS:
            options.add_argument(arg)
        driver = webdriver.Chrome(options)
        print("Chrome driver created successfully")
        print(driver)
        return driver
    except Exception as e:
        print(f"Error creating Chrome driver: {str(e)}")
        
def get_remote_driver():
    time.sleep(10)
    try:
        options = Options()
        options.set_capability("browserName", "chrome")
        options.headless = True
        for arg in ARGUMENTS:
            options.add_argument(arg)
        driver = webdriver.Remote(
            command_executor=SELE_HUB_URL,
            options=options
        )
    except Exception as e:
        print(f"Error creating Remote Chrome driver: {str(e)}")
    print("Remote Chrome driver created successfully")
    return driver

# driver = get_local_driver()

#! using Remote Selenium
#! Mandatory when deployed on AWS
driver = get_remote_driver()



