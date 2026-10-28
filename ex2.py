import requests
from bs4 import BeautifulSoup

url = 'https://www.musashino-u.ac.jp'
res=requests.get(url)

html_soup =BeautifulSoup(res.content,'html.parser')

print("----ためしに抽出----")
soup_p=html_soup.p
print(soup_p)
print(f"{type(soup_p)}")