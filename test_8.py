import datetime

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

from selenium.webdriver.common.by import By

service = Service(executable_path='./chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome()
base_url = 'https://demoqa.com/radio-button'
driver.get(base_url)
driver.maximize_window()


#check_box = driver.find_element(By.XPATH,"//span[@class='rct-checkbox']")
#check_box.click()

yes_checkbox = driver.find_element(By.XPATH,"//label[@for='yesRadio']")
yes_checkbox.click()
try:
    message = driver.find_element(By.XPATH,"//span[@class='text-success']")
    value_message = message.text
    print(value_message)
    assert value_message == "NO"
except AssertionError as exception:
    driver.refresh()
    yes_checkbox = driver.find_element(By.XPATH,"//label[@for='yesRadio']")
    yes_checkbox.click()
    message = driver.find_element(By.XPATH, "//span[@class='text-success']")
    value_message = message.text
    print(value_message)
    assert value_message == "Yes"
    print("checkbox yes")
print('test over')


time.sleep(100)