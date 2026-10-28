import requests
from bs4 import BeautifulSoup

url = 'https://www.musashino-u.ac.jp'
res=requests.get(url)

html_soup =BeautifulSoup(res.content,'html.parser')

soup_title=html_soup.title
print(soup_title)
print(f"{soup_title.string}")

a_all=html_soup.find_all('a')
for a in a_all:
    print(a)
print("aタグの場合")

