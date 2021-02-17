import requests
from bs4 import BeautifulSoup
 
webpage_response = requests.get('https://www.strayrescue.org/filter?searchword3=Dog&moduleId=119&Itemid=124')

webpage = webpage_response.content

soup = BeautifulSoup(webpage, "html.parser")

print(soup)
print(soup.find_all("h1"))
soup.select("a-name")