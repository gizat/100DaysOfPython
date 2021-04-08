from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/news")
yc_news_webpage = response.text

soup = BeautifulSoup(yc_news_webpage, "html.parser")

articles = soup.find_all(name="a", class_="storylink")
article_texts = [article.getText() for article in articles]
article_links = [article.get("href") for article in articles]
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

print(article_texts[article_upvotes.index(max(article_upvotes))])