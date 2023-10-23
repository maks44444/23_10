import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture(scope="function")
def driver(driver):
    driver = webdriver.Chrome()
    driver.get('https://www.saucedemo.com/')
    driver.maximize_window()
    driver.implicitly_wait(15)
    yield driver
    driver.quit()

@pytest.mark.parametrize('user_name', ["standard_user", "locked_out_user"])
class TestAutorisation:
    def test autorisation(self,driver, user_name):
        driver.find_element(By.XPATH,'//*[@id="user-name"]').send_keys('standard_user')
        driver.find_element(By.XPATH,'//*[@id="password"]').send_keys('secret_sauce')
        button = driver.find_element(By.XPATH,'//*[@id="login-button"]')
        button.click()

        time.sleep(5)
        driver.get('https://www.saucedemo.com/')