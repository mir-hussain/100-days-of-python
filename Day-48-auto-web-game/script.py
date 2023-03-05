from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_driver_path = "C:\Development\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)


driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")


def check_store():
    store = driver.find_elements(By.CSS_SELECTOR, "#store div")

    for item in store:
        item_block = item.find_element(By.TAG_NAME, "b")

        print(item.get_attribute("class"))


while True:
    cookie.click()
