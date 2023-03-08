import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By

load_dotenv()

email = os.getenv("email")
password = os.getenv("password")

print(email)
print(password)

chrome_driver_path = "c:\Development\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.linkedin.com/")

username_el = driver.find_element(By.NAME, "session_key")
username_el.send_keys(email)

time.sleep(1)

password_el = driver.find_element(By.NAME, "session_password")
password_el.send_keys(password)

time.sleep(1)

driver.find_element(
    By.XPATH, '//*[@id="main-content"]/section[1]/div/form[1]/div[2]/button').click()

while True:
    pass
