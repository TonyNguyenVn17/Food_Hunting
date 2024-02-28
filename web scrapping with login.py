from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import datetime
from dotenv import load_dotenv
import os

def is_today(string):
    today = datetime.datetime.today()
    formatted_date = today.strftime("%a, %b %d, %Y")
    return string == formatted_date

class Event:
    def __init__(self):
        self.name = ""
        self.id = ""
        self.tags = set()
        self.date = ""
        self.time = ""
        self.location = ""
    def get_info(self):
        return {"name"    :self.name,
                "id"      :self.id,
                "tags"    :self.tags,
                "date"    :self.date,
                "time"    :self.time,
                "location":self.location}

def format_events(event_html):
    event_object = Event()
    event_source = BeautifulSoup(event_html, "html.parser")

    li_container = event_source.find("li")
    listing_element = li_container.find("div",class_="listing-element")
    row = listing_element.find("div",class_="row")
    media_container = row.find("div",class_="listing-element__title-block col-md-8")
    media = media_container.find("div",class_="media")
    media_body = media.find("div",class_="media-body")

    name_container = media_body.find("h3")
    date_container = media_body.find("div",class_="row")
    tag_container = media_body.find("div",role="group")

    date_div = date_container.find_all("div", class_="media-heading")
    date_text = date_div[1].find_all("p")[0].text.strip()
    time_text = date_div[1].find_all("p")[1].text.strip()
    location_text = date_container.find("div",class_="col-md-4 col-lg-4").text

    for tag in tag_container.find_all("span"):
        event_object.tags.add(tag.text)

    event_object.name= name_container.find("a").text
    event_object.id = li_container["id"]
    event_object.date = date_text
    event_object.time = time_text
    event_object.location = location_text.strip()

    # if is_today(event_object.date):
    print(event_object.get_info())
    print("\n\n")


# sign in with usf account then log out then run the program again
#!DO NOT TURN OFF THE COMPUTER

load_dotenv()
CHROME_PROFILE_PATH = os.getenv('CHROME_PROFILE_PATH')
# CHROME_PROFILE_PATH = '/home/<username>/.config/google-chrome/Default'

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
time.sleep(5)
# Loop until a hooman log in and authenticate
while check_exists_by_ID("i011") == True or check_exists_by_ID("displayName")==True:  # Random elements in the USF login website
    print('Error: Need hooman authentication')
    time.sleep(10)  # Add an extra 10 second to the login time until someone log in
else:
    driver.get('https://bullsconnect.usf.edu/events?topic_tags=7276307')
    time.sleep(1)


driver.maximize_window()
pageSource = driver.page_source
time.sleep(5)
WAIT = WebDriverWait(driver,20)

try:
    all_event_list = WAIT.until(EC.visibility_of_element_located((By.ID,'divAllItems')))
    event_list = all_event_list.find_elements(By.TAG_NAME, "li") #return list of WebElement objects as all children of event list tag
except:
    print("Events not loaded")


events_true_list = []
for event in event_list:
    if "list-group-item" in event.get_attribute("class") and "display: none;" not in event.get_attribute("style"):
        events_true_list.append(event.get_attribute("outerHTML"))


#return new html source file of all true event
with open("bulls_connect_page_source.html","w",encoding="utf8") as event_source_file:
    for event_html in events_true_list:
        format_events(event_html)
        event_source_file.write(event_html+"\n")