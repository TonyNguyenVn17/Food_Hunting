import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scrape.get_food_event import find_events, check_login, open_food_page
from database.db import FoodDatabase
from typing import Dict, List
from datetime import datetime, time
import time as timer
"""
This script is used to scrape food events data and add to database at 11:59PM or 12:00PM
"""

def check_time() -> bool:
    """
    Check if it is time to scrape (between 11:55 PM and 12:05 AM or 11:55 AM and 12:05 PM).
    """
    now = datetime.now()
    noon = time(12, 0)
    before_midnight = time(23, 55)   # 11:55 PM
    after_midnight = time(0, 5)      # 12:05 AM
    before_noon = time(11, 55)       # 11:55 AM
    after_noon = time(12, 5)         # 12:05 PM

    current_time = now.time()
    return (before_midnight <= current_time <= noon or
            before_noon <= current_time <= after_noon or
            current_time <= after_midnight)

def scrape_data() -> Dict[str, List[Dict[str, str]]]:
    """
    scrape at 12AM and 12PM daily
    then add data to db
    """
    db = FoodDatabase()
    check_login()
    open_food_page()
    events = find_events()
    print(f"Scraped {len(events)} events")
    try:
        for event in events:
            db.add_event(event)
    except Exception as e:
        print("Error adding event to database:", e)
    

def scrape_by_time() -> None:
    print('Start Cronjob to Scrape Event at 12AM && 12PM')
    while True:
        if check_time():
            scrape_data()
        timer.sleep(300)  # run every 5 minutes

if __name__ == "__main__":
    scrape_data()