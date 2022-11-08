from behave.fixture import fixture, use_fixture
from selenium import webdriver


@fixture
def edge_browser(context) -> webdriver.Edge:
    context.browser = webdriver.Edge()
    context.browser.set_window_size(1920, 1080)
    yield context.browser
    context.browser.quit()


def before_scenario(context, scenario):
    if "web" in scenario.tags:
        use_fixture(edge_browser, context)
