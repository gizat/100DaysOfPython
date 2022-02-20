from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

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

links_soup = soup.find_all(name="a", href=True, class_="a-card__title")
links = ["https://krisha.kz"+link["href"] for link in links_soup]
print(links)

# Initialise Selenium driver
service = ChromeService(executable_path="/opt/homebrew/bin/chromedriver")
driver = webdriver.Chrome(service=service)

for i in range(len(addresses)):
    # Navigate to Google Forms and get data
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfaNRLYl276PrvuAGUHZn_YiLkF61OaGpVUNQxLOyLMoLxf1w/viewform?usp=sf_link")
    # Need to wait for Google Forms to load before sending keys
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, 'exportInput')))

    # Find the needed input forms
    input_forms = driver.find_elements(By.CSS_SELECTOR, "input[jsname='YPqjbf']")

    # Fill out the input forms
    input_forms[0].send_keys(addresses[i])  # Property address
    input_forms[1].send_keys(prices[i])  # Property price
    input_forms[2].send_keys(links[i])  # Property link

    # Find and click on the submit button
    submit_button = driver.find_elements(By.CSS_SELECTOR, ".appsMaterialWizButtonPaperbuttonLabel")
    submit_button[0].click()
