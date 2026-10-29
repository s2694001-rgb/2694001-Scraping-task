import requests
from bs4 import BeautifulSoup
import time

url = 'https://www.musashino-u.ac.jp'
res=requests.get(url)

html_soup =BeautifulSoup(res.content,'html.parser')

soup_title=html_soup.title
print(soup_title)
print(f"{soup_title.string}")

#a_all=html_soup.find_all('a')
#for a in a_all:
   # print(a)
#print("aタグの場合")

https_all= html_soup.find_all('a')
for a in https_all:
    href = a.get('href')
    #hrefの文字がはいいてる時の分岐
    if href:
        #/から始まっているのをチェック
        #省略されているため。
        if href.startswith('/'): 
            #こうしないと/の後だけ表示されてしまう
            print(url + href)
        #musashino-u.の文字が入ってる文字を抜き出す。
        # https:だとYouTubeとかも入ってきてしまった。
        elif 'musashino-u.' in href: 
            print(href)
            




