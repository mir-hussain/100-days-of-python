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

time.sleep(1)

username_el = driver.find_element(By.NAME, "session_key")
username_el.send_keys(email)

password_el = driver.find_element(By.NAME, "session_password")
password_el.send_keys(password)

driver.find_element(
    By.XPATH, '//*[@id="main-content"]/section[1]/div/form[1]/div[2]/button').click()

time.sleep(2)

driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")


while True:
    pass
