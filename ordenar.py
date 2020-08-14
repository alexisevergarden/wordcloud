from bs4 import BeautifulSoup
import requests
from wordcloud import WordCloud, STOPWORDS

url = 'https://es.stackoverflow.com/users/'
user = input(" Ingrese una id: ")
url = url + str(user) + "?tab=tags"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

u_user = soup.find_all('a', class_='post-tag')

nombres = list()

for i in u_user:
    nombres.append(i.text)

print (nombres)

numer = soup.find_all('span', class_='item-multiplier-count')#'div', class_='answer-votes'

numero = list()

for i in numer:
    numero.append(i.text)

print(numero)

with open('foo.txt', 'w') as file:
 file.write(str(nombres))


comment_words = ' '
stopwords = ['k',"'","""'"""]

f = open('foo.txt','r+')
textdata= f.read().replace('\n','')

wordcloud = WordCloud (width =800, height=800,
                       background_color= 'white',
                       stopwords= stopwords,
                       min_font_size =10,  max_words=300).generate(textdata)

wordcloud.to_file('Image2.png')

print('Image saved successfully')