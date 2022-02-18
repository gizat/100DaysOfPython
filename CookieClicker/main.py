from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import re

service = ChromeService(executable_path="/opt/homebrew/bin/chromedriver")
driver = webdriver.Chrome(service=service)

cookie_clicker_url = "https://orteil.dashnet.org/experiments/cookie/"
driver.get(cookie_clicker_url)
cookie_button = driver.find_element(By.CSS_SELECTOR, "#cookie")

store_elements = driver.find_elements(By.CSS_SELECTOR, "#store div:not(class)")
ids = {element.get_attribute("id"):0 for element in store_elements}
ids.popitem()
print(ids)

timeout = time.time() + 5
five_min = time.time() + 300

while True:
    cookie_button.click()

    if time.time() > timeout:
        prices_raw = driver.find_elements(By.CSS_SELECTOR, "#store div:not([class]) b")
        prices_raw.pop()
        prices = []

        for price in prices_raw:
            prices.append(int(re.sub(",", "", price.text.split("-")[1].strip())))

        i = 0
        for key in ids.keys():
            ids[key] = prices[i]
            i += 1

        timeout = time.time() + 5

    if time.time() > five_min:
        break





