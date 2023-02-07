import requests
url = "http://annuairesante.ameli.fr/"
page = requests.get(url)
print(page.content)
