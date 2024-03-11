from browser import Browser
from time import sleep
from selenium.webdriver.common.by import By
import logging

class Search_Product(Browser):

    SEARCH_BAR = (By.CSS_SELECTOR, '//div[@class="search"]//input[@id="mod_search_searchword"]')
    SEARCH_BTN = (By.CSS_SELECTOR, '//button[@value="Cauta"]')
    PRODUCT = (By.CSS_SELECTOR, '//a[normalize-space()="Casca open face/jet SCORPION EXO CITY II SOLID"]')
    RESULTS = (By.CLASS_NAME, 'search-results-title')


    def search_product(self):
        try:
            product = self.chrome.find_element(*self.SEARCH_BAR)
            product.send_keys('casca open face')
            logging.info('Successfully typed the product name')
        except Exception as i:
            logging.error(f'An error occurred while trying to type the product name: {str(i)}')


    def click_search_button(self):
        try:
            search_button = self.chrome.find_element(*self.SEARCH_BTN)
            search_button.click()
            logging.info('Successfully clicked the search button')
        except Exception as i:
            logging.error(f'An error occurred while trying to click the search button: {str(i)}')


    def verify_results(self):
        try:
            expected_text = 'Rezultatele cautarii pentru'
            results_text = self.chrome.find_element(*self.RESULTS).text
            assert expected_text in results_text
            logging.info('The search was successful')
        except Exception as i:
            logging.error(f'An error occurred while verifying the text results: {str(i)}')