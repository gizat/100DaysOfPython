from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

service = ChromeService(executable_path="/opt/homebrew/bin/chromedriver")
driver = webdriver.Chrome(service=service)

ebook_amazon_url = "https://www.amazon.com/gp/product/B084HJSJJ2?storeType=ebooks&pf_rd_p=ea5974d4-92b1-4b54-b3f4-10404cdc55d5&pf_rd_r=MMV1WYA94YVQBSKQH03G&pd_rd_wg=VDDvK&pd_rd_i=B084HJSJJ2&ref_=dbs_0_def_rwt_wigo_cp_recs_wigo_14&pd_rd_w=WuA92&pd_rd_r=43bcbefd-0ee1-4c7b-99fc-fb3b4eb8f38c"
driver.get(ebook_amazon_url)
# price = driver.find_element(By.CSS_SELECTOR, ".a-size-base.a-color-price.a-color-price")
price = driver.find_element(By.XPATH, '//*[@id="a-autoid-9-announce"]/span[2]/span')
print(price.text)

driver.quit()
