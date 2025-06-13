import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators
from faker import Faker


class TestAuthentication:

    def test_user_registration(self,driver):
        fake = Faker()
        email = fake.email()
        password = 'password1234'
        driver.get('https://qa-desk.stand.praktikum-services.ru/')

        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.NO_ACCOUNT).click()
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators. PASSWORD_INPUT ).send_keys(password)
        driver.find_element(*Locators.SUBMIT_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.SUBMIT_BUTTON).click()

        avatar = WebDriverWait(driver, 20).until(
            expected_conditions.visibility_of_element_located(Locators.AVATAR))

        user = WebDriverWait(driver, 20).until(
            expected_conditions.visibility_of_element_located(Locators.USER))
        assert  avatar.is_displayed()
        assert user.is_displayed()



    #Регистрация пользователя c email не по маске  *******@*******.***
    def test_registration_user_mask(self, driver):

        email = '*******@*******.***'
        password = '12345password'
        driver.get('https://qa-desk.stand.praktikum-services.ru/')

        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.NO_ACCOUNT).click()
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.SUBMIT_BUTTON).click()

        email_field = WebDriverWait(driver, 20).until(
            expected_conditions.presence_of_element_located(Locators.EMAIL_INPUT))

        password_field = WebDriverWait(driver, 20).until(
            expected_conditions.presence_of_element_located(Locators.PASSWORD_INPUT))
        submit_password_faild = WebDriverWait(driver, 20).until(
            expected_conditions.presence_of_element_located(Locators.SUBMIT_PASSWORD_INPUT))
        error = WebDriverWait(driver, 20).until(
            expected_conditions.visibility_of_element_located(Locators.ERROR_MESSAGE))
        red_flag = WebDriverWait(driver, 20).until(
            expected_conditions.visibility_of_element_located(Locators.RED_FLAG))

        assert  email_field.is_displayed()
        assert  password_field.is_displayed()
        assert submit_password_faild.is_displayed()
        assert error.is_displayed()
        assert red_flag.is_displayed()


    def test_registration_existing_user(self, driver):
        email = 'qwertasdfg@yandex.ru'
        password = 'qwert12345'
        driver.get('https://qa-desk.stand.praktikum-services.ru/')

        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.NO_ACCOUNT).click()
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.SUBMIT_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.SUBMIT_BUTTON).click()

        email_field = WebDriverWait(driver, 20).until(
            expected_conditions.presence_of_element_located(Locators.EMAIL_INPUT))

        password_field = WebDriverWait(driver, 20).until(
            expected_conditions.presence_of_element_located(Locators.PASSWORD_INPUT))
        submit_password_faild = WebDriverWait(driver, 20).until(
            expected_conditions.presence_of_element_located(Locators.SUBMIT_PASSWORD_INPUT))
        error = WebDriverWait(driver, 20).until(
            expected_conditions.visibility_of_element_located(Locators.ERROR_MESSAGE))
        red_flag = WebDriverWait(driver, 20).until(
            expected_conditions.visibility_of_element_located(Locators.RED_FLAG))

        assert email_field.is_displayed()
        assert password_field.is_displayed()
        assert submit_password_faild.is_displayed()
        assert error.is_displayed()
        assert red_flag.is_displayed()


