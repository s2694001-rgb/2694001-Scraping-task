import requests
from bs4 import BeautifulSoup
import time
import csv

url = 'https://www.musashino-u.ac.jp'
res=requests.get(url)

html_soup =BeautifulSoup(res.content,'html.parser')

sitemap = {}

   
title_tag = html_soup.find('title')
if title_tag is not None:
    print(title_tag.string)



#a_all=html_soup.find_all('a')
#for a in a_all:
   # print(a)
#print("aタグの場合")

key =[]
https_all= html_soup.find_all('a')
for a in https_all:
    href = a.get('href')
    #hrefの文字がはいいてる時の分岐
    if href:
        #/から始まっているのをチェック
        #省略されているため。
        if href.startswith('/'): 
            #こうしないと/の後だけ表示されてしまう
            urlis = url + href
            #もし、urlisに同じのが入っていなかったら、keyに入れる。
            if urlis not in key:
                key.append(urlis) 
                time.sleep(1)
                print(urlis)
        #musashino-u.の文字が入ってる文字を抜き出す。
        # https:だとYouTubeとかも入ってきてしまった。
        elif 'musashino-u.ac' in href: 
            if href not in key: 
                key.append(href) 
                #print(href)

print("----------------------------------------------")
#print(key)
valies={f"value:{title_tag.string}"}
URL_key={f"key:{key}"}
keys=f"{URL_key},{valies}"

with open("urls_output.csv", "w") as f:
    f.write(str(keys))
