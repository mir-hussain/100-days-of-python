import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get("https://tinder.com/app/recs")

login = driver.find_element(
    By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]")

login.click()

time.sleep(3)

driver.find_element(By.XPATH, '/html/body/div/div').click()

while True:
    pass
