from bs4 import BeautifulSoup
import requests
import smtplib

ebook_amazon_url = "https://www.amazon.com/gp/product/B084HJSJJ2?storeType=ebooks&pf_rd_p=ea5974d4-92b1-4b54-b3f4-10404cdc55d5&pf_rd_r=MMV1WYA94YVQBSKQH03G&pd_rd_wg=VDDvK&pd_rd_i=B084HJSJJ2&ref_=dbs_0_def_rwt_wigo_cp_recs_wigo_14&pd_rd_w=WuA92&pd_rd_r=43bcbefd-0ee1-4c7b-99fc-fb3b4eb8f38c"
response = requests.get(
    url=ebook_amazon_url,
    headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Safari/605.1.15",
             "Accept-Language":"en-CA,en-US;q=0.9,en;q=0.8"}
)

soup = BeautifulSoup(response.text, "lxml")
book_price_soup = soup.find_all(name="span", class_="a-size-base a-color-price a-color-price")
book_price = float(book_price_soup[0].getText().strip()[1:])

my_email = "gizat.m@yahoo.com"
my_password = "vhfsvlrtqewoxgvm"

if book_price < 6:
    with smtplib.SMTP("smtp.mail.yahoo.com", port=587) as connection:
        connection.starttls()  # Secure the connection
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="some_email",
            msg=f"Amazon Price Alert!\n\nThe Psychology of Money - Kindle edition is now {book_price}!"
                f"\n\n{ebook_amazon_url}")
