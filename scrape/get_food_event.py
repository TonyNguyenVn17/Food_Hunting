import time 
from typing import List, Dict, Union, Set  
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from bs4 import BeautifulSoup 
from scrape.login import driver 
from database.event import Event

try:
    WAIT = WebDriverWait(driver, 20)
    print("WebDriverWait object created successfully")
except Exception as e:
    print(f"Error creating WebDriverWait object: {str(e)}")

def format_events(event_html: str) -> Dict[str, str]:
    """
    convert HTML source code into event object
    """
    event_object = Event()

    # navigate through HTML containers to get to information texts
    event_source = BeautifulSoup(event_html, "html.parser")

    # nagivate to large parent containers
    li_container = event_source.find("li")
    listing_element = li_container.find("div", class_="listing-element")
    row = listing_element.find("div", class_="row")
    media_container = row.find(
        "div", class_="listing-element__title-block col-md-8")
    media = media_container.find("div", class_="media")
    media_body = media.find("div", class_="media-body")

    # navigate into specific containers for each information
    name_container = media_body.find("h3")
    date_container = media_body.find("div", class_="row")
    tag_container = media_body.find("div", role="group")
    date_div = date_container.find_all("div", class_="media-heading")

    # extract texts as event's information
    date_text = date_div[1].find_all("p")[0].text.strip()
    time_text = date_div[1].find_all("p")[1].text.strip()
    location_text = date_container.find("div", class_="col-md-4 col-lg-4").text
        
    # initialize attributes in Event object
    for tag in tag_container.find_all("span"):
        event_object.tags.add(tag.text)
    
    event_object.name = name_container.find("a").text
    event_object.id = li_container["id"]
    event_object.date = date_text
    event_object.time = time_text
    event_object.location = location_text.strip()

    # return Event object as dictionary
    return event_object.get_info()


def check_exists_by_ID(ID: str) -> bool:
    """
    check for whether element with given ID exists
    """
    try:
        driver.find_element(By.ID, ID)
    except:
        return False
    return True


def check_login() -> None:
    """
    direct driver to login page and let user login 
    user must manually login to the page
    """
    # go to login page
    
    try:
        print("Opening login page") 
        driver.get('https://www.campusgroups.com/shibboleth/login?idp=usf')
        time.sleep(5)
        # Keep login page open until user manually login  (login elements are no longer visible)
        while check_exists_by_ID("loginHeader") == True or check_exists_by_ID("displayName") == True:
            print('Error: Need hooman authentication')
            time.sleep(10)
        print("Login page access successful")
    except Exception as e:
        print(f"Error opening login page: {str(e)}")

def open_food_page() -> None:
    """ 
    direct driver to food page (after login)
    """
    try:
        print("Opening food page")
        driver.get('https://bullsconnect.usf.edu/events?topic_tags=7276307')
        time.sleep(5)
        print("Food page access successful")
    except Exception as e:
        print(f"Error opening bullsconnect food page: {str(e)}")

def find_events() -> List[Event]:
    """
    Scrape BullsConnect web and create list of Event objects from WebElement objects
    """
    output = []
    event_list = []
    # wait until all events on BullsConnect page are loaded, then collect all events as raw WebElement objects
    try:
        event_raw_list = WAIT.until(
            EC.visibility_of_element_located((By.ID, 'divAllItems')))
        # return all events as list of WebElement objects
        event_list = event_raw_list.find_elements(By.TAG_NAME, "li")
    except:
        print("Events not loaded")

    # process WebElement objects into HTML source code
    # filter out true events    
    events_source_list = []
    for event in event_list:
        if "list-group-item" in event.get_attribute("class") and "display: none;" not in event.get_attribute("style"):
            # return all events as HTML source code
            events_source_list.append(event.get_attribute("outerHTML"))
    print("Raw event scraped successfully")
    
    # process all HTML source code into Event objects
    for event in events_source_list:
        processed_event = format_events(event)
        output.append(processed_event)

    print("Events processed successfully")

    return output  # export list of Event objects

if __name__ == "__main__":
    """
    run scripts
    """
    from database.db import FoodDatabase
    db = FoodDatabase()
    check_login()
    open_food_page()
    events = find_events()
    data = {}
    for event in events:
        event_name = event['name']
        data[event_name] = [{
            "id": event['id'],
            "tags": event['tags'],
            "date": event['date'],
            "time": event['time'],
            "location": event['location']
        }]
        db.add_event(event)
    output = db.get_all_event()
