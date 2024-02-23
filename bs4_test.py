import requests
from bs4 import BeautifulSoup 
  
URL = "https://bullsconnect.usf.edu/events"
request = requests.get(URL)
soup = BeautifulSoup(request.content, 'html5lib') #create new beautiful soup object argument 1: the html content and 'html5lib' is the parser
print(soup.prettify()) 
with open("scraped_page.html", "w", encoding="utf-8") as html_file:
    # Write the prettified HTML content to the file
    html_file.write(soup.prettify())