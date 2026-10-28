import requests

# アクセスしたいWebサイトのURL
url = 'https://www.musashino-u.ac.jp'
res=requests.get(url)

print(f"メッセージコード:{res.status_code}")
print(f"ステータスメッセージ:{res.reason}")

with open ('musashino-u.html','w')as f:
    f.write(res.text)
