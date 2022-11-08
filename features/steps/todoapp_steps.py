import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'I am on the todo page')
def step_impl(context):
    context.browser.get("https://lambdatest.github.io/sample-todo-app/")


@when(u'I click done on all todos')
def step_impl(context):
    for element in context.browser.find_elements(By.XPATH, "//ul/li"):
        time.sleep(1)
        element.find_element(By.XPATH, "input").click()


@then(u'Remaining todos should read 0')
def step_impl(context):
    remaining_text = context.browser.find_element(By.CSS_SELECTOR, ".ng-binding").text
    remaining = int(remaining_text.split()[0])
    assert remaining == 0, f"{remaining} remaining todos, expected 0"

