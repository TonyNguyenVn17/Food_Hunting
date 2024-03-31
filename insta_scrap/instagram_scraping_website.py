import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from insta_web_links import keys_list
from insta_web_links import link
from config import driver # Self defined

WAIT = WebDriverWait(driver, 5)
def open_insta_website(link):
    driver.get(link) # specify link opened by driver
    return None

def find_insta_posts():
    WAIT.until(EC.presence_of_element_located((By.CLASS_NAME, '_aagw')))
    post_button_list = driver.find_elements(By.CLASS_NAME, '_aagw')
    return post_button_list

def get_insta_first_comment(post_button_list):
    comment_list = []
    i = 0
    for button in post_button_list:
        time.sleep(0.5)
        button.click()
        time.sleep(2)
        try:
            WAIT.until(EC.presence_of_element_located((By.CSS_SELECTOR, '._ap3b._aaco._aacu._aacx._aad7._aade')))
        except:
            comment_list.append('')
        else:
            first_comment = driver.find_element(By.CSS_SELECTOR, '._ap3b._aaco._aacu._aacx._aad7._aade').get_attribute('innerHTML')
        comment_list.append(first_comment)
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, '[aria-label="Close"]').click()
        i+=1
        if i > 2:
            break
    return comment_list

if __name__ == '__main__':
    clubs_dict = {}
    for i in range(0, len(keys_list())):
        open_insta_website(link(i, keys_list()))
        post_list = find_insta_posts()
        comment_list = get_insta_first_comment(post_list)
        clubs_dict[keys_list()[i]] = comment_list
        time.sleep(2)
    print(clubs_dict)