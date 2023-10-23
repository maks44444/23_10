from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    driver = webdriver.Chrome()
    driver.get('http://suninjuly.github.io/get_attribute.html')
    driver.maximize_window()

    box = driver.find_element(By.XPATH,'//*[@id="treasure"]')
    x = box.get_attribute('valuex')
    y = calc(x)

    print(y)

    answer = driver.find_element(By.XPATH,'//*[@id="answer"]')
    answer.send_keys(y)
    check = driver.find_element(By.XPATH,'//*[@id="robotCheckbox"]')
    check.click()
    radio = driver.find_element(By.XPATH,'//*[@id="robotsRule"]')
    radio.click()
    button = driver.find_element(By.XPATH, '/html/body/div/form/div/div/button')
    button.click()

finally:
    time.sleep(10)
    driver.quit()
