from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
from datetime import datetime


class Event:
    def __init__(self):
        self.name = ""
        self.id = ""
        self.tags = []
        self.date = datetime.min #(1,1,1,0,0) Year 1, month 1, date 1, hour 1, minute 1
        self.location = ""
    def get_info(self):
        return {"name"    :self.name,
                "id"      :self.id,
                "tags"    :self.tags,
                "date"    :self.date,
                "location":self.location}
        
def format_events(event_html):
    event_object = Event()
    event_source = BeautifulSoup(event_html, "html.parser")
    
    li_container = event_source.find("li")
    li_container_text = li_container.text
    
    event_object.id = li_container["id"]
    print(li_container_text.strip())
    print(event_object.id)
    print("\n\n")

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://bullsconnect.usf.edu/events")
pageSource = driver.page_source
time.sleep(5)
WAIT = WebDriverWait(driver,20)


try:
    #an absolute abomination of HTML tree traversal
    filter_btn = WebDriverWait(driver,15).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
    body = driver.find_element(By.TAG_NAME,"body")
    outer_shell = body.find_element(By.ID,'outer-shell')
    inner_shell = outer_shell.find_element(By.ID,'inner-shell')
    content_cont = inner_shell.find_element(By.ID,'content-cont')
    page_cont = content_cont.find_element(By.ID,'page-cont')
    list_filter = page_cont.find_element(By.ID,'listing__filters-cont')
    row = list_filter.find_element(By.CSS_SELECTOR,'#listing__filters-cont > div:nth-child(1)')
    row_filter_cont = row.find_element(By.ID,'listing__filters--filters-cont')
    row_filter_cont_under = row_filter_cont.find_element(By.CSS_SELECTOR,'div.select-group-justified:nth-child(2)')
    event_tag_container = row_filter_cont_under.find_element(By.CSS_SELECTOR,'div.select-group-justified:nth-child(2) > div:nth-child(1)')
    event_tag_container_span = event_tag_container.find_element(By.CSS_SELECTOR,'div.select-group-justified:nth-child(2) > div:nth-child(1) > span:nth-child(1)')
    event_tag_container_span_div = event_tag_container_span.find_element(By.CSS_SELECTOR,'div.select-group-justified:nth-child(2) > div:nth-child(1) > span:nth-child(1) > div:nth-child(2)')
    event_tag_button = event_tag_container_span_div.find_element(By.CSS_SELECTOR,'div.select-group-justified:nth-child(2) > div:nth-child(1) > span:nth-child(1) > div:nth-child(2) > button:nth-child(1)')
except:
    print("not founded")
    driver.quit()



event_tag_button.click()
time.sleep(5)


#another absolute abomination of  HTML traversal
event_tag_food = event_tag_container_span_div.find_element(By.CSS_SELECTOR,'.open > ul:nth-child(2)')
event_tag_food_li = event_tag_food.find_element(By.CSS_SELECTOR,'.open > ul:nth-child(2) > li:nth-child(9)')
event_tag_food_li_a = event_tag_food_li.find_element(By.CSS_SELECTOR,'.open > ul:nth-child(2) > li:nth-child(9) > a:nth-child(1)')
event_tag_food_li_a_div = event_tag_food_li_a.find_element(By.CSS_SELECTOR,'.open > ul:nth-child(2) > li:nth-child(9) > a:nth-child(1) > div:nth-child(1)')
event_tag_food_li_a_div.click()


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






# Close the browser
