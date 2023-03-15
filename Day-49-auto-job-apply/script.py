import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

load_dotenv()

email = os.getenv("email")
password = os.getenv("password")

chrome_driver_path = "c:\Development\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.linkedin.com/")

time.sleep(1)

username_el = driver.find_element(By.NAME, "session_key")
username_el.send_keys(email)

password_el = driver.find_element(By.NAME, "session_password")
password_el.send_keys(password)

driver.find_element(
    By.XPATH, '/html/body/main/section[1]/div/div/form[1]/div[2]/button').click()

time.sleep(2)

driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")

time.sleep(5)

job_list_container = driver.find_element(
    By.XPATH, '/html/body/div[5]/div[3]/div[4]/div/div/main/div/section[1]/div/ul')

driver.execute_script(
    'document.getElementsByClassName("jobs-search-results-list")[0].scroll(0, 5000)')

time.sleep(10)

job_list = job_list_container.find_elements(
    By.CLASS_NAME, "job-card-container")

print("Job found")
print(len(job_list))

for i, job in enumerate(job_list):
    job.click()
    time.sleep(2)

    save_button = driver.find_element(By.CLASS_NAME, "jobs-save-button")

    if save_button.find_element(By.TAG_NAME, "span").text == "Save":
        save_button.click()
        print(f"clicked {i}")

while True:
    pass
