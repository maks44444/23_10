import time # Импортируем библиотеку time. Для ипользования пауз time.sleep(5)

import pytest
from selenium import webdriver # Импортируем библиотеку веб-драйвер
from selenium.webdriver.common.by import By # Импортируем библиотеку By
@pytest.fixture(scope='class')
def browser():
    link = 'https://www.saucedemo.com/'
    browser = webdriver.Chrome()
    browser.get(link)
    browser.maximize_window()
    browser.implicitly_wait(5)
    yield browser
    browser.quit()
# @pytest.mark.parametrize('user_name', ['standard_user','locked_out_user', 'problem_user','performance_glitch_user','error_user','visual_user'])
@pytest.mark.parametrize('user_name', ['standard_user','locked_out_user'])
class TestAutorisation:
    def test_autorisation(self,browser, user_name):
        login = browser.find_element(By.XPATH,'//*[@id="user-name"]')
        login.send_keys(user_name)

        parol = browser.find_element(By.XPATH,'//*[@id="password"]')
        parol.send_keys('secret_sauce')

        button = browser.find_element(By.XPATH,'//*[@id="login-button"]')
        button.click()

        time.sleep(7)
        browser.get('https://www.saucedemo.com/')