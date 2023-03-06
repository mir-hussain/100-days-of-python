import time
import threading
from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_driver_path = "C:\Development\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)


driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")


def check_store():
    store = driver.find_elements(By.CSS_SELECTOR, "#store div")

    items_to_buy = []
    for item in store:
        class_name = item.get_attribute("class")

        if class_name == '':
            items_to_buy.append(item)

    if not len(items_to_buy) == 0:
        items_to_buy[-1].click()

    threading.Timer(5.0, check_store).start()


check_store()

timeout = time.time() + 60*5

while True:

    if time.time() > timeout:
        rate = driver.find_element(By.ID, "cps").text.split()[-1]
        print(rate)
        driver.quit()
        break

    cookie.click()
