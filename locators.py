from selenium.webdriver.common.by import By


class Locators:
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button.buttonSecondary.inButtonText")
    NO_ACCOUNT= (By.XPATH, "//button[.//text()='Нет аккаунта']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
    SUBMIT_PASSWORD_INPUT =(By.XPATH, "//input[@name='submitPassword']")
    SUBMIT_BUTTON = (By.XPATH, "//button[contains(text(), 'Создать аккаунт')]")
    AVATAR = (By.XPATH, "//button[@class='circleSmall']")
    USER = (By.XPATH,"//h3[@class='profileText name' and text()='User.']")
    ERROR_MESSAGE =  (By.XPATH, "//*[contains(text(), 'Ошибка')]")
    RED_FLAG = (By.CLASS_NAME, "input_inputError__fLUP9")
    ENTER = (By.XPATH, "//button[.//text()='Войти']")
    OUTPUT = (By.XPATH, "//button[contains(text(), 'Выйти')]")
    CREATING_ADS = (By.XPATH, "//button[.//text()='Разместить объявление']")
    CONTENT_TEXT = (By.XPATH, "//h1[contains(text(), 'Чтобы разместить объявление, авторизуйтесь')]")
    NAME = (By.XPATH,"//input[@name='name']")
    DESCRIPTION = ( By.XPATH, "//textarea[@name='description']")
    COST = (By.XPATH, "//input[@name='price']")
    DROPDOWN= (
    By.XPATH, "//button[@class='dropDownMenu_arrowDown__pfGL1 dropDownMenu_noDefault__wSKsP']")
    DROPDOWN_CATEGORY= (By.XPATH, "//button[.//span[text()='Технологии']]")
    DROPDOWN_2 = (By.XPATH,"(//button[@class='dropDownMenu_arrowDown__pfGL1 dropDownMenu_noDefault__wSKsP'])")
    DROPDOWN_CITY = (By.XPATH, "//span[contains(text(), 'Санкт-Петербург')]/ancestor::div[contains(@class, 'dropDownMenu_dropMenu__sBxhz')]")
    RADIOBUTTON_NEW =(By.XPATH, "//div[@class='radioUnput_inputRegular__FbVbr']")
    SUBMIT_AD_BUTTON = (By.XPATH, "//button[contains(text(), 'Опубликовать')]")
    MORPHIUS =  (By.XPATH, "(//div[@class='card'])")
    TEXT = (By.XPATH, ".//h2[@class='h2' and text()='Морфиус']")
    ARROW_BUTTON = (By.XPATH,"//button[@class='arrowButton arrowButton--right undefined']")



