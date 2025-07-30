import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.naver.com/breakingnews/section/103/376")
html = response.text
soup = BeautifulSoup(html, 'html.parser')
links = soup.select(".sa_text_title") # 결과는 리스트로 나옴

for link in links:
    title = link.text # 태그 안의 텍스트요소를 가져온다
    url = link.attrs['href'] # href의 속성값을 가져온다
    print(title, url)