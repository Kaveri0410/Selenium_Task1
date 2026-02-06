from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time

options = Options()
options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"

service = Service(executable_path=r"D:\Selenium_Task1\geckodriver.exe")

driver = webdriver.Firefox(service=service, options=options)

driver.get("https://the-internet.herokuapp.com/login")
driver.maximize_window()
time.sleep(2)

driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
time.sleep(3)

print(driver.find_element(By.ID, "flash").text)

driver.find_element(By.CSS_SELECTOR, "a.button.secondary.radius").click()
time.sleep(2)

print(driver.find_element(By.ID, "flash").text)

driver.quit()
