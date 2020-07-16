import requests
import os 
from bs4 import BeautifulSoup
import sys 

# Get HTML
def get_html(url):
    html = BeautifulSoup(requests.get(url).content, "lxml")
    return html

# Find HTML element by tag 
def find_element_by_tag(html,elem):
    return html(elem)

# Find element by HTML attribute value
def find_element_by_attribute_value(html,  **kwargs):
    code = html(**kwargs)
    if not code:
        print("Your element does not exist or is not native HTML (HTML added by JavaScript)") 
    else:
        return code


# Save HTML file 
def save_html(html, filename):
    with open(filename, "w") as file:
          file.write(html.prettify())
    





