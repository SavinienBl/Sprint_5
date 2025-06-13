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
    CREATING_ADS = (By.XPATH, "//button[contains(text(), 'Разместить объявление')]")
    CONTENT_TEXT = (By.XPATH, "//h1[contains(text(), 'Чтобы разместить объявление, авторизуйтесь')]")
    NAME = (By.XPATH,"//input[@name='name']")
    DESCRIPTION = ( By.XPATH, "//*[@id='root']/div/div[2]/div/form/div[4]/div/textarea")
    COST = (By.XPATH, "//input[@name='price']")
    DROPDOWN= (
    By.XPATH, "//button[@class='dropDownMenu_arrowDown__pfGL1 dropDownMenu_noDefault__wSKsP']")
    DROPDOWN_CATEGORY= (By.XPATH, "//button[.//span[text()='Технологии']]")
    DROPDOWN_2 = (By.XPATH,"(//button[@class='dropDownMenu_arrowDown__pfGL1 dropDownMenu_noDefault__wSKsP'])[2]")
    DROPDOWN_CITY = (By.XPATH, "//button[.//span[text()='Санкт-Петербург']]")
    RADIOBUTTON_NEW =(By.XPATH, "//*[@id='root']/div/div[2]/div/form/fieldset/div/div[2]/div")
    SUBMIT_AD_BUTTON = (By.XPATH, "//button[contains(text(), 'Опубликовать')]")
    MORPHIUS =  (By.XPATH, "(//div[@class='card'])[2]")
    TEXT = (By.XPATH, ".//h2[@class='h2' and text()='Морфиус']")
    ARROW_BUTTON = (By.XPATH,"//*[@id='root']/div/div[2]/div[4]/div/div[2]/button[2]")



