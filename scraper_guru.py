from bs4 import BeautifulSoup
import requests

site_url = 'https://www.guru99.com/'
session_object_rest = requests.Session()
response = session_object_rest.get(site_url)
# print(response.content)
response_soup = BeautifulSoup(response.content, features="html5lib")
print(response_soup.div)
