from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

from selenium.webdriver.common.by import By

service = Service(executable_path='./chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome()
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

login_standard_user = "standard_user"
password_all = 'secret_sauce'

user_name = driver.find_element(By.XPATH,"//*[@id='user-name']")
user_name.send_keys(login_standard_user)
print("Input Login")
password = driver.find_element(By.XPATH,"//*[@id='password']")
password.send_keys(password_all)
print("Input Password")
button_login = driver.find_element(By.XPATH,"//*[@id='login-button']")
button_login.click()
print("Click Login Button")
warring_text = driver.find_element(By.XPATH,"//h3[@data-test='error']")
value_warring_test = warring_text.text
assert value_warring_test == "Epic sadface: Username and password do not match any user in this service"
print("GOOD TEST")

driver.refresh()

time.sleep(30)