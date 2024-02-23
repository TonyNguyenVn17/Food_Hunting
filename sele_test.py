from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime
from datetime import date


#kinda useless function
# def check_food_filter():
#     try:
#         food_filter = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[5]/div[2]/div/div/div[6]/div[1]/ulli[3]//p/a[@aria-label="List all events filtered by Food"]')))
#         print(f"This event has f{food_filter.text}")
#         return True
#     except:
#         return False
def get_event_date(event):
    date_text = event.find_element(By.CSS_SELECTOR, 'div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > p:nth-child(1)')
    return date_text.text[5:18]
def get_today_date():
    TODAY_DATE = date.today()
    TODAY_DATE_FORMATTED = TODAY_DATE.strftime("%b %d, %Y")
    return TODAY_DATE_FORMATTED
    
    
driver = webdriver.Firefox()
driver.get("https://bullsconnect.usf.edu/events")
pageSource = driver.page_source
time.sleep(5)
WAIT = WebDriverWait(driver,20)
# with open("bulls_connect_page_source", "w", encoding="utf-8") as html_file:
#     html_file.write(pageSource)
# print(driver.title)
    
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

# print(event_tag_food_li_a_div.text)
event_tag_food_li_a_div.click()
try:
    # listing_cont = page_cont.find_element(By.ID, "listing-cont")
    # listing_elements_cont = listing_cont.find_element(By.ID,'listing__elements-cont')
    all_event_list = WAIT.until(EC.visibility_of_element_located((By.ID,'divAllItems')))
    event_list = all_event_list.find_elements(By.XPATH,"./*")
except:
    print("Events not loaded")
    
events_true_list = [event for event in event_list if "display: none" not in event.get_attribute("style") and "list-group__seperator" not in event.get_attribute("class")]

event_file = open("event_list.txt","w")

for event in events_true_list:
    event_file.write(event.text)

event_file.close()


# events_food_list = [food_event for food_event in events_list if get_event_date(food_event)==get_today_date()]

# for event in events_food_list:
#     today_date = get_today_date()
#     event_date = get_event_date(event)
#     print(f"Today's date: {today_date}")
#     print(f"Event's date: {event_date}\n")
#     print(f"Event information: ")
#     print(event.text)







# Close the browser
