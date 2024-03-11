from browser import Browser
from time import sleep
from selenium.common import NoAlertPresentException
from selenium.webdriver.common.by import By
import logging


class Home_Page(Browser):

    FIRST_LOGIN_BTN = (By.ID, 'HeadCustomerDropdown')
    SECOND_LOGIN_BTN = (By.XPATH, "//*[@class='headerElements']/div[1]/div[1]/ul/li/a")
    EMAIL = (By.ID, 'email')
    PASSWORD = (By.ID, 'parola')
    SIGN_IN = (By.XPATH, '//*[@id="login_form"]/div[3]/div/button')
    ERROR = (By.CLASS_NAME, 'error')

    def open_home_page(self):
        self.chrome.get("https://www.motoemotion.ro")

    def click_login_button(self):
        try:
            login_button1 = self.chrome.find_element(*self.FIRST_LOGIN_BTN)
            login_button2 = self.chrome.find_element(*self.SECOND_LOGIN_BTN)
            login_button1.click()
            sleep(1)
            login_button2.click()
            sleep(1)
            logging.info('Clicked the "Contul meu" button successfully')
        except Exception as i:
            logging.error(f'An error occurred while clicking the login button: {str(i)}')

    def insert_email(self):
        try:
            user_email = self.chrome.find_element(*self.EMAIL)
            user_email.send_keys("pirlogsilviu1@gmail.com")
            sleep(1)
        except Exception as i:
            logging.error(f"An error occurred while inserting the email : {str(i)}")

    def insert_invalid_password(self, password):
        try:
            user_password = self.chrome.find_element(*self.PASSWORD)
            user_password.send_keys(password)
            sleep(1)
        except Exception as i:
            logging.error(f"An error occurred while inserting the password : {str(i)}")


    def click_sign_in_button(self):
        try:
            sign_in_button = self.chrome.find_element(*self.SIGN_IN)
            sign_in_button.click()
            sleep(1)
        except Exception as i:
            logging.error(f"An error occurred while clicking the sign in button : {str(i)}")


    def login_failed(self, error_message):
        try:
            alerta = self.chrome.find_element(*self.ERROR)
            alerta_text = alerta.text
            assert error_message in alerta_text
            logging.info("Login failed {}".format(error_message))
        except Exception as i:
            logging.error(f'The error message does not match: {str(i)}')



    def insert_password(self):
        try:
            userpassword = self.chrome.find_element(*self.PASSWORD)
            userpassword.send_keys('tester123')
            sleep(1)
        except Exception as i:
            logging.error(f"An error occured while inserting the password: {str(i)}")


    def my_account_page(self):
        account_url = "https://www.motoemotion.ro/contul-meu/"
        assert self.chrome.current_url == account_url
        logging.info('Test passed: Current URL match the expected account URL')
        sleep(1)