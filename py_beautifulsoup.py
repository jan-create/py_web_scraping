import requests
from bs4 import BeautifulSoup
 
webpage_response = requests.get('https://www.namus.gov/Dashboard')

webpage = webpage_response.content

soup = BeautifulSoup(webpage, "html.parser")

print(soup)
#print(soup.find_all("h1"))
print(soup.select("case-summary"))

#soup.get_text()
