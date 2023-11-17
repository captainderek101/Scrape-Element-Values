from bs4 import BeautifulSoup 
import requests

# Web Scraping Program for finding the highest value of a class in a URL
# Created by Derek Reynolds, November 17 2023

# URL(s) to search, class to find on that page, and whether you only want the maximum value
urls_to_scrape = ["https://m.imdb.com/list/ls068976997/", "https://m.imdb.com/list/ls068976997/?page=2", "https://m.imdb.com/list/ls068976997/?page=3", "https://m.imdb.com/list/ls068976997/?page=4", "https://m.imdb.com/list/ls068976997/?page=5"]
class_to_find = 'imdb-rating'
find_max = True

# function to extract html document from given url 
def getHTMLdocument(url): 
      
    # request for HTML document of given url 
    response = requests.get(url) 
      
    # response will be provided in JSON format 
    return response.text 

element_values = []

for url_to_scrape in urls_to_scrape:
    # create document 
    html_document = getHTMLdocument(url_to_scrape) 
    
    # create soap object 
    soup = BeautifulSoup(html_document, 'html.parser') 

    # find all elements with specified class
    class_elements = soup.find_all(class_=class_to_find)

    # print("Elements with class " + class_to_find + ":")
    # for element in class_elements:
    #     print(element)

    # find all values of those elements
    [element_values.append(x.get_text()) for x in class_elements]

if(find_max):
    # show the max value
    print("Max value of element with class " + class_to_find + ":")
    print(max(element_values))
else: 
    # show all values
    print("Values with class " + class_to_find + ":")
    for element in element_values:
        print(element)