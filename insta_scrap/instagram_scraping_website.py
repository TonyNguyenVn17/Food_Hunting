import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from insta_web_links import clubs_list  # Self defined
from insta_web_links import link  # Self defined
from config import driver  # Self defined
WAIT = WebDriverWait(driver, 5)


def open_website(website_link):
    driver.get(website_link)  # Specify link opened by driver
    return None


def find_posts():
    WAIT.until(EC.presence_of_element_located((By.CLASS_NAME, '_aagw')))
    post_list = driver.find_elements(By.CLASS_NAME, '_aagw')
    return post_list


def find_image():
    WAIT.until(EC.presence_of_element_located((By.CLASS_NAME, '_aagv')))
    image_list = driver.find_elements(By.CLASS_NAME, '_aagv')
    return image_list


def get_image_content(image_list):
    image_contents_list =[]
    for content_path in image_list:
        content = content_path.get_attribute('innerHTML')
        image_contents_list.append(content)
    return image_contents_list


def get_first_comment(post_list):
    comment_list = []
    i = 0
    for post in post_list:
        time.sleep(0.5)
        post.click()
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


def merge_list_to_dict(comment_list, image_contents_list):
    i = 0
    dict = {}
    while i < len(comment_list) and i < len(image_contents_list):
        dict[f'Post {i+1}'] = {'Comment': {comment_list[i]}, 'Image content': {image_contents_list[i]}}
        i+=1
    return dict


if __name__ == '__main__':
    clubs_content = {}
    for i in range(0, len(clubs_list())):
        open_website(link(i, clubs_list()))
        post_list = find_posts()
        image_list = find_image()
        comment_list = get_first_comment(post_list)
        image_contents_list = get_image_content(image_list)
        comment_image_dict = merge_list_to_dict(comment_list, image_contents_list)
        clubs_content[clubs_list()[i]] = comment_image_dict
        time.sleep(2)
    print(clubs_content)