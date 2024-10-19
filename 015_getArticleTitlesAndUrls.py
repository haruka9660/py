import requests
from bs4 import BeautifulSoup

def get_article_titles_and_urls(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    articles = {}

    for a in soup.find_all('a'):
        if a.get('href') and a.text:
            articles[a.text] = a.get('href')

    return articles

articles = get_article_titles_and_urls('https://www.example.com/')
for title, url in articles.items():
    print(f"Title: {title}, URL: {url}")


