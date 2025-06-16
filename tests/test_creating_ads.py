import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators
import time
from selenium.common.exceptions import StaleElementReferenceException


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

        email_input = WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable(Locators.EMAIL_INPUT)
        )
        email_input.send_keys(email)

        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)


        enter_input = WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable(Locators.ENTER)
        )
        enter_input.click()

        eterations = 2

        for i in range(eterations):
            try:
                element = WebDriverWait(driver, 30).until(
                    expected_conditions.element_to_be_clickable((Locators.CREATING_ADS)))
                element.click()
                break
            except StaleElementReferenceException:
                driver.refresh()

        driver.find_element(*Locators.NAME).send_keys(name)


        DESC = WebDriverWait(driver, 40).until(
            expected_conditions.element_to_be_clickable(Locators.DESCRIPTION)
        )
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});",DESC)
        DESC.send_keys(description)


        COSTS = WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable(Locators.COST)
        )
        COSTS.send_keys(cost)
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", COSTS)

        DROPDOWNS = WebDriverWait(driver, 20).until(
            expected_conditions.element_to_be_clickable(Locators.DROPDOWN)
        )
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});",DROPDOWNS)
        DROPDOWNS.click()


        DROPDOWNS_CATEGORYS = WebDriverWait(driver, 20).until(
            expected_conditions.element_to_be_clickable(Locators.DROPDOWN_CATEGORY)
        )
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", DROPDOWNS_CATEGORYS)
        DROPDOWNS_CATEGORYS.click()


        DROPDOWNS_CITY = WebDriverWait(driver, 20).until(
            expected_conditions.element_to_be_clickable(Locators.DROPDOWN_CITY)
        )
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", DROPDOWNS_CITY )
        DROPDOWNS_CITY.click()


        RADIO_BUT = WebDriverWait(driver, 20).until(
            expected_conditions.element_to_be_clickable(Locators.RADIOBUTTON_NEW)
        )
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", RADIO_BUT)
        RADIO_BUT.click()


        SUBMIT_BUTTON= WebDriverWait(driver, 20).until(
            expected_conditions.element_to_be_clickable(Locators.SUBMIT_AD_BUTTON)
        )
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", SUBMIT_BUTTON)
        SUBMIT_BUTTON.click()


        PROFILE = WebDriverWait(driver, 20).until(
            expected_conditions.element_to_be_clickable(Locators.AVATAR))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", PROFILE )
        PROFILE.click()

        ARROW = WebDriverWait(driver, 20).until(
            expected_conditions.element_to_be_clickable(Locators.ARROW_BUTTON))

        ARROW.click()

        ARROW = WebDriverWait(driver, 20).until(
            expected_conditions.element_to_be_clickable(Locators.ARROW_BUTTON))

        ARROW.click()




        first_ads  = WebDriverWait(driver, 20).until(
            expected_conditions.presence_of_element_located(Locators.MORPHIUS))


        assert first_ads.is_displayed()



















