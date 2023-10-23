from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

base_url = "http://suninjuly.github.io/find_link_text"
a = str(math.ceil(math.pow(math.pi, math.e)*10000))
try:
    browser = webdriver.Chrome()
    browser.get(base_url)

    link = browser.find_element(By.PARTIAL_LINK_TEXT,a )
    link.click()

    input1 = browser.find_element(By.XPATH,"/html/body/div/form/div[1]/input" )
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.XPATH,"/html/body/div/form/div[2]/input" )
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.XPATH,"/html/body/div/form/div[3]/input" )
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.XPATH, "//*[@id='country']")
    input4.send_keys("Russia")
    button = browser.find_element(By.XPATH, "/html/body/div/form/button")
    button.click()
    time.sleep(15)
finally:
    browser.quit()

time.sleep(35)