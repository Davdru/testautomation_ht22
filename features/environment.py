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



# Hooks, funktioner vi definierar, verktyget (behave) kör dom vid rätt tidpunkt
# before_feature(context, feature)
# before_scenario(context, scenario)
# before_step(context, step)
# before_tag(context, tag)
# before_all(context) # körs först av allt

# after_all(context)
# after_tag(context, tag)
# after_step(context, step)
# after_scenario(context, scenario)
# after_feature(context, feature)

