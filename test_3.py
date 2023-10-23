from selenium import webdriver
from selenium.webdriver import Keys
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
password.send_keys(Keys.ENTER)

filter = driver.find_element(By.XPATH,"//select[@data-test='product_sort_container']")
filter.click()
print("Click Filter")
time.sleep(5)
filter.send_keys(Keys.PAGE_DOWN)
filter.send_keys(Keys.RETURN)
time.sleep(30)