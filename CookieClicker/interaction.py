from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

service = ChromeService(executable_path="/opt/homebrew/bin/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://en.wikipedia.org/wiki/Main_Page")
article_count = driver.find_elements(By.CSS_SELECTOR, '[title="Special:Statistics"]')
print(article_count[0].text)

driver.quit()
