import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link ='http://suninjuly.github.io/selects1.html'
browser= webdriver.Chrome()
browser.get(link)
browser.maximize_window()

num1 = browser.find_element(By.XPATH, '//*[@id="num1"]')
num1 = num1.text

num2 = browser.find_element(By.XPATH, '//*[@id="num2"]')
num2 = num2.text

y = int(num1)+int(num2)
y = str(y)

string = Select(browser.find_element(By.XPATH, '//*[@id="dropdown"]'))
string.select_by_visible_text(y)

button = browser.find_element(By.XPATH, '/html/body/div[1]/form/button')
button.click()

time.sleep(10)
browser.quit()