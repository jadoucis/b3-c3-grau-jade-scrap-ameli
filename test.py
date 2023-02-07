import requests
from bs4 import BeautifulSoup

url = "http://annuairesante.ameli.fr/"
header = {
    "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 OPR/93.0.0.0"
}

req = requests.Session()
page = requests.get(url, headers=header)

if page.status_code == 200:
    search_url = page.url

soup = BeautifulSoup(page.text, 'html.parser')

print(soup)
