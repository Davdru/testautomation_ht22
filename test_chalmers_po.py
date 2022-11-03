from __future__ import annotations
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

from chalmers_pages import ChalmersMainPage

RESOLUTIONS = ((1920, 1080),)
RESOLUTIONS2 = ((1920, 1080), (2560, 1440), (1024, 768))
HEADLESS = False


def get_chrome():
    options = ChromeOptions()
    if HEADLESS:
        options.add_argument("--headless")
    return webdriver.Chrome(options=options)


def get_edge():
    options = EdgeOptions()
    if HEADLESS:
        options.add_argument("headless")
    return webdriver.Edge(options=options)


BROWSERS = [get_chrome]
BROWSERS2 = [get_chrome, get_edge]

@pytest.fixture(params=BROWSERS, scope="module")
def driver(request):
    driver_maker = request.param
    d = driver_maker()

    yield d
    d.quit()


@pytest.fixture(params=RESOLUTIONS, scope="module")
def browser(request, driver):
    x, y = request.param
    driver.set_window_position(0, 0)
    driver.set_window_size(x, y)
    yield driver


def test_nav_till_program_grundniva(browser):
    browser.get("https://www.chalmers.se")
    main_page = ChalmersMainPage(browser)
    utbildning = main_page.click_utbildning()
    program_grund = utbildning.click_program_grundniva()
    assert program_grund.title == "Hello"
    #assert browser.current_url == "https://www.chalmers.se/sv/utbildning/Sidor/default.aspx"


def test_nav_till_utbildning(browser):
    # browser = webdriver.Edge() # Starta en webläsare och ge mig en referens till den så att jag kan styra den
    # browser.set_window_size(1920, 1080)
    browser.get("https://www.chalmers.se")
    main_page = ChalmersMainPage(browser)
    main_page.click_utbildning()
    assert browser.current_url == "https://www.chalmers.se/sv/utbildning/Sidor/default.aspx"


def test_nav_till_forskning(browser):
    # browser = webdriver.Edge()  # Starta en webläsare och ge mig en referens till den så att jag kan styra den
    # browser.set_window_size(1920, 1080)
    browser.get("https://www.chalmers.se")
    main_page = ChalmersMainPage(browser)
    main_page.click_forskning()
    assert browser.current_url == "https://www.chalmers.se/sv/forskning/Sidor/default.aspx"


# 1 målet
# Öppna en webläsare som vi har kontroll över och gå till www.chalmers.se


# Några problem med testfunktioner skrivna så här.
# 1. Hårdkodad data i testfunktionen. Exempelvis hur vi hittar olika element. Om systemet vi testar förändras måste vi manuellt rätta varje test
# 2. Setup av webläsare och upplösning inne i testfunktionen. Vill vi testa på flera webläsare och upplösnignar får vi skapa fler testfunktioner med dubblering av kod som följd
def test_nav_it(browser):
    # browser = webdriver.Edge() # Starta en webläsare och ge mig en referens till den så att jag kan styra den
    # browser.set_window_size(1920, 1080)
    browser.get("https://www.chalmers.se")  # Navigera till chalmers.se
    browser.find_element(By.LINK_TEXT, "Utbildning").click()  # hitta länk baserat på länktext och klicka på
    browser.find_element(By.LINK_TEXT, "Program på grundnivå").click()
    browser.find_element(By.LINK_TEXT, "Elektro, Data, IT och Medicinteknik").click()
    browser.find_element(By.CSS_SELECTOR, ".orange li:nth-child(5) .title").click()


def test_nav_data_civ(browser):
    # browser = webdriver.Edge() # Starta en webläsare och ge mig en referens till den så att jag kan styra den
    # browser.set_window_size(1920, 1080)
    browser.get("https://www.chalmers.se")  # Navigera till chalmers.se
    browser.find_element(By.LINK_TEXT, "Utbildning").click()  # hitta länk baserat på länktext och klicka på
    browser.find_element(By.LINK_TEXT, "Program på grundnivå").click()
    browser.find_element(By.LINK_TEXT, "Elektro, Data, IT och Medicinteknik").click()
    browser.find_element(By.CSS_SELECTOR, ".orange li:nth-child(1) .title").click()
