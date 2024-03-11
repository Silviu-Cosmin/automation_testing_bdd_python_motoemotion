from behave import *

@given('I am on the Motoemotion homepage and I want to initiate the login process with invalid password')
def step_impl(context):
    context.home_page.open_home_page()

@when('I click on "Contul meu" button')
def step_impl(context):
    context.home_page.click_login_button()

@when('I enter my valid email')
def step_impl(context):
    context.home_page.insert_email()

@when('I enter my invalid password "{user_password}"')
def step_impl(context, user_password):
    context.home_page.insert_invalid_password(user_password)

@when('I click on "Intra in cont" button')
def step_impl(context):
    context.home_page.click_login_button()

@then('I receive an "{alerta}"')
def step_impl(context, alerta):
    context.home_page.login_failed(alerta)

@when('I enter my valid password')
def step_impl(context):
    context.home_page.insert_password()

@when('I click on "Intra in cont"')
def step_impl(context):
    context.home_page.click_sign_in_button()

@then('I am redirected to my account page')
def step_impl(context):
    context.home_page.my_account_page()