from bs4 import BeautifulSoup
import requests
import re

krisha_link = "https://krisha.kz/prodazha/kvartiry/astana-esilskij/?das[live.rooms]=2&das[map.complex]=1256"
response = requests.get(
    url=krisha_link,
    headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Safari/605.1.15",
        "Accept-Language": "en-CA,en-US;q=0.9,en;q=0.8"}
)
krisha_page = response.text

soup = BeautifulSoup(krisha_page, "html.parser")

prices_soup = soup.find_all(name="div", class_="a-card__price")
prices = [int(price.getText().strip().replace(u'\xa0', u'')[:-1]) for price in prices_soup]
print(prices)

address_soup = soup.find_all(name="div", class_="a-card__subtitle")
addresses = [address.getText().strip().replace(u'\xa0', u'') for address in address_soup]
print(addresses)


# forms_link = "https://docs.google.com/forms/d/e/1FAIpQLSfaNRLYl276PrvuAGUHZn_YiLkF61OaGpVUNQxLOyLMoLxf1w/viewform?usp=sf_link"
