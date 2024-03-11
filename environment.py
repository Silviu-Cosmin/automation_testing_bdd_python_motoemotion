from browser import Browser
from pages.home_page import Home_Page
from pages.search_product_page import Search_Product

def before_all(context):
    context.browser = Browser()
    context.browser.maximise_window()
    context.home_page = Home_Page()
    context.search_product_page = Search_Product()


def after_all(context):
    context.browser.close_browser()