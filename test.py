import requests
from bs4 import BeautifulSoup

url = "http://annuairesante.ameli.fr/"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
print(soup)
