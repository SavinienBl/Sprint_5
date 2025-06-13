import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators
import time

class TestCreatind:
    def test_creatind_unauthorized_user(self,driver):
        driver.get('https://qa-desk.stand.praktikum-services.ru/')
        driver.find_element(*Locators.CREATING_ADS).click()

        content_text = WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(Locators.CONTENT_TEXT))

        assert  content_text.is_displayed()

    def test_creatind_uauthorized_user(self,driver):
        email = 'qwertasdfg@yandex.ru'
        password = 'qwert12345'
        name = 'Морфиус'
        description = 'Страх, неверие, сомнения отбрось — очисти свой мозг'
        cost = 8888888
        driver.get('https://qa-desk.stand.praktikum-services.ru/')

        driver.find_element(*Locators.LOGIN_BUTTON).click()
        time.sleep(2)
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.ENTER).click()
        time.sleep(10)
        CADS = WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable(Locators.CREATING_ADS)
        )
        CADS.click()

        driver.find_element(*Locators.NAME).send_keys(name)

        time.sleep(2)
        DESC = WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable(Locators.DESCRIPTION)
        )
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});",DESC)
        DESC.send_keys(description)

        time.sleep(2)
        COSTS= WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(Locators.COST)
        )
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", COSTS)
        COSTS.send_keys(cost)

        time.sleep(2)
        DROPDOWNS = WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(Locators.DROPDOWN)
        )
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});",DROPDOWNS)
        DROPDOWNS.click()

        time.sleep(2)
        DROPDOWNS_CATEGORYS = WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(Locators.DROPDOWN_CATEGORY)
        )
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", DROPDOWNS_CATEGORYS)
        DROPDOWNS_CATEGORYS.click()

        time.sleep(2)
        DROPDOWNS_FOR_CITY = WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(Locators.DROPDOWN_2)
        )
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", DROPDOWNS_FOR_CITY)
        DROPDOWNS_FOR_CITY .click()

        time.sleep(2)
        DROPDOWNS_CITY = WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(Locators.DROPDOWN_CITY)
        )
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", DROPDOWNS_CITY )
        DROPDOWNS_CITY.click()

        time.sleep(2)
        RADIO_BUT = WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(Locators.RADIOBUTTON_NEW)
        )
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", RADIO_BUT)
        RADIO_BUT.click()

        time.sleep(2)
        SUBMIT_BUTTON= WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(Locators.SUBMIT_AD_BUTTON)
        )
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", SUBMIT_BUTTON)
        SUBMIT_BUTTON.click()

        time.sleep(2)
        PROFILE = WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(Locators.AVATAR))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", PROFILE )
        PROFILE.click()

        time.sleep(2)
        driver.find_element(*Locators.ARROW_BUTTON).click()
        time.sleep(2)
        driver.find_element(*Locators.ARROW_BUTTON).click()

        time.sleep(10)
        FIRST_ADS  = WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located(Locators.MORPHIUS))


        assert FIRST_ADS.is_displayed()



















