from bs4 import BeautifulSoup 
import requests
import re

# Created by Derek Reynolds

search_url = 'https://coursefinder.illinoisstate.edu/directory/it'
root_url = 'https://coursefinder.illinoisstate.edu'
class_to_find = 'section_mid'

# function to extract html document from given url 
def getHTMLdocument(url):
    # request for HTML document of given url 
    response = requests.get(url) 
      
    # response will be provided in JSON format 
    return response.text 

# create document 
html_document = getHTMLdocument(search_url) 
# create soap object 
soup = BeautifulSoup(html_document, 'html.parser') 

li_elements = soup.find_all('li')

a_elements = []
for li in li_elements:
    [a_elements.append(x) for x in li.find_all('a', recursive=False)]

urls_to_scrape = []
[urls_to_scrape.append(x['href']) for x in a_elements]

for url_to_scrape in urls_to_scrape:
    # create document 
    html_document = getHTMLdocument(root_url+url_to_scrape) 
    # create soap object 
    soup = BeautifulSoup(html_document, 'html.parser') 

    class_elements = soup.find(class_=class_to_find).find_all('p', recursive=False)

    # find all values of those elements
    print(url_to_scrape)
    [print(x.get_text()) for x in class_elements if re.match(re.compile('.*Description:.*'), x.get_text())]