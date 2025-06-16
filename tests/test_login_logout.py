import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators
import time



class TestLoginLogout:
    def test_login(self,driver):

        email = 'qwertasdfg@yandex.ru'
        password = 'qwert12345'
        driver.get('https://qa-desk.stand.praktikum-services.ru/')
        time.sleep(4)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        time.sleep(4)
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        time.sleep(5)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        time.sleep(5)
        driver.find_element(*Locators.ENTER).click()

        avatar = WebDriverWait(driver, 20).until(
            expected_conditions.visibility_of_element_located(Locators.AVATAR))
        user = WebDriverWait(driver, 20).until(
            expected_conditions.visibility_of_element_located(Locators.USER))

        assert avatar.is_displayed(),"'circleSmall' не отображается"
        assert user.is_displayed(),"'User.' не отображен"
        assert driver.current_url  == 'https://qa-desk.stand.praktikum-services.ru/login'


    def test_logout(self,driver):
        email = 'qwertasdfg@yandex.ru'
        password = 'qwert12345'
        driver.get('https://qa-desk.stand.praktikum-services.ru/')

        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.ENTER).click()

        avatar = WebDriverWait(driver, 20).until(
            expected_conditions.visibility_of_element_located(Locators.AVATAR))
        user = WebDriverWait(driver, 20).until(
            expected_conditions.visibility_of_element_located(Locators.USER))
        login_button = WebDriverWait(driver, 20).until(
            expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON))
        WebDriverWait(driver, 30).until(
            expected_conditions.element_to_be_clickable(Locators.OUTPUT)).click()


        assert avatar.is_displayed(), "'circleSmall' не отображается"
        assert user.is_displayed() , "'User.' не отображен"
        assert login_button.is_displayed(), "кнопка 'Вход и регистрация' отображается"






