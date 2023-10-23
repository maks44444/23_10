import datetime

from selenium import webdriver
from selenium.webdriver import ActionChains
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

#url = "https://www.saucedemo.com/inventory.html"
#get_url = driver.current_url
#print(get_url)
#assert url == get_url
#print('GOOD URL')
now_date = datetime.datetime.utcnow().strftime("%Y.%n.%d.%H.%M.%S")
name_screenshot = 'screenshot' + now_date + '.png'
driver.save_screenshot(name_screenshot)
#driver.execute_script('window.scrollTo(0, 500)')
action = ActionChains(driver)
red_t_shirt = driver.find_element(By.XPATH,"//href[@id='item_3_img_link']")
action.move_to_element(red_t_shirt).perform()


time.sleep(10)