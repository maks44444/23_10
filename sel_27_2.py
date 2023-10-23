from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('https://www.gov.spb.ru/')
driver.get()

driver.maximize_window()
search_bar = driver.find_element(By.XPATH,'//*[@id="search_text"]')
search_bar.send_keys('финансирование')
search_bar = driver.find_element(By.XPATH,'//*[@id="button-addon2"]')
search_bar.click()



time.sleep(15)
driver.close()