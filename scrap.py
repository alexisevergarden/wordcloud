from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://es.stackoverflow.com/users'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')


ur = soup.find_all('div', class_='user-details')

user = list()

for i in ur:
   user.append(i.text)

tg = soup.find_all('div', class_='user-tab')
tags = list()

for i in tg:
    tags.append(i.text)

print(tg)

#df = pd.DataFrame({'Nombre': user,'Puntos': tags})
#df.to_csv('Clasificacion.csv', index=False)



