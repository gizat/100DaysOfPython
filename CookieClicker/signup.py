from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service = ChromeService(executable_path="/opt/homebrew/bin/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://secure-retreat-92358.herokuapp.com/")
fName = driver.find_element(By.NAME, "fName")
fName.send_keys("Gizat")

lName = driver.find_element(By.NAME, "lName")
lName.send_keys("Makhanov")

email = driver.find_element(By.NAME, "email")
email.send_keys("myemail@myemail.com")

email.send_keys(Keys.ENTER)
