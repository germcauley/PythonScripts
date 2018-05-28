from behave import given, when, then
from selenium import webdriver

@given(u'the user is on a Page')
def step_user_is_on_fund_transfer_page(context):
    context.driver.get("https://the-internet.herokuapp.com/login")

@when(u'he clicks the search field')
def step_he_clicks_search_field(context):
    context.driver.find_element_by_id("username").click()

@when(u'he enters search term')
def step_he_enters_search_term(context):
    context.driver.find_element_by_id("username").send_keys('hello123456')


# @when(u'he enters search term text')
# def step_impl(context,text):
#     raise NotImplementedError(u'STEP: When he enters search term {text}')
#





#context.driver.find_element_by_id("username").send_keys('hello')




#
# @when('he Submits request')
# def step_he_Submits_request(context):
#     context.driver.find_element_by_id("cludoquery").send_keys(Keys.ENTER)
#
# @then('ensure url is {text}')
# def step_ensure_url_is(context):
#     assert context.driver.url == xurl
#
# def step_he_enters_payee_name(context):
#     context.driver.find_element_by_id("cludoquery").send_keys('rate')
# @when('he enters rate ')
#
# def step_he_enters_amount(context, amount):
#     context.driver.find_element_by_id("cludoquery").send_keys(Keys.ENTER)
# @when('he Submits request')
#
# def step_he_enters_amount(context):
#     context.driver.find_element_by_id("transfer").click()
# @then('ensure the fund transfer is complete with {text}message')
#
# def step_ensure_fund_transfer_is_complete(context, text):
#     assert context.driver.find_element_by_id("message").text == text
# @then('ensure a transaction failure message {text} is displayed')
#
# def step_ensure_fund_transfer_is_complete(context, text):
#     assert context.driver.find_element_by_id("message").text == text
