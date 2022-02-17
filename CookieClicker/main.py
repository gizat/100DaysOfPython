from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

service = ChromeService(executable_path="/opt/homebrew/bin/chromedriver")
driver = webdriver.Chrome(service=service)

cookie_clicker_url = "https://orteil.dashnet.org/experiments/cookie/"
driver.get(cookie_clicker_url)
cookie_button = driver.find_element(By.CSS_SELECTOR, "#cookie")

store_elements = driver.find_elements(By.CSS_SELECTOR, "#store div")
ids = {element.get_attribute("id"):0 for element in store_elements}

timeout = time.time() + 5
five_min = time.time() + 300

while True:
    cookie_button.click()

    if time.time() > timeout:
        all_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")

        
        for element in ids:
            element.update()

        timeout = time.time() + 5

    if time.time() > five_min:
        break





