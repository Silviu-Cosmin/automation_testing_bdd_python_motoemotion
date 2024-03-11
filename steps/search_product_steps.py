from behave import *

@given('I am logged in my account')
def step_impl(context):
    context.home_page.open_home_page()
    # context.home_page.click_login_button()
    # context.home_page.insert_email()
    # context.home_page.insert_password()
    # context.home_page.click_sign_in_button()

@when('I type the product in the search bar')
def step_impl(context):
    context.search_product_page.search_product()

@when('I click on the search button')
def step_impl(context):
    context.search_product_page.click_search_button()

@then('The search results are displayed containing "Rezultatele cautarii pentru:"')
def step_impl(context):
    context.search_product_page.verify_results()