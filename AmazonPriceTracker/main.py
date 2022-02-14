from bs4 import BeautifulSoup
import requests
import pprint

response = requests.get(
    url="https://www.amazon.com/gp/product/B084HJSJJ2?storeType=ebooks&pf_rd_p=ea5974d4-92b1-4b54-b3f4-10404cdc55d5&pf_rd_r=MMV1WYA94YVQBSKQH03G&pd_rd_wg=VDDvK&pd_rd_i=B084HJSJJ2&ref_=dbs_0_def_rwt_wigo_cp_recs_wigo_14&pd_rd_w=WuA92&pd_rd_r=43bcbefd-0ee1-4c7b-99fc-fb3b4eb8f38c",
    headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Safari/605.1.15",
             "Accept-Language":"en-CA,en-US;q=0.9,en;q=0.8"}
)

soup = BeautifulSoup(response.text, "lxml")
book_price_soup = soup.find_all(name="span", class_="a-size-base a-color-price a-color-price")
book_price = float(book_price_soup[0].getText().strip()[1:])

pprint.pprint(book_price)
