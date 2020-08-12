import bs4 as bs4

from bs4 import BeautifulSoup
import requests


url = 'https://es.stackoverflow.com/users'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

for users in soup.find_all('div', class_='user-details'): #Especifica Etiqueta y clase
    print(users.getText().split("\n")[1])

